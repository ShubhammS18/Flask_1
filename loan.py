from flask import Flask, request
import pickle
import sklearn

#main variable to use
app = Flask(__name__)

with open("classifierr.pkl", "rb") as f:
    model = pickle.load(f)

#start creating the endpoints 

@app.route("/", methods=['GET'])
def hello():
    return "<h1> Loan Approval Application </h1>"

@app.route("/predict", methods=['GET'])
def predict():
    return "<h1> i will make the predictions </h1>"

@app.route("/predict", methods=['POST'])
def predict_post():
    loan_req = request.get_json()
    
    if loan_req["Gender"] == "Male":
        gender = 0
    else:
        gender = 1
    if loan_req["Married"] == "No":
        married = 0
    else:
        married = 1
    
    ApplicantIncome = loan_req["ApplicantIncome"]
    Credit_History = loan_req["Credit_History"]
    LoanAmount = loan_req["LoanAmount"]

    input_data = [[gender, married, ApplicantIncome, Credit_History, LoanAmount]]

    res = model.predict(input_data)
    
    if res[0] == 1:
        prediction = "Approved"
    else:
        prediction = "Rejected"

    return {"Loan_Status": prediction}