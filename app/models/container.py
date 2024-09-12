from typing import Optional
from app.forms.container_form import ContainerForm
class Container:
    _id : Optional[str] = None
    container_type : Optional[str] = None
    container_size : Optional[str] = None
    container_weight : Optional[str] = None
    container_seal_number : Optional[str]=None
    max_gross_weight : Optional[str] = None
    owner_operator_code: Optional[str] = None
    container_status : Optional[str] = None
    iso_code : Optional[str] = None
    container_condition: Optional[str] = None
    date_of_manufacture : Optional[str] = None
    last_inspection_date : Optional[str] = None
    cargo_type : Optional[str] = None

    def to_json(self) -> dict:
        """
        Convert the Shipment object to a JSON-compatible dictionary.
        """
        container_dict = {}
        for key, value in self.__dict__.items():
            container_dict[key] = value
        return container_dict
    @classmethod
    def form_to_container(cls, form: "ContainerForm") -> "Container":
        container = cls()
        container.container_type = form.container_type.data
        container.container_size = form.container_size.data
        container.container_weight = form.container_weight.data
        container.max_gross_weight = form.max_gross_weight.data
        container.container_seal_number = form.container_seal_number.data
        container.owner_operator_code= form.owner_or_operator_code.data
        container.container_status = form.container_status.data
        container.iso_code = form.iso_code.data
        container.container_condition = form.container_condtition.data
        container.date_of_manufacture = form.date_of_manufacture.data.strftime("%Y-%m-%dT%H:%M:%SZ") if form.date_of_manufacture.data else None
        container.last_inspection_date = form.last_date_inspection.data.strftime("%Y-%m-%dT%H:%M:%SZ") if form.last_date_inspection.data else None
        container.cargo_type = form.cargo_type.data
        return container