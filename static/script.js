
let menu = document.querySelector('#menu-bars');
let navbar = document.querySelector('.navbar');

//console.log('Si carga el script');
//alert('File loaded');

menu.onclick = () => {
    //console.log("Si hace click");
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
}

window.onscroll = () => {
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');
}

var swiper = new Swiper(".home-slider", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: "auto",
    coverflowEffect: {
      rotate: 0,
      stretch: 0,
      depth: 100,
      modifier: 2,
      slideShadows: true,
    },
    loop: true,
    autoplay:{
        delay: 3000,
        disableOnInteraction:false,
    }
  });


const signInBtnLink = document.querySelector('.signInBtn-link');
const signUpBtnLink = document.querySelector('.signUpBtn-link');
const wrapper = document.querySelector('.wrapper');

signUpBtnLink.addEventListener('click', () => {
    wrapper.classList.toggle('active');
})

signInBtnLink.addEventListener('click', () => {
    wrapper.classList.toggle('active');
})

