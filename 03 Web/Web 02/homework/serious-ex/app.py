from flask import Flask, render_template
from models.customer import Customer
import mlab

app = Flask(__name__)
mlab.connect()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/customer')
def customer():
    all_customers = Customer.objects()
    return render_template('customer.html', all_customers = all_customers)

@app.route('/male')
def search():
    customers = Customer.objects(gender = 1, contacted = False)[:10]
    return render_template("male.html", customers = customers)

if __name__ == '__main__':
  app.run(debug=True)
