# # app/routes.py
from flask import render_template, request, redirect, flash,url_for
from app import app
from app.forms.booking_form import BookingForm
from app.forms.container_form import ContainerForm,ContainerFormList
from app.services.shipment import get_shipments,create_shipment,update_shipment
from app.services.container import create_container,create_containers
from app.models.shipment import Shipment
from app.models.container import Container
from app.utils.auto_gen_id import *
from datetime import datetime,timezone
from flask import session
from app.forms.choices_config import *
import json
@app.route('/')
def dashboard():
    shipments = get_shipments()
    return render_template('dashboard.html',shipments = shipments)

@app.route('/shipment', methods=['GET', 'POST'])
def shipment():
    form = BookingForm()
    if form.validate_on_submit():
       current_datetime = datetime.now(timezone.utc)
       formatted_datetime = current_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')
       shipment = Shipment.form_to_shipment(form)
       shipment._id = generate_shipment_id()
       shipment.invoice_date = formatted_datetime
       shipment.invoice_number = generate_invoice_number()
       shipment.job_number = generate_job_id()
       shipment.job_date = formatted_datetime
       shipment.sb_number = generate_sb_id()
       shipment.sb_number_date = formatted_datetime
       response = create_shipment(shipment.to_json())
       if response:
          session["shipment_id"]=shipment._id
          flash("Shipment created succesfully",'success')
          return redirect(url_for('container'))
       else:
          return shipment.to_json()
    return render_template('booking.html',form = form)

@app.route('/container',methods=['GET', 'POST'])
def container():
 form = ContainerFormList()
 if form.validate_on_submit(): 
   containers =[]
   container_ids =[]
   for container_form in form.containers:
      if container_form.validate():        
         container = Container.form_to_container(container_form)
         container._id = generate_container_id()
         container_ids.append(container._id)
         containers.append(container.to_json())
   response = create_containers(containers)
   if response:
      shipment_id = session.get("shipment_id",None)
      update_shipment(shipment_id,{"container":container_ids})
      flash("Container Added Successfully")
      return redirect(url_for('dashboard'))
 return render_template('containerform.html',form=form,
                                             container_types=CONTAINER_TYPES, 
                                             container_status=CONTAINER_STATUS,
                                             container_condition=CONTAINER_CONDITION,
                                             cargo_types=CARGO_TYPES)


