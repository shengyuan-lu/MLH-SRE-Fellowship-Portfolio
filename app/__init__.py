import os
from flask import Flask, render_template, request
from dotenv import load_dotenv


load_dotenv()


app = Flask(__name__)


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

    return render_template('fellow.html', title="Fellow - Shengyuan Lu", fellowname=fellowname, aboutme=aboutme, education=education, work_experiences=work_experiences, url=os.getenv("URL"))

@app.route('/rami')
def rami():

    fellowname = "Rami Elsayed"

    aboutme = "Hi! I am Rami, a motivated and ambitious rising sophomore studying Computer Science at the University of Wisconsin - Madison. I have a deep passion for creating and tinkering with technology whether it's developing full-stack applications, designing systems programs, or crafting mobile apps."

    work_experiences = [
        {'company': 'Major League Hacking', 'position': 'Production Engineering Fellow', 'duration': 'June 2023 - Present'},
        {'company': 'Wisconsin Racing', 'position': 'Firmware Engineer', 'duration': 'Sept 2022 - Dec 2022'}
    ]

    education = [
        {'institution': 'University of Wisconsin, Madison', 'degree': 'Bachelor of Science, Computer Science', 'year': '2022 - 2026'},
    ]

    return render_template('fellow.html', title="Fellow - Rami Elsayed",  fellowname=fellowname, aboutme=aboutme, education=education, work_experiences=work_experiences, url=os.getenv("URL"))

if __name__ == '__main__':
    app.run(debug=True)