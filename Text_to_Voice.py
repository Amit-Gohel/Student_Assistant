import pyttsx3

def voice(text, gender = 'm'):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if gender == 'm':
        engine.setProperty('voice', voices[0].id)   #changing index, changes voices. o for male
    else:
        engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
    print("Assistant :- ",text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()