import pytest
from loan import app 

@pytest.fixture
def client():
    return app.test_client() #client acts as a dummy live server

def test_home(client):
    resp = client.get("/") #sends a get request to the home endpoint
    assert resp.status_code == 200
    assert resp.text == "<h1> Loan Approval Application </h1>"
    
def test_predict(client):
    test_data = {
    "ApplicantIncome":100,
    "Credit_History": 1,
    "Gender": "Male",
    "LoanAmount" : 120,
    "Married" : "No" 
    }
    resp = client.post("/predict", json=test_data)
    assert resp.status_code == 200
    assert resp.json == {"Loan_Status": "Approved"}