Comando para instalar as dependências do sistema:

```
pip install pandas flask bcrypt
```

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

Caso queira testar os demais serviços, aqui estão os comandos para utilizar no CMD, se desejar.

```
python TabelaCSV.py
```
```
python SimpleApi.py
```
```
python AsyncAwait.py
```
```
python loginCorrecao.py
```