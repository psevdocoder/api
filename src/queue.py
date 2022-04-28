import mysql.connector
from flask import request, Blueprint

from app import app
from config import mysql
from flask import jsonify
from flask import request


queue = Blueprint('queue', __name__)


@queue.route('/clearqueue', methods=['POST'])
def clearqueue:



@queue.route('/newposition', methods=['POST'])
def newposition:
