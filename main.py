from http import HTTPStatus

import requests
import streamlit as st

from settings import BASE_URL

pages = {
    'Início': [
        st.Page(
            'dotum_client/home.py', title='Início', icon=':material/home:'
        ),
    ],
    'Endpoints da API': [
        st.Page(
            'dotum_client/user.py',
            title='Usuário',
            icon=':material/account_circle:',
        ),
        st.Page(
            'dotum_client/account.py',
            title='Conta',
            icon=':material/account_balance:',
        ),
        st.Page(
            'dotum_client/insights.py',
            title='Insights',
            icon=':material/search_insights:',
        ),
    ],
}


pg = st.navigation(pages)
pg.run()


@st.dialog('Login')
def login():
    username = st.text_input('Username')
    password = st.text_input('Senha', type='password')

    if st.button('Entrar'):
        auth_data = {
            'username': username,
            'password': password,
        }

        response = requests.post(f'{BASE_URL}/token', data=auth_data)

        if response.status_code == HTTPStatus.OK:
            token = response.json()['access_token']
            st.session_state['token'] = token
            st.success('Login bem-sucedido!')
            st.balloons()
        else:
            st.error('Falha no login. Verifique as credenciais.')


if st.sidebar.button('Login', type='primary'):
    login()
