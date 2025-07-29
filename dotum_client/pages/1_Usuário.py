from http import HTTPStatus

import requests
import streamlit as st
from settings import BASE_URL

st.set_page_config(
    page_title='Dotum - User Page',
    page_icon=':bust_in_silhouette:',
    initial_sidebar_state='expanded',
)

st.sidebar.header('Usuário')
st.markdown('# Endpoint para gerenciar usuários')

st.write(
    'Esta rota permite gerenciar usuários, incluindo criação, edição e exclusão de contas.'
)

st.markdown('## Funcionalidades')
st.write("""
- **Criação de Usuário**: Permite adicionar novos usuários ao sistema.
- **Edição de Usuário**: Possibilita modificar detalhes de usuários existentes.
- **Exclusão de Usuário**: Remove usuários do sistema.
""")

st.markdown('## Criar usuário')
st.write('Use este endpoint para registrar um novo usuário no sistema.')

st.markdown("""
- Endpoint: `/user`
- Método: `POST`
""")

st.markdown('#### Corpo de da requisição')

st.code(
    """
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "password": "string"
}
""",
    language='json',
)

st.markdown('### Experimente')

username = st.text_input('Nome de usuário', width=300)
email = st.text_input('Email', width=300, placeholder='user@example.com')
first_name = st.text_input('Nome', width=300)
last_name = st.text_input('Sobrenome', width=300)
password = st.text_input('Senha', type='password', width=300)

if st.button('Criar Usuário'):
    if username and email and first_name and last_name and password:
        response = requests.post(
            f'{BASE_URL}/user',
            json={
                'username': username,
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
                'password': password,
            },
        )
        if response.status_code == HTTPStatus.CREATED:
            st.success('Usuário criado com sucesso!')
        else:
            st.error(f'Erro ao criar usuário: {response.text}')
    else:
        st.warning('Por favor, preencha todos os campos.')
