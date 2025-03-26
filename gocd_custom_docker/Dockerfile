FROM gocd/gocd-agent-alpine:v25.1.0

USER root

# Copiar o ficheiro de dependências para dentro da imagem
COPY requirements.txt .

# Instalar Python,  pip e dependências
RUN apk update && \
    apk add --no-cache python3 py3-pip && \
    ln -sf python3 /usr/bin/python && \
    pip3 install --break-system-packages -r requirements.txt

USER go
