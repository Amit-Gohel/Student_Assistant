import math

def basic_math(text):
    text = text.split(" ")
    x = 1
    answ = 0
    try:
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
        answ = f'the answer of given exam is {answ}'
    except:
        answ = "Something went wrong"

    return answ


def sin(text):
    pass


def cos(text):
    pass


def tan(text):
    pass


def cosin(text):
    pass


def sec(text):
    pass


def cot(text):
    pass


def factorial(text):
    pass


def log(text):
    pass


def root(text):
    pass




# do work for -input.
