import math

import Text_to_Voice as tv
import os
import random
import Math_Fun as mf

def body(text, voice = 'f'):

    # How are you
    if 'how' in text and 'are' in text and 'you' in text:
        voicetext = howareyou()
        tv.voice(voicetext, gender=voice)

    elif '+' in text or '-' in text or 'x' in text or '/' in text:
        text = bacis_split_num(text)
        answ = mf.basic_math(text[1])
        tv.voice(answ + '\n', gender=voice)

    elif 'sin' in text and ('answer' in text or 'value' in text):
        text = tangent_function_split(text)
        answ = mf.tangent_function(text[1], 1)
        tv.voice(answ + '\n', gender=voice)
    elif 'cos' in text and ('answer' in text or 'value' in text):
        text = tangent_function_split(text)
        answ = mf.tangent_function(text[1], 2)
        tv.voice(answ + '\n', gender=voice)
    elif 'tan' in text and ('answer' in text or 'value' in text):
        text = tangent_function_split(text)
        answ = mf.tangent_function(text[1], 3)
        tv.voice(answ + '\n', gender=voice)
    elif 'cosec' in text and ('answer' in text or 'value' in text):
        text = tangent_function_split(text)
        answ = mf.tangent_function(text[1], 4)
        tv.voice(answ + '\n', gender=voice)
    elif 'sec' in text and ('answer' in text or 'value' in text):
        text = tangent_function_split(text)
        answ = mf.tangent_function(text[1], 5)
        tv.voice(answ + '\n', gender=voice)
    elif 'cot' in text and ('answer' in text or 'value' in text):
        text = tangent_function_split(text)
        answ = mf.tangent_function(text[1], 6)
        tv.voice(answ + '\n', gender=voice)

    elif 'factorial' in text and ('answer' in text or 'value' in text):
        text = text.split(" ")
        try:
            ans = math.factorial(int(text[-2]))
            tv.voice(f'Answer of {text[-2]} factorial is {ans}\n', gender=voice)
        except:
            ans = math.factorial(int(text[-1]))
            tv.voice(f'Answer of log {text[-1]} factorial is {ans}\n', gender=voice)

    elif 'log' in text and ('answer' in text or 'value' in text):
        text = text.split(" ")
        ans = math.log(float(text[-1]), 10)
        ans = "{:.2f}".format(ans)
        tv.voice(f'Answer of log {text[-1]} is {ans}\n', gender=voice)

    elif 'root' in text:
        text = text.split(" ")
        ans = math.sqrt(float(text[-1]))
        ans = "{:.2f}".format(ans)
        tv.voice(f'Answer of root {text[-1]} is {ans}\n', gender=voice)

    # introduction line
    elif ('your' in text and 'introduction' in text) or ('introduce' in text and 'yourself' in text) or ('who' in text and 'are' in text and 'you' in text):
        tv.voice("Hii, I am Student Assistant.\n              "
                 "I will help you in study.\n              "
                 "You can ask me anything.\n", gender=voice)

    elif 'tell' in text and 'me' in text and 'joke' in text:
        voicetext = joke()
        tv.voice(voicetext, gender=voice)

    # change voice
    elif 'change' in text and 'voice' in text:
        if voice == 'm':
            tv.voice("Here's an example of one of my other voices.\n              "
                     "I will be happy to help you.\n", gender='f')
            return 'f'
        else:
            tv.voice("Here's an example of one of my other voices.\n              "
                     "I will be happy to help you.\n", gender='m')
            return 'm'

    elif 'open' in text and 'certificate' in text:
        os.system('Assets\GOOGEL_CODE_COMPETITION.pdf')
        tv.voice("Here's your certificate\n", gender=voice)
        return 's'

    # stop assistant
    elif ('stop' in text or 'store' in text or 'top' in text) and 'assistant' in text:
        tv.voice("Thank you.. We will meet soon.\n", gender=voice)
        return 's'

    # hi hello answers
    elif 'hi' in text or 'hello' in text or 'hey' in text or 'hay' in text or 'hai' in text:
        tv.voice("Hii, I hope your day goes great.\n              "
                 "I'm  always here if you need me.\n", gender=voice)

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

def joke():
    list = ["Why did the picture go to jail?\n              Because it was framed.\n",
            "What do horses say when they fall?\n              Help, I’ve fallen and I can’t giddy up.\n",
            "What do you call shoes made of banana peels?\n              Slippers.\n",
            "Why did the bicycle collapse?\n              It was two tired.\n",
            "Why did the restaurant hire a pig?\n              He was good at bacon.\n"]
    return random.choice(list)


def bacis_split_num(text):
    if 'sum of ' in text:
        text = text.split('sum of ')
    elif 'subtraction of' in text:
        text = text.split('subtraction of ')
    elif 'multiplication of' in text:
        text = text.split('multiplication of ')
    elif 'division of' in text:
        text = text.split('division of ')
    elif 'answer of' in text:
        text = text.split('answer of ')
    elif 'equation is' in text:
        text = text.split('equation is ')
    elif 'equation' in text:
        text = text.split('equation')
    elif 'answer' in text:
        text = text.split('answer')

    elif 'sum' in text:
        text = text.split('sum ')
    elif 'subtraction' in text:
        text = text.split('subtraction ')
    elif 'multiplication' in text:
        text = text.split('multiplication ')
    elif 'division' in text:
        text = text.split('division ')
    return text

def tangent_function_split(text):
    if 'sin' in text:
        text = text.split('sin ')
    elif 'cos' in text:
        text = text.split('cos ')
    elif 'cosin' in text:
        text = text.split('cosin ')
    elif 'tan' in text:
        text = text.split('tan ')
    elif 'cosec' in text:
        text = text.split('cosec ')
    elif 'sec' in text:
        text = text.split('sec ')
    elif 'cot' in text:
        text = text.split('cot ')
    return text

# elif ('show' in text or 'search' in text) and ('images' in text or 'image' in text):
 #        print(text)
 #        # googlesearch-python
