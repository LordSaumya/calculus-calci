import streamlit as st
import latex
from humanize import ordinal
from latex2sympy2 import latex2sympy
from sympy import *

def mac(func,ord):
    x = symbols("x")
    MacS = func.subs(x,0)
    for i in range(1,ord+1):
        MacS += simplify(((x**i*(diff(func,x,i)).subs(x,0))/factorial(i)))
    return MacS

st.title("Calculus Calci")
st.sidebar.write("Enter your expression, and this will give you the first two derivatives, the indefinite integral (with respect to x), and the fifth order of its Maclaurin series.\n\n -    Saumya Shah")
st.write("Enter f(x):")
rawInp = st.text_input("Please enter your function in latex and press enter (do not use 'c')")
st.write("Enter order of Maclaurin Polynomial:")
mOrder = st.number_input("Please enter a positive integer for the order of Maclaurin polynomial")
if (rawInp and mOrder):
    mOrder = abs(round(mOrder))
    st.warning("Large values for the order of Maclaurin polynomial may take more time to process.")
    x = symbols("x")
    symInp = latex2sympy(rawInp)
    st.write("Simplified Input:")
    st.latex("f(x) = " + str(latex(simplify(symInp))))
    st.write("First derivative:")
    st.latex("f'(x) = " + str(latex(simplify(diff(symInp,x)))))
    st.write("Second derivative:")
    st.latex("f''(x) = " + str(latex(simplify(diff(diff(symInp,x),x)))))
    st.write("Indefinite Integral:")
    st.latex("\int f(x) dx = " + str(latex(simplify(integrate(symInp,x)))) + " + C")
    st.write(ordinal(mOrder) + " order Maclaurin Series:")
    st.latex(str(latex(simplify(mac(symInp,mOrder)))))