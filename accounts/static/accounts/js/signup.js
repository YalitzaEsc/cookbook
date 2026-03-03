const checkbox = document.getElementById('terms');
const button = document.getElementById('submitBtn');

checkbox.addEventListener('change', function () {
    button.disabled = !this.checked;
});
