#Imports:
import streamlit as st
import latex
from latex2sympy2 import latex2sympy, latex2latex
from sympy import *
st.title("Calculus Calci")
st.sidebar.write("Enter your expression, and this will give you the first two derivatives, the indefinite integral (with respect to x), and the first three terms of its Maclaurin series.\n\n -    Saumya Shah")
st.write("Enter f(x):")
rawInp = st.text_input("Please enter your function in latex and press enter (do not use 'c')")
if (rawInp):
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
    st.write("Maclaurin Series:")
    st.latex(str(latex(simplify(symInp.subs(x,0)) + simplify(x*(diff(symInp,x)).subs(x,0))) + simplify(x**2*(diff(diff(symInp,x),x)).subs(x,0)/2)))