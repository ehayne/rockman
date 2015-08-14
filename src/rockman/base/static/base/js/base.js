// This controls the navbar highlighting
$(document).ready(function() {
    $('#navbar .nav a[href="' + this.location.pathname + '"]').parent().addClass('active');
    var dropdown = $('#navbar .nav a[href="' + this.location.pathname + '"]').parent().parent().parent();
    if (dropdown.length > 0 && dropdown[0].classList.contains("dropdown")) {
        dropdown.addClass('active');
    }
});