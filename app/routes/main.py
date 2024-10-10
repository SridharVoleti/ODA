# # app/routes.py
from flask import render_template, redirect, flash,url_for,Blueprint,request,jsonify
from app.forms.shipment_form import ShipmentForm
from app.services.shipment import get_shipments,create_shipment
from app.forms.choices_config import *
from flask_login import login_required,current_user
from app.utils.decorators import role_required
from app.forms.form_process import FormProcessor
main_bp = Blueprint('main', __name__)

@main_bp.route('/dashboard')
@login_required
def dashboard():
    shipments = get_shipments()
    return render_template('dashboard.html',shipments = shipments)

@main_bp.route('/')
@login_required
def index():
    return render_template('index.html')

@main_bp.route('/shipment-management/shipment-booking', methods=['GET', 'POST'])
@role_required('Admin')
def shipment():
    form = ShipmentForm(request.form)
    # Pass the form to the processor
    form_processor = FormProcessor(form)
    
    if request.method == "POST":
        if form.shipment_details.validate_on_submit() & form.container_details.validate_on_submit():
            # Process the form and generate the JSON response
            form_data = form_processor.process_form()
            response = create_shipment(form_data['booking'])
            if response:
                flash("Booking Successful","success")
                return redirect(url_for("main.index"))
            else:
                flash("Booking Unsuccessful","danger")
                return redirect(url_for("main.shipment"))
        # If form doesn't validate, you can log errors
        print("Form validation failed", form.errors, flush=True)
    
    # For GET requests, or when the form fails validation, render the HTML form
    return render_template('new_shipment.html', form=form,current_user = current_user)

@main_bp.route('/shipment-management')
def shipmentManagement():
   return render_template('shipment_management.html')