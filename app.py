from flask import Flask,request,render_template
from utils import hpp


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict',methods = ['POST'])
def predict():
    data = request.form
    hpp_obj = hpp(data)
    result = hpp_obj.predict()
    print("results is:",result)
   
    #return render_template('index.html',pred = result)
    return render_template('result.html',pred = result)



    

if __name__ == "__main__":
    app.run(debug = True) 