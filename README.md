# -MC2-Proyecto_202000774

Consiste en un programa que crea un grafo dirigido y muestra su recorrido en base a un vertice de inicio y un vertice de fin.

```
$PROJECT ROOT
│   # Archivo principal
├── Ventana.py
│   # Calculo de caminos
├── Grafo.py
│   
├── _pycache_
│   # Documentacion
└── README.md

```
## **Características Principales**

- **Interfaz Gráfica (GUI):** Creada con `tkinter` para una experiencia de usuario interactiva.
- **Manipulación de Grafos:** Añade y conecta nodos a través del módulo personalizado `Grafo` el cual los almacena y lleva un registro de los nodos.
- **Soporte para Imágenes:** Utiliza `Pillow` para cargar y mostrar imágenes relacionadas con los grafos este modulo solo se utiliza para el archivo bola.png.
- **Ejecución Concurrente:** Implementación de hilos (`threading`) para mantener la interfaz responsiva durante cálculos matemáticos complejos.
- **Cálculos Geométricos:** Manejo de operaciones matemáticas como distancias y ángulos mediante `math`.

---

## ** Requisitos **
- **Python 3.9+**
- Bibliotecas necesarias:
  - `tkinter` (incluida en la instalación estándar de Python)
  - [`Pillow`](https://pypi.org/project/Pillow/) (instalar con `pip install pillow`)
---

Para la creacion de vertice solo basta con dar doble click sobre la ventana y se abrira una ventana donde se podrá poner el nombre del nodo a crear, luego se podra crear una arista que por cierto es dirigida pulsando el boton que dice `Crear relacion` en donde aparece de que nodo a que no se desea hacer la arista ya que esta es una arista dirigida lo que implica que tiene un sentido.

Por ultimo se podra buscar un camino con la opción de `Camino` el cual busca el camino desde un nodo inicial hasta uno final y calculara la ruta mas rapida.