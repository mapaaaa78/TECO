
# TECO — prototipo funcional en Python

Este proyecto reproduce el flujo visual del prototipo TECO como una aplicación web móvil hecha con Python + Streamlit.

## 1. Instalar Python
Instala Python 3.12 desde python.org. Durante la instalación en Windows activa **Add Python to PATH**.

## 2. Instalar Visual Studio Code
Instala VS Code desde code.visualstudio.com.

## 3. Abrir el proyecto
Descomprime `TECO_app.zip`. En VS Code selecciona **File > Open Folder** y abre la carpeta `TECO_app`.

## 4. Abrir la terminal
En VS Code: **Terminal > New Terminal**.

## 5. Crear un entorno virtual (recomendado)
Windows:
```
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:
```
python3 -m venv .venv
source .venv/bin/activate
```

## 6. Instalar dependencias
```
pip install -r requirements.txt
```

## 7. Ejecutar TECO
```
streamlit run app.py
```

Se abrirá automáticamente en el navegador. Si no ocurre, copia la dirección local que aparece en la terminal, normalmente `http://localhost:8501`.

## Archivos
- `app.py`: toda la aplicación.
- `requirements.txt`: librerías necesarias.
- `README.md`: estas instrucciones.

## Importante
Es un prototipo funcional. Los mapas, recicladores, disponibilidad, clasificación automática por IA y recolecciones usan datos demostrativos. Para producción deben conectarse a servicios reales, una base de datos, autenticación, mapas y una fuente validada de gestores/puntos.
