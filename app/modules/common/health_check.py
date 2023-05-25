from flask import Blueprint

health_controller = Blueprint('health_controller', __name__)

@health_controller.route('/health', methods=['GET'])
def health_check():
    """
    Check the health status of the application.
    ---
    tags:
      - Health
    responses:
      200:
        description: Application is healthy.
    """
    return 'Healthy!', 200