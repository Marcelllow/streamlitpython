import streamlit as st
import pandas as pd
import numpy as np


def main():
    st.set_page_config(layout="wide")
    st.title("Verificação componentes na AOI")


    uploaded_files = st.file_uploader("Escolha os arquivos CSV", type="csv", accept_multiple_files=True)

    if uploaded_files:
        st.write("Arquivos Carregados:")
        for uploaded_file in uploaded_files:

            df = pd.read_csv(uploaded_file, sep=';', decimal=',')
            st.write(f"**{uploaded_file.name}**")
            df['Part Number'] = df['Unnamed: 1']
            df['Hor Threshold'] = pd.to_numeric(df['Unnamed: 6'], errors='coerce')
            df['Ver Threshold'] = pd.to_numeric(df['Unnamed: 7'], errors='coerce')
            df['Skew Threshold'] = pd.to_numeric(df['Unnamed: 8'], errors='coerce')
            df['Situação Hor'] = np.where(df['Hor Threshold'] > 100, 'Verificar tolerâcia', 'ok')
            df['Situação Ver'] = np.where(df['Ver Threshold'] > 100, 'Verificar tolerâcia', 'ok')
            condicao = (df['Hor Threshold'] > 100) | (df['Ver Threshold'] > 100)
            df2 = df[condicao]
            filt = df2.loc[13:200, 'Part Number':'Situação Ver']
            filt
















if __name__ == "__main__":
    main()
