import speech_recognition as sr

def voicetotext():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak anything :- \n")
        audio = r.listen(source, phrase_time_limit=8)

        try:
            text = r.recognize_google(audio)
            text = text.lower()
            return text
        except:
            text = "$can'tsay"
            return text