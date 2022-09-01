function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

document.addEventListener("DOMContentLoaded", function () {
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }
});
