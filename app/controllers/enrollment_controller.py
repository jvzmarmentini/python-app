from flask import Blueprint, jsonify, request
from config import db
from models.student import Student

enrollment_controller = Blueprint('enrollment_controller', __name__)

