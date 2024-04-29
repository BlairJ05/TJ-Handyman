document.addEventListener("DOMContentLoaded", function () {
  var reviews_list = document.querySelector(".reviews-cards-container");
  var selectedUserDetails = document.querySelector(".selected-user-details");

  if (selectedUserDetails) {
    reviews_list.style.display = "none";
  }
});

function submitForm(approvalValue) {
  const form = document.getElementById("approveReviewForm");

  const approvalInput = document.createElement("input");
  approvalInput.setAttribute("type", "hidden");
  approvalInput.setAttribute("name", "approved");
  approvalInput.setAttribute("value", approvalValue);

  form.appendChild(approvalInput);

  form.submit();

  const message =
    approvalValue === "True" ? "Review posted!" : "Review not posted.";
  alert(message);
}

function confirmChangeStatus(event, newStatus) {
  event.preventDefault();

  if (confirm(`Are you sure you want to set the status to ${newStatus}?`)) {
    window.location = event.target.href;
  } else {
    return false;
  }
}
