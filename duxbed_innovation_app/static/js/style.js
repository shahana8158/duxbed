
document.querySelector("form").addEventListener("submit", function(e) {
  const phone = document.getElementById("phone").value;
  const phoneError = document.getElementById("phoneError");

  // Allow only digits, check length = 10
  if (!/^\d{10}$/.test(phone)) {
    e.preventDefault(); // Prevent form submission
    phoneError.style.display = "block";
  } else {
    phoneError.style.display = "none";
  }
});

