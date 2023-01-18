import pymongo
from pymongo import MongoClient
from pprint import pprint
import urllib.parse
import pandas as pd
import numpy as np
from pandas import DataFrame
from bson.objectid import ObjectId
import datetime
import json
from flask import Flask,json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/parpracticeprogram/')
def parpracticeprogram():
    username = urllib.parse.quote_plus('admin')
    password = urllib.parse.quote_plus('A_dM!n|#!_2o20')
    client = MongoClient("mongodb://%s:%s@44.234.36.103:27017/" % (username, password))
    db=client.compass
    collection = db.audio_track_master
    query=[
        {"$match":{'USER_ID.ROLE_ID.ROLE_ID':{"$eq":2},                  
                'USER_ID.EMAIL_ID':{"$not":{"$regex":'test','$options':'i'}},
                'USER_ID.USER_NAME':{"$not":{"$regex":'test','$options':'i'}},
                'USER_ID.IS_DISABLE':{"$ne":'Y'},
                'USER_ID.INCOMPLETE_SIGNUP':{"$ne":'Y'},
                'USER_ID.EMAIL_ID':{"$not":{"$regex":'1gen','$options':'i'}}
                }},

    {"$project":{'USER_ID':'$USER_ID.USER_ID','PROGRAM_AUDIO_ID.AUDIO_ID':1,
        'PROGRAM_AUDIO_ID.PROGRAM_ID.PROGRAM_ID':1,
        'AGE_GROUP':'$PROGRAM_AUDIO_ID.PROGRAM_ID.AGE_GROUP',
        'AUDIO_NAME':1,'AUDIO_LENGTH':1,
        'IS_DONE':1,'PROGRAM_AUDIO_ID.AUDIO_DAY':1,'PROGRAM_AUDIO_ID.AUDIO_LENGTH':1,

        'PlayBack_Time_Percent':{"$round":[{"$divide":[{"$subtract":
            ['$CURSOR_END','$cursorStart']},'$PROGRAM_AUDIO_ID.AUDIO_LENGTH']},2]}}},


    { "$project": { 'USER_ID':1,'AGE_GROUP':1,

        "status": {
          "$cond": { "if": { "$regexMatch": { 
                                    "input": "$PROGRAM_AUDIO_ID.AUDIO_DAY",
                                    "regex": 'bonus','options': "i"  }}
              , 
          "then": 'Bonus', "else": {
             "$cond": { "if": { "$regexMatch": { 
                                    "input": "$PROGRAM_AUDIO_ID.AUDIO_DAY",
                                    "regex": "sound",'options': "i" }}, 
             "then": 'Sound', "else": 'daily'
             }}}}}}         

             ]

    x=list(collection.aggregate(query))
    df=pd.DataFrame(x)
    age_group_df=pd.DataFrame({'AGE_GROUP':list(set(df.AGE_GROUP.tolist()))}).dropna().sort_values(by=['AGE_GROUP'])

    practice_count_overall=pd.DataFrame(df.groupby(['AGE_GROUP','status'])['USER_ID'].count()).reset_index().rename(columns={'USER_ID':'Count'})
    age_group_df=pd.DataFrame({'AGE_GROUP':list(set(df.AGE_GROUP.tolist()))}).dropna().sort_values(by=['AGE_GROUP'])
    dailydf=practice_count_overall[practice_count_overall.status=='daily']
    dailycompdf=pd.merge(age_group_df,dailydf,on='AGE_GROUP',how='left')
    dailycompdf['status'].fillna('daily',inplace=True)
    dailycompdf['Count'].fillna(0,inplace=True)
    Sounddf=practice_count_overall[practice_count_overall.status=='Sound']
    Soundcompdf=pd.merge(age_group_df,Sounddf,on='AGE_GROUP',how='left')
    Soundcompdf['status'].fillna('Sound',inplace=True)
    Soundcompdf['Count'].fillna(0,inplace=True)
    Bonusdf=practice_count_overall[practice_count_overall.status=='Bonus']
    Bonuscompdf=pd.merge(age_group_df,Bonusdf,on='AGE_GROUP',how='left')
    Bonuscompdf['status'].fillna('Bonus',inplace=True)
    Bonuscompdf['Count'].fillna(0,inplace=True)
    temp={'daily':dailycompdf.Count.tolist(),'dtotal':dailycompdf.Count.sum(),'prog':age_group_df.AGE_GROUP.tolist(),
      'sound':Soundcompdf.Count.tolist(),'soundt':Soundcompdf.Count.sum(),
       'transition':Bonuscompdf.Count.tolist(),'trant':Bonuscompdf.Count.sum()}

    return json.dumps(temp)


@app.route('/parpracticeprogramunique/')
def parpracticeprogram_unique():
    username = urllib.parse.quote_plus('admin')
    password = urllib.parse.quote_plus('A_dM!n|#!_2o20')
    client = MongoClient("mongodb://%s:%s@44.234.36.103:27017/" % (username, password))
    db=client.compass
    collection = db.db.audio_track_master
    query=[
        {"$match":{'USER_ID.ROLE_ID.ROLE_ID':{"$eq":2},                  
                'USER_ID.EMAIL_ID':{"$not":{"$regex":'test','$options':'i'}},
                'USER_ID.USER_NAME':{"$not":{"$regex":'test','$options':'i'}},
                'USER_ID.IS_DISABLE':{"$ne":'Y'},
                'USER_ID.INCOMPLETE_SIGNUP':{"$ne":'Y'},
                'USER_ID.EMAIL_ID':{"$not":{"$regex":'1gen','$options':'i'}}
                }},

    {"$project":{'USER_ID':'$USER_ID.USER_ID','PROGRAM_AUDIO_ID.AUDIO_ID':1,
        'PROGRAM_AUDIO_ID.PROGRAM_ID.PROGRAM_ID':1,
        'AGE_GROUP':'$PROGRAM_AUDIO_ID.PROGRAM_ID.AGE_GROUP',
        'AUDIO_NAME':1,'AUDIO_LENGTH':1,
        'IS_DONE':1,'PROGRAM_AUDIO_ID.AUDIO_DAY':1,'PROGRAM_AUDIO_ID.AUDIO_LENGTH':1,

        'PlayBack_Time_Percent':{"$round":[{"$divide":[{"$subtract":
            ['$CURSOR_END','$cursorStart']},'$PROGRAM_AUDIO_ID.AUDIO_LENGTH']},2]}}},


    { "$project": { 'USER_ID':1,'AGE_GROUP':1,

        "status": {
          "$cond": { "if": { "$regexMatch": { 
                                    "input": "$PROGRAM_AUDIO_ID.AUDIO_DAY",
                                    "regex": 'bonus','options': "i"  }}
              , 
          "then": 'Bonus', "else": {
             "$cond": { "if": { "$regexMatch": { 
                                    "input": "$PROGRAM_AUDIO_ID.AUDIO_DAY",
                                    "regex": "sound",'options': "i" }}, 
             "then": 'Sound', "else": 'daily'
             }}}}}}         

             ]

    x=list(collection.aggregate(query))
    df=pd.DataFrame(x)
    age_group_df=pd.DataFrame({'AGE_GROUP':list(set(df.AGE_GROUP.tolist()))}).dropna().sort_values(by=['AGE_GROUP'])

    practice_count_overall=pd.DataFrame(df.groupby(['AGE_GROUP','status'])['USER_ID'].nunique()).reset_index().rename(columns={'USER_ID':'Count'})
    age_group_df=pd.DataFrame({'AGE_GROUP':list(set(df.AGE_GROUP.tolist()))}).dropna().sort_values(by=['AGE_GROUP'])
    dailydf=practice_count_overall[practice_count_overall.status=='daily']
    dailycompdf=pd.merge(age_group_df,dailydf,on='AGE_GROUP',how='left')
    dailycompdf['status'].fillna('daily',inplace=True)
    dailycompdf['Count'].fillna(0,inplace=True)
    Sounddf=practice_count_overall[practice_count_overall.status=='Sound']
    Soundcompdf=pd.merge(age_group_df,Sounddf,on='AGE_GROUP',how='left')
    Soundcompdf['status'].fillna('Sound',inplace=True)
    Soundcompdf['Count'].fillna(0,inplace=True)
    Bonusdf=practice_count_overall[practice_count_overall.status=='Bonus']
    Bonuscompdf=pd.merge(age_group_df,Bonusdf,on='AGE_GROUP',how='left')
    Bonuscompdf['status'].fillna('Bonus',inplace=True)
    Bonuscompdf['Count'].fillna(0,inplace=True)
    temp={'daily':dailycompdf.Count.tolist(),'dtotal':dailycompdf.Count.sum(),'prog':age_group_df.AGE_GROUP.tolist(),
      'sound':Soundcompdf.Count.tolist(),'soundt':Soundcompdf.Count.sum(),
       'transition':Bonuscompdf.Count.tolist(),'trant':Bonuscompdf.Count.sum()}
    return json.dumps(temp)

@app.route('/parpracticeprogramactive/')
def parpracticeprogramactive():
    username = urllib.parse.quote_plus('admin')
    password = urllib.parse.quote_plus('A_dM!n|#!_2o20')
    client = MongoClient("mongodb://%s:%s@44.234.36.103:27017/" % (username, password))
    db=client.compass
    collection = db.db.audio_track_master
    query=[
        {"$match":{'USER_ID.ROLE_ID.ROLE_ID':{"$eq":2},                  
                'USER_ID.EMAIL_ID':{"$not":{"$regex":'test','$options':'i'}},
                'USER_ID.USER_NAME':{"$not":{"$regex":'test','$options':'i'}},
                'USER_ID.IS_DISABLE':{"$ne":'Y'},
                'USER_ID.INCOMPLETE_SIGNUP':{"$ne":'Y'},
                'USER_ID.EMAIL_ID':{"$not":{"$regex":'1gen','$options':'i'}}
                }},

    {"$project":{'USER_ID':'$USER_ID.USER_ID','PROGRAM_AUDIO_ID.AUDIO_ID':1,
        'PROGRAM_AUDIO_ID.PROGRAM_ID.PROGRAM_ID':1,
        'AGE_GROUP':'$PROGRAM_AUDIO_ID.PROGRAM_ID.AGE_GROUP',
        'AUDIO_NAME':1,'AUDIO_LENGTH':1,
        'IS_DONE':1,'PROGRAM_AUDIO_ID.AUDIO_DAY':1,'PROGRAM_AUDIO_ID.AUDIO_LENGTH':1,

        'PlayBack_Time_Percent':{"$round":[{"$divide":[{"$subtract":
            ['$CURSOR_END','$cursorStart']},'$PROGRAM_AUDIO_ID.AUDIO_LENGTH']},2]}}},
        {"$match":{'PlayBack_Time_Percent':{"$gte":.5}}},


    { "$project": { 'USER_ID':1,'AGE_GROUP':1,

        "status": {
          "$cond": { "if": { "$regexMatch": { 
                                    "input": "$PROGRAM_AUDIO_ID.AUDIO_DAY",
                                    "regex": 'bonus','options': "i"  }}


              , 
          "then": 'Bonus', "else": {
             "$cond": { "if": { "$regexMatch": { 
                                    "input": "$PROGRAM_AUDIO_ID.AUDIO_DAY",
                                    "regex": "sound",'options': "i" }}, 
             "then": 'Sound', "else": 'daily'
             }}}}}}         

             ]

    x=list(collection.aggregate(query))
    df=pd.DataFrame(x)
    age_group_df=pd.DataFrame({'AGE_GROUP':list(set(df.AGE_GROUP.tolist()))}).dropna().sort_values(by=['AGE_GROUP'])

    practice_count_overall=pd.DataFrame(df.groupby(['AGE_GROUP','status'])['USER_ID'].count()).reset_index().rename(columns={'USER_ID':'Count'})
    age_group_df=pd.DataFrame({'AGE_GROUP':list(set(df.AGE_GROUP.tolist()))}).dropna().sort_values(by=['AGE_GROUP'])
    dailydf=practice_count_overall[practice_count_overall.status=='daily']
    dailycompdf=pd.merge(age_group_df,dailydf,on='AGE_GROUP',how='left')
    dailycompdf['status'].fillna('daily',inplace=True)
    dailycompdf['Count'].fillna(0,inplace=True)
    Sounddf=practice_count_overall[practice_count_overall.status=='Sound']
    Soundcompdf=pd.merge(age_group_df,Sounddf,on='AGE_GROUP',how='left')
    Soundcompdf['status'].fillna('Sound',inplace=True)
    Soundcompdf['Count'].fillna(0,inplace=True)
    Bonusdf=practice_count_overall[practice_count_overall.status=='Bonus']
    Bonuscompdf=pd.merge(age_group_df,Bonusdf,on='AGE_GROUP',how='left')
    Bonuscompdf['status'].fillna('Bonus',inplace=True)
    Bonuscompdf['Count'].fillna(0,inplace=True)
    temp={'daily':dailycompdf.Count.tolist(),'dtotal':dailycompdf.Count.sum(),'prog':age_group_df.AGE_GROUP.tolist(),
      'sound':Soundcompdf.Count.tolist(),'soundt':Soundcompdf.Count.sum(),
       'transition':Bonuscompdf.Count.tolist(),'trant':Bonuscompdf.Count.sum()}
    return json.dumps(temp)


@app.route('/parpracticeprogramactiveunique/')

def parpracticeprogram_unique_active():
    username = urllib.parse.quote_plus('admin')
    password = urllib.parse.quote_plus('A_dM!n|#!_2o20')
    client = MongoClient("mongodb://%s:%s@44.234.36.103:27017/" % (username, password))
    db=client.compass
    collection = db.db.audio_track_master
    query=[
        {"$match":{'USER_ID.ROLE_ID.ROLE_ID':{"$eq":2},                  
                'USER_ID.EMAIL_ID':{"$not":{"$regex":'test','$options':'i'}},
                'USER_ID.USER_NAME':{"$not":{"$regex":'test','$options':'i'}},
                'USER_ID.IS_DISABLE':{"$ne":'Y'},
                'USER_ID.INCOMPLETE_SIGNUP':{"$ne":'Y'},
                'USER_ID.EMAIL_ID':{"$not":{"$regex":'1gen','$options':'i'}}
                }},

    {"$project":{'USER_ID':'$USER_ID.USER_ID','PROGRAM_AUDIO_ID.AUDIO_ID':1,
        'PROGRAM_AUDIO_ID.PROGRAM_ID.PROGRAM_ID':1,
        'AGE_GROUP':'$PROGRAM_AUDIO_ID.PROGRAM_ID.AGE_GROUP',
        'AUDIO_NAME':1,'AUDIO_LENGTH':1,
        'IS_DONE':1,'PROGRAM_AUDIO_ID.AUDIO_DAY':1,'PROGRAM_AUDIO_ID.AUDIO_LENGTH':1,

        'PlayBack_Time_Percent':{"$round":[{"$divide":[{"$subtract":
            ['$CURSOR_END','$cursorStart']},'$PROGRAM_AUDIO_ID.AUDIO_LENGTH']},2]}}},
        {"$match":{'PlayBack_Time_Percent':{"$gte":.5}}},


    { "$project": { 'USER_ID':1,'AGE_GROUP':1,

        "status": {
          "$cond": { "if": { "$regexMatch": { 
                                    "input": "$PROGRAM_AUDIO_ID.AUDIO_DAY",
                                    "regex": 'bonus','options': "i"  }}


              , 
          "then": 'Bonus', "else": {
             "$cond": { "if": { "$regexMatch": { 
                                    "input": "$PROGRAM_AUDIO_ID.AUDIO_DAY",
                                    "regex": "sound",'options': "i" }}, 
             "then": 'Sound', "else": 'daily'
             }}}}}}         

             ]

    x=list(collection.aggregate(query))
    df=pd.DataFrame(x)
    age_group_df=pd.DataFrame({'AGE_GROUP':list(set(df.AGE_GROUP.tolist()))}).dropna().sort_values(by=['AGE_GROUP'])

    practice_count_overall=pd.DataFrame(df.groupby(['AGE_GROUP','status'])['USER_ID'].nunique()).reset_index().rename(columns={'USER_ID':'Count'})
    age_group_df=pd.DataFrame({'AGE_GROUP':list(set(df.AGE_GROUP.tolist()))}).dropna().sort_values(by=['AGE_GROUP'])
    dailydf=practice_count_overall[practice_count_overall.status=='daily']
    dailycompdf=pd.merge(age_group_df,dailydf,on='AGE_GROUP',how='left')
    dailycompdf['status'].fillna('daily',inplace=True)
    dailycompdf['Count'].fillna(0,inplace=True)
    Sounddf=practice_count_overall[practice_count_overall.status=='Sound']
    Soundcompdf=pd.merge(age_group_df,Sounddf,on='AGE_GROUP',how='left')
    Soundcompdf['status'].fillna('Sound',inplace=True)
    Soundcompdf['Count'].fillna(0,inplace=True)
    Bonusdf=practice_count_overall[practice_count_overall.status=='Bonus']
    Bonuscompdf=pd.merge(age_group_df,Bonusdf,on='AGE_GROUP',how='left')
    Bonuscompdf['status'].fillna('Bonus',inplace=True)
    Bonuscompdf['Count'].fillna(0,inplace=True)
    temp={'daily':dailycompdf.Count.tolist(),'dtotal':dailycompdf.Count.sum(),'prog':age_group_df.AGE_GROUP.tolist(),
      'sound':Soundcompdf.Count.tolist(),'soundt':Soundcompdf.Count.sum(),
       'transition':Bonuscompdf.Count.tolist(),'trant':Bonuscompdf.Count.sum()}

    return json.dumps(temp)


@app.route('/programwisecard/')

def programwise_card():
    username = urllib.parse.quote_plus('admin')
    password = urllib.parse.quote_plus('A_dM!n|#!_2o20')
    client = MongoClient("mongodb://%s:%s@44.234.36.103:27017/" % (username, password))
    db=client.compass
    collection = db.db.audio_track_master
    query=[
        {"$match":{'USER_ID.ROLE_ID.ROLE_ID':{"$eq":2},                  
                'USER_ID.EMAIL_ID':{"$not":{"$regex":'test','$options':'i'}},
                'USER_ID.USER_NAME':{"$not":{"$regex":'test','$options':'i'}},
                'USER_ID.IS_DISABLE':{"$ne":'Y'},
                'USER_ID.INCOMPLETE_SIGNUP':{"$ne":'Y'},
                'USER_ID.EMAIL_ID':{"$not":{"$regex":'1gen','$options':'i'}}
                }},
        {"$project":{'USER_ID':'$USER_ID.USER_ID','PROGRAM_AUDIO_ID.AUDIO_ID':1,
            'PROGRAM_AUDIO_ID.PROGRAM_ID.PROGRAM_ID':1,
            'AGE_GROUP':'$PROGRAM_AUDIO_ID.PROGRAM_ID.AGE_GROUP',
            'AUDIO_NAME':1,'AUDIO_LENGTH':1,
            'IS_DONE':1,'PROGRAM_AUDIO_ID.AUDIO_DAY':1,'PROGRAM_AUDIO_ID.AUDIO_LENGTH':1,
             'Mindful_Minutes':{"$round":[{"$divide":[{"$subtract":['$CURSOR_END','$cursorStart']},60]},2]},        

            'PlayBack_Time_Percent':{"$round":[{"$divide":[{"$subtract":
                ['$CURSOR_END','$cursorStart']},'$PROGRAM_AUDIO_ID.AUDIO_LENGTH']},2]}}}       
             

                 ]

    Overall=list(collection.aggregate(query))
    Overall_df=pd.DataFrame(Overall)
    card_df=pd.DataFrame({'Engaged':len(set(Overall_df.USER_ID.tolist())),
                 'Active':len(set(Overall_df[Overall_df['PlayBack_Time_Percent']>=.5]['USER_ID'].tolist())),
                  'Passive':len(set(Overall_df.USER_ID.tolist()))-
                          len(set(Overall_df[Overall_df['PlayBack_Time_Percent']>=.5]['USER_ID'].tolist())),
                 'Total Playbacks':len(Overall_df),
                  'Mindful Minutes':Overall_df.Mindful_Minutes.sum()
                 },index=[0]).reset_index(drop=True)

    data=[]
    for i,j in zip(card_df.columns.tolist(),card_df.iloc[0].tolist()):
        data.append([i,j])
    temp={"data":data}
    return json.dumps(temp)

# Family feedback card api


@app.route('/familyfeedbackcards/')

def familyfeedbackcard():
    username = urllib.parse.quote_plus('admin')
    password = urllib.parse.quote_plus('A_dM!n|#!_2o20')
    client = MongoClient("mongodb://%s:%s@44.234.36.103:27017/" % (username, password))
    db=client.compass
    collection = db.db.audio_track_master
    collection2=db.audio_feedback
    query=[{"$match":{'USER_ID.ROLE_ID.ROLE_ID':{"$eq":2},
         'USER_ID.USER_NAME':{"$not":{"$regex":"test",'$options':'i'}},
        'USER_ID.USER_ID.EMAIL_ID':{"$not":{"$regex":"test",'$options':'i'}},
        'USER_ID.EMAIL_ID':{"$not":{"$regex":"1gen",'$options':'i'}},
          'USER_ID.IS_BLOCKED':{"$ne":'Y'},
          'USER_ID.INCOMPLETE_SIGNUP':{"$ne":'Y'},
          'USER_ID.IS_DISABLED':{"$ne":'Y'},
        'USER_ID.EMAIL_ID':{'$ne':None}

            }},
         {"$project":{"_id":0, "USER_ID":'$USER_ID.USER_ID','MODIFIED_DATE':1}}]



    query2=[
    #     // {"$match":{'USER.ROLE_ID.ROLE_ID' :2
    #                    // ,
    #                     // "USER.IS_DISTABLED":{"$ne":"Y"},
    #                     // "USER.INCOMPLETE_SIGNUP":{"$ne":"Y"},
    #                     // "USER.EMAIL_ID":{"$not":{"$regex" : 'test','$options':'i'}},
    #                     // "USER.EMAIL_ID":{"$ne": None},
    #                     // "USER.EMAIL_ID":{"$not":{"$regex" : '1gen','$options':'i'}},
    #                     // "RATING":{'$ne':0},    
    #                     // "USER_NAME":{"$not":{"$regex" : 'test','$options':'i'}}}},


            {"$project":{'RATING':1,'COMMENT':1,'USER_ID':'$USER.USER','USER_NAME':'$USER.USER_NAME','EMAIL':'$USER.EMAIL_ID'}}]

    practice=list(collection.aggregate(query))
    practice_df=pd.DataFrame(practice)
    feedback=list(collection2.aggregate(query2))
    feedback_df=pd.DataFrame(feedback)
    card_df=pd.DataFrame({'Feedback_Percentage':(len(feedback_df[feedback_df['RATING']!=0])/len(practice_df))*100,
                 'Comment_per_feedback':len(feedback_df[(feedback_df['COMMENT'].notnull()) & (feedback_df['COMMENT']!='') ])/
                 len(feedback_df[feedback_df['RATING']!=0])*100,
                  'Total_Playbacks':len(practice_df),'Average_Rating':feedback_df[feedback_df['RATING']!=0]['RATING'].mean()},
                  index=[0])             

    data=[]
    for i,j in zip(card_df.columns.tolist(),card_df.iloc[0].tolist()):
        data.append([i,j])
    temp={"data":data}
    return json.dumps(temp)


if __name__ == '__main__':
    app.run(host='172.31.11.32',port=5010)
