#!/usr/bin/env python
# coding: utf-8

# install cmd if environment is new
# !pip install SpeechRecognition
# !pip install googletrans==4.0.0=rc1

# imports
import speech_recognition as sr
from googletrans import Translator

def s2t_multilang(languages):
    '''
    Convert audio to text while guessing which language to correctly use.
    '''

    with sr.Microphone() as source:
        r = sr.Recognizer()
        r.adjust_for_ambient_noise(source)
        
        # read audio sample from the default microphone
        print("Say something, I'm listening...")
        audio = r.listen(source)
       
        # convert speech to text
        print("Give me a minute, busy converting speech to text...")
        lang_conf = {}
        for l in languages:
            # convert to text for languages of interests
            #print("I'm trying {}...".format(l))
            try:
                # convert speech to text using Google Speech Recognition API
                transcript = r.recognize_google(audio, language=l, show_all=True)
                # assign confidence level to corresponding languages
                lang_conf[l] = transcript['alternative'][0]
            except:
                # could not convert speech to text for specific language
                pass
           
        # sorted dict by confidence level
        lang_conf = dict(sorted(lang_conf.items(), key=lambda x: x[1]['confidence'], reverse=True))
        
        return lang_conf
        
# english, korean, vietnamese, japanese, spanish, chinese(mandarin)
languages = ['en-US', 'ko-KR', 'vi-VN', 'ja-JP', 'es-MX', 'zh']
lang_conf = s2t_multilang(languages)

# print out language with highest confidence level
lang = list(lang_conf.keys())[0]
trans = list(lang_conf.values())[0]['transcript']

# use translate to print out result in spoken language
translator = Translator()
print("\nSwitching to {}...".format(lang))

# NOTE: language codes used by the 2 libraries are different
# supported languages for SpeechRecognition: https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages
# supported languages for googletrans: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
print(translator.translate("You said '{}' in {}.".format(trans, lang), src='en', dest=lang[:2]).text)
print("You said '{}' but in {}.".format(translator.translate(trans, src=lang[:2], dest='en').text, lang))