const startBtn = document.getElementById("startBtn");

const cover = document.getElementById("cover");

const book = document.getElementById("book");

startBtn.addEventListener("click", () => {

    cover.classList.add("fade-out");

    setTimeout(() => {

        cover.style.display = "none";

        book.classList.remove("hidden");

        book.classList.add("fade-in");

    }, 1200);

});
