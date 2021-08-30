import streamlit as st
import latex
from humanize import ordinal
from latex2sympy2 import latex2sympy
from sympy import *

def tay(func,ord,cc):
    x = symbols("x")
    tayS = 0
    for i in range(0,ord+1):
        tayS += simplify((((x-cc)**i*(diff(func,x,i)).subs(x,cc))/factorial(i)))
    return tayS

st.title("Calculus Calci")
st.sidebar.write("Enter your expression, and this will give you the first two derivatives, the indefinite integral (with respect to x), and the fifth order of its Maclaurin series.\n\n -    Saumya Shah")
st.write("Enter f(x):")
rawInp = st.text_input("Please enter your function in latex and press enter (do not use 'c')")
st.write("Enter order of Taylor Polynomial:")
tOrder = st.number_input("Please enter a positive integer for the order of Taylor series")
st.write("Enter centre of convergence for Taylor series")
cc = st.number_input("Enter a x-value for the centre of convergence for Taylor series (write 0 for Maclaurin polynomials)")
if (rawInp and tOrder):
    tOrder = abs(round(tOrder))
    st.warning("Large values for the order of Taylor series may take more time to process.")
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
    st.write(ordinal(tOrder) + " order Taylor Series with centre of convergence = " + str(cc) + ":")
    st.latex(str(latex(simplify(tay(symInp,tOrder,cc)))))