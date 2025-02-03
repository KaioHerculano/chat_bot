import os
from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv


# Carregar variaveis de ambiente
load_dotenv()

app = Flask(__name__)

# Obter as credencias do Twilio a partir das variaveis de ambiente
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')

# Inicializar o cliente Twilio
client = Client(account_sid, auth_token)


@app.route("/webhook", methods=["POST"])
def handle_message():
    # captura a mensagem (body) e o numero do remetente (from)
    incoming_msg = request.form.get('Body')
    from_number = request.form.get('From')

    print(f"Mensagem recebida: {incoming_msg}")
    print(f"De: {from_number}")

    # Mensagens pre definidas:
    pre_defined_messages = {
        'Oi': "Seja bem vindo a nossa central de atendimento!, digite:\n\n1- Para saber nossos planos\n\n2- Estou sem Internet\n\n3- Quero pagar minha internet",
        '1': "Temos planos apartir de 124,99, para mais informções venha até a nossa loja para conversamos melhor",
        '2': "Entendi, preciso que o senhor reinicie os equipamentos de internet, para reiniciar e simples basta tira-los da tomada esperar 30 segundos e colocar novamente, caso não volte digite-4",
        '3': "Você pode pagar sua mensalidade pela nossa central de pagamentos: https://central.com.br/pagamentos",
        '4': "Pedimos desculpas pelo transtorno, vou abrir uma ordem de serviço para que um técnico vá até sua residencia!",
        'default': "Desculpe, não entendi sua opção. Por favor, digite oi para saber as opções de dialogo!"
    }

    # Cria a mensagem automatica (mensagem pré-pronta)
    response = MessagingResponse()

    # Verifica a mensagem recebida e escolhe a resposta correspondente
    if incoming_msg in pre_defined_messages:
        msg = pre_defined_messages[incoming_msg]
    else:
        msg = pre_defined_messages["default"]

    # Envia a resposta ao usuario
    response.message(msg)

    # Retorna a resposta em formato XML para o Twilio
    return str(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
