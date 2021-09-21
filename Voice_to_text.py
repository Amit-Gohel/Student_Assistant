import speech_recognition as sr

def voiceTotext():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speck anything : ")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            return text
        except:
            text = "sorry could not recognize your voice"
            return text