import Text_to_Voice as tv
import os

def body(text, voice = 'f'):

    # How are you
    if 'how' in text and 'are' in text and 'you' in text:
        tv.voice("I'm tickety-boo.\nHow's your day going?", gender=voice)

    # change voice
    elif 'change' in text and 'voice' in text:
        if voice == 'm':
            tv.voice("Here's an example of one of my other voices.\nI will be happy to help you.", gender='f')
            return 'f'
        else:
            tv.voice("Here's an example of one of my other voices.\nI will be happy to help you.", gender='m')
            return 'm'

    elif 'open' in text and 'certificate' in text:
        os.system('Assets\GOOGEL_CODE_COMPETITION.pdf')
        tv.voice("Here's your certificate", gender=voice)
        return 's'

    # stop assistant
    elif 'stop' in text and 'assistant' in text:
        tv.voice("Thank you.. We will meet soon.", gender=voice)
        return 's'

    # hi hello answers
    elif 'hi' in text or 'hello' in text or 'hey' in text or 'hay' in text or 'hai' in text:
        tv.voice("Hii, I hope your day goes great.\nI'm  always here if you need me.", gender=voice)

    else:
        tv.voice("Sorry, I'm having trouble understanding.", gender=voice)
    return voice




 # elif ('show' in text or 'search' in text) and ('images' in text or 'image' in text):
 #        print(text)
 #        # googlesearch-python
