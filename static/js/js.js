$(function () {
	"use strict";
    var count = 0;
/* ================================================== */
/* ========== Banner Paralax Effet__1__(1) >>>>>>>>>> */
/* ================================================== */
    function bannerParallax(tiger){
        if(tiger) {
            var parallax = new Parallax(tiger, {
                pointerEvents: true
            });
        }
    }
    bannerParallax($('#scene')[0]);
    bannerParallax($('#scene1')[0]);
    bannerParallax($('#scene2')[0]);
    bannerParallax($('#scene3')[0]);
    bannerParallax($('#scene4')[0]);
    bannerParallax($('#scene5')[0]);
/* <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< */
/* ================================================== */
/* ========== Banner Atuo Typed Text__1__(1) >>>>>>>> */
/* ================================================== */ 
    function autoTyped(classSelector, typedTxt){
        new Typed(classSelector, {
			strings: [typedTxt],
			typeSpeed: 40,
			loop: false,
			showCursor: false,
		});
    }
    function myFunction(tiger, tigerTxt) {
        var typeCount = true;
        setInterval(function(){
            if($(tiger).parents().hasClass("swiper-slide-active") && typeCount){
                autoTyped(tiger, tigerTxt);
                typeCount = false;
            } 
        }, 1000);
    }
    myFunction('.typedTiger1', '<h2 style="display: inline">Erp Solutions</h2><br>\n<h5 style="display: inline">A Complete System That Provides A 360&#176;<br>View of Your Business</h5>');
    myFunction('.typedTiger2', '<h2 style="display: inline">Domain registration &amp; Hosting</h2><br>\n<h5 style="display: inline">Start your website with a good domain</h5>');
    myFunction('.typedTiger3', '<h2 style="display: inline">Online marketing</h2><br>\n<h5 style="display: inline">You have question we have answers</h5>');
    myFunction('.typedTiger4', '<h2 style="display: inline">Mobile Applications</h2><br>\n<h5 style="display: inline">our mobile apps let you take the possiblities<br>wherever you go</h5>');
    myFunction('.typedTiger5', '<h2 style="display: inline">Domain registration &amp; Hosting</h2><br>\n<h5 style="display: inline">Start your website with a good domain</h5>');
/* <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< */
/* ================================================== */
/* ========== Banner Slider part__1__(1) >>>>>>>>>>>> */
/* ================================================== */
    var swiper = new Swiper('.swiper-container', {
        loop: true,
        slidesPerView: 1,
        parallax: true,
        keyboard: {
            enabled: true,
        },
        autoplay: {
            delay: 10000,
            disableOnInteraction: false,
        },
        cubeEffect: {
            shadow: true,
            slideShadows: true,
            shadowOffset: 20,
            shadowScale: 0.94,
        },
        navigation: {
            nextEl: '.bannerNext',
            prevEl: '.bannerPrev',
        },
        pagination: {
            el: '.swiper-pagination',
            dynamicBullets: true,
            clickable: true,
        },
    });
/* <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< */
/* ================================================== */
/* ========== Team Slider part__1__(1) >>>>>>>>>>>>>> */
/* ================================================== */
    var screenShotSlider = new Swiper('.swiper-container2', {
        effect: 'coverflow',
        grabCursor: false,
        centeredSlides: true,
        slidesPerView: 'auto',
        paginationClickable: true,
        spaceBetween: 40,
        initialSlide: 0,
        loop: true,
        navigation: {
            nextEl: '.teamBtnNext',
            prevEl: '.teamBtnPrev',
        },
        coverflowEffect: {
        rotate: 30,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows : true,
      },
    });
/* <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< */
/* ================================================== */
/* ========== Active Nav Item Style__1__(1) >>>>>>>>> */
/* ================================================== */     
    var sections = $('section');
      var navigation_links = $('.navBarLink a');
      sections.waypoint({
        handler: function(direction) {
            var active_section;
            active_section = $(this);
            if (direction === "up") active_section = active_section.prev();
            var active_link = $('.navBarLink a[href="#' + active_section.attr("id") + '"]');
            navigation_links.removeClass("active");
            active_link.addClass("active");
        },
        offset: '35%'
      });
/* <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< */
/* ================================================== */
/* ========== Auto Progressbar__1__(2) >>>>>>>>>>>>>> */
/* ================================================== */
    function startCounter(classSelector, beforeTxt, afterTxt, countToValue, animateTime) {
		var bar = new ProgressBar.Circle(classSelector, {
			color: '#fff',
			strokeWidth: 8,
			trailWidth: 1,
			easing: 'easeInOut',
			duration: animateTime,
			text: {
				autoStyleContainer: false
			},
			from: { color: '#fff', width: 1 },
			to: { color: '#fff', width: 8 },
			step: function(state, circle) {
				circle.path.setAttribute('stroke', state.color);
				circle.path.setAttribute('stroke-width', state.width);

				var value = beforeTxt + Math.round(circle.value() * countToValue) + afterTxt;
				if (value === 0) {
					circle.setText('');
				} else {
					circle.setText(value);
				}
			}
		});
		bar.text.style.fontFamily = '"Faster One", cursive';
		bar.text.style.fontSize = '2rem';
		$(classSelector).css("padding-top", "0");
		bar.animate(1.0);
	}
/* <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< */
/* ================================================== */
/* ========== footer height calculate__1__(3) >>>>>>> */
/* ================================================== */
	function footerHeight() {
		$("body").css({
			"paddingBottom": $(".footer").height() + "px"
		});
	}
/* <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< */

	$(window).on("load", function () {
/* ================================================== */
/* ========== height calculate part__2__(3) >>>>>>>>> */
/* ================================================== */
		footerHeight();	
/* <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< */
	});
	
	
	$(window).on("resize", function () {
/* ================================================== */
/* ========== height calculate part__3__(3) >>>>>>>>> */
/* ================================================== */
		footerHeight();
/* <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< */
	});
    
	$(window).on("scroll", function () {
///* ================================================== */
///* ========== Active Header__1__(2) >>>>>>>>>>>>>>>>> */
///* ================================================== */
//        function activeNavBar() {
//        if ($(window).scrollTop() > 0) {
//            $(".header").addClass("active");
//        } else {
//            $(".header").removeClass("active");
//        }
//    }
    activeNavBar();
/* <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< */
/* ================================================== */
/* ========== Auto Progressbar__2__(2) >>>>>>>>>>>>>> */
/* ================================================== */
        var scrollTop = $(window).scrollTop(),
        elementOffset = $('#progress').offset().top,
        distance = (elementOffset - scrollTop);
        if(distance < 1 && count ===0){
            startCounter('.counterCircle', '<i class="fas fa-smile fa-3x"></i><br>', '%<br><h5 class="text-uppercase">client satisfaction</h5><br>', 100, 2500);
            startCounter('.counterCircle1', ' ', ' ', 9, 1500);
            startCounter('.counterCircle2', ' ', ' ', 1179, 2000);
            startCounter('.counterCircle3', ' ', ' ', 6, 1000);
            startCounter('.counterCircle4', ' ', ' ', 17, 1700);
            count++;
        }
/* <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< */
/* ================================================== */
/* ========== scrool to Top part__1__(2) >>>>>>>>>>>> */
/* ================================================== */
        if ($(window).scrollTop() > 1) {
            $(".scrollToTop").addClass("active");
        } else {
            $(".scrollToTop").removeClass("active");
        }
/* <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< */
	});

/* ================================================== */
/* ========== ON Click Function >>>>>>>>>>>>>>>>>>>>> */
/* ================================================== */
/* ================================================== */
/* ========== ON Click Function >>>>>>>>>>>>>>>>>>>>> */
/* ================================================== */
/* ================================================== */
/* ========== ON Click Function >>>>>>>>>>>>>>>>>>>>> */
/* ================================================== */
	$(".mobileMnuIcon").click(function() {
		$(this).children().fadeToggle();
		$('.navBarLink').toggleClass('active');
	});
	$(".scrollToTop").on('click', function () {
/* ================================================== */
/* ========== scrool to Top part__2__(2) >>>>>>>>>>>> */
/* ================================================== */
		$('html, body').animate({
			scrollTop: 0
		}, 500);
    });
/* <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< */
/* ================================================== */
/* ========== Shorting Tab Item__1__(1) >>>>>>>>>>>>> */
/* ================================================== */
	$(".protfolioTabArea a").click(function() {
		var tabClass = $(this).attr('data-tab');
		if(tabClass==="all"){
			$(".protfolioCntArea > div").animate({
					'opacity': '0',
			},700,function(){
				$(".protfolioCntArea > div").css({
					'display': 'block',
					'opacity': '1',
					'transition': '300ms'
				});
			});
		}else{
			$(".protfolioCntArea > div").animate({
			'opacity': '0'
			},700, function(){
				$(this).hide();
				$(tabClass).css({
					'display': 'block',
					'opacity': '1',
					'transition': '300ms'
				});
			});
		}
	});
/* ================================================== */
/* ========== Smooth Scrolling__1__(1) >>>>>>>>>>>>>> */
/* ================================================== */
    $(".navBarLink li > a").on('click', function (e) {
        var className = $(this).attr("href");
        console.log (className);
        if (className.charAt(0) === "#") {
            e.preventDefault();
            var hash = this.hash,
                scrollTopOffset = $(hash).offset().top;
            $('html, body').animate({
                scrollTop: scrollTopOffset
            }, 500);
        }
    });
/* <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< */
/* ================================================== */
/* ========== Theme Area Menu__1__(1) >>>>>>>>>>>>>>> */
/* ================================================== */
    $(".themeAreaMnu").on("click", function () {
        $(this).parent().toggleClass("active");
    });
/* <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< */
/* ================================================== */
/* ========== Set CSS LiNK tag Attribute__1__(1) >>>> */
/* ================================================== */
    $(".colorArea li a").on('click', function (e) {
        e.preventDefault();
        $(".colorArea li").removeClass("active");
        $(this).parent().addClass("active");
        $("#selectedTheme").attr("href", $(this).attr("href"));
    });
/* <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< */
});
