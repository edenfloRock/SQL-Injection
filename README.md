# SQL Injection

This project shows how SQL Injection works.

You need to create the table users if not exists before run the application.

- Download project
```sh
git clone
```
- Connect to PostgreSQL and run script_init.sql


- Create virtual environment and install dependencies:
```sh
python -m venv .venv
source .venv/bin/activate
sudo dnf install postgresql-devel  #sudo apt-get install libpq-dev
sudo dnf groupinstall "Development Tools"
pip install -r requirements.txt
```

- Modify *.env* file in order to connect to database.

- Run application
```sh
python app.py
```

