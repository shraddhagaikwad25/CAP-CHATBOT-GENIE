{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pygame 2.0.1 (SDL 2.0.14, Python 3.6.13)\n",
      "Hello from the pygame community. https://www.pygame.org/contribute.html\n",
      "A moment of silence, please...\n",
      "Set minimum energy threshold to 642.6172487589309\n",
      "Say something!\n",
      "Got it! Now to recognize it...\n",
      "You said hello\n",
      "Say something!\n",
      "Got it! Now to recognize it...\n",
      "You said how are you good evening\n",
      "Say something!\n",
      "Got it! Now to recognize it...\n",
      "Oops! Didn't catch that\n",
      "Say something!\n",
      "Tell me something:\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-e59a259a2c37>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     43\u001b[0m     \u001b[1;32mwith\u001b[0m \u001b[0msr\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mMicrophone\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0msource\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     44\u001b[0m         \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Tell me something:\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 45\u001b[1;33m         \u001b[0maudio\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mr\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlisten\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msource\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     46\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     47\u001b[0m             \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"You said:- \"\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0mr\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrecognize_google\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0maudio\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\yourenvname\\lib\\site-packages\\speech_recognition\\__init__.py\u001b[0m in \u001b[0;36mlisten\u001b[1;34m(self, source, timeout, phrase_time_limit, snowboy_configuration)\u001b[0m\n\u001b[0;32m    650\u001b[0m                     \u001b[1;32mbreak\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    651\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 652\u001b[1;33m                 \u001b[0mbuffer\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0msource\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstream\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msource\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mCHUNK\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    653\u001b[0m                 \u001b[1;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbuffer\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;32mbreak\u001b[0m  \u001b[1;31m# reached end of the stream\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    654\u001b[0m                 \u001b[0mframes\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbuffer\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\yourenvname\\lib\\site-packages\\speech_recognition\\__init__.py\u001b[0m in \u001b[0;36mread\u001b[1;34m(self, size)\u001b[0m\n\u001b[0;32m    159\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    160\u001b[0m         \u001b[1;32mdef\u001b[0m \u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msize\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 161\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpyaudio_stream\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msize\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexception_on_overflow\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mFalse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    162\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    163\u001b[0m         \u001b[1;32mdef\u001b[0m \u001b[0mclose\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\yourenvname\\lib\\site-packages\\pyaudio.py\u001b[0m in \u001b[0;36mread\u001b[1;34m(self, num_frames, exception_on_overflow)\u001b[0m\n\u001b[0;32m    606\u001b[0m                           paCanNotReadFromAnOutputOnlyStream)\n\u001b[0;32m    607\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 608\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mpa\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread_stream\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_stream\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mnum_frames\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexception_on_overflow\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    609\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    610\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mget_read_available\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "import random\n",
    "import datetime\n",
    "import webbrowser\n",
    "import pyttsx3\n",
    "import wikipedia\n",
    "from pygame import mixer\n",
    "import speech_recognition as sr\n",
    "from speech_recognition.__main__ import r, audio\n",
    "\n",
    "engine = pyttsx3.init()\n",
    "voices = engine.getProperty('voices')\n",
    "engine.setProperty('voice', voices[1].id)\n",
    "volume = engine.getProperty('volume')\n",
    "engine.setProperty('volume', 10.0)\n",
    "rate = engine.getProperty('rate')\n",
    "\n",
    "engine.setProperty('rate', rate - 25)\n",
    "\n",
    "greetings = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey']\n",
    "question = ['How are you?', 'How are you doing?']\n",
    "responses = ['Okay', \"I'm fine\"]\n",
    "var1 = ['who made you', 'who created you']\n",
    "var2 = ['I_was_created_by_Edward_right_in_his_computer.', 'Edward', 'Some_guy_whom_i_never_got_to_know.']\n",
    "var3 = ['what time is it', 'what is the time', 'time']\n",
    "var4 = ['who are you', 'what is you name']\n",
    "cmd1 = ['open browser', 'open google']\n",
    "cmd2 = ['play music', 'play songs', 'play a song', 'open music player']\n",
    "cmd3 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']\n",
    "jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!\"Doctor: Nine.']\n",
    "cmd4 = ['open youtube', 'i want to watch a video']\n",
    "cmd5 = ['tell me the weather', 'weather', 'what about the weather']\n",
    "cmd6 = ['exit', 'close', 'goodbye', 'nothing']\n",
    "cmd7 = ['what is your color', 'what is your colour', 'your color', 'your color?']\n",
    "colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']\n",
    "cmd8 = ['what is you favourite colour', 'what is your favourite color']\n",
    "cmd9 = ['thank you']\n",
    "\n",
    "repfr9 = ['youre welcome', 'glad i could help you']\n",
    "\n",
    "while True:\n",
    "    now = datetime.datetime.now()\n",
    "    r = sr.Recognizer()\n",
    "    with sr.Microphone() as source:\n",
    "        print(\"Tell me something:\")\n",
    "        audio = r.listen(source)\n",
    "        try:\n",
    "            print(\"You said:- \" + r.recognize_google(audio))\n",
    "        except sr.UnknownValueError:\n",
    "            print(\"Could not understand audio\")\n",
    "            engine.say('I didnt get that. Rerun the code')\n",
    "\n",
    "            engine.runAndWait()\n",
    "    if r.recognize_google(audio) in greetings:\n",
    "        random_greeting = random.choice(greetings)\n",
    "        print(random_greeting)\n",
    "        engine.say(random_greeting)\n",
    "        engine.runAndWait()\n",
    "    elif r.recognize_google(audio) in question:\n",
    "        engine.say('I am fine')\n",
    "        engine.runAndWait()\n",
    "        print('I am fine')\n",
    "    elif r.recognize_google(audio) in var1:\n",
    "        engine.say('I was made by edward')\n",
    "        engine.runAndWait()\n",
    "        reply = random.choice(var2)\n",
    "        print(reply)\n",
    "    elif r.recognize_google(audio) in cmd9:\n",
    "        print(random.choice(repfr9))\n",
    "        engine.say(random.choice(repfr9))\n",
    "        engine.runAndWait()\n",
    "    elif r.recognize_google(audio) in cmd7:\n",
    "        print(random.choice(colrep))\n",
    "        engine.say(random.choice(colrep))\n",
    "        engine.runAndWait()\n",
    "        print('It keeps changing every micro second')\n",
    "        engine.say('It keeps changing every micro second')\n",
    "        engine.runAndWait()\n",
    "    elif r.recognize_google(audio) in cmd8:\n",
    "        print(random.choice(colrep))\n",
    "        engine.say(random.choice(colrep))\n",
    "        engine.runAndWait()\n",
    "        print('It keeps changing every micro second')\n",
    "        engine.say('It keeps changing every micro second')\n",
    "        engine.runAndWait()\n",
    "    elif r.recognize_google(audio) in cmd2:\n",
    "        mixer.init()\n",
    "        mixer.music.load(\"song.wav\")\n",
    "        mixer.music.play()\n",
    "    elif r.recognize_google(audio) in var4:\n",
    "        engine.say('I am a bot, silly')\n",
    "        engine.runAndWait()\n",
    "    elif r.recognize_google(audio) in cmd4:\n",
    "        webbrowser.open('www.youtube.com')\n",
    "    elif r.recognize_google(audio) in cmd6:\n",
    "        print('see you later')\n",
    "        engine.say('see you later')\n",
    "        engine.runAndWait()\n",
    "        exit()\n",
    "    elif r.recognize_google(audio) in cmd5:\n",
    "        owm = pyowm.OWM('YOUR_API_KEY')\n",
    "        observation = owm.weather_at_place('Bangalore, IN')\n",
    "        observation_list = owm.weather_around_coords(12.972442, 77.580643)\n",
    "        w = observation.get_weather()\n",
    "        w.get_wind()\n",
    "        w.get_humidity()\n",
    "        w.get_temperature('celsius')\n",
    "        print(w)\n",
    "        print(w.get_wind())\n",
    "        print(w.get_humidity())\n",
    "        print(w.get_temperature('celsius'))\n",
    "        engine.say(w.get_wind())\n",
    "        engine.runAndWait()\n",
    "        engine.say('humidity')\n",
    "        engine.runAndWait()\n",
    "        engine.say(w.get_humidity())\n",
    "        engine.runAndWait()\n",
    "        engine.say('temperature')\n",
    "        engine.runAndWait()\n",
    "        engine.say(w.get_temperature('celsius'))\n",
    "        engine.runAndWait()\n",
    "    elif r.recognize_google(audio) in var3:\n",
    "\n",
    "        print(\"Current date and time : \")\n",
    "        print(now.strftime(\"The time is %H:%M\"))\n",
    "        engine.say(now.strftime(\"The time is %H:%M\"))\n",
    "        engine.runAndWait()\n",
    "    elif r.recognize_google(audio) in cmd1:\n",
    "        webbrowser.open('www.google.com')\n",
    "    elif r.recognize_google(audio) in cmd3:\n",
    "        jokrep = random.choice(jokes)\n",
    "        engine.say(jokrep)\n",
    "        engine.runAndWait()\n",
    "    else:\n",
    "        engine.say(\"please wait\")\n",
    "        engine.runAndWait()\n",
    "        print(wikipedia.summary(r.recognize_google(audio)))\n",
    "        engine.say(wikipedia.summary(r.recognize_google(audio)))\n",
    "        engine.runAndWait()\n",
    "        userInput3 = input(\"or else search in google\")\n",
    "        webbrowser.open_new('www.google.com/search?q=' + userInput3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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