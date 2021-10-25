import random


# joke function
def joke():
    list = ["Why did the picture go to jail?\n              Because it was framed.\n",
            "What do horses say when they fall?\n              Help, I’ve fallen and I can’t giddy up.\n",
            "What do you call shoes made of banana peels?\n              Slippers.\n",
            "Why did the bicycle collapse?\n              It was two tired.\n",
            "Why did the restaurant hire a pig?\n              He was good at bacon.\n"]
    return random.choice(list)


# how are you reply function
def howareyou():
    list = ["I'm tickety-boo.\n              How's your day going?\n",
            "I'm totally fine.\n              What about you?\n",
            "I'm good.\n              I hope that you are staying safe.\n",
            "I would say I am navigating somewhere between good and better.\n",
            "I'm quite fine. Thanks for asking.\n"]
    return random.choice(list)
