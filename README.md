# ChatBot de Atendimento

Este é um chatbot de atendimento desenvolvido com Flask e Twilio para responder automaticamente a mensagens recebidas via WhatsApp.

## Requisitos

- Python 3.8+
- Flask
- Twilio
- python-dotenv

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/chatbot-atendimento.git
    cd chatbot-atendimento
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Altere o arquivo [.env](http://_vscodecontentref_/0) na raiz do projeto e adicione suas credenciais do Twilio:
    ```env
    TWILIO_ACCOUNT_SID="seu_account_sid"
    TWILIO_AUTH_TOKEN="seu_auth_token"
    TWILIO_WHATSAPP_NUMBER="+seu_numero_twilio"
    ```

## Uso

1. Inicie o servidor Flask:
    ```sh
    python app.py
    ```

2. Configure seu webhook no Twilio para apontar para `http://seu_dominio/webhook`.

3. Envie mensagens para o número do WhatsApp configurado no Twilio e receba respostas automáticas.

## Estrutura do Projeto

- [app.py](http://_vscodecontentref_/1): Código principal do chatbot.
- [requirements.txt](http://_vscodecontentref_/2): Lista de dependências do projeto.
- [.env](http://_vscodecontentref_/3): Arquivo de configuração com variáveis de ambiente.
- [.flake8](http://_vscodecontentref_/4): Configuração do Flake8 para linting.
