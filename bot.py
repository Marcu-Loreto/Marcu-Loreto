import streamlit as st
#pip install streamlit 

#para rodar streamilt run bot.py
st.write("## Chat com Suporte")


#criando uma memoria para guardar as mensagens
if "lista_mensagem" not in st.session_state:
    st.session_state["lista_mensagem"] = []


sessioin_state = st.session_state
#pegar a entrada do usuario


mensagem_usuario = st.chat_input("Digite sua mensagem:")

if mensagem_usuario:                 
 #print(mensagem_usuario)
 st.chat_message("user").write(mensagem_usuario)
 mensagem = {"role": "user", "content": mensagem_usuario}
 st.session_state["lista_mensagem"].append(mensagem)

# pegar a resposta da IA

 resposta_ia = "Voce quer dizer:" + mensagem_usuario + "?"

 st.chat_message("assistant").write(resposta_ia)
 mensagem_ia = {"role": "assistant", "content": resposta_ia}
 st.session_state["lista_mensagem"].append(mensagem_ia)
 
 
 print(st.session_state["lista_mensagem"])
#st.chat_message("assistent").markdown(mensagem_usuario)
# st.session_state["mensagens"].append({"role": "user", "content": mensagem_usuario})
