function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function delay(time) {
  return new Promise(resolve => setTimeout(resolve, time));
}

function Create() {
  let xhr = new XMLHttpRequest();
  xhr.open("POST", 'http://127.0.0.1:80/create');
  xhr.setRequestHeader("Accept", "application/json");
  xhr.setRequestHeader("Content-Type", "application/json");
  const data = JSON.stringify({
    title: document.getElementById('title').value,
    content: document.getElementById('content').value
  });
  xhr.send(data);
}

function Edit() {
  let xhr = new XMLHttpRequest();
  xhr.open("POST", 'http://127.0.0.1:80/edit');
  xhr.setRequestHeader("Accept", "application/json");
  xhr.setRequestHeader("Content-Type", "application/json");
  const data = JSON.stringify({
    id: parseInt(event.target.parentElement.id),
    title: event.target.parentElement.querySelector('.card-title').innerText,
    content: event.target.parentElement.querySelector('.card-content').innerText
  });
  xhr.send(data);
}

function Trash() {
  let xhr = new XMLHttpRequest();
  xhr.open("POST", 'http://127.0.0.1:80/trash');
  xhr.setRequestHeader("Accept", "application/json");
  xhr.setRequestHeader("Content-Type", "application/json");
  const data = JSON.stringify({
    id: parseInt(event.target.parentElement.id)
  });
  xhr.send(data);
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
