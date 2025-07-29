from http import HTTPStatus

import pandas as pd
import requests
import streamlit as st

from settings import BASE_URL

st.set_page_config(
    page_title='Dotum - Contas',
    page_icon=':bust_in_silhouette:',
    initial_sidebar_state='expanded',
)

st.sidebar.header('Contas')
st.markdown('# Endpoints para gerenciar contas')

st.write(
    'Esta rota permite gerenciar as contas a pagar e a receber, incluindo criação, edição e exclusão de contas.'
)

st.markdown('## Funcionalidades')
st.write("""
- **Obter todas as Contas**: Retorna todas as contas registradas no sistema.
- **Registro de uma Conta**: Permite adicionar novas contas ao sistema.
- **Edição de Contas**: Possibilita modificar detalhes de contas registradas.
- **Exclusão de Conta**: Exclui contas do sistema.
""")

st.divider()

# Obtém todas as Contas registradas

st.markdown('## Obtém Contas registradas')
st.write(
    'Use este endpoint para obter todas as contas registradas no sistema.'
)

st.markdown("""
- Endpoint: `/account`
- Método: `GET`
""")

st.markdown('### Experimente')

if st.button('Obter Contas'):
    if 'token' in st.session_state:
        headers = {'Authorization': f'Bearer {st.session_state.token}'}
        with st.spinner('Obtendo contas...'):
            response = requests.get(
                f'{BASE_URL}/account/',
                headers=headers,
            )
        if response.status_code == HTTPStatus.OK:
            st.success('Contas obtidas com sucesso!')
            st.write('JSON:')
            st.json(response.json())

            df = pd.DataFrame(
                response.json()['accounts'],
                columns=[
                    'value',
                    'description',
                    'due_date',
                    'account_type',
                    'paid',
                ],
            )
            df.columns = [
                'Valor (R$)',
                'Descrição',
                'Vencimento',
                'Tipo',
                'Pago?',
            ]
            st.write('Tabela:')
            st.write(df)
        else:
            st.error(f'Erro ao obter contas: {response.json()["detail"]}')
    else:
        st.warning('Esse endpoint requer autenticação!')


st.divider()
