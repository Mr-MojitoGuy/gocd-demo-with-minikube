#!/bin/bash

# Verifica se o Python 3 está instalado
if command -v python3 &>/dev/null; then
    echo "Python 3 is already installed: $(python3 --version)"
    exit 0
fi

echo "Python 3 not found. Installing..."

# Detectar o sistema operacional
if [ -f /etc/debian_version ]; then
    echo "Debian distro detected..."
    apt update && apt install -y python3 python3-pip
elif [ -f /etc/redhat-release ]; then
    echo "RHEL distro detected..."
    yum install -y python3 python3-pip
else
    echo "This system isn't supported for automatic instalation. Please, install Python manually."
    exit 1
fi

# Confirmação
if command -v python3 &>/dev/null; then
    echo "Python 3 installed with success: $(python3 --version)"
else
    echo "Error installing Python 3."
    exit 1
fi
