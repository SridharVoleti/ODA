from pydantic import BaseModel, Field, constr
from fastapi.encoders import jsonable_encoder

from typing import Optional
from datetime import datetime

# Define a model for Container details
class ContainerDetails(BaseModel):
    container_id: str = Field(..., alias="_id")
    cargo_type: str
    container_condition: str
    container_seal_number: str
    container_size: str
    container_status: str
    container_type: str
    container_weight: float
    date_of_manufacture: datetime
    iso_code: str
    last_date_inspection: datetime
    max_gross_weight: float
    owner_or_operator_code: str

# Define a model for Shipment details
class ShipmentDetails(BaseModel):
    shipment_id: str = Field(..., alias="_id")
    shipping_company: str
    sender_name: str
    sender_address: str
    consignee: str
    consignee_address: str
    package_type: str
    weight: float
    dimensions: str
    shipping_date: datetime
    delivery_date: datetime
    shipping_method: str
    insurance: bool
    declared_value: Optional[float] = None
    special_instructions: Optional[str] = None
    bill_of_lading: str
    carting_point: str
    cbm: float
    cha: str
    clearance_place: str
    co_loader: str
    container_stuffing: str
    file_reference_number: str
    forwarder: str
    fpod: str
    gross_weight: float
    invoice_currency: str
    invoice_currency_value: float
    invoice_date: datetime
    invoice_number: str
    invoice_type: str
    item_description: Optional[str] = None
    job_date: datetime
    job_number: str
    job_type: str
    nature_of_contract: str
    nature_of_payment: str
    net_weight: float
    number_of_packages: int
    operation_handle_by: str
    plan_date: datetime
    pod: str
    pol: str
    por: str
    remarks: Optional[str] = None
    sales_person_name: str
    sb_number: str
    sb_number_date: datetime
    select_job: str
    series: str
    shipper_or_exporter: str
    shipping_line: str
    type_of_shipment: str
    unit: str
    unit_type: str

# Define a model to encapsulate both container and shipment details
class ShipmentBase(BaseModel):
    booking_id: str = Field(None, alias="_id")
    shipper_id: str
    container_details: list[ContainerDetails]
    shipment_details: ShipmentDetails

    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)

    def to_bson(self):
        data = self.model_dump(by_alias=True, exclude_none=True)
        if data.get("_id") is None:
            data.pop("_id", None)
        return data

# Define a model for POST requests where both container and shipment details are mandatory
class ShipmentCreate(ShipmentBase):
    pass

