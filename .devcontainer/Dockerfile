# FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

# use this Dockerfile to install additional tools you might need, e.g.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

# Instalar dependencias del sistema para PostgreSQL y Node.js (necesarias para psycopg2, etc.)
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
       python3-dev \
       postgresql-client \
       libpq-dev \
       nodejs \
       npm