
# 📌 Método Húngaro - Asignación Óptima de Tareas

Este proyecto implementa el **Método Húngaro** para resolver problemas de asignación de tareas a trabajadores de manera óptima, minimizando el coste total.

![Método Húngaro](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Hungarian_algorithm_example.svg/800px-Hungarian_algorithm_example.svg.png)

---

## 🚀 ¿Qué hace este programa?

Este sistema web permite:
1. Ingresar el número de trabajadores y tareas.
2. Capturar los costos individuales para asignar cada tarea a cada trabajador.
3. Resolver automáticamente el problema utilizando el **Método Húngaro**.
4. Mostrar visualmente la matriz de costos y la asignación óptima.
5. Retornar el costo mínimo total del trabajo asignado.

---

## 🧠 ¿Qué es el Método Húngaro?

El **Método Húngaro** es un algoritmo diseñado para resolver problemas de asignación de forma eficiente. Dado un conjunto de tareas y un conjunto de agentes (como trabajadores), cada uno con un costo asociado por realizar cada tarea, el objetivo es asignar una tarea a cada trabajador de forma que el **costo total sea mínimo** (o beneficio máximo si se adapta).

> Fue introducido por Harold Kuhn en 1955, basado en ideas de Dénes Kőnig y Jenő Egerváry.

---

## ⚙️ ¿Cómo funciona el algoritmo?

1. **Construcción de una matriz cuadrada**:  
   Se asegura que el número de trabajadores sea igual al número de tareas. Si no lo es, se agregan filas o columnas ficticias con ceros.

2. **Reducción por filas y columnas**:  
   Se resta el valor mínimo de cada fila y luego el mínimo de cada columna. Esto produce una matriz con ceros que representan posibles asignaciones óptimas.

3. **Cobertura de ceros**:  
   Se cubren los ceros de la matriz con el menor número de líneas posibles. Si se necesitan menos líneas que filas/columnas, se ajusta la matriz y se repite el proceso.

4. **Asignación**:  
   Se eligen ceros únicos por fila y columna para crear una solución. Si hay múltiples caminos, se ajusta hasta llegar a una asignación válida.

5. **Resultado**:  
   Se obtiene la asignación de tareas a trabajadores y el costo mínimo total.

---

## 🧾 Estructura del proyecto

```
📁 Metodo_hungaro/
├── templates/
│   ├── index.html              # Página de inicio
│   ├── datos_1.html            # Formulario: cantidad de trabajadores y tareas
│   ├── datos_2.html            # Formulario: matriz de costos
│   ├── resumen.html            # Muestra matriz de entrada
│   └── solucion.html           # Muestra matriz de solución y asignaciones
├── static/
│   └── style.css               # Estilos generales (opcional)
├── app.py (o main.py)         # Servidor Flask principal
└── algoritmo.py               # Implementación del Método Húngaro
```

---

## 🌐 ¿Cómo usarlo?

1. Clona este repositorio:
   ```bash
   git clone https://github.com/kevincj2415/Metodo_hungaro.git
   cd Metodo_hungaro
   ```

2. Instala Flask:
   ```bash
   pip install flask
   ```

3. Ejecuta la aplicación:
   ```bash
   python app.py
   ```

4. Abre tu navegador y accede a:  
   [http://localhost:5000](http://localhost:5000)

---

## 📷 Ejemplo de uso

1. Introduces 3 trabajadores y 3 tareas.
2. Cargas los costos de asignación como una matriz.
3. El sistema calcula y te muestra:
   - La matriz original de costos.
   - La asignación óptima.
   - El costo total mínimo.

---

## 🛠️ Dependencias

- Python 3.7+
- Flask

---

## 🤝 Créditos

- Desarrollado por [@kevincj2415](https://github.com/kevincj2415)
- Inspirado en el algoritmo de Kuhn (Hungarian Algorithm)

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

---

> 💡 ¡Ideal para aplicaciones de logística, planificación de producción, tareas en paralelo, o asignación de recursos!
