import requests

# URL do servidor Flask
url_login = "http://127.0.0.1:5000/login"
url_agenda = "http://127.0.0.1:5000/agenda"

# Dados de login (usuário e senha de teste)
login_data = {
    "usuario": "antonio",
    "senha": "senha123"
}

# 1. Fazer o login para obter o token
headers = {
    "Content-Type": "application/json"  # Garantir que o tipo de conteúdo seja JSON
}

response = requests.post(url_login, json=login_data, headers=headers)

if response.status_code == 200:
    # Extrair o token da resposta
    token = response.json().get("token")
    print("Token recebido:", token)
    
    # 2. Usar o token para acessar a agenda
    agenda_headers = {
        "Authorization": f"Bearer {token}"
    }
    
    agenda_response = requests.get(url_agenda, headers=agenda_headers)
    
    if agenda_response.status_code == 200:
        print("Agenda de hoje:", agenda_response.json())
    else:
        print("Erro ao acessar a agenda:", agenda_response.status_code, agenda_response.text)
else:
    print("Erro no login:", response.status_code, response.text)
