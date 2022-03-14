from flask import Flask
from flask import request
from guesslang import Guess

app = Flask(__name__)
guess = Guess()

@app.route("/")
def hello():
    return "Hello from Python!"

@app.route('/', methods = ['POST'])
def make_guess():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.get_json()
        return json
    elif (content_type == 'text/plain'):
        sample = request.data
        print(sample)
        name = guess.language_name(sample)
        print(name)
        return(name)
    else:
        return 'Content-Type not supported!'

def run():
    app.run(host='0.0.0.0')

if __name__ == "__main__":
    run()
