import math

def basic_math(text):
    text = text.split(" ")
    x = 1
    answ = 0
    try:
        if text[x+1] == '-':
            del text[x+1]
            text[x+1] = -float(text[x+1])

        if text[x] == '+':
            answ = float(text[x - 1]) + float(text[x + 1])
        elif text[x] == '-':
            answ = float(text[x - 1]) - float(text[x + 1])
        elif text[x] == 'x':
            answ = float(text[x - 1]) * float(text[x + 1])
        elif text[x] == '/':
            answ = float(text[x - 1]) / float(text[x + 1])
        x = x + 2

        while (x < len(text)):
            if text[x + 1] == '-':
                del text[x + 1]
                text[x + 1] = -float(text[x + 1])

            if text[x] == '+':
                answ = answ + float(text[x + 1])
            elif text[x] == '-':
                answ = answ - float(text[x + 1])
            elif text[x] == 'x':
                answ = answ * float(text[x + 1])
            elif text[x] == '/':
                answ = answ / float(text[x + 1])
            x = x + 2
        answ = "{:.2f}".format(answ)
        answ = f'The answer of given equation is {answ}.'
    except:
        answ = "Something went wrong"

    return answ


def tangent_function(text, num):
    try:
        if num == 1:
            print(int(text))
            answ = math.sin(math.radians(int(text)))
        elif num == 2:
            answ = math.cos(math.radians(int(text)))
        elif num == 3:
            answ = math.tan(math.radians(int(text)))
        elif num == 4:
            answ = 1/math.sin(math.radians(int(text)))
        elif num == 5:
            answ = 1/math.cos(math.radians(int(text)))
        elif num == 6:
            answ = 1/math.tan(math.radians(int(text)))

        answ = "{:.2f}".format(answ)
        return f"The answer is {answ}."
    except:
        return "Something went wrong."



