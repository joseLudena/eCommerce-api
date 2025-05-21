# eCommerce-api

Backend para la prueba técnica "Mini E-commerce" desarrollado en Python con FastAPI y base de datos SQL Azure.

---

## Requisitos

- Python 3.8 o superior  
- Git  
- ODBC Driver 17+ para SQL Server (para conectarse a SQL Azure)

---

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/joseLudena/eCommerce-api.git
cd eCommerce-api
```

2. Crea y activa un entorno virtual:

```bash
py -m venv venv
source venv/Scripts/activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

-Si no tienes uvicorn en el archivo, instálalo manualmente:

```bash
pip install uvicorn
```

4. Inicia el servidor FastAPI:

```bash
uvicorn src.main:app --reload
```

La API estará disponible en:
📍 http://localhost:8000
📚 Documentación automática en:
📄 http://localhost:8000/docs