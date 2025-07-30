from datetime import date
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
            st.markdown('**JSON:**')
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
            st.markdown('**Tabela:**')
            st.write(df)
        else:
            st.error(f'Erro ao obter contas: {response.json()["detail"]}')
    else:
        st.warning('Esse endpoint requer autenticação!')
st.divider()

# Registra uma nova Conta

st.markdown('## Registra uma nova Conta')
st.write('Use este endpoint para registrar uma nova conta no sistema.')

st.markdown("""
- Endpoint: `/account`
- Método: `POST`
""")

st.markdown('#### Corpo da requisição')

st.code(
    """
{
  "value": 0,
  "description": "string",
  "due_date": "2025-07-29",
  "account_type": "payable",
  "paid": false
}
""",
    language='json',
)

st.markdown('### Experimente')

with st.form('create_account_form'):
    value = st.number_input(
        'Valor', min_value=1.00, format='%0.2f', icon=':material/attach_money:'
    )
    description = st.text_input('Description', icon=':material/info:')
    due_date = st.date_input('Data de vencimento', format='DD/MM/YYYY')

    account_type = st.radio(
        'Qual o tipo de conta?',
        ['A Pagar', 'A Receber'],
        index=None,
    )

    account_type = 'payable' if account_type == 'A Pagar' else 'receivable'

    paid = st.checkbox('Pago')

    submitted = st.form_submit_button('Registrar')

    if submitted:
        if 'token' in st.session_state:
            headers = {'Authorization': f'Bearer {st.session_state.token}'}
            if value and description and due_date and account_type:
                with st.spinner('Registrando conta...'):
                    response = requests.post(
                        f'{BASE_URL}/account/',
                        json={
                            'value': value,
                            'description': description,
                            'due_date': due_date.isoformat(),
                            'account_type': account_type,
                            'paid': paid,
                        },
                        headers=headers,
                    )
                if response.status_code == HTTPStatus.CREATED:
                    st.success('Conta registrada com sucesso!')
                else:
                    st.error(
                        f'Erro ao registrar conta: {response.json()["detail"]}'
                    )
            else:
                st.warning('Por favor, preencha todos os campos.')
        else:
            st.warning('Esse endpoint requer autenticação!')
st.divider()

# Consultar uma conta registrada

st.markdown('## Consulta uma Conta registrada')
st.write(
    'Use este endpoint para consultar uma conta já registrada no sistema.'
)

st.markdown("""
- Endpoint: `/account/{account_id}`
- Método: `GET`
""")

st.markdown('### Experimente')

with st.form('get_account_form'):
    account_id = st.number_input(
        'ID da conta', value=1, min_value=1, icon=':material/tag:'
    )

    submitted = st.form_submit_button('Buscar conta')

    if submitted:
        if 'token' in st.session_state:
            headers = {'Authorization': f'Bearer {st.session_state.token}'}

            with st.spinner('Deletando usuário...'):
                response = requests.delete(
                    f'{BASE_URL}/account/{account_id}',
                    headers=headers,
                )
            if response.status_code == HTTPStatus.OK:
                st.success('Conta encontrada!')
                st.markdown('**JSON:**')
                st.json(response.json())
            else:
                st.error(f'Erro ao buscar conta: {response.json()["detail"]}')
        else:
            st.warning('Esse endpoint requer autenticação!')
st.divider()

# Atualiza uma Conta registrada

st.markdown('## Atualizar uma Conta registrada')
st.write(
    'Use este endpoint para atualizar uma conta já registrada no sistema.'
)

st.markdown("""
- Endpoint: `/account/{account_id}`
- Método: `PATCH`
""")

st.markdown('#### Corpo da requisição')

st.code(
    """
{
  "value": 0,
  "description": "string",
  "due_date": "2025-07-29",
  "account_type": "payable",
  "paid": false
}
""",
    language='json',
)

st.markdown('### Experimente')

with st.form('fetch_account_form'):
    st.markdown('**Buscar informações da conta**')
    account_id = st.number_input(
        'ID da conta', value=1, min_value=1, icon=':material/tag:'
    )

    # Obtém os dados atuais da conta
    submitted_update_account = st.form_submit_button('Buscar conta')

    if submitted_update_account:
        if 'token' not in st.session_state:
            st.warning('Esse endpoint requer autenticação!')
        elif not account_id:
            st.warning('Você precisa informar o ID da conta.')
        else:
            headers = {'Authorization': f'Bearer {st.session_state.token}'}
            response = requests.get(
                f'{BASE_URL}/account/{account_id}',
                headers=headers,
            )

            if response.status_code == HTTPStatus.OK:
                st.session_state.edit_data = response.json()
            else:
                st.error(f'Erro ao buscar conta: {response.json()["detail"]}')

if 'edit_data' in st.session_state:
    with st.form('update_account_form'):
        data = st.session_state.edit_data

        st.markdown('**Atualizar conta**')

        value = st.number_input(
            'Valor',
            value=data['value'],
            min_value=1.00,
            format='%0.2f',
            icon=':material/attach_money:',
        )
        description = st.text_input(
            'Description', icon=':material/info:', value=data['description']
        )
        due_date = st.date_input(
            'Data de vencimento',
            format='DD/MM/YYYY',
            value=date.fromisoformat(data['due_date']),
        )

        account_type_index = 0 if data['account_type'] == 'payable' else 1

        account_type = st.radio(
            'Qual o tipo de conta?',
            ['A Pagar', 'A Receber'],
            index=account_type_index,
        )

        account_type = 'payable' if account_type == 'A Pagar' else 'receivable'

        paid = st.checkbox('Pago', value=data['paid'])

        update_submitted = st.form_submit_button('Atualizar')

        if update_submitted:
            if 'token' in st.session_state:
                headers = {'Authorization': f'Bearer {st.session_state.token}'}
                if value and description and due_date and account_type:
                    account_type = (
                        'payable'
                        if account_type == 'A Pagar'
                        else 'receivable'
                    )
                    with st.spinner('Atualizando conta...'):
                        response = requests.patch(
                            f'{BASE_URL}/account/{account_id}',
                            json={
                                'value': value,
                                'description': description,
                                'due_date': due_date.isoformat(),
                                'account_type': account_type,
                                'paid': paid,
                            },
                            headers=headers,
                        )
                    if response.status_code == HTTPStatus.OK:
                        st.success('Conta atualizada com sucesso!')
                    else:
                        st.error(
                            f'Erro ao atualizar conta: {response.json()["detail"]}'
                        )
                else:
                    st.warning('Por favor, preencha todos os campos.')
            else:
                st.warning('Esse endpoint requer autenticação!')
st.divider()

# Deletar Conta

st.markdown('## Deletar uma Conta registrada')
st.write('Use este endpoint para excluir uma conta registrada no sistema.')

st.markdown("""
- Endpoint: `/account/{account_id}`
- Método: `DELETE`
""")

st.markdown('### Experimente')

with st.form('delete_account_form'):
    account_id = st.number_input('ID da conta', value=1, min_value=1)

    submitted = st.form_submit_button('Deletar')

    if submitted:
        if 'token' in st.session_state:
            headers = {'Authorization': f'Bearer {st.session_state.token}'}

            with st.spinner('Deletando conta...'):
                response = requests.delete(
                    f'{BASE_URL}/account/{account_id}',
                    headers=headers,
                )
            if response.status_code == HTTPStatus.OK:
                st.success('Conta deletada com sucesso!')
            else:
                st.error(f'Erro ao deletar conta: {response.json()["detail"]}')
        else:
            st.warning('Esse endpoint requer autenticação!')
