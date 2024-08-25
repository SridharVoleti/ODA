# app/db_helper.py

from app import mongo
from flask import flash

def insert_booking(booking):
    """
    Insert a booking record into the MongoDB collection.
    """
    return mongo.db.bookings.insert_one(booking)


def get_booking_by_id(shipment_id):
    """
    Retrieve a booking record by shipment_id.
    """
    return mongo.db.bookings.find_one({"shipment_id": shipment_id})

def update_booking(shipment_id, update_fields):
    """
    Update a booking record with the given shipment_id and fields.
    """
    return mongo.db.bookings.update_one({"shipment_id": shipment_id}, {"$set": update_fields})

def delete_booking(shipment_id):
    """
    Delete a booking record by shipment_id.
    """
    return mongo.db.bookings.delete_one({"shipment_id": shipment_id})
