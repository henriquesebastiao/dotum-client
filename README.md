# 🗃️ Dotum Client - Sistema de Contas

Este projeto é uma solução para um desafio de programação back-end, cujo objetivo é desenvolver uma aplicação para o controle de contas a pagar e contas a receber. A proposta foca na construção de uma lógica sólida, estrutura de código bem organizada e cumprimento dos requisitos funcionais.

Este é cliente web desenvolvido com [Streamlit](https://streamlit.io/) para consumir a API de back-end da aplicação.

Os links do projeto estão listados a baixo:

- [github.com/henriquesebastiao/dotum](https://github.com/henriquesebastiao/dotum) - Repositório da API
- [dotum-api.henriquesebastiao.com](https://dotum-api.henriquesebastiao.com) - Painel Swagger da API
- [github.com/henriquesebastiao/dotum-client](https://github.com/henriquesebastiao/dotum-client) - Repositório deste cliente para a API
- [dotum.henriquesebastiao.com](https://dotum.henriquesebastiao.com) - Cliente web da API

O back-end da aplicação da aplicação foi desenvolvido com as seguintes ferramentas:

- Python
- [FastAPI](https://fastapi.tiangolo.com/)
- Docker
- [SQLAlchemy](https://www.sqlalchemy.org/)
- PostgreSQL

### Como executar o cliente web

1. Clone o repositório e entre nele com o seguinte comando:

    ```shell
    git clone https://github.com/henriquesebastiao/dotum-client && cd dotum-client
    ```

2. Crie um arquivo `.env` que conterá as variáveis de ambiente exigidas pela aplicação, você pode fazer isso apenas copiando o arquivo de exemplo:

    ```shell
    cat .env.example > .env
    ```

3. Agora execute o docker compose e toda aplicação será construída e iniciada em modo de desenvolvimento 🚀

    ```shell
    docker compose up -d
    ```

Pronto! Você já pode abrir seu navegador e acessar o cliente web do sistema em [http://localhost:9004](http://localhost:9004).
