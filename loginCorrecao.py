from flask import Flask, request
import bcrypt

app = Flask(__name__)

#Estou criptografando a senha por ser um dado sensível, evitando armazenar texto simples.
users = {
    "admin": bcrypt.hashpw(b"1234", bcrypt.gensalt())
}

#Crio as função e atribuo sua lógica
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    hashed_password = users[username]

    #VErifico se o usuario existe
    if username not in users:
        return "Acesso negado", 401

    if bcrypt.checkpw(password.encode(), hashed_password):
        return "Acesso concedido", 200
    return "Acesso negado", 401

#Atribuo false para não demosntrar dados sensíveis no console da aplicação
if __name__ == '__main__':
    app.run(debug=False)
