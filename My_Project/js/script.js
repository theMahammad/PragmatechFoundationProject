let nav = $('.nav');
let scroll;
$(window).scroll(function (e) {
    scroll = $(window).scrollTop();
    if (scroll > 130) {


        nav.css('width', '100%');
        nav.css("border-radius", "0px")
    }
    if (scroll <= 130) {


        nav.css("width", "1000px");
        nav.css("border-radius", "50px")
    }


})



var listItem = $('.slider-item-list > li')

//function display(arg, arr) {
//    $(arg).html(arr[0]);
//
//    var i = 1;
//    var myVar = setInterval(function () {
//        $(arg).fadeOut(500, 'linear', function () {
//            $(arg).append(arr[i]).fadeIn(500);
//            i++;
//        });
//        if (i == 3) {
//            clearInterval(myVar);
//        }
//
//    }, 1000);
//
//
//}
//display($('.slider-item-list'), listItem);
var slideIndex = 0;
showSlides();
function showSlides() {
  var i;
  var sliderItems = document.getElementsByClassName("slider-item");
 
  for (i = 0; i < sliderItems.length; i++) {
    sliderItems[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex >=  sliderItems.length) {slideIndex = 1}    
  
  sliderItems[slideIndex-1].style.display = "block";  
 
  setTimeout(showSlides, 2000); // Change image every 2 seconds
}
