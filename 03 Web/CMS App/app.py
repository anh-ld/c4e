from flask import *
from model.video import Video
import mlab
from youtube_dl import YoutubeDL

app = Flask(__name__)
mlab.connect()
app.secret_key = "atom"
ydl = YoutubeDL()

@app.route('/')
def index():
    videos = Video.objects()
    return render_template('index.html', videos = videos)

@app.route('/admin', methods = ['GET', 'POST'])
def admin():
    if request.method == 'GET':
        if "logged_in" in session:
            videos = Video.objects()
            return render_template('admin.html', videos = videos)
        else:
            return render_template("error.html")
    elif request.method == 'POST':
        form = request.form
        link = form['link']
        data = ydl.extract_info(link, download=False)
        title = data['title']
        thumbnail = data['thumbnail']
        views = data['view_count']
        youtubeid = data['id']
        new_video = Video(title = title, thumbnail = thumbnail, views = views, link = link, youtubeid = youtubeid)
        new_video.save()

        return redirect(url_for('admin'))

@app.route('/detail/<youtubeid>')
def detail(youtubeid):
    return render_template('detail.html', youtubeid = youtubeid)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']

        if username == "admin" and password == "admin":
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            return "Fail"

@app.route('/logout')
def logout():
    del session['logged_in']
    return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=True)
