import streamlit as st
from bmp_steganography import encode_image, decode_image
def hide_text_in_bmp():
    st.title("Лаба2Шифрование")
    st.write("Данная программа позволяет вам зашифровать текст в bmp-файле и расшифровать его.")
    action = st.radio("Действие", ["Зашифровать", "Расшифровать"])
    if action == "Зашифровать":
        file = st.file_uploader("Загрузите файл", type=['bmp'])
        if file is not None:
            bytes_data = file.getvalue()
            st.write("Введите текст:")
            text = st.text_area("Текст")
            if text != "":
                encrypted_bmp = encode_image(bytes_data, text)
                st.write("Зашифрованный файл:")
                st.download_button(
                    label="Скачать",
                    data=encrypted_bmp,
                    file_name="encrypted.bmp",
                    mime="image/bmp",
                )
    else:
        file = st.file_uploader("Загрузите файл", type=['bmp'])
        if file is not None:
            bytes_data = file.getvalue()
            st.write("Расшифрованный текст:")
            st.write(decode_image(bytes_data))