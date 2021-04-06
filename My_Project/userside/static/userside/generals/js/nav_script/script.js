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