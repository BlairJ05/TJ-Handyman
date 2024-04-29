document.addEventListener("DOMContentLoaded", function () {
  var reviews_list = document.querySelector(".reviews-cards-container");
  var selectedUserDetails = document.querySelector(".selected-user-details");

  if (selectedUserDetails) {
    reviews_list.style.display = "none";
  }
});
