#Intalando o python
FROM python:3.12
#Criando uma pasta para trabalhar
WORKDIR /app
#Copio o arquivo principal que vou utilizar
COPY SimpleApi.py .
#Instalo a dependência do projeto
RUN pip install --no-cache-dir flask
#Exponho a porta
EXPOSE 5000
#Aplico o comando para iniciar o projeto assim que rodar o container.
CMD ["python", "SimpleApi.py"]