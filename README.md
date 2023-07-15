# Portfolio Site

## Screenshots
![Screenshot 2023-06-28 at 10 15 22](https://github.com/shengyuan-lu/mlh-sre-fellowship-portfolio/assets/70995597/f27cb223-e38a-47d1-9e38-aec622b5f4f5)
![Screenshot 2023-06-28 at 10 15 17](https://github.com/shengyuan-lu/mlh-sre-fellowship-portfolio/assets/70995597/8f9f8cec-adb5-4c1d-88f8-7f26c44c797f)
![Screenshot 2023-06-28 at 10 15 10](https://github.com/shengyuan-lu/mlh-sre-fellowship-portfolio/assets/70995597/3c15aefd-0db5-4337-8b30-6e816a965a09)

## Installation
Note: You need Python3 and pip installed
Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

### Setup .env
Make sure to supply your own Google Map API Key and MySQL Database.
Create an `example.env` file

> URL=localhost:5000

> google_maps_api_key=YOUR_API_KEY

## Usage

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 
