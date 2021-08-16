
!(function ($) {
  "use strict";

  // Preloader
  $(window).on('load', function () {
    if ($('#preloader').length) {
      $('#preloader').delay(100).fadeOut('slow', function () {
        $(this).remove();
      });
    }
  });

  // Smooth scroll for the navigation menu and links with .scrollto classes
  var scrolltoOffset = $('#header').outerHeight() - 2;
  $(document).on('click', '.nav-menu a, .mobile-nav a, .scrollto', function (e) {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      if (target.length) {
        e.preventDefault();

        var scrollto = target.offset().top - scrolltoOffset;

        if ($(this).attr("href") == '#header' || $(this).attr("href") == 'index.html#header') {
          scrollto = 0;
        }

        $('html, body').animate({
          scrollTop: scrollto
        }, 1500, 'easeInOutExpo');

        if ($(this).parents('.nav-menu, .mobile-nav').length) {
          $('.nav-menu .active, .mobile-nav .active').removeClass('active');
          $(this).closest('li').addClass('active');
        }

        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
          $('.mobile-nav-overly').fadeOut();
        }
        return false;
      }
    }
  });

  // Activate smooth scroll on page load with hash links in the url
  $(document).ready(function () {
    // Data Table related

    $('#tbleCust').DataTable({
      "pagingType": "full_numbers",
      dom: 'Bfrtip',
      buttons: [
        'copy', 'csv', 'excel'
      ]
    });

    $('#tbleCust1').DataTable({
      "pagingType": "full_numbers",
      dom: 'Bfrtip',
      buttons: [
        'copy', 'csv', 'excel'
      ]
    });

    $("#mobile-collapse,#mobile-collapse1").click(function(e){$(window)[0].innerWidth<992&&($(".pcoded-navbar").toggleClass("mob-open"),e.stopPropagation())});


    // $('#tbleCust thead tr').clone(true).appendTo('#tbleCust thead');
    // $('#tbleCust thead tr:eq(1) th').each(function (i) {
    //   var title = $(this).text();
    //   $(this).html('<input type="text" placeholder="Search ' + title + '" />');
    //   $(this).css( "background", "blanchedalmond" );

    //   $('input', this).on('keyup change', function () {
    //     if (table.column(i).search() !== this.value) {
    //       table
    //         .column(i)
    //         .search(this.value)
    //         .draw();
    //     }
    //   });
    // });

    // var table = $('#tbleCust').DataTable({
    //   orderCellsTop: true,
    //   fixedHeader: true,
    //   "pagingType": "full_numbers",
    //   dom: 'Bfrtip',
    //   buttons: [
    //     'copy', 'csv', 'excel'
    //   ]
    // });

    $('#pills-contact-tab').click(function () {
      debugger;
      $('#tbleCust2').DataTable({
        responsive: true,
        columnDefs: [
          { responsivePriority: 1, target: -1 }
        ]
      }).columns.adjust()
        .responsive.recalc();
    });

    if (window.location.hash) {
      var initial_nav = window.location.hash;
      if ($(initial_nav).length) {
        var scrollto = $(initial_nav).offset().top - scrolltoOffset;
        $('html, body').animate({
          scrollTop: scrollto
        }, 1500, 'easeInOutExpo');
      }
    }
  });

  // Mobile Navigation
  if ($('.nav-menu').length) {
    var $mobile_nav = $('.nav-menu').clone().prop({
      class: 'mobile-nav d-lg-none'
    });
    $('body').append($mobile_nav);
    $('body').prepend('<button type="button" class="mobile-nav-toggle d-lg-none"><i class="icofont-navigation-menu"></i></button>');
    $('body').append('<div class="mobile-nav-overly"></div>');

    $(document).on('click', '.mobile-nav-toggle', function (e) {
      $('body').toggleClass('mobile-nav-active');
      $('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
      $('.mobile-nav-overly').toggle();
    });

    $(document).on('click', '.mobile-nav .drop-down > a', function (e) {
      e.preventDefault();
      $(this).next().slideToggle(300);
      $(this).parent().toggleClass('active');
    });

    $(document).click(function (e) {
      var container = $(".mobile-nav, .mobile-nav-toggle");
      if (!container.is(e.target) && container.has(e.target).length === 0) {
        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
          $('.mobile-nav-overly').fadeOut();
        }
      }
    });
  } else if ($(".mobile-nav, .mobile-nav-toggle").length) {
    $(".mobile-nav, .mobile-nav-toggle").hide();
  }

  // Navigation active state on scroll
  var nav_sections = $('section');
  var main_nav = $('.nav-menu, #mobile-nav');

  $(window).on('scroll', function () {
    var cur_pos = $(this).scrollTop() + 200;

    nav_sections.each(function () {
      var top = $(this).offset().top,
        bottom = top + $(this).outerHeight();

      if (cur_pos >= top && cur_pos <= bottom) {
        if (cur_pos <= bottom) {
          main_nav.find('li').removeClass('active');
        }
        main_nav.find('a[href="#' + $(this).attr('id') + '"]').parent('li').addClass('active');
      }
      if (cur_pos < 300) {
        $(".nav-menu ul:first li:first").addClass('active');
      }
    });
  });

  // Toggle .header-scrolled class to #header when page is scrolled
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      $('#header').addClass('header-scrolled');
      $('#topbar').addClass('topbar-scrolled');
    } else {
      $('#header').removeClass('header-scrolled');
      $('#topbar').removeClass('topbar-scrolled');
    }
  });

  if ($(window).scrollTop() > 100) {
    $('#header').addClass('header-scrolled');
    $('#topbar').addClass('topbar-scrolled');
  }

  // Back to top button
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      $('.back-to-top').fadeIn('slow');
    } else {
      $('.back-to-top').fadeOut('slow');
    }
  });

  $('.back-to-top').click(function () {
    $('html, body').animate({
      scrollTop: 0
    }, 1500, 'easeInOutExpo');
    return false;
  });

  // Intro carousel
  var heroCarousel = $("#heroCarousel");

  heroCarousel.on('slid.bs.carousel', function (e) {
    $(this).find('h2').addClass('animate__animated animate__fadeInDown');
    $(this).find('p, .btn-get-started').addClass('animate__animated animate__fadeInUp');
  });

  // Clients carousel (uses the Owl Carousel library)
  $(".clients-carousel").owlCarousel({
    autoplay: true,
    dots: true,
    loop: true,
    responsive: {
      0: {
        items: 2
      },
      768: {
        items: 4
      },
      900: {
        items: 6
      }
    }
  });

  // Porfolio isotope and filter
  $(window).on('load', function () {
    var portfolioIsotope = $('.portfolio-container').isotope({
      itemSelector: '.portfolio-item',
      layoutMode: 'fitRows'
    });

    $('#portfolio-flters li').on('click', function () {
      $("#portfolio-flters li").removeClass('filter-active');
      $(this).addClass('filter-active');

      portfolioIsotope.isotope({
        filter: $(this).data('filter')
      });
      aos_init();
    });

    // Initiate venobox (lightbox feature used in portofilo)
    $(document).ready(function () {
      $('.venobox').venobox();
    });
  });

  // Scroll to a section with hash in url
  $(window).on('load', function () {

    if (window.location.hash) {
      var initial_nav = window.location.hash;
      if ($(initial_nav).length) {
        var target_hash = $(initial_nav);
        var scrollto_hash = target_hash.offset().top - $('#header').outerHeight();
        $('html, body').animate({
          scrollTop: scrollto_hash
        }, 1500, 'easeInOutExpo');
        $('.nav-menu .active, .mobile-nav .active').removeClass('active');
        $('.nav-menu, .mobile-nav').find('a[href="' + initial_nav + '"]').parent('li').addClass('active');
      }
    }

  });

  // Portfolio details carousel
  $(".portfolio-details-carousel").owlCarousel({
    autoplay: true,
    dots: true,
    loop: true,
    items: 1
  });

  // Init AOS
  function aos_init() {
    AOS.init({
      duration: 1000,
      easing: "ease-in-out-back",
      once: true
    });
  }
  $(window).on('load', function () {
    aos_init();
  });

})(jQuery);

// Ajax Call main method
function callAjaxPost(url, dataToSend, _success, _error, showLoading, header) {
  $.ajax({
    url: url,
    type: 'post',
    dataType: 'json',
    contentType: 'application/json',
    beforeSend: function (xhr, settings) {
      xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    },
    success: _success,
    error: _error,
    data: dataToSend
  });
}
function callAjaxGet(url, dataToSend, _success, _error, showLoading, header) {
  $.ajax({
    url: url,
    type: 'get',
    dataType: 'json',
    contentType: 'application/json',
    beforeSend: function (xhr, settings) {
      xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    },
    success: _success,
    error: _error,
    data: dataToSend
  });
}

function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function dateformat() {
  var date = new Date();
  if (!isNaN(date.getTime())) {
    // Months use 0 index.
    return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate();
  }
}

function deletefromdiscussion(pk) {
  Swal.fire({
    title: 'Are you sure?',
    text: "Comment will be deleted!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, delete!'
  }).then((result) => {
    if (result.isConfirmed) {
      console.log(pk)
      $('#col_com').val(pk);
      $('#formmasterid').submit();
    }
  })
}

function banfromdatatable(pk) {
  Swal.fire({
    title: 'Are you sure?',
    text: "User will be banned!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, ban user!'
  }).then((result) => {
    if (result.isConfirmed) {
      console.log(pk)
      $('#hdn_ban_pk').val(pk);
      $('#formmasterid').submit();
    }
  })
}

function unbanfromdatatable(pk) {
  Swal.fire({
    title: 'Are you sure?',
    text: "Ban will be removed from User!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, remove ban!'
  }).then((result) => {
    if (result.isConfirmed) {
      console.log(pk)
      $('#hdn_ban_pk').val(pk);
      $('#formmasterid').submit();
    }
  })
}

function deletefromdatatable(pk) {
  Swal.fire({
    title: 'Are you sure?',
    text: "User will be deleted!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, delete it!'
  }).then((result) => {
    if (result.isConfirmed) {
      console.log(pk)
      $('#hdn_PK').val(pk);
      $('#formmasterid').submit();
    }
  })
}

function deletedatafoAll(pk, url) {
  Swal.fire({
    title: 'Are you sure?',
    text: "You won't be able to revert this!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, delete it!'
  }).then((result) => {
    if (result.isConfirmed) {
      _success = function (result) {
        if (result.Status) {
          Swal.fire('Success', result.Message, 'success').then(function () {
            location.reload();
          })
        }
        else {
          swal('Error', result.Message, 'error')
        }

      }
      _error = function (err) {
        swal('Error', 'Somthing went wrong Please Try Again', 'error')
      }
      callAjaxGet(url + "/" + pk, '', _success, _error);
    }
  })
}