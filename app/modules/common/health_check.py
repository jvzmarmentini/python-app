from flask import Blueprint

health_controller = Blueprint('health_controller', __name__)

@health_controller.route('/health', methods=['GET'])
def health_check():
    return 'Healthy!', 200