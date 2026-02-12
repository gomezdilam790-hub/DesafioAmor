import os
import random
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Rectangle, RoundedRectangle, Ellipse, Line, Quad
from kivy.animation import Animation
from kivy.clock import Clock

class DesafioApp(App):
    def build(self):
        self.title = "Matrimonio a Prueba de Fuego"
        self.store = JsonStore('progreso.json')
        
        if not self.store.exists('config'):
            self.store.put('config', inicio=datetime.now().strftime("%Y-%m-%d"))
        
        self.lista_retos = self.cargar_retos()

        # --- CONTENEDOR RAÍZ ---
        self.main_layout = FloatLayout()
        
        with self.main_layout.canvas.before:
            # Fondo Rojo Sangre Oscuro (Efecto Cuero)
            Color(0.15, 0.02, 0.02, 1) 
            self.rect_bg = Rectangle(size=Window.size, pos=(0,0))
            
            # Resplandor Inferior del Fuego (Glow)
            Color(0.8, 0.2, 0, 0.3)
            self.glow = Ellipse(size=(Window.width * 1.5, Window.height * 0.4), 
                               pos=(-Window.width*0.25, -Window.height*0.1))

        # Partículas de llamas (Llamas vivas)
        Clock.schedule_interval(self.crear_llama, 0.05)

        # --- LA PÁGINA (ESTILO PERGAMINO QUEMADO) ---
        self.hoja = FloatLayout(size_hint=(0.85, 0.85), pos_hint={'center_x': 0.52, 'center_y': 0.5})
        
        with self.hoja.canvas.before:
            # Sombra arrojada del libro
            Color(0, 0, 0, 0.4)
            self.sombra = RoundedRectangle(size=self.hoja.size, pos=(self.hoja.x + 10, self.hoja.y - 10), radius=[3, 30, 30, 3])
            
            # Papel Envejecido (Cuerpo de la página)
            Color(0.92, 0.88, 0.78, 1)
            self.rect_hoja = RoundedRectangle(size=self.hoja.size, pos=self.hoja.pos, radius=[3, 30, 30, 3])
            
            # Bordes Carbonizados (Efecto Quemado)
            Color(0.1, 0.05, 0, 0.6)
            self.borde_quemado = Line(rounded_rectangle=(self.hoja.x, self.hoja.y, self.hoja.width, self.hoja.height, 3, 30, 30, 3), width=3)
            
            # Lomo del Libro (Profundidad)
            Color(0.3, 0.1, 0.1, 1)
            self.lomo = Rectangle(size=(35, self.hoja.height), pos=self.hoja.pos)

        self.hoja.bind(size=self._update_ui, pos=self._update_ui)

        # --- CONTENIDO INTERNO ---
        self.layout_texto = BoxLayout(orientation='vertical', padding=50, spacing=20, 
                                     size_hint=(1, 1), pos_hint={'x': 0, 'y': 0})

        self.label_titulo = Label(
            text="[b][color=4d1a1a]EL DESAFÍO DEL AMOR[/color][/b]",
            markup=True, font_size='32sp', size_hint_y=0.2
        )

        self.label_reto = Label(
            text="[color=1a1a1a]“El fuego no destruye el oro,\nlo purifica.”[/color]\n\n[i][color=333333]Toca para abrir el libro.[/color][/i]",
            markup=True, font_size='22sp', text_size=(Window.width * 0.6, None),
            halign="center", valign="middle"
        )

        self.btn_accion = Button(
            text="VER PÁGINA", size_hint=(0.9, 0.12), pos_hint={'center_x': 0.5},
            background_normal='', background_color=get_color_from_hex('#8B0000'),
            color=(1, 1, 1, 1), font_size='18sp', bold=True
        )
        self.btn_accion.bind(on_press=self.pasar_pagina_efecto)

        self.layout_texto.add_widget(self.label_titulo)
        self.layout_texto.add_widget(self.label_reto)
        self.layout_texto.add_widget(self.btn_accion)
        
        self.hoja.add_widget(self.layout_texto)
        self.main_layout.add_widget(self.hoja)
        return self.main_layout

    def crear_llama(self, dt):
        # Genera partículas que parecen fuego real (naranjas, amarillas y rojas)
        with self.main_layout.canvas.after:
            color = random.choice([
                (1, 0.4, 0, 0.8), # Naranja
                (1, 0.2, 0, 0.6), # Rojo fuego
                (1, 0.7, 0, 0.5)  # Amarillo
            ])
            c = Color(*color)
            t = random.uniform(5, 15)
            fuego = Ellipse(pos=(random.uniform(0, Window.width), -20), size=(t, t))
            
            # Animación: Suben rápido y se encogen
            anim = Animation(pos=(fuego.pos[0] + random.uniform(-60, 60), Window.height * 0.4), 
                             size=(0, 0), duration=random.uniform(1.5, 3), t='out_quad')
            anim_c = Animation(a=0, duration=random.uniform(1.5, 3))
            anim.start(fuego)
            anim_c.start(c)

    def _update_ui(self, instance, value):
        self.rect_hoja.pos = instance.pos
        self.rect_hoja.size = instance.size
        self.sombra.pos = (instance.x + 10, instance.y - 10)
        self.sombra.size = instance.size
        self.lomo.pos = instance.pos
        self.lomo.size = (35, instance.height)
        self.rect_bg.size = Window.size
        self.glow.pos = (-Window.width*0.25, -Window.height*0.1)

    def cargar_retos(self):
        ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "retos.txt")
        if os.path.exists(ruta):
            with open(ruta, "r", encoding="utf-8") as f:
                return [line.strip() for line in f.readlines()]
        return ["Error: Crea el archivo retos.txt"] * 40

    def pasar_pagina_efecto(self, instance):
        # Animación de "Libro"
        pandeo = Animation(size_hint_x=0, opacity=0, duration=0.5, t='in_back')
        
        def cambio(*args):
            self.actualizar_logica()
            regreso = Animation(size_hint_x=0.85, opacity=1, duration=0.5, t='out_back')
            regreso.start(self.hoja)

        pandeo.bind(on_complete=cambio)
        pandeo.start(self.hoja)

    def actualizar_logica(self):
        fecha_inicio = datetime.strptime(self.store.get('config')['inicio'], "%Y-%m-%d")
        dia = (datetime.now() - fecha_inicio).days + 1
        
        if 1 <= dia <= 40:
            self.label_titulo.text = f"[b][color=8B0000]DÍA {dia}[/color][/b]"
            self.label_reto.text = f"[color=1a1a1a]{self.lista_retos[dia-1]}[/color]"
            self.btn_accion.text = "LIBRO CERRADO HASTA MAÑANA"
            self.btn_accion.disabled = True
            self.btn_accion.background_color = (0.3, 0.3, 0.3, 1)
        else:
            self.label_reto.text = "¡Misión Cumplida!"

if __name__ == "__main__":
    DesafioApp().run()