# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto
COPY hora.py .

# Comando para ejecutar el script
CMD ["python", "hora.py"]