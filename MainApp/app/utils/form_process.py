from flask_login import current_user

from datetime import datetime,timezone
from app.utils.auto_gen_id import *

class FormProcessor:
    def __init__(self, form):
        self.form = form

    def is_valid(self):
        """
        Check if the form is valid.
        :return: Boolean
        """
        return self.form.validate_on_submit()
    
    def process_form(self):
        """
        Process the form and return data in JSON format.
        :return: JSON response containing form data
        """
        if not self.is_valid():
            return {
                "status": "error",
                "errors": self.get_errors()
            }

        current_datetime = datetime.now(timezone.utc)
        formatted_datetime = current_datetime.strftime('%Y-%m-%dT%H:%M:%S')
        
        # Shipment details
        form_data = {
            "_id": generate_booking_id(),
            "shipper_id": current_user._id,
            "shipment_details": {
                "shipping_company": self.form.shipping_company.data,
                "sender_name": self.form.sender_name.data,
                "sender_address": self.form.sender_address.data,
                "consignee": self.form.consignee.data,
                "consignee_address": self.form.consignee_address.data,
                "package_type": self.form.package_type.data,
                "weight": self.form.weight.data,
                "dimensions": self.form.dimensions.data,
                "shipping_date": self.form.shipping_date.data.strftime("%Y-%m-%dT%H:%M:%S") if self.form.shipping_date.data else None,
                "delivery_date": self.form.delivery_date.data.strftime("%Y-%m-%dT%H:%M:%S") if self.form.delivery_date.data else None,
                "shipping_method": self.form.shipping_method.data,
                "insurance": self.form.insurance.data,
                "declared_value": self.form.declared_value.data,
                "special_instructions": self.form.special_instructions.data,
                "bill_of_lading": self.form.bill_of_lading.data,
                "carting_point": self.form.carting_point.data,
                "cbm": self.form.cbm.data,
                "cha": self.form.cha.data,
                "clearance_place": self.form.clearance_place.data,
                "co_loader": self.form.co_loader.data,
                "container_stuffing": self.form.container_stuffing.data,
                "file_reference_number": self.form.file_reference_number.data,
                "forwarder": self.form.forwarder.data,
                "fpod": self.form.fpod.data,
                "gross_weight": self.form.gross_weight.data,
                "invoice_currency": self.form.invoice_currency.data,
                "invoice_currency_value": self.form.invoice_currency_value.data,
                "invoice_type": self.form.invoice_type.data,
                "item_description": self.form.item_description.data,
                "job_type": self.form.job_type.data,
                "nature_of_contract": self.form.nature_of_contract.data,
                "nature_of_payment": self.form.nature_of_payment.data,
                "net_weight": self.form.net_weight.data,
                "number_of_packages": self.form.number_of_packages.data,
                "operation_handle_by": self.form.operation_handle_by.data,
                "plan_date": self.form.plan_date.data.strftime("%Y-%m-%dT%H:%M:%S") if self.form.plan_date.data else None,
                "pod": self.form.pod.data,
                "pol": self.form.pol.data,
                "por": self.form.por.data,
                "remarks": self.form.remarks.data,
                "sales_person_name": self.form.sales_person_name.data,
                "select_job": self.form.select_job.data,
                "series": self.form.series.data,
                "shipper_or_exporter": self.form.shipper_or_exporter.data,
                "shipping_line": self.form.shipping_line.data,
                "type_of_shipment": self.form.type_of_shipment.data,
                "unit": self.form.unit.data,
                "unit_type": self.form.unit_type.data,
                "_id": generate_shipment_id(),
                "invoice_date": formatted_datetime,
                "invoice_number": generate_invoice_number(),
                "job_number": generate_job_id(),
                "job_date": formatted_datetime,
                "sb_number": generate_sb_id(),
                "sb_number_date": formatted_datetime,
            },
            "container_details": [
                {
                    "_id": generate_container_id(),
                    "container_type": container['container_type'],
                    "container_size": container['container_size'],
                    "container_weight": container['container_weight'],
                    "max_gross_weight": container['max_gross_weight'],
                    "container_seal_number": container['container_seal_number'],
                    "owner_or_operator_code": container['owner_or_operator_code'],
                    "container_status": container['container_status'],
                    "iso_code": container['iso_code'],
                    "container_condition": container['container_condition'],
                    "date_of_manufacture": container['date_of_manufacture'].strftime("%Y-%m-%dT%H:%M:%S") if container.get('date_of_manufacture') else None,
                    "last_date_inspection": container['last_date_inspection'].strftime("%Y-%m-%dT%H:%M:%S") if container.get('last_date_inspection') else None,
                    "cargo_type": container['cargo_type'],
                } for container in self.form.containers.data  # Iterating over multiple containers
            ]
        }

        return {
                "status": "success",
                "booking": form_data
            }

    def get_errors(self):
        """
        Extract form errors.
        :return: Dictionary of errors.
        """
        errors = {}
        for field_name, field in self.form._fields.items():
            if field.errors:
                errors[field_name] = field.errors
        return errors
