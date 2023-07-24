import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv('example.env')

app = Flask(__name__)
app.config['GOOGLE_MAPS_API_KEY'] = os.getenv("google_maps_api_key")

if os.getenv("TESTING") == "True":

    print("Running in test mode..")

    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)

    class TimelinePost(Model):
        name = CharField()
        email = CharField()
        content = TextField()
        created_at = DateTimeField(default=datetime.datetime.now())

        class Meta:
            database = mydb

    mydb.connect()

    with mydb:
        mydb.create_tables([TimelinePost], safe=True)

        print("TimelinePost in-memory table created")

else:

    print("Running in normal mode..")

    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                  user=os.getenv("MYSQL_USER"),
                  password=os.getenv("MYSQL_PASSWORD"),
                  host=os.getenv("MYSQL_HOST"),
                  port=3306
    )

    class TimelinePost(Model):
        name = CharField()
        email = CharField()
        content = TextField()
        created_at = DateTimeField(default=datetime.datetime.now())

        class Meta:
            database = mydb

    mydb.connect()

    with mydb:
        mydb.create_tables([TimelinePost], safe=True)

        print("TimelinePost real table created")


print(mydb)

@app.route('/')
def index():
    return render_template('index.html', title="Meet MLH Fellows", url=os.getenv("URL"))


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
        {'city': 'Dayton', 'country': 'USA'},
        {'city': 'Hangzhou', 'country': 'China'},
    ]

    return render_template('fellow.html', title="Fellow - Shengyuan Lu", fellowname=fellowname, aboutme=aboutme, education=education, work_experiences=work_experiences, hobbies=hobbies, visited_places=visited_places, google_maps_api_key=app.config['GOOGLE_MAPS_API_KEY'], url=os.getenv("URL"))


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
            model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }


@app.route('/timeline', methods=['GET', 'POST'])
def timeline():
    return render_template('timeline.html', title="Timeline")


if __name__ == '__main__':
    app.run(debug=True)