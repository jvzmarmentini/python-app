from flask import Blueprint, jsonify, request
from config import db
from app.modules.students.student import Student

enrollment_controller = Blueprint('enrollment_controller', __name__)

