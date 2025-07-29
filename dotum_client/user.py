from http import HTTPStatus

import requests
import streamlit as st

from settings import BASE_URL

st.set_page_config(
    page_title='Dotum - Usuário',
    page_icon='🙂',
    initial_sidebar_state='expanded',
)

st.sidebar.header('Usuário')
st.markdown('# Endpoints para gerenciar usuários')

st.write(
    'Esta rota permite gerenciar usuários, incluindo criação, edição e exclusão de contas.'
)

st.markdown('## Funcionalidades')
st.write("""
- **Criação de Usuário**: Permite adicionar novos usuários ao sistema.
- **Edição de Usuário**: Possibilita modificar detalhes de usuários existentes.
- **Exclusão de Usuário**: Remove usuários do sistema.
""")

st.divider()

# Criar Usuário

st.markdown('## Criar usuário')
st.write('Use este endpoint para registrar um novo usuário no sistema.')

st.markdown("""
- Endpoint: `/user`
- Método: `POST`
""")

st.markdown('#### Corpo da requisição')

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

with st.form('create_user_form'):
    username = st.text_input('Nome de usuário')
    email = st.text_input('Email', placeholder='user@example.com')
    first_name = st.text_input('Nome')
    last_name = st.text_input('Sobrenome')
    password = st.text_input('Senha', type='password')

    submitted = st.form_submit_button('Registrar')

    if submitted:
        if username and email and first_name and last_name and password:
            with st.spinner('Registrando usuário...'):
                response = requests.post(
                    f'{BASE_URL}/user/',
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
                st.balloons()
            else:
                st.error(f'Erro ao criar usuário: {response.json()["detail"]}')
        else:
            st.warning('Por favor, preencha todos os campos.')

st.divider()

# Atualizar Usuário

st.markdown('## Atualizar usuário')
st.write(
    'Use este endpoint para atualizar os dados de um usuário registrado no sistema.'
)

st.markdown("""
- Endpoint: `/user/{user_id}`
- Método: `PATCH`
""")

st.markdown('#### Corpo da requisição')

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

st.markdown('### Experimente :material/key:')

with st.form('update_user_form'):
    user_id = st.number_input('ID do usuário', value=1, min_value=1)
    username = st.text_input('Nome de usuário')
    email = st.text_input('Email', placeholder='user@example.com')
    first_name = st.text_input('Nome')
    last_name = st.text_input('Sobrenome')
    password = st.text_input('Senha', type='password')

    submitted = st.form_submit_button('Atualizar')

    if submitted:
        if 'token' in st.session_state:
            if not any([username, email, first_name, last_name, password]):
                st.warning('Por favor, insira algum dado para atualização.')
            else:
                json = {
                    'username': username,
                    'email': email,
                    'first_name': first_name,
                    'last_name': last_name,
                    'password': password,
                }

                # Remove campos vazios
                json = {k: v for k, v in json.items() if v}
                headers = {'Authorization': f'Bearer {st.session_state.token}'}

                with st.spinner('Atualizando usuário...'):
                    response = requests.patch(
                        f'{BASE_URL}/user/{user_id}',
                        json=json,
                        headers=headers,
                    )
                if response.status_code == HTTPStatus.OK:
                    st.success('Usuário atualizado com sucesso!')
                else:
                    st.error(
                        f'Erro ao atualizar usuário: {response.json()["detail"]}'
                    )
        else:
            st.warning('Esse endpoint requer autenticação!')

st.divider()

# Deletar Usuário

st.markdown('## Deletar usuário')
st.write('Use este endpoint para excluir um usuário registrado no sistema.')

st.markdown("""
- Endpoint: `/user/{user_id}`
- Método: `DELETE`
""")

st.markdown('### Experimente')

with st.form('delete_user_form'):
    user_id = st.number_input('ID do usuário', value=1, min_value=1)

    submitted = st.form_submit_button('Deletar')

    if submitted:
        if 'token' in st.session_state:
            headers = {'Authorization': f'Bearer {st.session_state.token}'}

            with st.spinner('Deletando usuário...'):
                response = requests.delete(
                    f'{BASE_URL}/user/{user_id}',
                    headers=headers,
                )
            if response.status_code == HTTPStatus.OK:
                st.success('Usuário deletado com sucesso!')
            else:
                st.error(
                    f'Erro ao deletar usuário: {response.json()["detail"]}'
                )
        else:
            st.warning('Esse endpoint requer autenticação!')
