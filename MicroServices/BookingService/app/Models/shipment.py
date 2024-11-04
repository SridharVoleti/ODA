from pydantic import BaseModel, Field, constr
from typing import Optional
from datetime import datetime
from fastapi.encoders import jsonable_encoder

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


#Making fields optional for update
class ContainerUpdateDetails(BaseModel):
    container_id: Optional[str] = Field(None, alias="_id")
    cargo_type: Optional[str] = None
    container_condition: Optional[str] = None
    container_seal_number: Optional[str] = None
    container_size: Optional[str] = None
    container_status: Optional[str] = None
    container_type: Optional[str] = None
    container_weight: Optional[float] = None
    date_of_manufacture: Optional[datetime] = None
    iso_code: Optional[str] = None
    last_date_inspection: Optional[datetime] = None
    max_gross_weight: Optional[float] = None
    owner_or_operator_code: Optional[str] = None

class ShipmentUpdateDetails(BaseModel):
    shipment_id: Optional[str] = Field(None, alias="_id")
    shipping_company: Optional[str] = None
    sender_name: Optional[str] = None
    sender_address: Optional[str] = None
    consignee: Optional[str] = None
    consignee_address: Optional[str] = None
    package_type: Optional[str] = None
    weight: Optional[float] = None
    dimensions: Optional[str] = None
    shipping_date: Optional[datetime] = None
    delivery_date: Optional[datetime] = None
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
    invoice_date: Optional[datetime] = None
    invoice_number: Optional[str] = None
    invoice_type: Optional[str] = None
    item_description: Optional[str] = None
    job_date: Optional[datetime] = None
    job_number: Optional[str] = None
    job_type: Optional[str] = None
    nature_of_contract: Optional[str] = None
    nature_of_payment: Optional[str] = None
    net_weight: Optional[float] = None
    number_of_packages: Optional[int] = None
    operation_handle_by: Optional[str] = None
    plan_date: Optional[datetime] = None
    pod: Optional[str] = None
    pol: Optional[str] = None
    por: Optional[str] = None
    remarks: Optional[str] = None
    sales_person_name: Optional[str] = None
    sb_number: Optional[str] = None
    sb_number_date: Optional[datetime] = None
    select_job: Optional[str] = None
    series: Optional[str] = None
    shipper_or_exporter: Optional[str] = None
    shipping_line: Optional[str] = None
    type_of_shipment: Optional[str] = None
    unit: Optional[str] = None
    unit_type: Optional[str] = None
# Define a model for PUT requests where both container and shipment details are optional
class ShipmentUpdate(ShipmentBase):
    booking_id: Optional[str] = Field(None, alias="_id")
    shipper_id: Optional[str]=None
    container_details: Optional[list[ContainerUpdateDetails]]=None
    shipment_details:Optional[ShipmentUpdateDetails]=None
