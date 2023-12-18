import streamlit as st
from caesar import cifrar_mensaje, descifrar_mensaje

def main():

    ### MAIN ###
    st.title('CAESAR X REGX')

    def update_both_text():
        update_encrypt_input()
        update_decrypt_input()
        
    ### SIDE BAR ###
    st.sidebar.title("Parameters")
    shift = st.sidebar.number_input('Shift', min_value=0, value=0, on_change=update_both_text)
    
    # Callback function to handle changes in the first text input
    def update_encrypt_input():
        # Update the value of the second input based on the first input's value
        st.session_state.output_encrypt_value = cifrar_mensaje(st.session_state.input_encrypt_value, shift)

    def update_decrypt_input():
        # Update the value of the second input based on the first input's value
        st.session_state.output_decrypt_value = descifrar_mensaje(st.session_state.input_decrypt_value, shift)


    ### CRYPTO COMPONENTS ###

    # Initialize session state variables if they don't exist
    if 'shift' not in st.session_state:
        st.session_state.shift = shift
    elif st.session_state.shift != shift:
        st.session_state.shift = shift
        update_encrypt_input()
        update_decrypt_input()

    if 'input_encrypt_value' not in st.session_state:
        st.session_state.input_encrypt_value = ""
    if 'output_encrypt_value' not in st.session_state:
        st.session_state.output_encrypt_value = ""
    if 'input_decrypt_value' not in st.session_state:
        st.session_state.input_decrypt_value = ""
    if 'output_decrypt_value' not in st.session_state:
        st.session_state.output_decrypt_value = ""

    #### Encrypt ####
    st.subheader('Encrypt')
    st.text_input("Here goes the original", value="", key="input_encrypt_value",
                on_change=update_encrypt_input)

    st.text_input("Your Welcome...", value=st.session_state.output_encrypt_value, key="output_encrypt_value")

    #### Decrypt ####
    st.subheader('Decrypt')
    st.text_input("Here goes gibberish", value="", key="input_decrypt_value",
                on_change=update_decrypt_input)

    st.text_input("Enjoyy 😇", value=st.session_state.output_decrypt_value, key="output_decrypt_value")

    st.divider()
    
    st.subheader('By Regx')
    st.code(
    """
    def descifrar_mensaje(mensaje_cifrado, desplazamiento):
        mensaje_descifrado = ''
        for letra in mensaje_cifrado:

            if letra.isalpha():
                codigo = ord(letra)

                if letra.isupper():
                    codigo_descrifrado = (codigo - 65 - desplazamiento) % 26 + 65
                else:
                    codigo_descrifrado = (codigo - 97 - desplazamiento) % 26 + 97
                
                letra_descifrada = chr(codigo_descrifrado)
                mensaje_descifrado += letra_descifrada
            else:
                mensaje_descifrado += letra

        return mensaje_descifrado
    """)
    
if __name__ == "__main__":
    main()