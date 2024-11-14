from flask import Blueprint, request, jsonify

from data_base.db import get_collection

bp_email = Blueprint('email', __name__)


@bp_email.route('/api/email', methods=['POST'])
def get_email():
    data = request.get_json()
    conn =get_collection()
    conn.insert_one(data)
    # conn.commit()
    # conn.close()


    return jsonify({'message': 'Email sent successfully'}), 200
