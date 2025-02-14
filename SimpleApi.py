from flask import Flask, request, jsonify
#Atribuo a biblioteca utilizada na var "app", como boa pratica
app = Flask(__name__)

#Crio as rotas e suas respectivas lógicas
@app.route("/saudacao", methods=['GET'])
def get_nome():
    nome = request.args.get("nome")
    return jsonify({"mensagem": f"Olá, {nome}, seja muito bem-vindo!"})

@app.route("/soma", methods=['POST'])
def post_soma():
    dados = request.get_json()
    num1 = dados.get("num1")
    num2 = dados.get("num2")
    resultado = num1 + num2
    return jsonify({"resultado": resultado})

#Verifico a execução do arquivo, permito o acesso a rede e ao modo depuração
if __name__ == "__main__": 
    app.run(host="0.0.0.0", debug=True)