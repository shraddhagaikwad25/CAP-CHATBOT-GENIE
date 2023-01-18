{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Loading your AI personal assistant - G One\n",
      "Hello,Good Evening\n",
      "Listening...\n",
      "user said:hello how are you\n",
      "\n",
      "Listening...\n"
     ]
    }
   ],
   "source": [
    "import speech_recognition as sr\n",
    "import pyttsx3\n",
    "import datetime\n",
    "import wikipedia\n",
    "import webbrowser\n",
    "import os\n",
    "import time\n",
    "import subprocess\n",
    "from ecapture import ecapture as ec\n",
    "import wolframalpha\n",
    "import json\n",
    "import requests\n",
    "\n",
    "\n",
    "print('Loading your AI personal assistant - G One')\n",
    "\n",
    "engine=pyttsx3.init('sapi5')\n",
    "voices=engine.getProperty('voices')\n",
    "engine.setProperty('voice','voices[0].id')\n",
    "\n",
    "\n",
    "def speak(text):\n",
    "    engine.say(text)\n",
    "    engine.runAndWait()\n",
    "\n",
    "def wishMe():\n",
    "    hour=datetime.datetime.now().hour\n",
    "    if hour>=0 and hour<12:\n",
    "        speak(\"Hello,Good Morning\")\n",
    "        print(\"Hello,Good Morning\")\n",
    "    elif hour>=12 and hour<18:\n",
    "        speak(\"Hello,Good Afternoon\")\n",
    "        print(\"Hello,Good Afternoon\")\n",
    "    else:\n",
    "        speak(\"Hello,Good Evening\")\n",
    "        print(\"Hello,Good Evening\")\n",
    "\n",
    "def takeCommand():\n",
    "    r=sr.Recognizer()\n",
    "    with sr.Microphone() as source:\n",
    "        print(\"Listening...\")\n",
    "        audio=r.listen(source)\n",
    "\n",
    "        try:\n",
    "            statement=r.recognize_google(audio,language='en-in')\n",
    "            print(f\"user said:{statement}\\n\")\n",
    "\n",
    "        except Exception as e:\n",
    "            speak(\"Pardon me, please say that again\")\n",
    "            return \"None\"\n",
    "        return statement\n",
    "\n",
    "speak(\"Loading your AI personal assistant G-One\")\n",
    "wishMe()\n",
    "\n",
    "\n",
    "if __name__=='__main__':\n",
    "\n",
    "\n",
    "    while True:\n",
    "        speak(\"Tell me how can I help you now?\")\n",
    "        statement = takeCommand().lower()\n",
    "        if statement==0:\n",
    "            continue\n",
    "\n",
    "        if \"good bye\" in statement or \"ok bye\" in statement or \"stop\" in statement:\n",
    "            speak('your personal assistant G-one is shutting down,Good bye')\n",
    "            print('your personal assistant G-one is shutting down,Good bye')\n",
    "            break\n",
    "\n",
    "\n",
    "\n",
    "        if 'wikipedia' in statement:\n",
    "            speak('Searching Wikipedia...')\n",
    "            statement =statement.replace(\"wikipedia\", \"\")\n",
    "            results = wikipedia.summary(statement, sentences=3)\n",
    "            speak(\"According to Wikipedia\")\n",
    "            print(results)\n",
    "            speak(results)\n",
    "\n",
    "        elif 'open youtube' in statement:\n",
    "            webbrowser.open_new_tab(\"https://www.youtube.com\")\n",
    "            speak(\"youtube is open now\")\n",
    "            time.sleep(5)\n",
    "\n",
    "        elif 'open google' in statement:\n",
    "            webbrowser.open_new_tab(\"https://www.google.com\")\n",
    "            speak(\"Google chrome is open now\")\n",
    "            time.sleep(5)\n",
    "\n",
    "        elif 'open gmail' in statement:\n",
    "            webbrowser.open_new_tab(\"gmail.com\")\n",
    "            speak(\"Google Mail open now\")\n",
    "            time.sleep(5)\n",
    "\n",
    "        elif \"weather\" in statement:\n",
    "            api_key=\"8ef61edcf1c576d65d836254e11ea420\"\n",
    "            base_url=\"https://api.openweathermap.org/data/2.5/weather?\"\n",
    "            speak(\"whats the city name\")\n",
    "            city_name=takeCommand()\n",
    "            complete_url=base_url+\"appid=\"+api_key+\"&q=\"+city_name\n",
    "            response = requests.get(complete_url)\n",
    "            x=response.json()\n",
    "            if x[\"cod\"]!=\"404\":\n",
    "                y=x[\"main\"]\n",
    "                current_temperature = y[\"temp\"]\n",
    "                current_humidiy = y[\"humidity\"]\n",
    "                z = x[\"weather\"]\n",
    "                weather_description = z[0][\"description\"]\n",
    "                speak(\" Temperature in kelvin unit is \" +\n",
    "                      str(current_temperature) +\n",
    "                      \"\\n humidity in percentage is \" +\n",
    "                      str(current_humidiy) +\n",
    "                      \"\\n description  \" +\n",
    "                      str(weather_description))\n",
    "                print(\" Temperature in kelvin unit = \" +\n",
    "                      str(current_temperature) +\n",
    "                      \"\\n humidity (in percentage) = \" +\n",
    "                      str(current_humidiy) +\n",
    "                      \"\\n description = \" +\n",
    "                      str(weather_description))\n",
    "\n",
    "            else:\n",
    "                speak(\" City Not Found \")\n",
    "\n",
    "\n",
    "\n",
    "        elif 'time' in statement:\n",
    "            strTime=datetime.datetime.now().strftime(\"%H:%M:%S\")\n",
    "            speak(f\"the time is {strTime}\")\n",
    "\n",
    "        elif 'who are you' in statement or 'what can you do' in statement:\n",
    "            speak('I am G-one version 1 point O your persoanl assistant. I am programmed to minor tasks like'\n",
    "                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' \n",
    "                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')\n",
    "\n",
    "\n",
    "        elif \"who made you\" in statement or \"who created you\" in statement or \"who discovered you\" in statement:\n",
    "            speak(\"I was built by Mirthula\")\n",
    "            print(\"I was built by Mirthula\")\n",
    "\n",
    "        elif \"open stackoverflow\" in statement:\n",
    "            webbrowser.open_new_tab(\"https://stackoverflow.com/login\")\n",
    "            speak(\"Here is stackoverflow\")\n",
    "\n",
    "        elif 'news' in statement:\n",
    "            news = webbrowser.open_new_tab(\"https://timesofindia.indiatimes.com/home/headlines\")\n",
    "            speak('Here are some headlines from the Times of India,Happy reading')\n",
    "            time.sleep(6)\n",
    "\n",
    "        elif \"camera\" in statement or \"take a photo\" in statement:\n",
    "            ec.capture(0,\"robo camera\",\"img.jpg\")\n",
    "\n",
    "        elif 'search'  in statement:\n",
    "            statement = statement.replace(\"search\", \"\")\n",
    "            webbrowser.open_new_tab(statement)\n",
    "            time.sleep(5)\n",
    "\n",
    "        elif 'ask' in statement:\n",
    "            speak('I can answer to computational and geographical questions and what question do you want to ask now')\n",
    "            question=takeCommand()\n",
    "            app_id=\"R2K75H-7ELALHR35X\"\n",
    "            client = wolframalpha.Client('R2K75H-7ELALHR35X')\n",
    "            res = client.query(question)\n",
    "            answer = next(res.results).text\n",
    "            speak(answer)\n",
    "            print(answer)\n",
    "\n",
    "\n",
    "        elif \"log off\" in statement or \"sign out\" in statement:\n",
    "            speak(\"Ok , your pc will log off in 10 sec make sure you exit from all applications\")\n",
    "            subprocess.call([\"shutdown\", \"/l\"])\n",
    "\n",
    "time.sleep(3)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "yourenvname",
   "language": "python",
   "name": "yourenvname"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}