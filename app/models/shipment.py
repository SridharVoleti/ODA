from typing import Optional
from app.forms.shipment_form import ShipmentForm
class Shipment:
    _id: Optional[str] = None
    shipping_company: Optional[str] = None
    sender_name: Optional[str] = None
    sender_address: Optional[str] = None
    consignee: Optional[str] = None
    consignee_address: Optional[str] = None
    package_type: Optional[str] = None
    weight: Optional[float] = None
    dimensions: Optional[str] = None
    shipping_date: Optional[str] = None
    delivery_date: Optional[str] = None
    shipping_method: Optional[str] = None
    insurance: Optional[bool] = None
    declared_value: Optional[float] = None
    special_instructions: Optional[str] = None
    bill_of_lading: Optional[str] = None
    carting_point: Optional[str] = None
    cbm: Optional[float] = None
    cha: Optional[str] = None
    clearance_place: Optional[str] = None
    co_loader: Optional[str] = None
    container_stuffing: Optional[str] = None
    file_reference_number: Optional[str] = None
    forwarder: Optional[str] = None
    fpod: Optional[str] = None
    gross_weight: Optional[float] = None
    invoice_currency: Optional[str] = None
    invoice_currency_value: Optional[float] = None
    invoice_date: Optional[str] = None
    invoice_number: Optional[str] = None
    invoice_type: Optional[str] = None
    item_description: Optional[str] = None
    job_date: Optional[str] = None
    job_number: Optional[str] = None
    job_type: Optional[str] = None
    nature_of_contract: Optional[str] = None
    nature_of_payment: Optional[str] = None
    net_weight: Optional[float] = None
    number_of_packages: Optional[int] = None
    operation_handle_by: Optional[str] = None
    plan_date: Optional[str] = None
    pod: Optional[str] = None
    pol: Optional[str] = None
    por: Optional[str] = None
    remarks: Optional[str] = None
    sales_person_name: Optional[str] = None
    sb_number: Optional[str] = None
    sb_number_date: Optional[str] = None
    select_job: Optional[str] = None
    series: Optional[str] = None
    shipper_exporter: Optional[str] = None
    shipping_line: Optional[str] = None
    type_of_shipment: Optional[str] = None
    unit: Optional[str] = None
    unit_type: Optional[str] = None
    container: Optional[list] = None

    def to_json(self) -> dict:
        """
        Convert the Shipment object to a JSON-compatible dictionary.
        """
        shipment_dict = {}
        for key, value in self.__dict__.items():
            shipment_dict[key] = value
        return shipment_dict

    @classmethod
    def form_to_shipment(cls, form: "ShipmentForm") -> "Shipment":
        """
        Map BookingForm fields to Shipment fields.
        """
        shipment = cls()  # Create an instance of the Shipment class
        
        # Mapping fields from form to Shipment object
        shipment.shipping_company = form.shipping_company.data
        shipment.sender_name = form.sender_name.data
        shipment.sender_address = form.sender_address.data
        shipment.consignee = form.consignee.data
        shipment.consignee_address = form.consignee_address.data
        shipment.package_type = form.package_type.data
        shipment.weight = form.weight.data
        shipment.dimensions = form.dimensions.data
        shipment.shipping_date = form.shipping_date.data.strftime("%Y-%m-%dT%H:%M:%SZ") if form.shipping_date.data else None
        shipment.delivery_date = form.delivery_date.data.strftime("%Y-%m-%dT%H:%M:%SZ") if form.delivery_date.data else None
        shipment.shipping_method = form.shipping_method.data
        shipment.insurance = form.insurance.data
        shipment.declared_value = form.declared_value.data
        shipment.special_instructions = form.special_instructions.data
        shipment.bill_of_lading = form.bill_of_lading.data
        shipment.carting_point = form.carting_point.data
        shipment.cbm = form.cbm.data
        shipment.cha = form.cha.data
        shipment.clearance_place = form.clearance_place.data
        shipment.co_loader = form.co_loader.data
        shipment.container_stuffing = form.container_stuffing.data
        shipment.file_reference_number = form.file_reference_number.data
        shipment.forwarder = form.forwarder.data
        shipment.fpod = form.fpod.data
        shipment.gross_weight = form.gross_weight.data
        shipment.invoice_currency = form.invoice_currency.data
        shipment.invoice_currency_value = form.invoice_currency_value.data
        shipment.invoice_type = form.invoice_type.data
        shipment.item_description = form.item_description.data
        shipment.job_type = form.job_type.data
        shipment.nature_of_contract = form.nature_of_contract.data
        shipment.nature_of_payment = form.nature_of_payment.data
        shipment.net_weight = form.net_weight.data
        shipment.number_of_packages = form.number_of_packages.data
        shipment.operation_handle_by = form.operation_handle_by.data
        shipment.plan_date = form.plan_date.data.strftime("%Y-%m-%dT%H:%M:%SZ") if form.plan_date.data else None
        shipment.pod = form.pod.data
        shipment.pol = form.pol.data
        shipment.por = form.por.data
        shipment.remarks = form.remarks.data
        shipment.sales_person_name = form.sales_person_name.data
        shipment.select_job = form.select_job.data
        shipment.series = form.series.data
        shipment.shipper_exporter = form.shipper_or_exporter.data
        shipment.shipping_line = form.shipping_line.data
        shipment.type_of_shipment = form.type_of_shipment.data
        shipment.unit = form.unit.data
        shipment.unit_type = form.unit_type.data

        return shipment
