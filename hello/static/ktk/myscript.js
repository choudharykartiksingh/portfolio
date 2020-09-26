console.log("hello");
// When the user scrolls down 20px from the top of the document, slide down the navbar
// When the user scrolls to the top of the page, slide up the navbar (50px out of the top view)

window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    document.getElementById("navigationbar").style.top = "0";
  } else {
    document.getElementById("navigationbar").style.top = "-56px";
  }
}

var typed = $(".typed");

$(function () {
  typed.typed({
    strings: [
      "Public Speaker",
      "Web Developer",
      "Programmer",
      "Footballer",
      "Designer",
      "Poet",
    ],
    typeSpeed: 100,
    loop: true,
  });
});

$("#navmenu").onePageNav({
  currentClass: "act",
  changeHash: false,
  scrollSpeed: 750,
  scrollThreshold: 0.5,
  filter: "",
  easing: "swing",
});

$(".animation").each(function () {
  var waypoint = new Waypoint({
    element: this,
    handler: function (direction) {
      if (direction == "down") {
        var animation = $(this.element).attr("data-animation");
        $(this.element).css("opacity", "1");
        $(this.element).removeClass("zoomOut");
        $(this.element).addClass(" animated " + animation);
      }
      if (direction == "up") {
        var animation = $(this.element).attr("data-animation");
        // $(this.element).css("opacity", "0");
        $(this.element).removeClass("animated");
        $(this.element).removeClass(animation);
        $(this.element).addClass(" animated " + "zoomOut");
      }
    },
    offset: "75%",
  });
});

$(".skillanimation").each(function () {
  var waypoint = new Waypoint({
    element: this,
    handler: function (direction) {
      if (direction == "down") {
        var animation = $(this.element).attr("data-animation");
        $(this.element).addClass(animation);
      } else {
        var animation = $(this.element).attr("data-animation");
        $(this.element).removeClass(animation);
      }
    },

    offset: "75%",
  });
});


// $("#percentage").each(function () {
//   var waypoint = new Waypoint({
//     element: this,
//     handler: function (direction) {
//       if (direction == "down") {
//         // var animation = $(this.element).attr("data-animation");
//         $(this.element).addClass("counter-up");
//       } else {
//         // var animation = $(this.element).attr("data-animation");
//         $(this.element).removeClass("counter-up");
//       }
//     },

//     offset: "75%",
//   });
// });

$(".counter-up").counterUp({
  delay: 10,
  time: 500
});


$(".button-scroll").on("click", function() {
  var scrollTo = $(this).attr("data-scrollTo");
  $("body, html").animate({
      scrollTop: $("#" + scrollTo).offset().top - 50
  }, 1e3)
});