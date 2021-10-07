from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_word():
    return 'Hello Student!!!'


@app.route('/student1/')
def hello_word1():
    return 'student 1!'

@app.route('/student2/')
def hello_word2():
    return 'student 2!'

if __name__ == "__main__":
    app.run(debug=True)