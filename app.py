from flask import Flask, jsonify # import main Flask class. Jsonfiy for the response, not necessary.
import os # To check if file exist
path='/counterpath/counter.txt'

if not os.path.exists(path): #Check if file exist, if not - create it and put a 0 in it
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write("0")

# create the Flask app
app = Flask(__name__)
@app.route('/', methods = ['POST']) #Post request part of the app
def content(): 
    with open(path, "r") as file: #Read the file to get the current number
        increment = int(file.read())
    with open(path, "w") as filewrite: #Write new number to file
        incrementTotal = increment + 1 
        filewrite.write(str(incrementTotal))
        resp = jsonify(success=True)
        return resp

@app.route('/', methods = ['GET']) #Get request part of the app
def read(): 
    with open(path, "r") as file:
        total = file.read()
        return total

if __name__ == '__main__':
    # run app in debug mode on port 80
    app.run(debug=True, port=80)