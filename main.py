from flask import Flask
from flask import request
from wafw00f import main
import sys 
from io import StringIO  # Python 3
import os


app = Flask(__name__)
# woof = main.main()

@app.route('/'+os.environ['EF_NAME'])
def hello():
    return "Hello from Python!"

@app.route('/'+os.environ['EF_NAME'], methods = ['POST'])
def make_guess():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.get_json()
        return json
    elif (content_type == 'text/plain'):
        sample = request.data.decode("utf-8") 
        # print(sample)
        sys.argv.append(str(sample))
        print(sys.argv)
        temp_out = StringIO()
        sys.stdout = temp_out
        name = main.main()
        sys.argv.remove(str(sample))
        # print(name)
        sys.stdout = sys.__stdout__
        return(str(temp_out.getvalue()))
        # return(str(name))
    else:
        return 'Content-Type not supported!'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    
