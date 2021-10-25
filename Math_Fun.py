import math

# calculated function
# Basic maths function
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


# maths tangent function
def tangent_function(text, num):
    try:
        if num == 1:
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


# Split function
# get number from bacis function sentence
def bacis_split_num(text):
    if 'sum of ' in text:
        text = text.split('sum of ')
    elif 'value of' in text:
        text = text.split('value of ')
    elif 'value' in text:
        text = text.split('value')
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
    if type(text) == list:
        return text[1]
    return text

# get number from tangent function sentence
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
