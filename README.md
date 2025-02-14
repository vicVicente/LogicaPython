Comando usados para iniciar o container:

Para criar a imagem docker:
```
Docker build -t simpleapi .
```

Para iniciar o container:
```
Docker run -p 5000:5000 simpleapi
```

Dentro da pasta "Postman", deixei a collection em JSON exportada para o teste do sistema após o serviço ser iniciado.
