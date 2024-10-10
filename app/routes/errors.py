from flask import Blueprint, render_template


errors_bp = Blueprint('error', __name__)

@errors_bp.route('/unauthorised')
def unauthorised():
    return render_template('unauthorised.html')

