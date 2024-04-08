import streamlit as st
def DemonSlayer():
    name = st.text_input("Nome do Hashira:")
    age = st.number_input("Idade do Hashira:", value=0, step=1, min_value=0,  max_value=1500)
    return name, age
st.title("Demon Slayer App")
st.subheader("Por favor, informe seus dados abaixo:")
# Pede o nome e a idade do Hashira usando a função Hashira
name, age = DemonSlayer()
# Cria uma lista suspensa com as categorias de Hashira
st.write("Selecione qual Hashira você é:")
category = st.selectbox("Hashira de Demon Slayer:", ("Giyu Tomioka", "Shinobu Kocho", "Sanemi Shinazugawa", "Mitsuri Kanroji", "Obanai Iguro", "Gyomei Himejima", "Tengen Uzui", "Kyojuro Rengoku", "Muichiro Tokito"))
# Cria um botão para enviar os dados
submit = st.button("Enviar dados")
# Se o botão for pressionado, exibe uma mensagem de confirmação
if submit:
    st.write("Seus dados foram enviados!")
    # Exibe uma mensagem com os dados do Hashira
    st.write("O Hashira", name, "de Demon Slayer", category, "tem", age, "anos.")
# Exibe uma imagem de um Hashira na página
st.image("hashira.png", width=700)
