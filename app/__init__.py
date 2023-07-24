import datetime
import os
from flask import Flask, render_template, request, jsonify
from playhouse.shortcuts import model_to_dict
from dotenv import load_dotenv
from peewee import *

load_dotenv('example.env')

app = Flask(__name__)
print("URL:", os.getenv("URL"))
print("Database:", os.getenv("MYSQL_DATABASE"))
print("User:", os.getenv("MYSQL_USER"))
print("Password:", os.getenv("MYSQL_PASSWORD"))
print("Host:", os.getenv("MYSQL_HOST"))
print("Port:", os.getenv("MYSQL_PORT"))

app.config['GOOGLE_MAPS_API_KEY'] = os.getenv("google_maps_api_key")

if os.getenv("TESTING") == "True":
    print("Running in test mode..")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)

    mydb.connect()

else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                  user=os.getenv("MYSQL_USER"),
                  password=os.getenv("MYSQL_PASSWORD"),
                  host=os.getenv("MYSQL_HOST"),
                  port=3306
    )

    mydb.connect()

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

@app.before_request
def before_request():
    mydb.connect()

@app.before_first_request
def create_tables():
    with mydb:
        mydb.create_tables([TimelinePost], safe=True)

@app.route('/')
def index():
    return render_template('index.html', title="Meet MLH Fellows", url=os.getenv("URL"))

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']

    # Simple validation to pass tests/test_app.py
    if not name:
        return jsonify({'error': 'Invalid name'}), 400
    if not email or '@' not in email or '.' not in email:
        return jsonify({'error': 'Invalid email'}), 400
    if not content:
        return jsonify({'error': 'Invalid content'}), 400

    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post), 200

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/timeline', methods=['GET'])
def timeline_post():
    return render_template('timeline_post.html')

@app.route('/shengyuan')
def shengyuan():

    fellowname = "Shengyuan Lu"

    aboutme = "I am an engineer by training, a software developer by profession, and a creative artist by heart. If what I want doesn’t exist, I build it from scratch. From the chemistry board game I designed in high school to my newest iOS app ZotMeal, I am obsessed with turning ideas into reality."

    education = [
        {'institution': 'University of California, Irvine', 'degree': 'Bachelor of Science, Computer Science', 'year': '2020 - 2024'},
        {'institution': 'Carroll High School', 'degree': 'High School Diploma', 'year': '2016 - 2020'},
    ]

    work_experiences = [
        {'company': 'University of California', 'position': 'Software Engineering Intern', 'duration': 'July 2022 - Present'},
        {'company': 'University of California', 'position': 'IT Support', 'duration': 'Sept 2021 - Dec 2021'},
        {'company': 'Zoom Video Communications', 'position': 'Software Quality Assurance Intern', 'duration': 'July 2021 - Sept 2021'}
    ]

    hobbies = [
        {"title": "Photography", "description": "I love capturing precious moments", "img": "shengyuan-photography.jpeg"}
    ]

    visited_places = [
        {'city': 'San Francisco', 'country': 'USA'},
        {'city': 'Los Angeles', 'country': 'USA'},
        {'city': 'New York City', 'country': 'USA'},
        {'city': 'Seattle', 'country': 'USA'},
    ]

    return render_template('fellow.html', title="Fellow - Shengyuan Lu", fellowname=fellowname, aboutme=aboutme, education=education, work_experiences=work_experiences, hobbies=hobbies, visited_places=visited_places, google_maps_api_key=app.config['GOOGLE_MAPS_API_KEY'], url=os.getenv("URL"))

@app.route('/rami')
def rami():

    fellowname = "Rami Elsayed"

    aboutme = "I am a motivated and ambitious rising sophomore studying Computer Science at the University of Wisconsin - Madison. I have a deep passion for creating and tinkering with technology, whether it's developing full-stack applications, designing systems programs, or crafting mobile apps. The ability to bring ideas to life through my own skills and designs is incredibly fulfilling to me. I am driven by my love for technology and constantly seek out new opportunities to expand my knowledge and expertise. Nice to meet you 😊!"

    work_experiences = [
        {'company': 'Major League Hacking', 'position': 'Production Engineering Fellow', 'duration': 'June 2023 - Present'},
        {'company': 'Wisconsin Racing', 'position': 'Firmware Engineer', 'duration': 'Sept 2022 - Dec 2022'}
    ]

    education = [
        {'institution': 'University of Wisconsin, Madison', 'degree': 'Bachelor of Science, Computer Science', 'year': '2022 - 2026'},
    ]

    hobbies = [
        {"title": "Watching Mini-Documentaries", "description": "Easy way to learn more", "img": "rami-miniDoc.jpg"},
        {"title": "Gaming", "description": "I love immersing myself in a new world", "img": "rami-gaming.jpeg"}
    ]

    visited_places = [
        {'city': 'Khartoum', 'country': 'Sudan'},
        {'city': 'Chicago', 'country': 'USA'},
        {'city': 'Doha', 'country': 'Qatar'},
        {'city': 'Jeddah', 'country': 'Saudi Arabia'},
        {'city': 'New York City', 'country': 'USA'},
        {'city': 'Cairo', 'country': 'Egypt'},
        {'city': 'Milwaukee', 'country': 'USA'},
    ]

    return render_template('fellow.html', title="Fellow - Shengyuan Lu", fellowname=fellowname, aboutme=aboutme, education=education, work_experiences=work_experiences, hobbies=hobbies, visited_places=visited_places, google_maps_api_key=app.config['GOOGLE_MAPS_API_KEY'],url=os.getenv("URL"))
if __name__ == '__main__':
    app.run(debug=True)