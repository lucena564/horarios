from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

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
