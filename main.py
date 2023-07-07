#Importing dependencies 
import pyttsx3
import speech_recognition as sr
from googletrans import Translator 
from langdetect import detect

#Creating instances of the required classes 
translator = Translator(service_urls=['translate.google.com'])
recogniser = sr.Recognizer()
text_to_speech = pyttsx3.init()

#Main logic
while True:
    with sr.Microphone() as source:
        print("Speak to translate...")
        recogniser.adjust_for_ambient_noise(source)
        audio = recogniser.listen(source)
    try:
        text = recogniser.recognize_google(audio)
        input_language = detect(text)
        if input_language == "de":
            translation = translator.translate(text, dest='en')
            print(f"You said: {translation.text}")
            text_to_speech.say(translation.text)
            text_to_speech.runAndWait()
        elif input_language == "es":
            translation = translator.translate(text, dest='en')
            print(f"You said: {translation.text}")
            text_to_speech.say(translation.text)
            text_to_speech.runAndWait()
        elif input_language == "fr":
            translation = translator.translate(text, dest='en')
            print(f"You said: {translation.text}")
            text_to_speech.say(translation.text)
            text_to_speech.runAndWait()
        elif input_language == "ml":
            translation = translator.translate(text, dest='en')
            print(f"You said: {translation.text}")
            text_to_speech.say(translation.text)
            text_to_speech.runAndWait()
        elif input_language == "pt-BR":
            translation = translator.translate(text, dest='en')
            print(f"You said: {translation.text}")
            text_to_speech.say(translation.text)
            text_to_speech.runAndWait()
        elif input_language == "hi":
            translation = translator.translate(text, dest='en')
            print(f"You said: {translation.text}")
            text_to_speech.say(translation.text)
            text_to_speech.runAndWait()
        elif input_language == "ja":
            translation = translator.translate(text, dest='en')
            print(f"You said: {translation.text}")
            text_to_speech.say(translation.text)
            text_to_speech.runAndWait()
        elif input_language == "zh-CN":
            translation = translator.translate(text, dest='en')
            print(f"You said: {translation.text}")
            text_to_speech.say(translation.text)
            text_to_speech.runAndWait()
        else:
            print("Language is unsupported at the moment...")
    except sr.UnknownValueError:
        print("Please try again...")
    except sr.RequestError as a:
        print(f"Unknown error occured: {a}")