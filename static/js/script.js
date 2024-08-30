/** @format */

const signInBtn = document.querySelector("#sign-in");
signInBtn.addEventListener("click", () => {
  window.location = "/register";
});

document.querySelectorAll(".wrapper").forEach((wrapper) => {
  const slide = wrapper.querySelector(".imageContainer");
  const firstImg = slide.querySelectorAll("img")[0];
  const arrowIcons = wrapper.querySelectorAll("i");

  let isDragStart = false,
    isDragging = false,
    prevPageX,
    prevScrollLeft,
    positionDiff;

  const showHideIcons = () => {
    let scrollWidth = slide.scrollWidth - slide.clientWidth;
    arrowIcons[0].style.display = slide.scrollLeft == 0 ? "none" : "block";
    arrowIcons[1].style.display =
      slide.scrollLeft == scrollWidth ? "none" : "block";
  };

  arrowIcons.forEach((icon) => {
    let firstImgWidth = firstImg.clientWidth + 14;
    icon.addEventListener("click", () => {
      slide.scrollLeft += icon.id == "left" ? -firstImgWidth : firstImgWidth;
      setTimeout(() => showHideIcons(), 60);
    });
  });

  const autoSlide = () => {
    if (slide.scrollLeft == slide.scrollWidth - slide.clientWidth) return;
    positionDiff = Math.abs(positionDiff);
    let firstImgWidth = firstImg.clientWidth + 14;
    let valDifference = firstImgWidth - positionDiff;
    if (slide.scrollLeft > prevScrollLeft) {
      return (slide.scrollLeft +=
        positionDiff > firstImgWidth / 3 ? valDifference : -positionDiff);
    }
    slide.scrollLeft -=
      positionDiff > firstImgWidth / 3 ? valDifference : -positionDiff;
  };

  const dragStart = (e) => {
    isDragStart = true;
    prevPageX = e.pageX || e.touches[0].pageX;
    prevScrollLeft = slide.scrollLeft;
  };

  const dragging = (e) => {
    if (!isDragStart) return;
    e.preventDefault();
    isDragging = true;
    slide.classList.add("dragging");
    positionDiff = (e.pageX || e.touches[0].pageX) - prevPageX;
    slide.scrollLeft = prevScrollLeft - positionDiff;
  };

  const dragStop = () => {
    isDragStart = false;
    slide.classList.remove("dragging");
    if (!isDragging) return;
    isDragging = false;
    autoSlide();
  };

  slide.addEventListener("mousedown", dragStart);
  slide.addEventListener("touchstart", dragStart);

  slide.addEventListener("mousemove", dragging);
  slide.addEventListener("touchmove", dragging);

  slide.addEventListener("mouseleave", dragStop);
  slide.addEventListener("touchend", dragStop);
  slide.addEventListener("mouseup", dragStop);
});

function showLoadingAnimation() {
  document.getElementById("loading-animation").style.display = "flex";
}
