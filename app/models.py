# app/models.py

from app.helper import db_helper
from flask import flash
def create_booking(shipment_id, shipping_company, sender_name, sender_address, consignee, consignee_address, package_type,weight,dimensions,shipping_date,delivery_date,shipping_method,insurance,declared_value,special_instructions,bill_of_lading,carting_point,cbm,cha,clearance_place,co_loader,container_stuffing,file_reference_number,forwarder,fpod,gross_weight,invoice_currency,invoice_currency_value,invoice_date,invoice_number,invoice_type,item_description,job_date,job_number,job_type,nature_of_contract,nature_of_payment,net_weight,number_of_packages,operation_handle_by,plan_date,pod,pol,por,remarks,sales_person_name,sb_number,sb_number_date,select_job,series,shipper_or_exporter,shipping_line,type_of_shipment,unit,unit_type):
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
        "package_type": package_type,
        "weight": weight,
        "dimensions": dimensions,
        "shipping_date": shipping_date,
        "delivery_date": delivery_date,
        "shipping_method": shipping_method,
        "insurance": insurance,
        "declared_value": declared_value,
        "special_instructions": special_instructions,
        "bill_of_lading": bill_of_lading,
        "carting_point": carting_point,
        "cbm": cbm,
        "cha": cha,
        "clearance_place": clearance_place,
        "co_loader": co_loader,
        "container_stuffing": container_stuffing,
        "file_reference_number": file_reference_number,
        "forwarder": forwarder,
        "fpod": fpod,
        "gross_weight": gross_weight,
        "invoice_currency": invoice_currency,
        "invoice_currency_value": invoice_currency_value,
        "invoice_date": invoice_date,
        "invoice_number": invoice_number,
        "invoice_type": invoice_type,
        "item_description": item_description,
        "job_date": job_date,
        "job_number": job_number,
        "job_type": job_type,
        "nature_of_contract": nature_of_contract,
        "nature_of_payment": nature_of_payment,
        "net_weight": net_weight,
        "number_of_packages": number_of_packages,
        "operation_handle_by": operation_handle_by,
        "plan_date": plan_date,
        "pod": pod,
        "pol": pol,
        "por": por,
        "remarks": remarks,
        "sales_person_name": sales_person_name,
        "sb_number": sb_number,
        "sb_number_date": sb_number_date,
        "select_job": select_job,
        "series": series,
        "shipper_or_exporter": shipper_or_exporter,
        "shipping_line": shipping_line,
        "type_of_shipment": type_of_shipment,
        "unit": unit,
        "unit_type": unit_type
    }
    try:
        return db_helper.insert_booking(booking) #used helper class instead of mangodb ; added by rachana
    except:
        flash('error in insert_booking', 'danger')