function setupSingleSelection(groupSelector) {
  const buttons = document.querySelectorAll(groupSelector);
  buttons.forEach(button => {
    button.addEventListener('click', () => {
      buttons.forEach(btn => btn.classList.remove('selected'));
      button.classList.add('selected');
    });
  });
}

document.addEventListener('DOMContentLoaded', () => {
  setupSingleSelection('.condition-buttons .condition-button');
  setupSingleSelection('.price-buttons .condition-button');
  setupSingleSelection('.deal-buttons .condition-button');
  setupSingleSelection('.payment-buttons .condition-button');
});

function previewImage(event) {
  const reader = new FileReader();
  reader.onload = function () {
    const preview = document.getElementById('preview-image');
    preview.src = reader.result;
  };
  reader.readAsDataURL(event.target.files[0]);
}
