# import Voice_to_text as vt
# import body_assistant as bs
#
# voice = 'f'
# text = ""
# not_understand = False
# while(voice != 's'):
#     if text == "$can'tsay":
#         print("  System  :- sorry could not recognize your voice")
#         text = str(input("Type text :- "))
#
#     elif not_understand == True:
#         text = str(input("Type text :- "))
#
#     else:
#         text = vt.voicetotext()
#         print("   You    :- ", text)
#     voice, not_understand = bs.body(text, voice)



from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/result',methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    print(output)
    name = output["name"]
    return render_template('index.html', name = name)

if __name__ == "__main__":
    app.run(debug=True)