# app/models.py
import uuid
from app.utils.auto_gen_id import *
from datetime import datetime
from app.helper import db_helper
from flask import flash
def create_shipment(shipping_company, sender_name, sender_address, consignee, consignee_address, package_type,weight,dimensions,shipping_date,delivery_date,shipping_method,insurance,declared_value,special_instructions,bill_of_lading,carting_point,cbm,cha,clearance_place,co_loader,container_stuffing,file_reference_number,forwarder,fpod,gross_weight,invoice_currency,invoice_currency_value,invoice_type,item_description,job_type,nature_of_contract,nature_of_payment,net_weight,number_of_packages,operation_handle_by,plan_date,pod,pol,por,remarks,sales_person_name,select_job,series,shipper_or_exporter,shipping_line,type_of_shipment,unit,unit_type):
    """
    Insert a new booking record into the 'bookings' collection in MongoDB.
    """
    shipment = {
        # Auto generated fields
        "_id" : uuid.uuid1(),
        "invoice_date" : str(datetime.today().date()),
        "invoice_number" : generate_invoice_number(),
        "job_date" : str(datetime.today().date()),
        "job_number" : generate_job_id(),
        "sb_number" : generate_sb_id(),
        "sb_number_date" : str(datetime.today().date()),
        # Fields from form data
        "shipping_company": shipping_company,
        "sender_name": sender_name,
        "sender_address": sender_address,
        "consignee": consignee,
        "consignee_address": consignee_address,
        "package_type": package_type,
        "weight": weight,
        "dimensions": dimensions,
        "shipping_date": str(shipping_date),
        "delivery_date": str(delivery_date),
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
        "invoice_type": invoice_type,
        "item_description": item_description,
        "job_type": job_type,
        "nature_of_contract": nature_of_contract,
        "nature_of_payment": nature_of_payment,
        "net_weight": net_weight,
        "number_of_packages": number_of_packages,
        "operation_handle_by": operation_handle_by,
        "plan_date": str(plan_date),
        "pod": pod,
        "pol": pol,
        "por": por,
        "remarks": remarks,
        "sales_person_name": sales_person_name,
        "select_job": select_job,
        "series": series,
        "shipper_or_exporter": shipper_or_exporter,
        "shipping_line": shipping_line,
        "type_of_shipment": type_of_shipment,
        "unit": unit,
        "unit_type": unit_type
    }
    try:
        return db_helper.insert_booking(shipment) #used helper class instead of mangodb ; added by rachana
    except:
        flash('error in insert_booking', 'danger')

def create_container(container_type,container_size,container_weight,max_gross_weight,owner_or_operator_code,container_status,iso_code,container_condtition,date_of_manufacture,last_date_inspection,cargo_type):
    container = {
        "_id":uuid.uuid1(),
        "container_type":container_type,
        "container_size":container_size,
        "container_weight":container_weight,
        "max_gross_weight":max_gross_weight,
        "owner_or_operator_code":owner_or_operator_code,
        "container_status":container_status,
        "iso_code":iso_code,
        "container_condtition":container_condtition,
        "date_of_manufacture":date_of_manufacture,
        "last_date_inspection":last_date_inspection,
        "cargo_type":cargo_type
    }