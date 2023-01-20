import streamlit as st
from streamlit_option_menu import option_menu
from matrix import matrix_display
from bmp_hide import hide_text_in_bmp


page_names_to_funcs = {
    "Лаба1.Матрица": matrix_display,
    "Лаба2.Шифрование": hide_text_in_bmp,
}

with st.sidebar:
    selected = option_menu("Лабы.Стеганография", ["Лаба1.Матрица", 'Лаба2.Шифрование'], 
        icons=['table', 'file-earmark-lock'], menu_icon="cast", default_index=0)
page_names_to_funcs[selected]()