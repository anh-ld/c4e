from flask import Flask, render_template, redirect
app = Flask(__name__)

users = {
    "quy" : {
        "name" : "Dinh Cong Quy",
        "age" : 20,
        "gender": 1,
        "hobby": "programming"
    },
    "tuananh" : {
        "name" : "Huynh Tuan Anh",
        "age" : 22,
        "gender" : 1,
        "hobby" : "programming"
    },
    "chi" : {
        "name" : "Pham Thuc Chi",
        "age" : 23,
        "gender" : 0,
        "hobby" : "teaching English"
    },
}

@app.route("/user/<username>")
def user(username):
    if username in users:
        return render_template("users.html", users = users[username])
    else:
        return "User not found!"

if __name__ == "__main__":
    app.run(debug = True)
