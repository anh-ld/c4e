from flask import *
from models.service import Service
from models.user import User
from models.order import Order
from datetime import datetime
from gmail import GMail, Message
import mlab

app = Flask(__name__)
app.secret_key = "atom"
mlab.connect()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search/<int:gender>')
def search(gender):
    all_services = Service.objects(gender = gender)
    return render_template("search.html", all_services = all_services)

@app.route('/admin')
def admin():
    services = Service.objects()
    return render_template("admin.html", services = services)

@app.route('/delete/<service_id>')
def delete(service_id):
    service = Service.objects.with_id(service_id)
    if service is None:
        return render_template('base.html', result = "Not found")
    else:
        service.delete()
    return redirect(url_for('admin'))

@app.route('/new-service', methods = ['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template('new-service.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        address = form['address']
        gender = form['gender']
        phone = form['phone']
        height = form['height']
        description = form['description']
        measurements = [int(form['meas0']), int(form['meas1']), int(form['meas2'])]
        if form['status'] == "True":
            status = True
        else:
            status = False
        new_service = Service(name = name, yob = yob, address = address, gender = gender,
        phone = phone, height = height, description = description, measurements = measurements,
        status = status)
        new_service.save()
        return redirect(url_for("admin"))

@app.route('/update-service/<service_id>', methods = ['GET', 'POST'])
def update(service_id):
    service = Service.objects.with_id(service_id)
    if service == None:
        return render_template('base.html', result = "Not found")
    elif request.method == "GET":
        return render_template('update-service.html', service = service)
    elif request.method == "POST":
        form = request.form
        service.name = form['name']
        service.yob = form['yob']
        service.address = form['address']
        service.gender = form['gender']
        service.phone = form['phone']
        service.height = form['height']
        service.description = form['description']
        service.measurements = [int(form['meas0']), int(form['meas1']), int(form['meas2'])]
        if form['status'] == "True":
            service.status = True
        else:
            service.status = False

        service.save()
        return redirect(url_for("admin"))

@app.route('/detail/<service_id>', methods = ['GET', 'POST'])
def detail(service_id):
    service = Service.objects.with_id(service_id)
    if 'logged_in' in session:
        if service is None:
            return render_template('base.html', result = "Not found")
        else:
            return render_template("detail.html", service = service)
    else:
        return redirect(url_for('login'))

@app.route('/sign-up', methods = ['GET', 'POST'])
def signup():
    if request.method == "GET":
        if "logged_in" not in session:
            return render_template("signup.html")
        else:
            return render_template('base.html', result = "Pls log out before signing up an account")
    elif request.method == "POST":
        form = request.form
        f_user = User.objects(username = form['username'])
        f_user2 = User.objects(email = form['email'])
        if len(f_user) > 0:
            return render_template('base.html', result = "Username existed")
        elif len(f_user2) > 0:
            return render_template('base.html', result = "Email existed")
        else:
            new_user = User(
                name = form['name'],
                email = form['email'],
                username = form['username'],
                password = form['password']
            )
            new_user.save()
            return render_template('base.html', result = "Success")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        if "logged_in" not in session:
            return render_template("login.html")
        else:
            return render_template('base.html', result = "You have already logged in")
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']
        f_user = User.objects(username = username, password = password)
        if len(f_user) > 0:
            session['logged_in'] = True
            session['user_id'] = str(f_user[0].id)
            return render_template('base.html', result = "Logged In")
        else:
            return render_template('base.html', result = "Log In Failed. Please try again.")

@app.route('/logout')
def logout():
    if "logged_in" not in session:
        return render_template('base.html', result = "You have not logged in")
    else:
        del session['logged_in']
        del session['user_id']
        return redirect(url_for('index'))

@app.route('/order/<service_id>')
def order(service_id):
    new_order = Order(
        service_id = service_id,
        user_id = session['user_id'],
        time = datetime.now().strftime("%I:%M%p %d-%B-%Y"),
        is_accepted = False
    )
    new_order.save()
    return render_template('base.html', result = 'Da Gui Yeu Cau')

@app.route('/order-list')
def order_list():
    all_orders = Order.objects(is_accepted = False)
    return render_template("order-list.html", all_orders = all_orders)

@app.route('/edit-order/<order>')
def edit_order(order):
    f_order = Order.objects.with_id(order)
    f_order.update(set__is_accepted=True)

    gmail = GMail("duyanhle41@gmail.com","minimalism")
    html_content = """
    <p> Yêu cầu của bạn đã được xử lý, chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất. Cảm ơn bạn đã sử dụng dịch vụ của ‘Mùa Đông Không Lạnh’</p>
    """
    msg = Message('Xac nhan yeu cau',to=f_order.user_id.email,html=html_content)
    gmail.send(msg)

    return redirect(url_for('order_list'))

if __name__ == '__main__':
  app.run(debug=True)
