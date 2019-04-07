from flask import Flask, render_template
from models.service import Service
import mlab

app = Flask(__name__)
mlab.connect()


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search/<int:gender>')
def search(gender):

    all_services = Service.objects(gender = gender, yob__lte = 1998, address__iexact = "Ha Noi")
    return render_template("search.html", all_services = all_services)

if __name__ == '__main__':
  app.run(debug=True)
