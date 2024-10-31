from flask import Flask 
from app.db.database import init_db

app = Flask

if __name__ == "__main__":
    init_db()

