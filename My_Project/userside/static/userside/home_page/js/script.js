const root = document.documentElement;
const marqueeElementsDisplayed = getComputedStyle(root).getPropertyValue("--marquee-elements-displayed");
const marqueeContent = document.querySelector("ul.marquee-content");

root.style.setProperty("--marquee-elements", marqueeContent.children.length);

for(let i=0; i<marqueeElementsDisplayed; i++) {
  marqueeContent.appendChild(marqueeContent.children[i].cloneNode(true));
}

$(window).on('load', function() {

	let nbImg = 0;
	$('.slider .container-images img').each(function() {
		nbImg += 1;
	});

	$('.slider .arrow').click(function() {
		let n = imageActive();
		
		$('.slider').removeClass('right left');

		if($(this).hasClass('left')) { 
			n -= 1;
			$('.slider').addClass('left');
			setTimeout(function() {
				$('.slider .container-images img.active').addClass('to_left');
			}, 50)
		}
		else if($(this).hasClass('right')) { 
			n += 1;
			$('.slider').addClass('right');
			setTimeout(function() {
				$('.slider .container-images img.active').addClass('to_right');
			}, 50)
		}

		if(n > nbImg) n = 1;
		if(n < 1) n = nbImg;

		setTimeout(function() {
			$('.slider .container-images img').removeClass('active');
			$('.slider .container-images img:nth-child('+n+')').addClass('active');
		
			setTimeout(function() {
				$('.slider .container-images img').removeClass('to_left');
				$('.slider .container-images img').removeClass('to_right');
			}, 500)
		}, 50)
	});

	function imageActive() {
		let n = 1;
		$('.slider .container-images img').each(function(index) {
			if($(this).hasClass('active')) {
				n += index;
			}
		});
		return n;
	}

});
(function($) {
 
  var SliceSlider = {
    
    /**
     * Settings Object
     */
    settings: {
      delta:              0,
      currentSlideIndex:  0,
      scrollThreshold:    40,
      slides:             $('.slide'),
      numSlides:          $('.slide').length,
      navPrev:            $('.js-prev'),
      navNext:            $('.js-next'),
    },
    
    /**
     * Init
     */
    init: function() {
      s = this.settings;
      this.bindEvents();
    },
    
    /**
     * Bind our click, scroll, key events
     */
    bindEvents: function(){
      
      // Scrollwheel & trackpad
      s.slides.on({
        'DOMMouseScroll mousewheel' : SliceSlider.handleScroll
      });
      // On click prev
      s.navPrev.on({
        'click' : SliceSlider.prevSlide
      });
      // On click next
      s.navNext.on({
        'click' : SliceSlider.nextSlide
      });
      // On Arrow keys
      $(document).keyup(function(e) {
        // Left or back arrows
        if ((e.which === 37) ||  (e.which === 38)){
          SliceSlider.prevSlide();
        }
        // Down or right
        if ((e.which === 39) ||  (e.which === 40)) {
          SliceSlider.nextSlide();
        }
      });
    },
    
    /** 
     * Interept scroll direction
     */
    handleScroll: function(e){

      // Scrolling up
      if (e.originalEvent.detail < 0 || e.originalEvent.wheelDelta > 0) { 

        s.delta--;
     
        if ( Math.abs(s.delta) >= s.scrollThreshold) {
          SliceSlider.prevSlide();
        }
      }
 
      // Scrolling Down
      else {
 
        s.delta++;
 
        if (s.delta >= s.scrollThreshold) {
          SliceSlider.nextSlide();
        }
      }
 
      // Prevent page from scrolling
      return false;
    },

    /**
     * Show Slide
     */
    showSlide: function(){ 
      // reset
      s.delta = 0;
      // Bail if we're already sliding
      if ($('body').hasClass('is-sliding')){
        return;
      }
      // Loop through our slides
      s.slides.each(function(i, slide) {

        // Toggle the is-active class to show slide
        $(slide).toggleClass('is-active', (i === s.currentSlideIndex)); 
        $(slide).toggleClass('is-prev', (i === s.currentSlideIndex - 1)); 
        $(slide).toggleClass('is-next', (i === s.currentSlideIndex + 1)); 
        
        // Add and remove is-sliding class
        $('body').addClass('is-sliding');

        setTimeout(function(){
            $('body').removeClass('is-sliding');
        }, 1000);
      });
    },

    /**
     * Previous Slide
     */
    prevSlide: function(){
      
      // If on first slide, loop to last
      if (s.currentSlideIndex <= 0) {
        s.currentSlideIndex = s.numSlides;
      }
      s.currentSlideIndex--;
      
      SliceSlider.showSlide();
    },

    /**
     * Next Slide
     */
    nextSlide: function(){
      
      s.currentSlideIndex++;
   
      // If on last slide, loop to first
      if (s.currentSlideIndex >= s.numSlides) { 
        s.currentSlideIndex = 0;
      }
 
      SliceSlider.showSlide();
    },
  };
  SliceSlider.init();
})(jQuery);

if( $bool==false ){
  $('.like-or-dislike a').click(function(e){
      e.preventDefault()
      alert("Reaksiya vermək üçün daxil olun")
  })
}else{
  
}

      





    $('.card').hover(function(){
       let rest =  jQuery(this).find(".restaurant-logo")
       rest.attr('class','animate__animated animate__flash')
       let read_more =  jQuery(this).find(".read-more")
       read_more.attr('class','d-inline-block animate__animated animate__tada')
       let stars =  jQuery(this).find(".taste-rating-score")
       stars.addClass('animate__animated animate__flip')
       let srv_stars =  jQuery(this).find(".service-rating-score")
       srv_stars.addClass('animate__animated animate__flip')
       let atmp_stars =  jQuery(this).find(".atmp-rating-score")
       atmp_stars.addClass('animate__animated animate__flip')
    })
       
  (function() {
  
    var autoUpdate = false,
        timeTrans = 4000;
    
    var cdSlider = document.querySelector('.cd-slider'),
      item = cdSlider.querySelectorAll("li"),
      nav = cdSlider.querySelector("nav");
  
    item[0].className = "current_slide";
  
    for (var i = 0, len = item.length; i < len; i++) {
      var color = item[i].getAttribute("data-color");
      item[i].style.backgroundColor=color;
    }
  
    // Detect IE
    // hide ripple effect on IE9
    var ua = window.navigator.userAgent;
      var msie = ua.indexOf("MSIE");
      if ( msie > 0 ) {
        var version = parseInt(ua.substring(msie+ 5, ua.indexOf(".", msie)));
        if (version === 9) { cdSlider.className = "cd-slider ie9";}
    }
  
    if (item.length <= 1) {
      nav.style.display = "none";
    }
  
    function prevSlide() {
      var currentSlide = cdSlider.querySelector("li.current_slide"),
        prevElement = currentSlide.previousElementSibling,
        prevSlide = ( prevElement !== null) ? prevElement : item[item.length-1],
        prevColor = "rgb(241, 97, 33)",
        el = document.createElement('span');
  
      currentSlide.className = "";
      prevSlide.className = "current_slide";
  
      nav.children[0].appendChild(el);
  
      var size = ( cdSlider.clientWidth >= cdSlider.clientHeight ) ? cdSlider.clientWidth*2 : cdSlider.clientHeight*2,
          ripple = nav.children[0].querySelector("span");
  
      ripple.style.height = size + 'px';
      ripple.style.width = size + 'px';
      ripple.style.backgroundColor = prevColor;
  
      ripple.addEventListener("webkitTransitionEnd", function() {
        if (this.parentNode) {
          this.parentNode.removeChild(this);
        }
      });
  
      ripple.addEventListener("transitionend", function() {
        if (this.parentNode) {
          this.parentNode.removeChild(this);
        }
      });
  
    }
  
    function nextSlide() {
      var currentSlide = cdSlider.querySelector("li.current_slide"),
        nextElement = currentSlide.nextElementSibling,
        nextSlide = ( nextElement !== null ) ? nextElement : item[0],
        nextColor = "rgb(241, 97, 33)",
        el = document.createElement('span');
  
      currentSlide.className = "";
      nextSlide.className = "current_slide";
  
      nav.children[1].appendChild(el);
  
      var size = ( cdSlider.clientWidth >= cdSlider.clientHeight ) ? cdSlider.clientWidth*2 : cdSlider.clientHeight*2,
          ripple = nav.children[1].querySelector("span");
  
      ripple.style.height = size + 'px';
      ripple.style.width = size + 'px';
      ripple.style.backgroundColor = nextColor;
  
      ripple.addEventListener("webkitTransitionEnd", function() {
        if (this.parentNode) {
          this.parentNode.removeChild(this);
        }
      });
  
      ripple.addEventListener("transitionend", function() {
        if (this.parentNode) {
          this.parentNode.removeChild(this);
        }
      });
  
    }
  
    updateNavColor();
  
    function updateNavColor () {
      var currentSlide = cdSlider.querySelector("li.current_slide");
  
      var nextColor = ( currentSlide.nextElementSibling !== null ) ? currentSlide.nextElementSibling.getAttribute("data-color") : item[0].getAttribute("data-color");
      var	prevColor = ( currentSlide.previousElementSibling !== null ) ? currentSlide.previousElementSibling.getAttribute("data-color") : item[item.length-1].getAttribute("data-color");
  
      if (item.length > 2) {
        nav.querySelector(".prev").style.backgroundColor = prevColor;
        nav.querySelector(".next").style.backgroundColor = nextColor;
      }
    }
  
    nav.querySelector(".next").addEventListener('click', function(event) {
      event.preventDefault();
      nextSlide();
      updateNavColor();
    });
  
    nav.querySelector(".prev").addEventListener("click", function(event) {
      event.preventDefault();
      prevSlide();
      updateNavColor();
    });
    
    //autoUpdate
    setInterval(function() {
      if (autoUpdate) {
        nextSlide();
        updateNavColor();
      };
    },timeTrans);
  
  })();
  
  
