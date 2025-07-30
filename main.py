from http import HTTPStatus

import requests
import streamlit as st

from settings import BASE_URL

pages = {
    'Início': [
        st.Page('dotum_client/home.py', title='Início'),
    ],
    'Endpoints da API': [
        st.Page('dotum_client/user.py', title='Usuário'),
        st.Page('dotum_client/account.py', title='Conta'),
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
