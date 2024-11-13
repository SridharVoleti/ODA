# # app/routes.py
from flask import render_template, redirect, flash,url_for,Blueprint,request
from flask_login import login_required,current_user
import requests
import os

from datetime import datetime
from app.utils.decorators import role_required
from app.utils.form_process import FormProcessor
from app.forms.shipment_form import ShipmentForm
from app.utils.choices_config import *

main_bp = Blueprint('main', __name__)


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
            try:
            # Process the form and generate the JSON response
                form_processor = FormProcessor(form)
                form_data = form_processor.process_form()
                headers = {
                    "Authorization": f"Bearer {current_user.access_token}"
                }
                response = requests.post(f"{os.getenv("BOOKING_SERVICE_URL")}/shipment",json=form_data["booking"],headers=headers)
                if response.status_code == 201:
                    return redirect(url_for("main.documentManagement"))
                else:
                    flash(response.json().get("description"), "danger")
            except Exception as e:
                flash("Something went wrong...Try Again","danger")
                print(f"Create Booking Error: {str(e)}",flush=True)
    return render_template('booking_form.html', form=form,current_user = current_user)

@main_bp.route('/shipment-management/update-shipment/<string:Id>', methods=["GET", "POST"])
@role_required(['Shipper'])
def updateBooking(Id):
    try:
        headers={
            "Authorization": f"Bearer {current_user.access_token}"
        }
        response = requests.get(f"{os.getenv("BOOKING_SERVICE_URL")}/shipment/{Id}",headers=headers)
        if response.status_code != 200:
            flash("Shipment not found", "danger")
            return redirect(url_for("main.documentManagement"))
        shipment = response.json()
    except Exception as e:
        flash("Something went wrong...Try Again","danger")
        print(f"Get Booking Error in update: {str(e)}",flush=True)
        return redirect(url_for("main.documentManagement"))
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
        date_format = "%Y-%m-%dT%H:%M:%S"  
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
        try:
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
                headers = {
                    "Authorization": f"Bearer {current_user.access_token}"
                }
                response = requests.put(f"{os.getenv("BOOKING_SERVICE_URL")}/shipment/{Id}",json=data,headers=headers)
                if response.status_code == 200:
                    flash("Booking updated","success")
                    return redirect(url_for("main.documentManagement"))
                else:
                    flash(response.json().get("description"), "danger")
                    return redirect(url_for("main.updateBooking", Id=Id))
        except Exception as e:
            flash("Something weent wrong...Try Again", "danger")
            print(f"Update Booking Error: {str(e)}")
    # Render the form for GET requests or if form validation fails
    return render_template('booking_form.html', form=form, current_user=current_user)

@main_bp.route('/shipment-management/delete-shipment/<string:Id>', methods=["GET", "POST"])
@role_required(['Shipper'])
def deleteBooking(Id):
    try:
        headers={
            "Authorization": f"Bearer {current_user.access_token}"
        }
        response = requests.delete(f"{os.getenv("BOOKING_SERVICE_URL")}/shipment/{Id}",headers=headers)
        if response.status_code==200:
            flash(response.json().get("desctiption"),"success")
        else:
            flash(response.json().get("desctiption"),"danger")
    except Exception as e:
        flash("Something went wrong...Try Again", "danger")
        print(f"Delete Booking Error: {str(e)}")
    return redirect(url_for("main.documentManagement"))
      
@main_bp.route('/shipment-management')
@login_required
def shipmentManagement():
   return render_template('shipment_management.html')

@main_bp.route('/document-management')
@role_required(['Shipper'])
def documentManagement():
    shipments = []
    try:
        headers={
            "Authorization": f"Bearer {current_user.access_token}"
        }
        response = requests.get(f"{os.getenv("BOOKING_SERVICE_URL")}/shipments/{current_user._id}",headers=headers)
        shipments = response.json() if response.status_code == 200 else []
    except Exception as e:
        flash("Something went wrong...Try Again", "danger")
        print(f"Document Management Error: {str(e)}",flush=True)
    return render_template('document_management.html',shipments=shipments)
