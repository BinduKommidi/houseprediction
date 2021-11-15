#import Flask 

#import Flask
from flask import Flask, render_template
import joblib

import numpy as np

#create an instance of Flask
app = Flask(__name__)



import pickle
#loaded_model = pickle.load(open("Linearmodel.pkl", 'rb'))

@app.route('/')
def home():
    return render_template('home.html')



def housepredict(location,area,size,bath,balcony,total_sqft):
    print('HELLO')
    output = np.zeros(151)
    output[0] = total_sqft
    output[1] = bath
    output[2] = balcony
    output[3] = size
    #file = open("Linearmodel.pkl","rb")
    print('HH')
    print('HEHAHA')
    file = open("Linearmodel.pkl","rb")
    
    #load trained model
    trained_model = joblib.load(file)
    print('Model not loading')
    print('Sandeep')
    # result_location = location
    # if result_location not in location_cat:
    #     output[146] = 1
    # else:
    #     output[index_dict[str(location)]] = 1
    
    return trained_model.predict([output])[0] 

#import Flask
from flask import Flask, render_template, request
@app.route('/predict/', methods=['GET','POST'])



def predict():
    if request.method == "POST":

        #get form data
        location_ = request.form.get('location')
        print(location_)
        area_type_ = request.form.get('area_type')
        size_ = request.form.get('size')
        no_of_bathrooms_ = request.form.get('no_of_bathrooms')
        no_of_bacolnies_ = request.form.get('no_of_bacolnies')
        tsqft_ = request.form.get('tsqft')
        print(tsqft_)

        try:
            print('sri')
            prediction = housepredict(location_,area_type_,size_,no_of_bathrooms_,no_of_bacolnies_,tsqft_)
            print(prediction)
            print("prediction")
            #pass prediction to template
            return render_template('predict.html', prediction = prediction)
        
        #return render_template('predict.html')
        except:
            return render_template('predict.html', prediction = "Something went wrong!!")








if __name__ == '__main__':
    app.run(debug=True)