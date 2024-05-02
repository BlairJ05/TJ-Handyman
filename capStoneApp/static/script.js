const wrapper = document.querySelector('.wrapper')
const registerLink = document.querySelector('.register-link')
const loginLink = document.querySelector('.login-link')

registerLink.onclick = () => {
    wrapper.classList.add('active');
}
loginLink.onclick = () => {
    wrapper.classList.remove('active');
}


function slideshow() {
    // clone
    $('.slider-1').clone().removeClass('slider-1').addClass('slider-2').insertAfter($('.slider'));
  
    // set first
    $('.slider-1').slick({
      draggable: false,
      dots: false,
      infinite: true,
      responsive: true,
      asNavFor: '.slider-2',
      touchThreshold: 20,
      speed: 1000,
      fade: true
    });
  
    // set second
    $('.slider-2').slick({
      dots: true,
      infinite: true,
      responsive: true,
      asNavFor: '.slider-1',
      arrows: false,
      speed: 1000,
      easing: 'easeInOutQuart'
    });
  }
  
$(function() {
    slideshow();
    setTimeout(function() {
      $('.slider-1 .slick-next').click();
    }, 1000);
});

(function () {
    "use strict";
  
    var carousels = function () {
      $(".owl-carousel1").owlCarousel({
        loop: true,
        center: true,
        margin: 0,
        responsiveClass: true,
        nav: false,
        responsive: {
          0: {
            items: 1,
            nav: false
          },
          680: {
            items: 2,
            nav: false,
            loop: false
          },
          1000: {
            items: 3,
            nav: true
          }
        }
      });
    };
  
    (function ($) {
      carousels();
    })(jQuery);
})();

function openChatWindow(){
  document.getElementById('chat-form-container').style.display = "block";
}

function closeChatWindow(){
  document.getElementById('chat-form-container').style.display = "none";  
}