from spellchecker import SpellChecker
import random
import multiprocessing
from flask import Flask,json, render_template, request
from flask_cors import CORS
import time
import nltk
from multiprocessing import Process
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import json
import numpy as np
from keras.models import load_model
model = load_model('chatbot_model.h5')
intents = json.loads(open('cap_intents.json',encoding="utf8").read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
app= Flask(__name__)
CORS(app)
@app.route('/run/<msg>') 
def chatbot(msg):
    msg=SpellChecker().correction(msg)
    
    def clean_up_sentence(sentence):
        # token,aize the pattern - split words into array
        sentence_words = nltk.word_tokenize(sentence)
        # stem each word - create short form for word
        sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
        return sentence_words
    # return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
    def bow(sentence, words, show_details=True):
        # tokenize the pattern
        sentence_words = clean_up_sentence(sentence)
        # bag of words - matrix of N words, vocabulary matrix
        bag = [0]*len(words)  
        for s in sentence_words:
            for i,w in enumerate(words):
                if w == s: 
                    # assign 1 if current word is in the vocabulary position
                    bag[i] = 1
                    if show_details:
                        print ("found in bag: %s" % w)
        return(np.array(bag))
    def predict_class(sentence, model):
        # filter out predictions below a threshold
        p = bow(sentence, words,show_details=False)
        
        res = model.predict(np.array([p]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
        # sort by strength of probability
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
        return return_list 
    def getResponse(ints, intents_json):
        tag = ints[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if(i['tag']== tag):
                result = random.choice(i['responses'])
                #result1 = random.choice(i['responses1'])
                break
        return result
        
    
    def chatbot_response(text):
        ints = predict_class(text, model)
        res = getResponse(ints, intents)
        return res
    
    def send():
        print(msg,"input")
        while True:#it used to be in continunation and to stop it press alt+cntrl+c
            #msg=input("You:- ")
            
            if msg=="quit":
                break
            else:
                res=chatbot_response(msg)
                
                return {"Bot":[res]}
    return send()
    if __name__ == '__main__':
        p = Process(target=chatbot)
        p.start()
        p.join()
if __name__== "__main__":
    app.run(threaded=False,port=5000)
#   app.run(host='172.31.52.129',port=5000)
