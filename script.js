const pages = [
{
number: "01",
image: "assets/photos/foto01.jpeg",
text: "Hola Valeria. Si ves este texto escribiéndose, todo funciona."
}
];

let currentPage = 0;

const startBtn = document.getElementById("startBtn");
const cover = document.getElementById("cover");
const book = document.getElementById("book");

startBtn.addEventListener("click", () => {
cover.style.display = "none";
book.classList.remove("hidden");
renderPage();
});

function renderPage(){

book.innerHTML = `

<div class="page">

<div class="left-page">
<img src="${pages[currentPage].image}" class="page-image">
</div>

<div class="right-page">

<div id="typingText" class="letter"></div>

</div>

</div>
`;

typeWriter(
pages[currentPage].text,
document.getElementById("typingText")
);

}

function typeWriter(text, element){

let i = 0;

element.innerHTML = "";

function write(){

if(i < text.length){

element.innerHTML += text.charAt(i);

i++;

setTimeout(write, 50);

}

}

write();

}
