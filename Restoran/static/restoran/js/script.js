const slider = document.querySelector('.preview')
const sliderItems = Array.from(slider.children);
const btn_next = document.querySelector('.arrow_right')
const btn_previous = document.querySelector('.arrow_left')
const poloska = document.querySelector(".poloska_under")
let offset = 0
var timer = null 
let nextSlideIndex
sliderItems.forEach(function (slide, index, options) {
    console.log(slide)   
    
    if (index !== 0) {
        slide.classList.add('hidden')
    }

    slide.dataset.Index = index;

    sliderItems[0].setAttribute('data-active', '')

    // slide.addEventListener('click',function(){
    
    //     slide.classList.add('hidden')
    //     slide.removeAttribute('data-active')

    //     let nextSlideIndex = index + 1 === sliderItems.length ? 0 : index + 1 

    //     const nextSlide = slider.querySelector(`[data--index="${nextSlideIndex}"]`);
    //     nextSlide.classList.remove('hidden')
    //     nextSlide.setAttribute('data-active', '')
    // });

});


btn_next.onclick = function () {
    showNextSlide("next")
}

btn_previous.onclick = function () {
    showNextSlide("prev")
}
afterTime(4000)
let currentSlideIndex
function showNextSlide(direction){

    const currentSlide = slider.querySelector('[data-active]')
    currentSlideIndex = +currentSlide.dataset.Index;
    currentSlide.classList.add('hidden')
    currentSlide.removeAttribute('data-active')

    
    if(direction === "next"){
        nextSlideIndex = currentSlideIndex + 1 === sliderItems.length ? 0 : currentSlideIndex + 1 ;
        offset += 15.63;
        if(offset > 62.50){
            offset = 0
        }
        poloska.style.left = offset + 'vw';
    }else if(direction === "prev"){
        nextSlideIndex = currentSlideIndex === 0 ? sliderItems.length - 1 : currentSlideIndex - 1 ;
        offset -= 15.63;
        if(offset < 0){
            offset = 46.89
        }
        poloska.style.left = offset + 'vw';
    }

    const nextSlide = slider.querySelector(`[data--index="${nextSlideIndex}"]`);
    nextSlide.classList.remove('hidden')
    nextSlide.setAttribute('data-active', '')

    afterTime(4000)
}

function afterTime(delay){
    clearInterval(timer)
    console.log("123")
    timer = setInterval(()=>{
        nextSlideIndex = currentSlideIndex + 1 === sliderItems.length ? 0 : currentSlideIndex + 1 ;
        showNextSlide("next")
    }, delay)
}

setTimeout(function() {
    document.body.classList.add('body_visible');
}, 200)

function reveal() {
    var reveals = document.querySelectorAll(".reveal");
    for (var i = 0; i < reveals.length; i++) {
        var windowHeight = window.innerHeight;
        var elementTop = reveals[i].getBoundingClientRect().top;
        var elementVisible = 150;
        if (elementTop < windowHeight - elementVisible) {
          reveals[i].classList.add("active");
        }
    }
}
window.addEventListener("scroll", reveal);