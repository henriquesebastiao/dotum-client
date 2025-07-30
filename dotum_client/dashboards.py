from http import HTTPStatus

import plotly.express as px
import requests
import streamlit as st

from settings import BASE_URL

st.set_page_config(
    page_title='Dotum - Dashboards',
    page_icon='📊',
)

st.title('Dashboards')
st.write(
    'Esta página exibe um breve dashboard com informações gerais das contas registradas no sistema.'
)

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
            label=':red[A Pagar]',
            value=f'R$ {payable.json()["total"]:.2f}',
            border=True,
        )
        col2.metric(
            label=':green[A Receber]',
            value=f'R$ {receivable.json()["total"]:.2f}',
            border=True,
        )
        col3.metric(
            label=f':{grand_total_color}[Balanço Geral]',
            value=f'R$ {grand_total:.2f}',
            border=True,
        )

        categories = ['A Pagar', 'A Receber']
        values = [payable.json()['total'], receivable.json()['total']]
        colors = ['#F66151', '#33D17A']

        # Gráfico de pizza
        fig = px.pie(
            names=categories,
            values=values,
            title='Balanço de contas',
            subtitle='Percentual de contas pagar e contas a receber',
            color_discrete_sequence=colors,
        )

        st.plotly_chart(fig)
else:
    st.warning('Faça login para ver os dashboards.')
