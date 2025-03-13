# Usa uma imagem leve do Python
FROM python:3.9-slim

# Define um diretório de trabalho dentro do container
WORKDIR /app

# Copia apenas o arquivo de dependências primeiro (para otimizar cache)
COPY requirements.txt .

# Instala as dependências da aplicação
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos para o container
COPY . .

# Expõe a porta usada pelo Flask
EXPOSE 5000

# Define o comando para rodar a aplicação
CMD ["python", "horarios.py"]
