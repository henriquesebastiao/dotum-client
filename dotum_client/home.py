from http import HTTPStatus

import requests
import streamlit as st

from settings import BASE_URL

st.set_page_config(
    page_title='Dotum',
    page_icon=':rocket:',
    initial_sidebar_state='expanded',
)

st.sidebar.header('Início')

st.title('🗃️ Dotum - Sistema de contas')

st.markdown("""
Este projeto é uma solução para um desafio de programação back-end, cujo objetivo é desenvolver uma aplicação para o controle de contas a pagar e contas a receber. A proposta foca na construção de uma lógica sólida, estrutura de código bem organizada e cumprimento dos requisitos funcionais.

Este é cliente web desenvolvido com [Streamlit](https://streamlit.io/) para consumir a API de back-end da aplicação.
Os links do projeto estão listados a baixo:

- [github.com/henriquesebastiao/dotum](https://github.com/henriquesebastiao/dotum) - Repositório da API
- [dotum-api.henriquesebastiao.com](https://dotum-api.henriquesebastiao.com) - Painel Swagger da API
- [github.com/henriquesebastiao/dotum-client](https://github.com/henriquesebastiao/dotum-client) - Repositório deste cliente para a API
- [dotum.henriquesebastiao.com](https://dotum.henriquesebastiao.com) - Cliente web da API (Você está aqui ✨)

O back-end da aplicação da aplicação foi desenvolvido com as seguintes ferramentas:

- Python
- [FastAPI](https://fastapi.tiangolo.com/)
- Docker
- [SQLAlchemy](https://www.sqlalchemy.org/)
- PostgreSQL

### Interaja com a aplicação

No menu lateral 👈 você pode acessar as páginas que consomente a API do sistema.

Abaixo é exibido um breve resumo do geral de contas registradas no sistema:
""")

if 'token' in st.session_state:
    headers = {'Authorization': f'Bearer {st.session_state.token}'}

    with st.spinner('Buscando insights...'):
        payable = requests.get(
            f'{BASE_URL}/insights/total-accounts-payable',
            headers=headers,
        )
        receivable = requests.get(
            f'{BASE_URL}/insights/total-accounts-receivable',
            headers=headers,
        )
        grand_total = requests.get(
            f'{BASE_URL}/insights/grand-total-of-accounts',
            headers=headers,
        )
    if (
        payable.status_code == HTTPStatus.OK
        and receivable.status_code == HTTPStatus.OK
        and grand_total.status_code == HTTPStatus.OK
    ):
        col1, col2, col3 = st.columns(3)

        grand_total = grand_total.json()['total']
        grand_total_color = 'green' if grand_total >= 0 else 'red'

        col1.metric(
            label=':red[A Pagar]', value=f'R$ {payable.json()["total"]:.2f}'
        )
        col2.metric(
            label=':green[A Receber]',
            value=f'R$ {receivable.json()["total"]:.2f}',
        )
        col3.metric(
            label=f':{grand_total_color}[Balanço Geral]',
            value=f'R$ {grand_total:.2f}',
        )
    else:
        st.error(
            f'Erro ao consultar total a pagar: {payable.json()["detail"]}'
        )
else:
    st.warning(
        'Faça login para ver informações gerais das contas registradas.'
    )
