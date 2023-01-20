import streamlit as st
import numpy as np

class InvalidMatrix(Exception):
    pass

def matrix_nth_root(matrix, n):
    if not np.allclose(matrix, matrix.conj().T):
        raise InvalidMatrix
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    return eigenvectors @ np.diag(eigenvalues**(1/n)) @ np.linalg.inv(eigenvectors)

def matrix_display():
    """raise a matrix to a power of n and if possible find the n-th root of the matrix"""
    st.title("Лаба1.Матрица")
    st.write("Данная программа позволяет вам возвести матрицу в степень n и, если возможно, в степень 1/n")
    st.write("Введите матрицу:")
    matrix = st.text_area("Матрица", value="4 -3 1\n-3 5 2\n1 2 6")
    if matrix != "":
        st.write("Введите степень:")
        power = st.number_input("Степень", min_value=1, value=2, step=1)
        if power != "":
            try:
                matrix = np.array([list(map(int, row.split())) for row in matrix.splitlines()])
                st.write("Ваша матрица:")
                st.write(matrix)
                st.write(f"Ваша матрица в степени {power}:")
                st.write(np.linalg.matrix_power(matrix, power))
                st.write(f"Ваша матрица в степени 1/{power}:")
                st.write(matrix_nth_root(matrix, power))
            except InvalidMatrix:
                st.write("Ваша матрица не является симметричной")
            except:
                st.write("Введеные данные неверны")