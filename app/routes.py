# # app/routes.py

import uuid
from flask import render_template, request, redirect, url_for, flash
from app import app
from app.forms.booking_form import BookingForm
from datetime import datetime
from app.models import create_booking
from app.utils.auto_gen_id import *
@app.route('/booking', methods=['GET', 'POST'])
def booking():
    form = BookingForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            # Process the valid form data
            # For example, save the data to the database or perform other actions
            # Extract data from form
            shipment_id = uuid.uuid1()
            shipping_company = form.shipping_company.data
            sender_name = form.sender_name.data
            sender_address = form.sender_address.data
            consignee = form.consignee.data
            consignee_address = form.consignee_address.data
            package_type = form.package_type.data
            weight = form.weight.data
            dimensions = form.dimensions.data
            shipping_date = form.shipping_date.data
            delivery_date = form.delivery_date.data
            shipping_method = form.shipping_method.data
            insurance = form.insurance.data
            declared_value = form.declared_value.data
            special_instructions = form.special_instructions.data
            bill_of_lading = form.bill_of_lading.data
            carting_point = form.carting_point.data
            cbm = form.cbm.data
            cha = form.cha.data
            clearance_place = form.clearance_place.data
            co_loader = form.co_loader.data
            container_stuffing = form.container_stuffing.data
            file_reference_number = form.file_reference_number.data
            forwarder = form.forwarder.data
            fpod = form.fpod.data
            gross_weight = form.gross_weight.data
            invoice_currency = form.invoice_currency.data
            invoice_currency_value = form.invoice_currency_value.data
            invoice_date = datetime.today().date()
            invoice_number = generate_invoice_number()
            invoice_type = form.invoice_type.data
            item_description = form.item_description.data
            job_date = datetime.today().date()
            job_number = generate_job_id()
            job_type = form.job_type.data
            nature_of_contract = form.nature_of_contract.data
            nature_of_payment = form.nature_of_payment.data
            net_weight = form.net_weight.data
            number_of_packages = form.number_of_packages.data
            operation_handle_by = form.operation_handle_by.data
            plan_date = form.plan_date.data
            pod = form.pod.data
            pol = form.pol.data
            por = form.por.data
            remarks = form.remarks.data
            sales_person_name = form.sales_person_name.data
            sb_number = generate_sb_id()
            sb_number_date = datetime.today().date()
            select_job = form.select_job.data
            series = form.series.data
            shipper_or_exporter = form.shipper_or_exporter.data
            shipping_line = form.shipping_line.data
            type_of_shipment = form.type_of_shipment.data
            unit = form.unit.data
            unit_type = form.unit_type.data
            try:
                # Save the data in MongoDB
                create_booking(shipment_id, shipping_company, sender_name, sender_address, consignee, consignee_address, package_type,weight,dimensions,shipping_date,delivery_date,shipping_method,insurance,declared_value,special_instructions,bill_of_lading,carting_point,cbm,cha,clearance_place,co_loader,container_stuffing,file_reference_number,forwarder,fpod,gross_weight,invoice_currency,invoice_currency_value,invoice_date,invoice_number,invoice_type,item_description,job_date,job_number,job_type,nature_of_contract,nature_of_payment,net_weight,number_of_packages,operation_handle_by,plan_date,pod,pol,por,remarks,sales_person_name,sb_number,sb_number_date,select_job,series,shipper_or_exporter,shipping_line,type_of_shipment,unit,unit_type)
                flash('Booking created successfully!', 'success')
                return redirect(url_for('container'))
            except:
                flash('An error occurred while creating the booking. Please try again.', 'danger')
                return redirect(url_for('booking'))
        else:
            flash("something went wrong",'danger')
    # If it's a GET request or form validation failed, render the form template
    return render_template('booking.html', form=form)

@app.route('/container')
def container():
 return render_template('container.html')

