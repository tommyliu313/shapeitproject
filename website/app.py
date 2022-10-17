#import item
from flask import Flask, jsonify, request, render_template, Blueprint, session, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from jinja2 import TemplateNotFound
from sqlalchemy import Column, Integer, String, Float
#from flask_jwt_extended import JWTManager, jwt_required, create_access_token
#from flask_marshmallow import Marshmallow
#from flask_s3 import FlaskS3
from datetime import datetime
from werkzeug.security import generate_password_hash
import os
import json

# initialized the class
app = Flask(__name__, template_folder='app/templates', static_folder="app/static")