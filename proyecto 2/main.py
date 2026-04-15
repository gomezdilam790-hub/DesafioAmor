const express = require("express");
const sqlite3 = require("sqlite3").verbose();
const app = express();

app.use(express.json());

// 🗄️ DB
const db = new sqlite3.Database("./database.sqlite");

db.serialize(() => {
  db.run(`CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    precio REAL,
    stock INTEGER
  )`);

  db.run(`CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT,
    total REAL
  )`);

  db.run(`CREATE TABLE IF NOT EXISTS caja (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT,
    total_ventas REAL,
    dinero_real REAL,
    diferencia REAL
  )`);
});

// 🌐 FRONTEND (TODO EMBEBIDO)
app.get("/", (req, res) => {
  res.send(`
    <h2>📦 Inventario</h2>
    <input id="nombre" placeholder="Nombre">
    <input id="precio" placeholder="Precio">
    <input id="stock" placeholder="Stock">
    <button onclick="agregar()">Agregar</button>

    <ul id="lista"></ul>

    <h2>🛒 Venta</h2>
    <input id="id" placeholder="ID Producto">
    <input id="cantidad" placeholder="Cantidad">
    <button onclick="vender()">Vender</button>

    <h2>💰 Caja</h2>
    <input id="dinero" placeholder="Dinero en caja">
    <button onclick="caja()">Cerrar Caja</button>

    <script>
      const API = "";

      async function cargar() {
        const res = await fetch("/productos");
        const data = await res.json();

        const lista = document.getElementById("lista");
        lista.innerHTML = "";

        data.forEach(p => {
          const li = document.createElement("li");
          li.textContent = p.id + " - " + p.nombre + " | Stock: " + p.stock + " | $" + p.precio;
          lista.appendChild(li);
        });
      }

      async function agregar() {
        const nombre = document.getElementById("nombre").value;
        const precio = parseFloat(document.getElementById("precio").value);
        const stock = parseInt(document.getElementById("stock").value);

        await fetch("/productos", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ nombre, precio, stock })
        });

        cargar();
      }

      async function vender() {
        const id = parseInt(document.getElementById("id").value);
        const cantidad = parseInt(document.getElementById("cantidad").value);

        const res = await fetch("/ventas", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ items: [{ id, cantidad }] })
        });

        const data = await res.json();
        alert("Total: " + data.total);
        cargar();
      }

      async function caja() {
        const dinero = parseFloat(document.getElementById("dinero").value);

        const res = await fetch("/caja", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ dinero_real: dinero })
        });

        const data = await res.json();
        alert("Ventas: " + data.totalVentas + " | Diferencia: " + data.diferencia);
      }

      cargar();
    </script>
  `);
});

// 📦 PRODUCTOS
app.get("/productos", (req, res) => {
  db.all("SELECT * FROM productos", [], (err, rows) => {
    res.json(rows);
  });
});

app.post("/productos", (req, res) => {
  const { nombre, precio, stock } = req.body;

  db.run(
    "INSERT INTO productos (nombre, precio, stock) VALUES (?,?,?)",
    [nombre, precio, stock],
    function () {
      res.json({ id: this.lastID });
    }
  );
});

// 🛒 VENTAS
app.post("/ventas", (req, res) => {
  const { items } = req.body;
  let total = 0;

  db.serialize(() => {
    items.forEach((item) => {
      db.get(
        "SELECT * FROM productos WHERE id=?",
        [item.id],
        (err, producto) => {
          if (!producto || producto.stock < item.cantidad) return;

          total += producto.precio * item.cantidad;

          db.run(
            "UPDATE productos SET stock = stock - ? WHERE id=?",
            [item.cantidad, item.id]
          );
        }
      );
    });

    db.run(
      "INSERT INTO ventas (fecha, total) VALUES (?,?)",
      [new Date().toISOString(), total],
      function () {
        res.json({ total });
      }
    );
  });
});

// 💰 CAJA
app.post("/caja", (req, res) => {
  const { dinero_real } = req.body;
  const hoy = new Date().toISOString().split("T")[0];

  db.get(
    "SELECT SUM(total) as total FROM ventas WHERE fecha LIKE ?",
    [hoy + "%"],
    (err, row) => {
      const totalVentas = row.total || 0;
      const diferencia = dinero_real - totalVentas;

      db.run(
        "INSERT INTO caja (fecha, total_ventas, dinero_real, diferencia) VALUES (?,?,?,?)",
        [hoy, totalVentas, dinero_real, diferencia],
        function () {
          res.json({ totalVentas, diferencia });
        }
      );
    }
  );
});

// 🚀 SERVIDOR
app.listen(3000, () => {
  console.log("http://localhost:3000");
});
