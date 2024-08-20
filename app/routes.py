# app/routes.py

from flask import render_template, request, redirect, url_for, flash
from app import app
from app.forms import BookingForm
from app.models import create_booking

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    """
    Route to display the booking form and handle form submission.
    """
    form = BookingForm()
    
    if form.validate_on_submit():
        # Extract data from form
        shipment_id = form.shipment_id.data
        shipping_company = form.shipping_company.data
        sender_name = form.sender_name.data
        sender_address = form.sender_address.data
        consignee = form.consignee.data
        consignee_address = form.consignee_address.data
        package_type = form.package_type.data
        
        # Save the data in MongoDB
        create_booking(shipment_id, shipping_company, sender_name, sender_address, consignee, consignee_address, package_type)
        
        flash('Booking created successfully!', 'success')
        return redirect(url_for('booking'))
    
    return render_template('booking.html', form=form)
