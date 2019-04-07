from flask import Flask
app = Flask(__name__)

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight, height):
    height = height / 100
    bmi = round(weight / (height ** 2),3)

    if bmi < 16:
        result = "Severely underweight"
    elif bmi < 18.5:
        result = "Underweight"
    elif bmi < 25:
        result = "Normal"
    elif bmi < 30:
        result = "Overweight"
    else:
        result = "Obese"

    return "BMI = {}. Your condition: {}".format(bmi,result)

if __name__ == "__main__":
    app.run(debug = True)
