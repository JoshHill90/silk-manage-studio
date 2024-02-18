let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mini-Slides");
  let dots = document.getElementsByClassName("demo");

  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  try {

      slides[slideIndex-1].style.display = "block";
      dots[slideIndex-1].className += " active";

  } catch (error) {
    console.log('pass error, no sliders');
    // Expected output: ReferenceError: nonExistentFunction is not defined
    // (Note: the exact output may be browser-dependent)
  }
}
