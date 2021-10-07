import Voice_to_text as vt
import body_assistant as bs

stop = 1

while(stop):
    text = vt.voicetotext()
    print(text)
    stop = bs.body(text)
