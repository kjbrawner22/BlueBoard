# BlueBoard
CrimsonHacks2018 - A collaborative study room app.

## Usage and Installation
- To install you will need to proceed with the following steps:
  - Make sure you have python3 and pip3 installed on your machine
  - Clone this repo and then run move in to the directory with `cd BlueBoard`
  - make a virtual environment with `python3 -m venv venv`
  - activate the virtual environment with `source venv/bin/activate` or for windows cmd, `venv\Scripts\activate`
  - run `python3 install -r requirements.txt`
  - run `flask db upgrade` to build the SQL database architecture into a file called `app.db`
    - Note: this builds the database on your pc, it will not be stored anywhere else.
  - run `export FLASK_APP=run.py` or for windows, `set FLASK_APP=run.py`
  - `flask run` will now start a dev server on `http://localhost:5000`

## Progress
- 4/15/18
  - By the end of the hackathon, we have a real-time editor and messaging system implemented, with email login and basic room creation. 
