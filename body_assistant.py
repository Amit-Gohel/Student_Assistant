import Text_to_Voice as tv

def body(text):
    if 'how' in text and 'are' in text and 'you' in text:
        tv.voice("I am fine.\nHow are you..")

    elif 'stop assistant' in text:
        return 0

    elif 'hi' in text or 'hello' in text or 'hey' in text or 'hay' in text or 'hai' in text:
        tv.voice("hi, i am student assistant.\nhow can I help you??")

    return 1