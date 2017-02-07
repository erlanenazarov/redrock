
$(document).ready(function () {


  $.datetimepicker.setLocale('en');
  $('#fromdate').datetimepicker({
    timepicker:false,
    format: 'Y/m/d'
  });
  $('#todate').datetimepicker({
    timepicker:false,
    format: 'Y/m/d'
  });
  $('.slider2').slick({
    centerMode: true,
    centerPadding: '60px',
    slidesToShow: 3,
    index: 2,
    responsive: [
      {
        breakpoint: 768,
        settings: {
          arrows: false,
          centerMode: false,
          centerPadding: '40px',
          slidesToShow: 2,
        }
      },
      {
        breakpoint: 480,
        settings: {
          arrows: false,
          centerMode: false,
          centerPadding: '40px',
          slidesToShow: 1
        }
      }

    ]
  });
  $('.slider3').slick({
    slidesToShow: 3,
    index: 2,
    autoplay: true,
    autoplaySpeed: 2000,
    prevArrow: '<button type="button" class="prev"></button>',
    nextArrow: '<button type="button" class="next"></button>',
    responsive: [
      {
        breakpoint: 768,
        settings: {
          arrows: false,
          centerMode: false,
          centerPadding: '40px',
          slidesToShow: 2,
        }
      },
      {
        breakpoint: 480,
        settings: {
          arrows: false,
          centerMode: false,
          centerPadding: '40px',
          slidesToShow: 1
        }
      }

    ]
  });
  $('.slider4').slick({
    slidesToShow: 4,
    index: 2,
    autoplay: true,
    autoplaySpeed: 2000,
    prevArrow: '<button type="button" class="prev"></button>',
    nextArrow: '<button type="button" class="next"></button>',
    responsive: [
      {
        breakpoint: 768,
        settings: {
          arrows: false,
          centerMode: false,
          centerPadding: '40px',
          slidesToShow: 2,
        }
      },
      {
        breakpoint: 480,
        settings: {
          arrows: false,
          centerMode: false,
          centerPadding: '40px',
          slidesToShow: 1
        }
      }

    ]
  });
  $('.watcsslider').slick({
    arrows: true,
    slidesToShow: 1,
    autoplay: false,
    autoplaySpeed: 2000,
    prevArrow: '<button type="button" class="whatcsprev"></button>',
    nextArrow: '<button type="button" class="whatcsnext"></button>',
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          arrows: false,
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          arrows: false,
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          arrows: false,
        }
      }
    ]
  });
  $('.blogslider').slick({
    slidesToShow: 1,
    arrows: false,
    fade: true,
    asNavFor: '.blogsliderthumb'
  });
  $('.blogsliderthumb').slick({
    arrows: true,
    slidesToShow: 4,
    asNavFor: '.blogslider',
    dots: false,
    focusOnSelect: true
  });
  $('.hotels').slick({
    slidesToShow: 4,
    prevArrow: '<button type="button" class="hbut1"></button>',
    nextArrow: '<button type="button" class="hbut2"></button>',
    responsive: [
      {
        breakpoint: 1025,
        settings: {
          arrows: false,
          slidesToShow: 4,
        }
      },
      {
        breakpoint: 769,
        settings: {
          arrows: false,
          slidesToShow: 3,
        }
      },
      {
        breakpoint: 767,
        settings: {
          arrows: false,
          slidesToShow: 2,
        }
      }, ]
    });
  });

  $(document).ready(function () {
    var radioButtons = $('.radio-trigger');

    function resetAllRadioButtons() {
      $(radioButtons).each(function (i, obj) {
        var input = $('input', $(obj));
        var label = $('label', $(obj));
        $(label).removeClass('active');
        // $(input).removeAttr('checked');
      });
    }

    $(radioButtons).on('click', function () {
      var input = $('input', $(this));
      var label = $('label', $(this));
      resetAllRadioButtons();
      $(input).attr('checked', "true");
      $(label).addClass('active');
    });

    var radioButtons2 = $('.radio-trigger2');

    function resetAllRadioButtons2() {
      $(radioButtons2).each(function (i, obj) {
        var input = $('input', $(obj));
        var label = $('label', $(obj));
        $(label).removeClass('active');
        // $(input).removeAttr('checked');
      });
    }

    $(radioButtons2).on('click', function () {
      var input = $('input', $(this));
      var label = $('label', $(this));
      resetAllRadioButtons2();
      $(input).attr('checked', "true");
      $(label).addClass('active');
    });

    var radioButtonsNo = $('.not1');

    $(radioButtonsNo).on('click', function () {
      var input = $('input', $(this));
      var label = $('label', $(this));
      $(input).attr('checked', "true");
      $(label).addClass('active');
    });

  });
  // if ($(' input:checked')) {
  //
  // }
  $( ".hitems label").on( "click", function() {
    a = this;
    setTimeout(function(){
      if($(a).parent().siblings().eq(0).is(':checked')){
        $( ".hitems").removeClass('optionselected')
        $(a).parents().eq(3).addClass('optionselected')
      }
      console.log($(a).parent().siblings().eq(0).is(':checked'))
    }, 0);

  });
  $( ".transport").on( "click", function() {
    b = this;
    setTimeout(function(){
      if($(b).children().eq(0).is(':checked')){
        $(b).siblings().removeClass('optionselected')
        $(b).addClass('optionselected')
      }
      console.log($(a).parent().siblings().eq(0).is(':checked'))
    }, 0);
  });
