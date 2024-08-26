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

// Timeout function to hide flash messages after 5 seconds with fade-out animation
setTimeout(function () {
  var flashMessages = document.querySelectorAll(".flash-message");
  flashMessages.forEach(function (message) {
    message.style.opacity = "0"; // Start fade out

    // After the transition ends, set display to none
    message.addEventListener("transitionend", function () {
      message.style.display = "none";
    });
  });
}, 3000); // 5000ms = 5 seconds

document.getElementById("add-form").addEventListener("click", function () {
  var formContainer = document.getElementById("form-container");
  var newFormWrapper = formContainer
    .querySelector(".form-wrapper")
    .cloneNode(true);

  // Reset form fields in the cloned form
  var inputs = newFormWrapper.querySelectorAll("input, select, textarea");
  inputs.forEach(function (input) {
    input.value = ""; // Clear the input values
  });

  // Add Remove button to the cloned form
  var removeBtn = document.createElement("button");
  removeBtn.type = "button";
  removeBtn.className = "button booking-remove";
  removeBtn.innerText = "Remove";
  newFormWrapper.appendChild(removeBtn);

  // Attach event listener to the new Remove button
  removeBtn.addEventListener("click", function () {
    newFormWrapper.remove();
  });

  // Add the cloned form to the container
  formContainer.appendChild(newFormWrapper);
});
