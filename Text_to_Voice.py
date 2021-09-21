import pyttsx3

def voice(text, gender=0):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if gender == 0:
        engine.setProperty('voice', voices[0].id)   #changing index, changes voices. o for male
    else:
        engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

    engine.say(text)
    engine.runAndWait()
    engine.stop()