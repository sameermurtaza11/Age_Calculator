from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__, template_folder='F:\Python CODE\CODE_002')

@app.route('/')
def index():
    return render_template('age_calculator.html')

@app.route('/submit', methods=['POST'])
def submit():
    birthdate = request.form.get('birthdate')
    CurrentD = request.form.get('currentdate')
    
    
    # Parse the birthdate and current date strings into datetime objects
    DateOfBirth = datetime.strptime(birthdate, "%Y-%m-%d")
    CurrentDate = datetime.strptime(CurrentD, "%Y-%m-%d")
    
    # Calculate the difference between the CurrentDate and DateOfBirth
    delta = CurrentDate - DateOfBirth

    # Calculation of Age in Years, Months, and Days
    Years = delta.days / 365.25
    Months = (Years - int(Years)) * 12
    Days = ((Months - int(Months)) * 30.4375)
    YMD = f"{int(Years)} Years {int(Months)} Months and {int(Days)} Days"
    
    # Calculation of Age in Months, and Days
    Months_2 = delta.days / 30.4375
    Days_2 = (Months_2 - int(Months_2)) * 30.4375
    MD = f"{int(Months_2)} Months {int(Days_2)} Days"
    
    # Calculation of Age in Weeks, and Days
    Weeks = Months_2 * 4.3482
    Days_3 = (Weeks - int(Weeks)) * 7
    WD = f"{int(Weeks)} Weeks {int(Days_3)} Days"
    
    # Calculation of Age in Days
    Days_4 = delta.days
    D = f"{Days_4} Days"
    
    
    return render_template('age_calculator.html', YMD = YMD, MD = MD, WD = WD, D = D)

    # return f" {delta.days} and {Years} and {Months} and {Days}"

if __name__ == '__main__':
    app.run(debug=True)
