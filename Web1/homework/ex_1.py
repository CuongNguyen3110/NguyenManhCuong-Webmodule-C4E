from flask import Flask, render_template

bmi_condition = Flask(__name__)

@bmi_condition.route("/bmi/<int:weight>/<int:height>")
def bmi(weight, height):
    bmi = weight / (height/100) ** 2
    if bmi < 16:
        condition = "Severely underweight"
    elif 16 <= bmi < 18.5:
        condition = "Underweight"
    elif 18.5 <= bmi < 25:
        condition = "Normal"
    elif 25 <= bmi < 30:
        condition = "Overweight"
    else:
        condition = "Obese"
    return render_template("bmi.html", bmi=bmi, condition=condition)

if __name__ == "__main__":
    bmi_condition.run(debug=True)