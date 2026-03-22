# Preparando sistema
FROM python:3.14-slim

RUN apt-get update && apt-get install -y curl && apt-get clean
RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

# Copiando projeto
WORKDIR /app
COPY app .
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Instalando dependencias
RUN poetry install & poetry sync

# Subindo projeto
EXPOSE 80
ENTRYPOINT [ "/entrypoint.sh" ]
CMD ["poetry", "run", "server", "--config", "docker"]
