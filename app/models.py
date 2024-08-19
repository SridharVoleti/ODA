# app/models.py

from app import mongo

def create_booking(shipment_id, shipping_company, sender_name, sender_address, consignee, consignee_address, package_type):
    """
    Insert a new booking record into the 'bookings' collection in MongoDB.
    """
    booking = {
        "shipment_id": shipment_id,
        "shipping_company": shipping_company,
        "sender_name": sender_name,
        "sender_address": sender_address,
        "consignee": consignee,
        "consignee_address": consignee_address,
        "package_type": package_type
    }
    return mongo.db.bookings.insert_one(booking)
