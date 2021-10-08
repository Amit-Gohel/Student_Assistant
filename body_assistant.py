import Text_to_Voice as tv

def body(text, voice = 'f'):

    # How are you
    if 'how' in text and 'are' in text and 'you' in text:
        tv.voice("I am fine.\nHow are you..", gender=voice)

    # change voice
    elif 'change' in text and 'voice' in text:
        if voice == 'm':
            tv.voice("I am changing my voice", gender='f')
            return 'f'
        else:
            tv.voice("I am changing my voice", gender='m')
            return 'm'

    # stop assistant
    elif 'stop assistant' in text:
        tv.voice("Thank you.. We will meet soon.", gender=voice)
        return 's'

    # hi hello answers
    elif 'hi' in text or 'hello' in text or 'hey' in text or 'hay' in text or 'hai' in text:
        tv.voice("hi, i am student assistant.\nhow can I help you??", gender=voice)

    return voice




 # elif ('show' in text or 'search' in text) and ('images' in text or 'image' in text):
 #        print(text)
 #        # googlesearch-python
