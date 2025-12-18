from flask import Flask, request
import pickle
import sklearn

#main variable to use
app = Flask(__name__)

with open("classifierr.pkl", "rb") as f:
    model = pickle.load(f)

#start creating the endpoints 

@app.route("/predict", methods=['GET'])
def hello():
    return "<h1> Loan Approval Application </h1>"

@app.route("/predict", methods=['POST'])
def predict():
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
    CreditHistory = loan_req["CreditHistory"]
    LoanAmount = loan_req["LoanAmount"]
    
    input_data = [[gender, married, ApplicantIncome, CreditHistory, LoanAmount]]
    
    prediction = model.predict(input_data)

    return "Loan Approved" if prediction[0] == 1 else "Loan Not Approved"