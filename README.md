# eCommerce-api

Backend para la prueba técnica "Mini E-commerce" desarrollado en Python con FastAPI y base de datos SQL Azure.

---

## Requisitos

- Python 3.8 o superior  
- Git  


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

## Base de Datos
Para poder visualizar la base de datos:

- Server Name:
```bash
server-west-2.database.windows.net
```

- Login (User)  
```bash
supp
```

- Password:
```bash
G7v#9XpL!zQ2&fRt
```

- Options > Connections Properties > Connect to DataBase:
```bash
neoShop_db
```

La API estará disponible en:
📍 http://localhost:8000
📚 Documentación automática en:
📄 http://localhost:8000/docs