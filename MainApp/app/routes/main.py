# # app/routes.py
from flask import render_template, redirect, flash,url_for,Blueprint,request,jsonify
from flask_login import login_required,current_user

from datetime import datetime
from app.utils.decorators import role_required
from app.utils.form_process import FormProcessor
from app.forms.shipment_form import ShipmentForm
from app.services.shipment import get_shipments,create_shipment,get_shipper_shipments,update_shipment,get_shipment,delete_shipment
from app.utils.choices_config import *

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
def createBooking():
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
                return redirect(url_for("main.documentManagement"))
            else:
                flash("Booking Unsuccessful","danger")
                return redirect(url_for("main.createBooking"))
    
    # For GET requests, or when the form fails validation, render the HTML form
    return render_template('booking_form.html', form=form,current_user = current_user)

@main_bp.route('/shipment-management/update-shipment/<string:Id>', methods=["GET", "POST"])
@role_required(['Shipper'])
def updateBooking(Id):
    shipment = get_shipment(Id)
    form = ShipmentForm()

    # Prepopulate the form with shipment data if this is a GET request
    if request.method == "GET" and shipment:
        # Loop through shipment details and set each form field
        for field_name, value in shipment.get("shipment_details").items():
            if hasattr(form, field_name):
                getattr(form, field_name).data = value

        # Handle container entries
        for container in shipment.get("containers",[]):
            entry = form.containers.append_entry()
            entry.container_id.data = container.get('container_id')
            entry.container_type.data = container.get('container_type')
            entry.container_weight.data = container.get('container_weight')
            # Populate additional container fields as needed
        # Prepopulate date fields with `datetime` objects
        date_format = "%Y-%m-%dT%H:%M:%S"  # or whatever format your date strings are in

        shipping_date_str = shipment.get("shipment_details").get("shipping_date")
        if isinstance(shipping_date_str, str):
            form.shipping_date.data = datetime.strptime(shipping_date_str, date_format)

        delivery_date_str = shipment.get("shipment_details").get("delivery_date")
        if isinstance(delivery_date_str, str):
            form.delivery_date.data = datetime.strptime(delivery_date_str, date_format)
        
        plan_date_str = shipment.get("shipment_details").get("plan_date")
        if isinstance(plan_date_str, str):
            form.plan_date.data = datetime.strptime(plan_date_str, date_format)

    # Handle form submission for POST requests
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
            data = form_data['booking']
            data['_id']=Id
            response = update_shipment(Id,data)  # Update the function to update shipment
            if response:
                return redirect(url_for("main.documentManagement"))
            else:
                flash("Update Unsuccessful", "danger")
                return redirect(url_for("main.updateBooking", Id=Id))

    # Render the form for GET requests or if form validation fails
    return render_template('booking_form.html', form=form, current_user=current_user)

@main_bp.route('/shipment-management/delete-shipment/<string:Id>', methods=["GET", "POST"])
@role_required(['Shipper'])
def deleteBooking(Id):
    response = delete_shipment(Id)
    if response:
        flash("Deleted","success")
    return redirect(url_for("main.documentManagement"))
      
@main_bp.route('/shipment-management')
@login_required
def shipmentManagement():
   return render_template('shipment_management.html')

@main_bp.route('/document-management')
@role_required(['Shipper'])
def documentManagement():
    shipments = get_shipper_shipments(current_user.user_id)
    return render_template('document_management.html',shipments=shipments)
