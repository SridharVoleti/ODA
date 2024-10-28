// Remove flash messages after 3 seconds
setTimeout(() => {
  document.querySelectorAll(".flash-message").forEach((message) => {
    message.remove(); // Immediately remove the element from the DOM
  });
}, 3000); // 3000ms = 3 seconds

//---------------------------------------------------------------------------
function addContainerForm() {
  const containerFormsDiv = document.getElementById("container-forms");
  const formIndex = containerFormsDiv.children.length;

  const containerFormHTML = `
  <h4>Container ${formIndex}</h4>
      <div class="container-form grid grid-cols-6 gap-3">

          <div class="container-form-group">
          <label class="form-label" for="containers-${formIndex}-container_type">Container Type:</label class="form-label">
          <select class="form-control" id="containers-${formIndex}-container_type" name="containers-${formIndex}-container_type">
          <option value="20FT">20FT</option>
          <option value="40FT">40FT</option>
          </select>
          </div>

          <div class="container-form-group">
          <label class="form-label" for="containers-${formIndex}-container_size">Container Size:</label class="form-label">
          <input class="form-control" type="text" id="containers-${formIndex}-container_size" name="containers-${formIndex}-container_size" required>
          </div>

          <div class="container-form-group">
          <label class="form-label" for="containers-${formIndex}-container_weight">Container Weight:</label class="form-label">
          <input class="form-control" type="text" id="containers-${formIndex}-container_weight" name="containers-${formIndex}-container_weight">
          </div>

          <div class="container-form-group">
          <label class="form-label" for="containers-${formIndex}-max_gross_weight">Max Gross Weight:</label class="form-label">
          <input class="form-control" type="text" id="containers-${formIndex}-max_gross_weight" name="containers-${formIndex}-max_gross_weight">
          </div>

          <div class="container-form-group">
          <label class="form-label" for="containers-${formIndex}-container_seal_number">Container Seal Number:</label class="form-label">
          <input class="form-control" type="text" id="containers-${formIndex}-container_seal_number" name="containers-${formIndex}-container_seal_number">
          </div>

          <div class="container-form-group">
          <label class="form-label" for="containers-${formIndex}-owner_operator_code">Owner Operator Code:</label class="form-label">
          <input class="form-control" type="text" id="containers-${formIndex}-owner_operator_code" name="containers-${formIndex}-owner_operator_code">
          </div>

          <div class="container-form-group">
          <label class="form-label" for="containers-${formIndex}-container_status">Container Status:</label class="form-label">
          <select class="form-control" id="containers-${formIndex}-container_status" name="containers-${formIndex}-container_status">
          <option value="Loaded">Loaded</option>
          <option value="In transit">In transit</option>
          <option value="Empty">Empty</option>
          </select>
          </div>

          <div class="container-form-group">
          <label class="form-label" for="containers-${formIndex}-iso_code">ISO Code:</label class="form-label">
          <input class="form-control" type="text" id="containers-${formIndex}-iso_code" name="containers-${formIndex}-iso_code">
          </div>

          <div class="container-form-group">
          <label class="form-label" for="containers-${formIndex}-container_condition">Container Condition:</label class="form-label">
          <select class="form-control" id="containers-${formIndex}-container_condition" name="containers-${formIndex}-container_condition">
          <option value="Clean">Clean</option>
          <option value="Damaged">Damaged</option>
          </select>
          </div>

          <div class="container-form-group">
          <label class="form-label" for="containers-${formIndex}-date_of_manufacture">Date of Manufacture:</label class="form-label">
          <input class="form-control" type="date" id="containers-${formIndex}-date_of_manufacture" name="containers-${formIndex}-date_of_manufacture">
          </div>

          <div class="container-form-group">
          <label class="form-label" for="containers-${formIndex}-last_inspection_date">Last Inspection Date:</label class="form-label">
          <input class="form-control" type="date" id="containers-${formIndex}-last_inspection_date" name="containers-${formIndex}-last_inspection_date">
          </div>

          <div class="container-form-group">
          <label class="form-label" for="containers-${formIndex}-cargo_type">Cargo Type:</label class="form-label">
          <select class="form-control" id="containers-${formIndex}-cargo_type" name="containers-${formIndex}-cargo_type">
          <option value="General">General</option>
          <option value="Hazardous">Hazardous</option>
          </select>
          </div>
      </div>
  `;
  containerFormsDiv.insertAdjacentHTML("beforeend", containerFormHTML);
}
//---------------------------------------------------------------------------
function toggleAccordion(event) {
  const content = event.currentTarget.nextElementSibling;
  const isHidden = content.classList.contains("hidden");
  if (isHidden) {
    content.classList.remove("hidden");
  } else {
    content.classList.add("hidden");
  }
}

const btn_open = document.querySelector(".side-menu-btn");
const btn_close = document.querySelector(".close-side-menu");
const sidebar = document.querySelector(".sidebar");
let isSidebarOpen = false;

// add our event listener for the click
btn_open.addEventListener("click", () => {
  sidebar.classList.toggle("-translate-x-full");
});

// add our event listener for the click
btn_close.addEventListener("click", () => {
  sidebar.classList.toggle("-translate-x-full");
});

profile_btn = document.querySelector(".user-profile");
user_card = document.querySelector(".user-card");
profile_btn.addEventListener("click", () => {
  console.log("hello");
  console.log(user_card.classList);
  user_card.classList.toggle("hidden");
});
