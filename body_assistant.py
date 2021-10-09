import Text_to_Voice as tv
import os
import random

def body(text, voice = 'f'):

    # How are you
    if 'how' in text and 'are' in text and 'you' in text:
        voicetext = howareyou()
        tv.voice(voicetext, gender=voice)

    # change voice
    elif 'change' in text and 'voice' in text:
        if voice == 'm':
            tv.voice("Here's an example of one of my other voices.\n              I will be happy to help you.\n", gender='f')
            return 'f'
        else:
            tv.voice("Here's an example of one of my other voices.\n              I will be happy to help you.\n", gender='m')
            return 'm'

    elif 'open' in text and 'certificate' in text:
        os.system('Assets\GOOGEL_CODE_COMPETITION.pdf')
        tv.voice("Here's your certificate\n", gender=voice)
        return 's'

    # stop assistant
    elif 'stop' in text and 'assistant' in text:
        tv.voice("Thank you.. We will meet soon.\n", gender=voice)
        return 's'

    # hi hello answers
    elif 'hi' in text or 'hello' in text or 'hey' in text or 'hay' in text or 'hai' in text:
        tv.voice("Hii, I hope your day goes great.\n              I'm  always here if you need me.\n", gender=voice)

    else:
        tv.voice("Sorry, I'm having trouble understanding.\n", gender=voice)
    return voice



def howareyou():
    list = ["I'm tickety-boo.\n              How's your day going?\n",
            "I'm totally fine.\n              What about you?\n",
            "I'm good.\n              I hope that you are staying safe.\n",
            "I would say I am navigating somewhere between good and better.\n",
            "I'm quite fine. Thanks for asking.\n"]
    return random.choice(list)

 # elif ('show' in text or 'search' in text) and ('images' in text or 'image' in text):
 #        print(text)
 #        # googlesearch-python
