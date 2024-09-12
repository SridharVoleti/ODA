// Selecting all the menu items and assigning them to menuItems variable
const menuItems = document.querySelectorAll(".menu-item");

menuItems.forEach((item) => {
  item.addEventListener("click", () => {
    // Remove the active class from all menu items
    menuItems.forEach((menuItem) => {
      menuItem.classList.remove("menu-item-active");
    });

    // Add the active class to the clicked menu item
    item.classList.add("menu-item-active");

    // Handle submenu display
    const submenu = item.querySelector(".submenu");
    const isVisible = submenu.style.display === "flex";

    // Hide all other submenus
    document.querySelectorAll(".submenu").forEach((sub) => {
      sub.style.display = "none";
    });

    // Toggle the clicked submenu
    submenu.style.display = isVisible ? "none" : "flex";
  });
});

// Close submenu and remove custom class when clicking outside of the menu bar
document.addEventListener("click", (event) => {
  if (!event.target.closest(".menu-item")) {
    menuItems.forEach((menuItem) => {
      menuItem.classList.remove("menu-item-active");
    });
    document.querySelectorAll(".submenu").forEach((sub) => {
      sub.style.display = "none";
    });
  }
});

// Remove flash messages after 3 seconds
setTimeout(() => {
  document.querySelectorAll(".flash-message").forEach((message) => {
    message.remove(); // Immediately remove the element from the DOM
  });
}, 3000); // 3000ms = 3 seconds

//---------------------------------------------------------------------------

// Initialize containerCount with the number of forms initially rendered
let containerCount = document.querySelectorAll(".container-form").length;

// Function to add a new container form dynamically
function addContainerForm() {
  containerCount++; // Increment the form count for unique form IDs
  const containerFormsDiv = document.getElementById("container-forms"); // Get the div holding all forms

  // Create a new container form dynamically
  const newForm = `
        <div class="container-form" id="container-form-${containerCount}">
            <fieldset class="relative grid grid-cols-6 gap-3 w-screen">
                
                <!-- Dynamic container fields -->
                <div class="form-group">
                    <label for="containers-${containerCount}-container_type">Container Type</label>
                    <select class="form-control" id="containers-${containerCount}-container_type" name="containers-${containerCount}-container_type">
                        {% for choice in form.containers[0].container_type.choices %}
                            <option value="{{ choice[0] }}">{{ choice[1] }}</option>
                        {% endfor %}
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="containers-${containerCount}-container_size">Container Size</label>
                    <input class="form-control" id="containers-${containerCount}-container_size" name="containers-${containerCount}-container_size" type="text" required>
                </div>
                
                <div class="form-group">
                    <label for="containers-${containerCount}-container_weight">Container Weight</label>
                    <input class="form-control" id="containers-${containerCount}-container_weight" name="containers-${containerCount}-container_weight" type="number" required>
                </div>
                
                <div class="form-group">
                    <label for="containers-${containerCount}-max_gross_weight">Max Gross Weight</label>
                    <input class="form-control" id="containers-${containerCount}-max_gross_weight" name="containers-${containerCount}-max_gross_weight" type="number" required>
                </div>
                
                <div class="form-group">
                    <label for="containers-${containerCount}-container_seal_number">Container Seal Number</label>
                    <input class="form-control" id="containers-${containerCount}-container_seal_number" name="containers-${containerCount}-container_seal_number" type="text" required>
                </div>
                
                <div class="form-group">
                    <label for="containers-${containerCount}-owner_or_operator_code">Owner/Operator Code</label>
                    <input class="form-control" id="containers-${containerCount}-owner_or_operator_code" name="containers-${containerCount}-owner_or_operator_code" type="text" required>
                </div>
                
                <div class="form-group">
                    <label for="containers-${containerCount}-container_status">Container Status</label>
                    <select class="form-control" id="containers-${containerCount}-container_status" name="containers-${containerCount}-container_status">
                        {% for choice in form.containers[0].container_status.choices %}
                            <option value="{{ choice }}">{{ choice }}</option>
                        {% endfor %}
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="containers-${containerCount}-iso_code">ISO CODE</label>
                    <input class="form-control" id="containers-${containerCount}-iso_code" name="containers-${containerCount}-iso_code" type="text" required>
                </div>
                
                <div class="form-group">
                    <label for="containers-${containerCount}-container_condtition">Container Condition</label>
                    <select class="form-control" id="containers-${containerCount}-container_condtition" name="containers-${containerCount}-container_condtition">
                        {% for choice in form.containers[0].container_condtition.choices %}
                            <option value="{{ choice }}">{{ choice }}</option>
                        {% endfor %}
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="containers-${containerCount}-date_of_manufacture">Date of Manufacture</label>
                    <input class="form-control" id="containers-${containerCount}-date_of_manufacture" name="containers-${containerCount}-date_of_manufacture" type="date" required>
                </div>
                
                <div class="form-group">
                    <label for="containers-${containerCount}-last_date_inspection">Last Inspection Date</label>
                    <input class="form-control" id="containers-${containerCount}-last_date_inspection" name="containers-${containerCount}-last_date_inspection" type="date" required>
                </div>
                
                <div class="form-group">
                    <label for="containers-${containerCount}-cargo_type">Cargo Type</label>
                    <select class="form-control" id="containers-${containerCount}-cargo_type" name="containers-${containerCount}-cargo_type">
                        {% for choice in form.containers[0].cargo_type.choices %}
                            <option value="{{ choice }}">{{ choice }}</option>
                        {% endfor %}
                    </select>
                </div>
                
                <!-- Remove button for dynamically added forms -->
                <button type="button" class="button" onclick="removeContainerForm(${containerCount})">Remove</button>
            </fieldset>
        </div>
    `;

  // Insert the new form into the page
  containerFormsDiv.insertAdjacentHTML("beforeend", newForm);
}

// Function to remove a container form by its index
function removeContainerForm(index) {
  const formDiv = document.getElementById(`container-form-${index}`); // Find the form by its ID
  formDiv.remove(); // Remove it from the DOM
}

// Event listener for adding a new form
document
  .getElementById("add-container-btn")
  .addEventListener("click", addContainerForm);
