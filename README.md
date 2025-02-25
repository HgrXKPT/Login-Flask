# Sistema de Login e Registro de Problemas

Este projeto é uma aplicação web desenvolvida com Flask e SQLite que permite aos usuários se registrarem, fazerem login e registrarem problemas.

## Sumário

- [Introdução](#introdução)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Introdução

O projeto permite que os usuários se registrem com um email e senha, façam login e registrem problemas. Utiliza Flask para o backend e SQLite como banco de dados. O design da interface é feito com Bootstrap.

## Tecnologias Utilizadas

- Flask
- SQLite
- Flask-Login
- Werkzeug
- Bootstrap

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/seu-usuario/SistemaLoginRegistro.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd SistemaLoginRegistro
    ```

3. Crie e ative um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Inicie o servidor Flask:

    ```bash
    flask run
    ```

2. Acesse a aplicação no seu navegador em `http://127.0.0.1:5000/`.

## Estrutura do Projeto

- `app.py`: Contém a lógica principal do aplicativo Flask, incluindo rotas para login, registro e registro de problemas.
- `templates/`: Contém os arquivos HTML para as páginas de login, registro e home.
  - `login.html`: Página de login.
  - `register.html`: Página de registro.
  - `home.html`: Página inicial onde os usuários podem registrar problemas.
- `static/style.css`: Contém os estilos customizados para a aplicação.
- `requirements.txt`: Lista de dependências do projeto.

### Exemplo de `requirements.txt`

Certifique-se de incluir as dependências necessárias no seu arquivo `requirements.txt`:

