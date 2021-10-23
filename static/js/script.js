$(document).ready(function () {
  $('.sidenav').sidenav();
});


// $("#music").change(function () {
//   var form = document.getElementsByTagName('form')
//   var music = document.getElementById('music')
//   console.log(music.value)
//   console.log("HIEIEIF")

//   form.innerHTML=`<h1>Hello</h1>`

// })


$("#myselect").on("change", function() {
  $("#" + $(this).val()).show().siblings().change();
  console.log("HELLO")
})

// function changeForm(){
//   let form = document.getElementsByTagName('form')
  
//   if(form.classList.contains("record"){
//     form.classList.remove("record")
//   })
// }



