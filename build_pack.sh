#!/bin/bash

# Nome do pacote
PACKAGE_NAME="pathobs"

# Verifica se o script está sendo executado no diretório correto
if [ ! -f "setup.py" ]; then
    echo "Erro: setup.py não encontrado. Execute este script no diretório raiz do projeto."
    exit 1
fi

# Limpa builds anteriores
echo "Limpando builds anteriores..."
rm -rf dist/
rm -rf build/
rm -rf *.egg-info

# Cria o pacote distribuível
echo "Criando pacote distribuível..."
python3 setup.py sdist bdist_wheel

# Verifica se o pacote foi criado com sucesso
if [ $? -ne 0 ]; then
    echo "Erro ao criar o pacote distribuível."
    exit 1
fi

# Verifica se twine está instalado
if ! command -v twine &> /dev/null; then
    echo "Twine não está instalado. Instalando twine..."
    sudo apt install twine
    #pip install twine
fi

# Faz o upload do pacote para o PyPI
echo "Fazendo upload do pacote para o PyPI..."
twine upload dist/*

# Verifica se o upload foi bem-sucedido
if [ $? -ne 0 ]; then
    echo "Erro ao fazer upload do pacote para o PyPI."
    exit 1
fi

echo "Pacote publicado com sucesso no PyPI!"

# Opção para instalar o pacote localmente
read -p "Deseja instalar o pacote localmente? (y/n): " INSTALL_LOCAL

if [ "$INSTALL_LOCAL" = "y" ]; then
    echo "Instalando o pacote localmente..."
    pip install .
    if [ $? -eq 0 ]; then
        echo "Pacote instalado com sucesso!"
    else
        echo "Erro ao instalar o pacote localmente."
        exit 1
    fi
fi

echo "Script finalizado."
