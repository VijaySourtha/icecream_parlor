from flask import Blueprint
from controllers.icecreamController import create, update, delete, availability

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['POST'])(create)
blueprint.route('/<id>', methods=['PUT'])(update)
blueprint.route('/<id>', methods=['DELETE'])(delete)
blueprint.route('/availability', methods=['GET'])(availability)
