document.addEventListener("DOMContentLoaded", () => {
  const editButtons  = document.querySelectorAll(".btn-edit");
  const deleteButtons = document.querySelectorAll(".btn-delete");

  const commentText  = document.getElementById("id_body");
  const commentForm  = document.getElementById("commentForm");
  const submitButton = document.getElementById("submitButton");

  // Delete modal bits (guard if not present)
  const deleteModalEl = document.getElementById("deleteModal");
  const deleteConfirm = document.getElementById("deleteConfirm");
  const deleteModal = deleteModalEl ? new bootstrap.Modal(deleteModalEl) : null;

  // --- EDIT ---
  editButtons.forEach((button) => {
    button.addEventListener("click", (e) => {
      const id  = e.currentTarget.dataset.commentId;
      const url = e.currentTarget.dataset.editUrl; // <-- full, correct URL from Django

      const bodyEl = document.getElementById(`comment${id}`);
      const content = bodyEl ? bodyEl.textContent.trim() : "";

      if (commentText) commentText.value = content;
      if (submitButton) submitButton.textContent = "Update";
      if (commentForm && url) commentForm.setAttribute("action", url);
      if (commentText) commentText.focus();
    });
  });

  // --- DELETE ---
  deleteButtons.forEach((button) => {
    button.addEventListener("click", (e) => {
      const url = e.currentTarget.dataset.deleteUrl; // <-- from Django
      if (deleteConfirm) deleteConfirm.href = url;
      if (deleteModal) deleteModal.show();
    });
  });
});
