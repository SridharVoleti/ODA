import json
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
        formatted_datetime = current_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')
        form_data = {
            "shipment_details": {
                "shipping_company": self.form.shipment_details.shipping_company.data,
                "sender_name": self.form.shipment_details.sender_name.data,
                "sender_address": self.form.shipment_details.sender_address.data,
                "consignee": self.form.shipment_details.consignee.data,
                "consignee_address": self.form.shipment_details.consignee_address.data,
                "package_type": self.form.shipment_details.package_type.data,
                "weight": self.form.shipment_details.weight.data,
                "dimensions": self.form.shipment_details.dimensions.data,
                "shipping_date": self.form.shipment_details.shipping_date.data.strftime("%Y-%m-%dT%H:%M:%SZ") if self.form.shipment_details.shipping_date.data else None,
                "delivery_date": self.form.shipment_details.delivery_date.data.strftime("%Y-%m-%dT%H:%M:%SZ") if self.form.shipment_details.delivery_date.data else None,
                "shipping_method": self.form.shipment_details.shipping_method.data,
                "insurance": self.form.shipment_details.insurance.data,
                "declared_value": self.form.shipment_details.declared_value.data,
                "special_instructions": self.form.shipment_details.special_instructions.data,
                "bill_of_lading": self.form.shipment_details.bill_of_lading.data,
                "carting_point": self.form.shipment_details.carting_point.data,
                "cbm": self.form.shipment_details.cbm.data,
                "cha": self.form.shipment_details.cha.data,
                "clearance_place": self.form.shipment_details.clearance_place.data,
                "co_loader": self.form.shipment_details.co_loader.data,
                "container_stuffing": self.form.shipment_details.container_stuffing.data,
                "file_reference_number": self.form.shipment_details.file_reference_number.data,
                "forwarder": self.form.shipment_details.forwarder.data,
                "fpod": self.form.shipment_details.fpod.data,
                "gross_weight": self.form.shipment_details.gross_weight.data,
                "invoice_currency": self.form.shipment_details.invoice_currency.data,
                "invoice_currency_value": self.form.shipment_details.invoice_currency_value.data,
                "invoice_type": self.form.shipment_details.invoice_type.data,
                "item_description": self.form.shipment_details.item_description.data,
                "job_type": self.form.shipment_details.job_type.data,
                "nature_of_contract": self.form.shipment_details.nature_of_contract.data,
                "nature_of_payment": self.form.shipment_details.nature_of_payment.data,
                "net_weight": self.form.shipment_details.net_weight.data,
                "number_of_packages": self.form.shipment_details.number_of_packages.data,
                "operation_handle_by": self.form.shipment_details.operation_handle_by.data,
                "plan_date": self.form.shipment_details.plan_date.data.strftime("%Y-%m-%dT%H:%M:%SZ") if self.form.shipment_details.plan_date.data else None,
                "pod": self.form.shipment_details.pod.data,
                "pol": self.form.shipment_details.pol.data,
                "por": self.form.shipment_details.por.data,
                "remarks": self.form.shipment_details.remarks.data,
                "sales_person_name": self.form.shipment_details.sales_person_name.data,
                "select_job": self.form.shipment_details.select_job.data,
                "series": self.form.shipment_details.series.data,
                "shipper_or_exporter": self.form.shipment_details.shipper_or_exporter.data,
                "shipping_line": self.form.shipment_details.shipping_line.data,
                "type_of_shipment": self.form.shipment_details.type_of_shipment.data,
                "unit": self.form.shipment_details.unit.data,
                "unit_type": self.form.shipment_details.unit_type.data,
                "_id" : generate_shipment_id(),
                "invoice_date" : formatted_datetime,
                "invoice_number" : generate_invoice_number(),
                "job_number" : generate_job_id(),
                "job_date" : formatted_datetime,
                "sb_number" : generate_sb_id(),
                "sb_number_date" : formatted_datetime,       
            },
            "container_details": {
                "_id": generate_container_id(),
                "container_type":self.form.container_details.container_type.data,
                "container_size": self.form.container_details.container_size.data,
                "container_weight": self.form.container_details.container_weight.data,
                "max_gross_weight": self.form.container_details.max_gross_weight.data,
                "container_seal_number": self.form.container_details.container_seal_number.data,
                "owner_or_operator_code": self.form.container_details.owner_or_operator_code.data,
                "container_status": self.form.container_details.container_status.data,
                "iso_code": self.form.container_details.iso_code.data,
                "container_condition": self.form.container_details.container_condtition.data,
                "date_of_manufacture": self.form.container_details.date_of_manufacture.data.strftime("%Y-%m-%dT%H:%M:%SZ") if self.form.container_details.date_of_manufacture.data else None,
                "last_date_inspection": self.form.container_details.last_date_inspection.data.strftime("%Y-%m-%dT%H:%M:%SZ") if self.form.container_details.last_date_inspection.data else None,
                "cargo_type": self.form.container_details.cargo_type.data,
            }
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
