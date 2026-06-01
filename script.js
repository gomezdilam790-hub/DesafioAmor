const pages = [
{
number: "01",
image: "assets/photos/foto01.jpeg",
text: `No sé si esta carta tiene un propósito.

Tal vez no busca cambiar nada.

Tal vez solo existe porque hay cosas que llevo guardando demasiado tiempo y ya pesan más de lo que debería.`
},

{
number: "02",
image: "assets/photos/foto02.jpeg",
text: `A veces pienso en nosotros y me pregunto en qué momento dejamos que todo se quedara a medio camino.

Hubo problemas, situaciones que nos superaron, momentos en los que ninguno de los dos supo cómo manejar lo que estaba pasando.`
},

{
number: "03",
image: "assets/photos/foto03.jpeg",
text: `Lo que más me cuesta no es aceptar que las cosas cambiaron.

Lo que más me cuesta es fingir que para mí cambió todo.`
}
];

let currentPage = 0;

const startBtn = document.getElementById("startBtn");
const cover = document.getElementById("cover");
const book = document.getElementById("book");

startBtn.addEventListener("click", () => {

```
cover.classList.add("fade-out");

setTimeout(() => {

    cover.style.display = "none";

    book.classList.remove("hidden");

    renderPage();

}, 800);
```

});

function renderPage(){

```
const page = pages[currentPage];

book.innerHTML = `
<div class="page page-turn">

    <div class="left-page">

        <img
            src="${page.image}"
            alt="foto"
            class="page-image"
        >

        <div class="page-number">
            ${page.number}
        </div>

    </div>

    <div class="right-page">

        <div class="page-decoration">
            ✈
        </div>

        <div
            class="letter"
            id="typingText">
        </div>

        <div class="controls">

            <button id="prevBtn">
                ←
            </button>

            <button id="nextBtn">
                →
            </button>

        </div>

    </div>

</div>
`;

document
    .getElementById("prevBtn")
    .addEventListener("click", prevPage);

document
    .getElementById("nextBtn")
    .addEventListener("click", nextPage);

typeWriter(
    page.text,
    document.getElementById("typingText")
);
```

}

function typeWriter(text, element){

```
let i = 0;

element.innerHTML = "";

function write(){

    if(i >= text.length){
        return;
    }

    const char = text.charAt(i);

    if(char === "\n"){
        element.innerHTML += "<br>";
    }else{
        element.innerHTML += char;
    }

    i++;

    setTimeout(write, 25);
}

write();
```

}

function nextPage(){

```
if(currentPage < pages.length - 1){

    currentPage++;

    renderPage();
}
```

}

function prevPage(){

```
if(currentPage > 0){

    currentPage--;

    renderPage();
}
```

}
