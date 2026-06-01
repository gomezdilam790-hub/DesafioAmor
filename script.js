const pages = [

{
number:"01",
image:"./assets/photos/foto01.jpeg",
text:`Querida Valeria,

No sé si esta carta tiene un propósito.

Tal vez no busca cambiar nada.

Tal vez solo existe porque hay cosas que llevo guardando demasiado tiempo y ya pesan más de lo que debería.`
},

{
number:"02",
image:"./assets/photos/foto02.jpeg",
text:`A veces pienso en nosotros y me pregunto en qué momento dejamos que todo se quedara a medio camino.

Hubo problemas, situaciones que nos superaron, momentos en los que ninguno de los dos supo cómo manejar lo que estaba pasando.

Y aunque entiendo las razones que nos llevaron a tomar distancia, hay una parte de mí que todavía siente que la decisión llegó demasiado pronto.`
},

{
number:"03",
image:"./assets/photos/foto03.jpeg",
text:`Lo que más me cuesta no es aceptar que las cosas cambiaron.

Lo que más me cuesta es fingir que para mí cambió todo.

Porque tú pareces capaz de estar ahí, de hablar conmigo y seguir adelante desde un lugar tranquilo.`
},

{
number:"04",
image:"./assets/photos/foto04.jpeg",
text:`Y yo quisiera decir que puedo hacer lo mismo.

Pero no sería verdad.

No sé cómo verte solamente como una amiga cuando todavía sonrío cada vez que aparece una foto tuya.`
},

{
number:"05",
image:"./assets/photos/foto05.jpeg",
text:`Y quizás eso pasa porque nunca fuiste una persona más para mí.

Fuiste refugio.

Fuiste una de las pocas personas que logró hacerme sentir querido, acompañado y realmente amado.`
},

{
number:"06",
image:"./assets/photos/foto06.jpeg",
text:`Todavía recuerdo aquella fiesta donde te conocí.

Se suponía que solo íbamos a pasar el rato.

Pero algo pasó.

No sé explicarlo.`
},

{
number:"07",
image:"./assets/photos/foto07.jpeg",
text:`Y desde ese momento, cada día a tu lado comenzó a sentirse un poco más especial que el anterior.

Recuerdo tu sonrisa tímida.

Recuerdo tus abrazos cuando estaba a punto de derrumbarme.`
},

{
number:"08",
image:"./assets/photos/foto08.jpeg",
text:`Recuerdo tus besos.

No por lo físicos que fueron.

Sino por cómo me hacían sentir.

Deseado. Elegido. Querido.`
},

{
number:"09",
image:"./assets/photos/foto09.jpeg",
text:`Porque al final no fueron los grandes momentos los que me hicieron quedarme.

Fueron todos los pequeños momentos.

Tus mensajes.

Tus risas.

Tus ocurrencias.`
},

{
number:"10",
image:"./assets/photos/foto10.jpeg",
text:`Tu manera de preocuparte por mí.

Tu forma de hacerme sentir que tenía a alguien caminando a mi lado.

Sentía que estaba construyendo algo valioso.`
},

{
number:"11",
image:"./assets/photos/foto11.jpeg",
text:`Por eso duele tanto.

Porque no estoy extrañando algo que tuve.

Estoy extrañando algo que quería construir.`
},

{
number:"12",
image:"./assets/photos/foto12.jpeg",
text:`Siempre pensé que si algún día nuestras historias tomaban caminos diferentes sería por la distancia.

Nunca pensé que sería por esto.

Nunca pensé que sería por momentos difíciles que quizá habríamos podido superar juntos.`
},

{
number:"13",
image:"./assets/photos/foto13.jpeg",
text:`No me quedé por costumbre.

Me quedé porque te quería.

Porque entre todas las personas que han pasado por mi vida, tú fuiste una de las pocas que logró hacerme sentir en casa.`
},

{
number:"14",
image:"./assets/photos/foto14.jpeg",
text:`Todavía me importas.

Todavía pienso en ti más de lo que debería.

Y si algún día te preguntas qué significaste para mí, quiero que recuerdes esto:

Fuiste una de las historias más bonitas que me ha tocado vivir.

Con cariño,

Dilan`
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

}, 1000);
```

});

function renderPage(){

book.innerHTML = `

<div class="page page-turn">

```
<div class="left-page">

    <img
        src="${pages[currentPage].image}"
        class="page-image"
        alt="foto"
    >

    <div class="page-number">
        ${pages[currentPage].number}
    </div>

</div>

<div class="right-page">

    <div class="text-container">

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
```

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

```
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
```

}

write();

}

function nextPage(){

if(currentPage < pages.length - 1){

```
currentPage++;

renderPage();
```

}

}

function prevPage(){

if(currentPage > 0){

```
currentPage--;

renderPage();
```

}

}

