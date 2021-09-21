import pyttsx3

def Voice(text):
    text_speech = pyttsx3.init()

    answer = text
    text_speech.say(answer)
    text_speech.runAndWait()