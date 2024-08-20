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
