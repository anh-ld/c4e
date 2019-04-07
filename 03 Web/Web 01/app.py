from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts = [
        {
            "title" : "Thơ con chó",
            "content" : """Hôm nay trăng lên cao quá,
                        anh muốn hôn em vào má""",
            "author" : "Tuấn Anh",
            "gender" : 1
        },
        {
            "title" : "Thơ con mèo",
            "content" : """Hôm nay trăng lên cao tít,
                        anh muốn hôn em vào má""",
            "author" : "Quý",
            "gender" : 1
        },
        {
            "title" : "Không biết làm thơ",
            "content" : "Tóc Đức gội đầu ntn?",
            "author" : "Hồng Anh",
            "gender" : 0
        }
    ]
    return render_template("index.html", posts = posts)

@app.route("/hello")
def hello():
    return "Hello C4E16"

@app.route("/sayhi/<name>/<age>")
def sayhi(name, age):
    return "Hi " + name + ". You're " + age

@app.route("/sum/<int:num1>/<int:num2>")
def sum(num1, num2):
    return str(num1 + num2)

if __name__ == '__main__':
  app.run(debug=True)
