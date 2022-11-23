import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Records(db.Mode):
