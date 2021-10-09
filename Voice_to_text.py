import speech_recognition as sr

def voicetotext():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speck anything :- \n")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            text = text.lower()
            return text
        except:
            text = "sorry could not recognize your voice"
            return text