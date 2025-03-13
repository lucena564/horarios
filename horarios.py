from flask import Flask, jsonify, request, abort
from datetime import datetime
import jwt
import datetime as dt
import json

app = Flask(__name__)

# Chave para acessar o token - Colocar em uma variável de ambiente futuramente
SECRET_KEY = "secreta_chave"

# Carrega o json com os logins e senhas das pessoas que podem acessar o sistema
def carregar_usuarios():
    with open("usuarios.json", "r") as f:
        return json.load(f)

# Função para verificar o token
def verify_token(token):
    try:
        # Decodifica o token e verifica se é válido
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

# Função para validar o login e senha da requisição com os dados do arquivo JSON de usuários autorizados
def validar_login(usuario, senha):
    usuarios = carregar_usuarios()
    if usuario in usuarios and usuarios[usuario]["senha"] == senha:
        return True
    return False

# Endpoint de login - Recebe um JSON com usuário que verifica se tem o usuário cadastrado e senha correta desse usuário e retorna um token JWT
@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        usuario = data.get("usuario")
        senha = data.get("senha")

        print(usuario, senha)  # Adicionando log de usuário e senha
        print(validar_login(usuario, senha))  # Adicionando log de validação

        if not usuario or not senha:
            abort(400, description="Usuário e senha são obrigatórios.")

        if validar_login(usuario, senha):
            # Gerar um token com um tempo de expiração de 1 hora
            expiration = datetime.utcnow() + dt.timedelta(hours=1)  
            token = jwt.encode({"exp": expiration}, SECRET_KEY, algorithm="HS256")
            return jsonify({"token": token})
        else:
            abort(401, description="Credenciais inválidas.")
    
    except Exception as e:
        print(f"Erro ao processar login: {e}")  # Adicionando log de erro
        abort(500, description="Erro interno no servidor.")


# Agenda sem a disciplina "ELETRÔNICA 1"
AGENDA = {
    "segunda": [
        ("08:00 - 10:00", "Neurotech (2h)"),
        ("13:00 - 14:00", "Servo Mecanismo P/ Eng. Computação"),
        ("14:00 - 16:00", "Neurotech (2h)"),
        ("16:00 - 18:00", "Neurotech (2h)"),
        ("18:00 - 20:00", "Neurotech (2h)")
    ],
    "terca": [
        ("08:00 - 09:00", "F676 - Método Expressão Tec-Científica"),
        ("09:00 - 11:00", "F677 - Lógica Para Computação"),
        ("14:00 - 16:00", "Neurotech (2h)"),
        ("16:00 - 18:00", "Neurotech (2h)"),
        ("18:00 - 20:00", "Neurotech (2h)"),
        ("20:00 - 22:00", "Neurotech (2h)")
    ],
    "quarta": [
        ("08:00 - 10:00", "Neurotech (2h)"),
        ("10:00 - 12:00", "E5344 - Princípios de Comunicação"),
        ("13:00 - 14:00", "Servo Mecanismo P/ Eng. Computação"),
        ("14:00 - 16:00", "Neurotech (2h)"),
        ("16:00 - 18:00", "Neurotech (2h)"),
        ("18:00 - 20:00", "Neurotech (2h)")
    ],
    "quinta": [
        ("08:00 - 09:00", "F677 - Lógica Para Computação"),
        ("09:00 - 11:00", "F676 - Método Expressão Tec-Científica"),
        ("14:00 - 16:00", "Neurotech (2h)"),
        ("16:00 - 18:00", "Neurotech (2h)"),
        ("18:00 - 20:00", "Neurotech (2h)"),
        ("20:00 - 22:00", "Neurotech (2h)")
    ],
    "sexta": [
        ("08:00 - 10:00", "Neurotech (2h)"),
        ("10:00 - 12:00", "E5344 - Princípios de Comunicação"),
        ("14:00 - 16:00", "Neurotech (2h)"),
        ("16:00 - 18:00", "Neurotech (2h)"),
        ("18:00 - 20:00", "Neurotech (2h)")
    ]
}

@app.route("/agenda", methods=["GET"])
def get_agenda():
    # Pegando o token do cabeçalho
    token = request.headers.get("Authorization")
    
    # Verificando se o token está presente e se é válido
    if not token or not token.startswith("Bearer "):
        abort(401, description="Token não fornecido ou inválido.")
    
    token = token.split(" ")[1]  # Remove o 'Bearer' da string
    payload = verify_token(token)
    
    if payload is None:
        abort(401, description="Token inválido ou expirado.")
    
    # Se o token for válido, continue com a lógica da agenda
    dia_atual = datetime.today().strftime('%A').lower()
    dia_traduzido = {
        "monday": "segunda",
        "tuesday": "terca",
        "wednesday": "quarta",
        "thursday": "quinta",
        "friday": "sexta",
        "saturday": "sábado",
        "sunday": "domingo"
    }
    dia_semana = dia_traduzido.get(dia_atual, "domingo")
    agenda_hoje = AGENDA.get(dia_semana, [])
    return jsonify({"dia": dia_semana, "horarios": agenda_hoje})

@app.route("/", methods=["GET"])
def get_comandos():
    return "Olá! Para ver a agenda de hoje, acesse /agenda"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
