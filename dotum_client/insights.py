from http import HTTPStatus

import requests
import streamlit as st

from settings import BASE_URL

st.set_page_config(
    page_title='Dotum - Insights',
    page_icon='🔍',
    initial_sidebar_state='expanded',
)

st.sidebar.header('Contas')
st.markdown('# Endpoints para obter balanço de contas')

st.write(
    'Esta rota permite obter dados gerais de contas, como total a pagar, a receber e geral.'
)

st.markdown('## Funcionalidades')
st.write("""
- **Obter total a pagar**: Retorna o valor total de contas a pagar.
- **Obter total a receber**: Retorna o valor total de contas a receber.
- **Obter total geral**: Retorna o balanço geral entre contas receber e contas a pagar.
""")

st.divider()

# Obter total de contas a pagar

st.markdown('## Total de contas a pagar')
st.write('Este endpoint retorna o total de contas a pagar.')

st.markdown("""
- Endpoint: `/insights/total-accounts-payable`
- Método: `GET`
""")

st.markdown('### Experimente')

if st.button('Obter total a pagar'):
    if 'token' in st.session_state:
        headers = {'Authorization': f'Bearer {st.session_state.token}'}

        with st.spinner('Consultando total a pagar...'):
            response = requests.get(
                f'{BASE_URL}/insights/total-accounts-payable',
                headers=headers,
            )
        if response.status_code == HTTPStatus.OK:
            st.success('Consulta feita com sucesso!')
            st.markdown(
                f'##### Total a pagar: R$ {response.json()["total"]:.2f}'
            )
        else:
            st.error(
                f'Erro ao consultar total a pagar: {response.json()["detail"]}'
            )
    else:
        st.warning('Esse endpoint requer autenticação!')
st.divider()

# Obter total de contas a receber

st.markdown('## Total de contas a receber')
st.write('Este endpoint retorna o total de contas a receber.')

st.markdown("""
- Endpoint: `/insights/total-accounts-receivable`
- Método: `GET`
""")

st.markdown('### Experimente')

if st.button('Obter total a receber'):
    if 'token' in st.session_state:
        headers = {'Authorization': f'Bearer {st.session_state.token}'}

        with st.spinner('Consultando total a receber...'):
            response = requests.get(
                f'{BASE_URL}/insights/total-accounts-receivable',
                headers=headers,
            )
        if response.status_code == HTTPStatus.OK:
            st.success('Consulta feita com sucesso!')
            st.markdown(
                f'##### Total a receber: R$ {response.json()["total"]:.2f}'
            )
        else:
            st.error(
                f'Erro ao consultar total a receber: {response.json()["detail"]}'
            )
    else:
        st.warning('Esse endpoint requer autenticação!')
st.divider()

# Obter total geral de contas

st.markdown('## Total geral de contas')
st.write('Este endpoint retorna o total geral de contas.')

st.markdown("""
- Endpoint: `/insights/grand-total-of-accounts`
- Método: `GET`
""")

st.markdown('### Experimente')

if st.button('Obter total geral'):
    if 'token' in st.session_state:
        headers = {'Authorization': f'Bearer {st.session_state.token}'}

        with st.spinner('Consultando total geral...'):
            response = requests.get(
                f'{BASE_URL}/insights/grand-total-of-accounts',
                headers=headers,
            )
        if response.status_code == HTTPStatus.OK:
            st.success('Consulta feita com sucesso!')
            st.markdown(
                f'##### Total geral: R$ {response.json()["total"]:.2f}'
            )
        else:
            st.error(
                f'Erro ao consultar total geral: {response.json()["detail"]}'
            )
    else:
        st.warning('Esse endpoint requer autenticação!')
