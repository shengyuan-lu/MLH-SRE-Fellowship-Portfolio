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
    work_experiences = [
        {'company': 'University of California', 'position': 'Software Engineering Intern', 'duration': 'July 2022 - Present'},
        {'company': 'University of California', 'position': 'IT Support', 'duration': 'Sept 2021 - Dec 2021'},
        {'company': 'Zoom Video Communications', 'position': 'Software Quality Assurance Intern', 'duration': 'July 2021 - Sept 2021'}
    ]

    education = [
        {'institution': 'University of California, Irvine', 'degree': 'Bachelor of Science, Computer Science', 'year': '2020 - 2024'},
        {'institution': 'Carroll High School', 'degree': 'High School Diploma', 'year': '2016 - 2020'},
    ]

    return render_template('fellow.html', title="Fellow - Shengyuan Lu", work_experiences=work_experiences, education=education, url=os.getenv("URL"))

@app.route('/rami')
def rami():

    work_experiences = [
        {'company': 'Company A', 'position': 'Position A', 'duration': '2010-2012'},
        {'company': 'Company B', 'position': 'Position B', 'duration': '2012-2015'},
        {'company': 'Company C', 'position': 'Position C', 'duration': '2015-2020'}
    ]

    education = [
        {'institution': 'University of Wisconsin, Madison', 'degree': 'Bachelor of Science, Computer Science', 'year': '2022 - 2026'},
    ]

    return render_template('fellow.html', title="Fellow - Rami Elsayed",  work_experiences=work_experiences, education=education, url=os.getenv("URL"))

if __name__ == '__main__':
    app.run(debug=True)