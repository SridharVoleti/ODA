from app.forms.shipment_form import ShipmentForm 
# Test case for validating a form with all required fields provided
def test_valid_form(request_context,form_data):
    form = ShipmentForm(data=form_data)
    assert form.validate() is True  # Assert that the form should be valid with the given data


# Test case for validating a form with a invalid shipping_company
def test_invalid_shipping_company(request_context, form_data):
    form_data['shipping_company'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'shipping_company' in form.errors

# Test case for validating a form with a invalid sender_name
def test_invalid_sender_name(request_context, form_data):
    form_data['sender_name'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'sender_name' in form.errors

# Test case for validating a form with a invalid sender_address
def test_invalid_sender_address(request_context, form_data):
    form_data['sender_address'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'sender_address' in form.errors

# Test case for validating a form with a invalid consignee
def test_invalid_consignee(request_context, form_data):
    form_data['consignee'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'consignee' in form.errors

# Test case for validating a form with a invalid consignee_address
def test_invalid_consignee_address(request_context, form_data):
    form_data['consignee_address'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'consignee_address' in form.errors

# Test case for validating a form with a invalid package_type
def test_invalid_package_type(request_context, form_data):
    form_data['package_type'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'package_type' in form.errors

# Test case for validating a form with a invalid weight
def test_invalid_weight(request_context, form_data):
    form_data['weight'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'weight' in form.errors

# Test case for validating a form with a invalid dimensions
def test_invalid_dimensions(request_context, form_data):
    form_data['dimensions'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'dimensions' in form.errors

# Test case for validating a form with a invalid shipping_date
def test_invalid_shipping_date(request_context, form_data):
    form_data['shipping_date'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'shipping_date' in form.errors

# Test case for validating a form with a invalid delivery_date
def test_invalid_delivery_date(request_context, form_data):
    form_data['delivery_date'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'delivery_date' in form.errors

# Test case for validating a form with a invalid shipping_method
def test_invalid_shipping_method(request_context, form_data):
    form_data['shipping_method'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'shipping_method' in form.errors

# Test case for validating a form with a invalid insurance
def test_invalid_insurance(request_context, form_data):
    form_data['insurance'] = ''
    form = ShipmentForm(data=form_data)
    form.validate()
    assert 'insurance' not in form.errors 

# Test case for validating a form with a invalid declared_value
def test_invalid_declared_value(request_context, form_data):
    form_data['declared_value'] = ''
    form = ShipmentForm(data=form_data)
    form.validate()
    assert 'declared_value' not in form.errors 

# Test case for validating a form with a invalid special_instructions
def test_invalid_special_instructions(request_context, form_data):
    form_data['special_instructions'] = ''
    form = ShipmentForm(data=form_data)
    form.validate()
    assert 'special_instructions' not in form.errors 

# Test case for validating a form with a invalid bill_of_lading
def test_invalid_bill_of_lading(request_context, form_data):
    form_data['bill_of_lading'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'bill_of_lading' in form.errors

# Test case for validating a form with a invalid carting_point
def test_invalid_carting_point(request_context, form_data):
    form_data['carting_point'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'carting_point' in form.errors

# Test case for validating a form with a invalid cbm
def test_invalid_cbm(request_context, form_data):
    form_data['cbm'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'cbm' in form.errors

# Test case for validating a form with a invalid cha
def test_invalid_cha(request_context, form_data):
    form_data['cha'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'cha' in form.errors

# Test case for validating a form with a invalid clearance_place
def test_invalid_clearance_place(request_context, form_data):
    form_data['clearance_place'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'clearance_place' in form.errors

# Test case for validating a form with a invalid co_loader
def test_invalid_co_loader(request_context, form_data):
    form_data['co_loader'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'co_loader' in form.errors

# Test case for validating a form with a invalid container_stuffing
def test_invalid_container_stuffing(request_context, form_data):
    form_data['container_stuffing'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'container_stuffing' in form.errors

# Test case for validating a form with a invalid file_reference_number
def test_invalid_file_reference_number(request_context, form_data):
    form_data['file_reference_number'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'file_reference_number' in form.errors

# Test case for validating a form with a invalid forwarder
def test_invalid_forwarder(request_context, form_data):
    form_data['forwarder'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'forwarder' in form.errors

# Test case for validating a form with a invalid fpod
def test_invalid_fpod(request_context, form_data):
    form_data['fpod'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'fpod' in form.errors

# Test case for validating a form with a invalid gross_weight
def test_invalid_gross_weight(request_context, form_data):
    form_data['gross_weight'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'gross_weight' in form.errors

# Test case for validating a form with a invalid invoice_currency
def test_invalid_invoice_currency(request_context, form_data):
    form_data['invoice_currency'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'invoice_currency' in form.errors

# Test case for validating a form with a invalid invoice_currency_value
def test_invalid_invoice_currency_value(request_context, form_data):
    form_data['invoice_currency_value'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'invoice_currency_value' in form.errors

# Test case for validating a form with a invalid invoice_date
# def test_invalid_invoice_date(request_context, form_data):
#     form_data['invoice_date'] = ''
#     form = ShipmentForm(data=form_data)
#     assert form.validate() is False
#     assert 'invoice_date' in form.errors

# Test case for validating a form with a invalid invoice_number
# def test_invalid_invoice_number(request_context, form_data):
#     form_data['invoice_number'] = ''
#     form = ShipmentForm(data=form_data)
#     assert form.validate() is False
#     assert 'invoice_number' in form.errors

# Test case for validating a form with a invalid invoice_type
def test_invalid_invoice_type(request_context, form_data):
    form_data['invoice_type'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'invoice_type' in form.errors

# Test case for validating a form with a invalid item_description
def test_invalid_item_description(request_context, form_data):
    form_data['item_description'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'item_description' in form.errors

# Test case for validating a form with a invalid job_date
# def test_invalid_job_date(request_context, form_data):
#     form_data['job_date'] = ''
#     form = ShipmentForm(data=form_data)
#     assert form.validate() is False
#     assert 'job_date' in form.errors

# Test case for validating a form with a invalid job_number
# def test_invalid_job_number(request_context, form_data):
#     form_data['job_number'] = ''
#     form = ShipmentForm(data=form_data)
#     assert form.validate() is False
#     assert 'job_number' in form.errors

# Test case for validating a form with a invalid job_type
def test_invalid_job_type(request_context, form_data):
    form_data['job_type'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'job_type' in form.errors

# Test case for validating a form with a invalid nature_of_contract
def test_invalid_nature_of_contract(request_context, form_data):
    form_data['nature_of_contract'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'nature_of_contract' in form.errors

# Test case for validating a form with a invalid nature_of_payment
def test_invalid_nature_of_payment(request_context, form_data):
    form_data['nature_of_payment'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'nature_of_payment' in form.errors

# Test case for validating a form with a invalid net_weight
def test_invalid_net_weight(request_context, form_data):
    form_data['net_weight'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'net_weight' in form.errors

# Test case for validating a form with a invalid number_of_packages
def test_invalid_number_of_packages(request_context, form_data):
    form_data['number_of_packages'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'number_of_packages' in form.errors

# Test case for validating a form with a invalid operation_handle_by
def test_invalid_operation_handle_by(request_context, form_data):
    form_data['operation_handle_by'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'operation_handle_by' in form.errors

# Test case for validating a form with a invalid plan_date
def test_invalid_plan_date(request_context, form_data):
    form_data['plan_date'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'plan_date' in form.errors

# Test case for validating a form with a invalid pod
def test_invalid_pod(request_context, form_data):
    form_data['pod'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'pod' in form.errors

# Test case for validating a form with a invalid pol
def test_invalid_pol(request_context, form_data):
    form_data['pol'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'pol' in form.errors

# Test case for validating a form with a invalid por
def test_invalid_por(request_context, form_data):
    form_data['por'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'por' in form.errors

# Test case for validating a form with a invalid remarks
def test_invalid_remarks(request_context, form_data):
    form_data['remarks'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'remarks' in form.errors

# Test case for validating a form with a invalid sales_person_name
def test_invalid_sales_person_name(request_context, form_data):
    form_data['sales_person_name'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'sales_person_name' in form.errors

# Test case for validating a form with a invalid sb_number
# def test_invalid_sb_number(request_context, form_data):
#     form_data['sb_number'] = ''
#     form = ShipmentForm(data=form_data)
#     assert form.validate() is False
#     assert 'sb_number' in form.errors

# Test case for validating a form with a invalid sb_number_date
# def test_invalid_sb_number_date(request_context, form_data):
#     form_data['sb_number_date'] = ''
#     form = ShipmentForm(data=form_data)
#     assert form.validate() is False
#     assert 'sb_number_date' in form.errors

# Test case for validating a form with a invalid select_job
def test_invalid_select_job(request_context, form_data):
    form_data['select_job'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'select_job' in form.errors

# Test case for validating a form with a invalid series
def test_invalid_series(request_context, form_data):
    form_data['series'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'series' in form.errors

# Test case for validating a form with a invalid shipper_exporter
def test_invalid_shipper_or_exporter(request_context, form_data):
    form_data['shipper_or_exporter'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'shipper_or_exporter' in form.errors

# Test case for validating a form with a invalid shipping_line
def test_invalid_shipping_line(request_context, form_data):
    form_data['shipping_line'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'shipping_line' in form.errors

# Test case for validating a form with a invalid type_of_shipment
def test_invalid_type_of_shipment(request_context, form_data):
    form_data['type_of_shipment'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'type_of_shipment' in form.errors

# Test case for validating a form with a invalid unit
def test_invalid_unit(request_context, form_data):
    form_data['unit'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'unit' in form.errors

# Test case for validating a form with a invalid unit_type
def test_invalid_unit_type(request_context, form_data):
    form_data['unit_type'] = ''
    form = ShipmentForm(data=form_data)
    assert form.validate() is False
    assert 'unit_type' in form.errors


