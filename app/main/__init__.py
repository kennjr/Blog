from flask import Blueprint

# app = Flask(__name__)
main = Blueprint('main', __name__)

from app.main import views