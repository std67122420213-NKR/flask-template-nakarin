from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    title = 'Home Page'
    return render_template('index.html',title='My Home Page')

@app.route('/about')
def about():
    title = 'About Page'
    name = 'Nakarin Chaleekeaw'
    email = 'std.67122420213@ubru.ac.th'
    mobile = '089-721xxxx'
    age = 20
    return render_template('about.html', title=title,
                           name=name,
                           email=email,
                           mobile=mobile,
                           age=age)

@app.route('/favorite/foods')
def favorite_foods():
    title = 'Favorite Foods Page'
    foods = ['ข้าวผัด','หมูกรอบ','บะหมี่']
    return render_template('favorite_foods.html',
                           title=title,
                           foods=foods)

@app.route('/favorite/sports')
def favorite_sports():
    title = 'Favorite Sports Page'
    sports = ['ฟุตบอล','บาสเก็ตบอล','วอลเลห์บอล']
    return render_template('favorite_sports.html',
                           title=title,
                           sports=sports)

@app.route('/favorite/movies')
def favorite_movies():
    title = 'Favorite Movies Page'
    movies = ['John Wick','Mission Impossible','Reacher','The Lord of the Rings','Harry Potter']
    return render_template('favorite_movies.html',
                           title=title,
                           movies=movies)