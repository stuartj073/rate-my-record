$(document).ready(function () {
  $('.sidenav').sidenav();
  $(".dropdown-trigger").dropdown();
  $('.datepicker').datepicker({
    format: "dd mmmm, yyyy",
    yearRange:100,
    maxDate: 0,
    showClearBtn: true,
    i18n: {
      done:"Select"
    }
  });
});
