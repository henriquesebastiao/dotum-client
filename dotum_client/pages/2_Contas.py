import streamlit as st

st.set_page_config(
    page_title='Dotum - User Page',
    page_icon=':bust_in_silhouette:',
    initial_sidebar_state='expanded',
)

st.sidebar.header('Account')
st.markdown('# Account Page')
st.write(
    'This is the account page where you can view your account details and preferences.'
)
