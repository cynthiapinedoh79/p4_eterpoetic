#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Crear un entorno virtual si no existe
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv .venv
fi

# Activar el entorno virtual para que todos los comandos usen el python/pip correctos
source .venv/bin/activate
  
# Asegurar que pip esté funcional y actualizado
echo "Upgrading pip in the new virtual environment..."
pip install --upgrade pip

# Instalar dependencias
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Opcional: Ejecutar migraciones de Django
echo "Running Django migrations..."
python manage.py migrate

echo "Setup complete. Your environment is ready!"