FROM python:3.11-slim

# Instala dependencias del sistema
RUN apt-get update && apt-get install -y curl gnupg2 apt-transport-https unixodbc-dev

# Instala ODBC Driver 17 para SQL Server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
 && curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list > /etc/apt/sources.list.d/mssql-release.list \
 && apt-get update \
 && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Instala dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia tu app
COPY . /app
WORKDIR /app

# Puerto
EXPOSE 8000

# Comando para arrancar FastAPI
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
