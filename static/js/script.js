$(document).ready(function () {
  $('.sidenav').sidenav();
});

$("select").change(function(){
  $("#" + $(this).val()).show().siblings().hide();
});

