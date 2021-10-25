import math
import Text_to_Voice as tv
import os
import Math_Fun as mf
import Random_function as nf


def body(text, voice = 'f'):

    # How are you
    if 'how' in text and 'are' in text and 'you' in text:
        voicetext = nf.howareyou()
        tv.voice(voicetext, gender=voice)

    # Bacis maths function
    elif '+' in text or '-' in text or 'x' in text or '/' in text:
        text = mf.bacis_split_num(text)
        answ = mf.basic_math(text)
        tv.voice(answ + '\n', gender=voice)

    # Maths Tangent function
    elif 'sin' in text:
        text = mf.tangent_function_split(text)
        answ = mf.tangent_function(text[1], 1)
        tv.voice(answ + '\n', gender=voice)
    elif 'cos' in text:
        text = mf.tangent_function_split(text)
        answ = mf.tangent_function(text[1], 2)
        tv.voice(answ + '\n', gender=voice)
    elif 'tan' in text:
        text = mf.tangent_function_split(text)
        print(text[1])
        if int(text[1]) == 90:
            tv.voice('Something went wrong\n', gender=voice)
        else:
            answ = mf.tangent_function(text[1], 3)
            tv.voice(answ + '\n', gender=voice)
    elif 'cosec' in text:
        text = mf.tangent_function_split(text)
        answ = mf.tangent_function(text[1], 4)
        tv.voice(answ + '\n', gender=voice)
    elif 'sec' in text:
        text = mf.tangent_function_split(text)
        answ = mf.tangent_function(text[1], 5)
        tv.voice(answ + '\n', gender=voice)
    elif 'cot' in text:
        text = mf.tangent_function_split(text)
        answ = mf.tangent_function(text[1], 6)
        tv.voice(answ + '\n', gender=voice)

    # Maths factorial function
    elif 'factorial' in text:
        text = text.split(" ")
        try:
            ans = math.factorial(int(text[-2]))
            tv.voice(f'Answer of {text[-2]} factorial is {ans}\n', gender=voice)
        except:
            ans = math.factorial(int(text[-1]))
            tv.voice(f'Answer of log {text[-1]} factorial is {ans}\n', gender=voice)

    # Maths log function
    elif 'log' in text:
        text = text.split(" ")
        try:
            ans = math.log(float(text[-1]), 10)
            ans = "{:.2f}".format(ans)
            tv.voice(f'Answer of log {text[-1]} is {ans}\n', gender=voice)
        except:
            tv.voice(f'Something went wrong.\n', gender=voice)

    # Maths Root function
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

    # Joke function
    elif 'tell' in text and 'me' in text and 'joke' in text:
        voicetext = nf.joke()
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

    # Open certificate function
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

    # If assistant dose not understand
    else:
        tv.voice("Sorry, I'm having trouble understanding.\n", gender=voice)

    return voice

