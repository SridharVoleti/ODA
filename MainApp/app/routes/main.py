# # app/routes.py
from flask import render_template, redirect, flash,url_for,Blueprint,request,jsonify
from app.forms.shipment_form import ShipmentForm
from app.services.shipment import get_shipments,create_shipment,get_shipper_shipments
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
@role_required(['Shipper'])
def Booking():
    form = ShipmentForm()
    if request.method == "POST":
        if form.add_container.data:
            form.containers.append_entry(None)
        elif form.remove_container.data:
            if len(form.containers.entries) > 1:
                form.containers.pop_entry()
        elif form.validate_on_submit():
            # Process the form and generate the JSON response
            form_processor = FormProcessor(form)
            form_data = form_processor.process_form()
            response = create_shipment(form_data['booking'])
            if response:
                return redirect(url_for("main.index"))
            else:
                flash("Booking Unsuccessful","danger")
                return redirect(url_for("main.Booking"))
        # If form doesn't validate, you can log errors
        print("Form validation failed", form.errors, flush=True)
    
    # For GET requests, or when the form fails validation, render the HTML form
    return render_template('booking_form.html', form=form,current_user = current_user)

@main_bp.route('/shipment-management')
@login_required
def shipmentManagement():
   return render_template('shipment_management.html')

@main_bp.route('/document-management')
@role_required(['Shipper'])
def documentManagement():
    shipments = get_shipper_shipments(current_user.user_id)
    print(shipments,flush=True)
    return render_template('document_management.html',shipments=shipments)