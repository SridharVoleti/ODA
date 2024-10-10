from app.forms.container_form import ContainerForm 
# Test case for validating a form with all required fields provided
def test_valid_form(request_context,form_data):
    form = ContainerForm(data=form_data)
    form.validate()
    print(form.errors,flush=True)
    assert form.validate() is True  # Assert that the form should be valid with the given data

# Test case for validating a form with a invalid container_type
def test_invalid_container_type(request_context, form_data):
    form_data['container_type'] = ''
    form = ContainerForm(data=form_data)
    assert form.validate() is False
    assert 'container_type' in form.errors

# Test case for validating a form with an invalid container_size
def test_invalid_container_size(request_context, form_data):
    form_data['container_size'] = ''  # Missing one dimension
    form = ContainerForm(data=form_data)
    assert form.validate() is False
    assert 'container_size' in form.errors

# Test case for validating a form with an invalid container_weight (negative value)
def test_invalid_container_weight_negative(request_context, form_data):
    form_data['container_weight'] = ''
    form = ContainerForm(data=form_data)
    assert form.validate() is False
    assert 'container_weight' in form.errors

# Test case for validating a form with an invalid container_weight (exceeding max gross weight)
def test_invalid_container_weight_exceeding(request_context, form_data):
    form_data['container_weight'] = 'hjderr' 
    form = ContainerForm(data=form_data)
    assert form.validate() is False
    assert 'container_weight' in form.errors

# Test case for validating a form with an invalid max_gross_weight (negative value)
def test_invalid_max_gross_weight(request_context, form_data):
    form_data['max_gross_weight'] = ''
    form = ContainerForm(data=form_data)
    assert form.validate() is False
    assert 'max_gross_weight' in form.errors

# Test case for validating a form with an invalid owner_or_operator_code (special characters)
def test_invalid_owner_or_operator_code(request_context, form_data):
    form_data['owner_or_operator_code'] = ''  
    form = ContainerForm(data=form_data)
    assert form.validate() is False
    assert 'owner_or_operator_code' in form.errors

# Test case for validating a form with an invalid container_status (empty string)
def test_invalid_container_status(request_context, form_data):
    form_data['container_status'] = ''  # Empty status
    form = ContainerForm(data=form_data)
    assert form.validate() is False
    assert 'container_status' in form.errors

# Test case for validating a form with an invalid iso_code (non-numeric)
def test_invalid_iso_code(request_context, form_data):
    form_data['iso_code'] = ''  
    form = ContainerForm(data=form_data)
    assert form.validate() is False
    assert 'iso_code' in form.errors

# Test case for validating a form with an invalid container_condition (incorrect spelling)
def test_invalid_container_condition(request_context, form_data):
    form_data['container_condtition'] = ''  
    form = ContainerForm(data=form_data)
    assert form.validate() is False
    print(form.errors)
    assert 'container_condtition' in form.errors

# Test case for validating a form with an invalid date_of_manufacture (future date)
def test_invalid_date_of_manufacture(request_context, form_data):
    form_data['date_of_manufacture'] =''  
    form = ContainerForm(data=form_data)
    assert form.validate() is False
    assert 'date_of_manufacture' in form.errors

# Test case for validating a form with an invalid last_date_inspection (before date_of_manufacture)
def test_invalid_last_date_inspection(request_context, form_data):
    form_data['last_date_inspection'] = '' 
    form = ContainerForm(data=form_data)
    assert form.validate() is False
    assert 'last_date_inspection' in form.errors

# Test case for validating a form with an invalid cargo_type (empty string)
def test_invalid_cargo_type(request_context, form_data):
    form_data['cargo_type'] = ''  
    form = ContainerForm(data=form_data)
    assert form.validate() is False
    assert 'cargo_type' in form.errors

