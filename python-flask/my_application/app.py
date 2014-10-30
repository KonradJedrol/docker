from flask import Flask
from flask import request
import os, sys
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

@app.route('/listfiles')
def listfiles():
    path = "./uploads/"
    dirs = os.listdir( path )
    f_str=""
    for name in dirs:
        f_str +=(str)(name)+"\n"
    return f_str

@app.route('/euler1')
def run_euler1():
  sum = 0
  for i in range (1, 1000):
    if i%3 or i%5:
    sum = sum + i
  return sum(str)