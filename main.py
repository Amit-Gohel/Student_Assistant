import Voice_to_text as vt
import body_assistant as bs

voice = 'f'
text = ""
not_understand = False
while(voice != 's'):
    if text == "$can'tsay":
        print("  System  :- sorry could not recognize your voice")
        text = str(input("Type text :- "))

    elif not_understand == True:
        text = str(input("Type text :- "))

    else:
        text = vt.voicetotext()
        print("   You    :- ", text)
    voice, not_understand = bs.body(text, voice)
