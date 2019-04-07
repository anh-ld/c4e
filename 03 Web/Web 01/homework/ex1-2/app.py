from flask import Flask, render_template
app = Flask(__name__)

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight, height):
    height = height / 100
    bmi = round(weight / (height ** 2),3)
    return render_template("bmi.html", bmi = bmi)

if __name__ == "__main__":
    app.run(debug = True)
