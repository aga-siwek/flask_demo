# FLASK DEMO

## Project Description

Repository with several simple flask HTTP applications. 

Used as examples during "How Internet Works" course. 

## How to Set Up Project

create virtual env

`python -m venv .venv`

activate virtual env

```
# windows (cmd)
.\.venv\Scripts\activate.bat

# windows (PowerShell)
.\.venv\Scripts\activate.ps1

# macos, linux
source .venv/bin/activate
```

install project dependencies

`pip install .`

## How to run server

you can start flask application by several different way:

run as python script

`python src/01_flask_simple/app.py`

run with flask

`python -m flask --app src/01_flask_simple/app.py run --host 0.0.0.0 --port 8080`

run with flask (with debug & autoreload)

`python -m flask --app src/01_flask_simple/app.py --debug run --host 0.0.0.0 --port 8080`