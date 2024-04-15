import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Teste
# Gerando dados fictícios
def generate_data():
    date_range = pd.date_range(start='2020-01-01', end='2024-12-31')
    data = {
        'Date': date_range,
        'Value': np.random.randn(len(date_range)).cumsum()
    }
    return pd.DataFrame(data)

# Função principal do app
def main():
    st.title('Série Temporal com Streamlit')

    # Gerando os dados
    data = generate_data()

    # Criando gráfico de linha
    st.subheader('Gráfico de Linha')
    st.line_chart(data.set_index('Date'))

    # Opção para mostrar os dados brutos
    if st.checkbox('Mostrar dados brutos'):
        st.subheader('Dados')
        st.write(data)

if __name__ == "__main__":
    main()
