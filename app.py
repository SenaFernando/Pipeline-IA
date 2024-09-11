import streamlit as st 
from datetime import datetime, time
from contrato import Vendas
from pydantic import ValidationError
from database import salvar_no_postgresql

def main():
    
    st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simples")
    email = st.text_input("Campo de Texto Para a Inserção do E-mail")
    data = st.date_input("Data da Compra", datetime.now())
    hora = st.time_input("Hora da compra", value=time(9,0)) # Valor padrão: 9:00
    valor = st.number_input("Valor da Venda Realizada", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de Produtos", min_value=1, step=1)
    produto = st.selectbox("Produto", options=["ZapFlow com Gemini", "ZapFlow com ChatGPT", "ZapFlow com Lhama3.0"])
   
    if st.button("Salvar"):    
       try:
            data_hora = datetime.combine(data, hora)
       
            venda = Vendas(
                    email= email,
                    data= data_hora,
                    valor= valor,
                    quantidade= quantidade,
                    produto= produto
                    
                )
       
       
            st.write(venda)
            salvar_no_postgresql()
       except ValidationError as e:
                st.error(f"Ocorreu um erro: {e}")
         
if __name__ == "__main__":
    main()