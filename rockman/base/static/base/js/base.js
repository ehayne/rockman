
$(document).ready(function() {

//    $(".nav a").on("click", function () {
//        $(".nav").find(".active").removeClass("active");
//        $(this).parent().addClass("active");
//    });
////
//var url = window.location;
//// Will only work if string in href matches with location
//$('nav a[href="'+ url +'"]').parent().addClass('active');
//
//// Will also work for relative and absolute hrefs
//$('nav a').filter(function() {
//    return this.href == url;
//}).parent().addClass('active');

    $('.nav li a').on('click', function() {
    $(this).parent().parent().find('.active').removeClass('active');
    $(this).parent().addClass('active');
});

});