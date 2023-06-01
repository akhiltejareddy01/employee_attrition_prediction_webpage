from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
from sklearn.preprocessing import RobustScaler
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("E:/HR analytics and prediction/Pickle Files/stc_model", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Total Stops
        EnvironmentSatisfaction = int(request.form["EnvironmentSatisfaction"])
        # print(Total_stops)
        JobInvolvement = int(request.form["JobInvolvement"])

        JobRole = int(request.form["JobRole"])

        JobSatisfaction = int(request.form["JobSatisfaction"])

        StockOptionLevel = int(request.form["StockOptionLevel"])

        WorkLifeBalance = int(request.form["WorkLifeBalance"])

        DistanceFromHome = int(request.form["DistanceFromHome"])

        Age = int(request.form["Age"])

        NumCompaniesWorked = int(request.form["NumCompaniesWorked"])

        PercentSalaryHike = int(request.form["PercentSalaryHike"])

        DailyRate = float(request.form["DailyRate"])

        MonthlyIncome = float(request.form["MonthlyIncome"])

        TotalWorkingYears = int(request.form["TotalWorkingYears"])

        YearsAtCompany = int(request.form["YearsAtCompany"])

        YearsInCurrentRole = int(request.form["YearsInCurrentRole"])

        EducationField=request.form['EducationField']
        if(EducationField=='Human Resources'):
            EducationField_Human_Resources = 1
            EducationField_Life_Sciences = 0
            EducationField_Marketing = 0
            EducationField_Medical = 0
            EducationField_Other= 0
            EducationField_Technical_Degree = 0

        elif (EducationField=='Life Sciences'):
            EducationField_Human_Resources = 0
            EducationField_Life_Sciences = 1
            EducationField_Marketing = 0
            EducationField_Medical = 0
            EducationField_Other= 0
            EducationField_Technical_Degree = 0

        elif (EducationField=='Marketing'):
            EducationField_Human_Resources = 0
            EducationField_Life_Sciences = 0
            EducationField_Marketing = 1
            EducationField_Medical = 0
            EducationField_Other= 0
            EducationField_Technical_Degree = 0
            
        elif (EducationField=='Medical'):
            EducationField_Human_Resources = 0
            EducationField_Life_Sciences = 0
            EducationField_Marketing = 0
            EducationField_Medical = 1
            EducationField_Other= 0
            EducationField_Technical_Degree = 0
            
        elif (EducationField=='Others'):
            EducationField_Human_Resources = 0
            EducationField_Life_Sciences = 0
            EducationField_Marketing = 0
            EducationField_Medical = 0
            EducationField_Other= 1
            EducationField_Technical_Degree = 0
            
        else:
            EducationField_Human_Resources = 0
            EducationField_Life_Sciences = 0
            EducationField_Marketing = 0
            EducationField_Medical = 0
            EducationField_Other= 0
            EducationField_Technical_Degree = 1

        MaritalStatus = request.form["MaritalStatus"]
        if (MaritalStatus == 'Single'):
            MaritalStatus_Single = 1
            MaritalStatus_Divorced = 0
            MaritalStatus_Married = 0

        elif (MaritalStatus == 'Married'):
            MaritalStatus_Single = 0
            MaritalStatus_Divorced = 0
            MaritalStatus_Married = 1

        else:
            MaritalStatus_Single = 0
            MaritalStatus_Divorced = 1
            MaritalStatus_Married = 0

        OverTime = request.form["OverTime"]
        if (OverTime == 'Yes'):
            OverTime_Yes = 1
            OverTime_No = 0

        else:
            OverTime_Yes = 0
            OverTime_No = 1
            
        prediction=model.predict([[
            Age,
            DistanceFromHome,
            EnvironmentSatisfaction,
            JobInvolvement,
            JobRole,
            JobSatisfaction,
            NumCompaniesWorked,
            PercentSalaryHike,
            StockOptionLevel,
            TotalWorkingYears,
            WorkLifeBalance,
            YearsAtCompany,
            YearsInCurrentRole,
            EducationField_Human_Resources,
            EducationField_Life_Sciences,
            EducationField_Marketing,
            EducationField_Medical,
            EducationField_Other,
            EducationField_Technical_Degree,
            MaritalStatus_Divorced,
            MaritalStatus_Married,
            MaritalStatus_Single,
            OverTime_No,
            OverTime_Yes,
            DailyRate,
            MonthlyIncome           
        ]])
          
        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Employee Attrition is {}, Where 1 is employee willing to leave, 0 is employee not willing to leave the company".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
