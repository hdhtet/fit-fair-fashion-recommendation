const buttons = document.querySelectorAll(".toggleButton");

buttons.forEach((button) => {
  button.addEventListener("click", function () {
    const content = this.parentElement.nextElementSibling;
    const icon = this.querySelector("i");

    if (content.classList.contains("hidden")) {
      content.classList.remove("hidden");
      icon.classList.replace("fa-chevron-down", "fa-chevron-up");
    } else {
      content.classList.add("hidden");
      icon.classList.replace("fa-chevron-up", "fa-chevron-down");
    }
  });
});

function changeImage(imagePath, altText) {
  const image = document.getElementById("bodyTypeImage");
  image.src = imagePath;
  image.alt = altText;
}
