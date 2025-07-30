from http import HTTPStatus
from time import sleep

import requests
import streamlit as st

from settings import BASE_URL

pages = {
    'Início': [
        st.Page(
            'dotum_client/home.py', title='Início', icon=':material/home:'
        ),
        st.Page(
            'dotum_client/dashboards.py',
            title='Dashboards',
            icon=':material/dashboard:',
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

            # Tempo para a animação ser exibida
            sleep(2)
            st.rerun()
        else:
            st.error('Falha no login. Verifique as credenciais.')


if st.sidebar.button('Login', type='primary'):
    login()

if st.sidebar.button('Login as Demo user'):
    auth_data = {
        'username': 'demo',
        'password': 'demo',
    }

    response = requests.post(f'{BASE_URL}/token', data=auth_data)

    if response.status_code == HTTPStatus.OK:
        token = response.json()['access_token']
        st.session_state['token'] = token
        st.sidebar.success('Login bem-sucedido!')
        st.balloons()

        # Tempo para a animação ser exibida
        sleep(2)
        st.rerun()
    else:
        st.sidebar.error('Falha no login. Verifique as credenciais.')

if st.sidebar.button('Exit'):
    if 'token' in st.session_state:
        del st.session_state.token
        st.sidebar.success('Usuário desconectado!')

        # Tempo para o aviso de sucesso ser exibido
        sleep(1)
        st.rerun()
    else:
        pass
