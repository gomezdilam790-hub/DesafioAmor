const pages = [

{
number: "01",
image: "./assets/photos/foto01.jpeg",
text: `No sé si esta carta tiene un propósito.

Tal vez no busca cambiar nada.

Tal vez solo existe porque hay cosas que llevo guardando demasiado tiempo y ya pesan más de lo que debería.`
},

{
number: "02",
image: "./assets/photos/foto02.jpeg",
text: `A veces pienso en nosotros y me pregunto en qué momento dejamos que todo se quedara a medio camino.

Hubo problemas, situaciones que nos superaron, momentos en los que ninguno de los dos supo cómo manejar lo que estaba pasando.`
},

{
number: "03",
image: "./assets/photos/foto03.jpeg",
text: `Lo que más me cuesta no es aceptar que las cosas cambiaron.

Lo que más me cuesta es fingir que para mí cambió todo.`
}

];

let currentPage = 0;

const startBtn = document.getElementById("startBtn");
const cover = document.getElementById("cover");
const book = document.getElementById("book");

startBtn.addEventListener("click", () => {

    cover.classList.add("fade-out");

    setTimeout(() => {

        cover.style.display = "none";

        book.classList.remove("hidden");

        renderPage();

    }, 1000);

});

function renderPage() {

    book.innerHTML = `

    <div class="page page-turn">

        <div class="left-page">

            <img
                src="${pages[currentPage].image}"
                alt="foto"
                class="page-image"
            >

            <div class="page-number">
                ${pages[currentPage].number}
            </div>

        </div>

        <div class="right-page">

            <div>

                <div class="page-decoration">
                    ✈
                </div>

                <div
                    id="typingText"
                    class="letter">
                </div>

            </div>

            <div class="controls">

                <button onclick="prevPage()">
                    ←
                </button>

                <button onclick="nextPage()">
                    →
                </button>

            </div>

        </div>

    </div>

    `;

    typeWriter(
        pages[currentPage].text,
        document.getElementById("typingText")
    );

}

function typeWriter(text, element){

    element.innerHTML = "";

    let i = 0;

    function write(){

        if(i < text.length){

            const char = text.charAt(i);

            if(char === "\n"){
                element.innerHTML += "<br>";
            }else{
                element.innerHTML += char;
            }

            i++;

            setTimeout(write, 20);
        }
    }

    write();
}

function nextPage(){

    if(currentPage < pages.length - 1){

        currentPage++;

        renderPage();
    }
}

function prevPage(){

    if(currentPage > 0){

        currentPage--;

        renderPage();
    }
}
