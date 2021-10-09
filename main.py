import Voice_to_text as vt
import body_assistant as bs

voice = 'f'

while(voice != 's'):
    text = vt.voicetotext()
    print("   You    :- ", text)
    voice = bs.body(text, voice)
