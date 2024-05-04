import streamlit as st
import matplotlib.pyplot as plt

a = st.slider(
        'a', 
        value=1,
        min_value=-10,
        max_value=10,
        step=1
    )
b = st.slider(
        'b', 
        value=1,
        min_value=-10,
        max_value=10,
        step=1
    )
c = st.slider(
         'c', 
        value=1,
        min_value=-10,
        max_value=10,
        step=1
    )
d = st.slider(
        'd', 
        value=1,
        min_value=-10,
        max_value=10,
        step=1
    )

def f(x):
    return a*x*x*x + b*x*x + c*x + d 

P = []
for i in range(-20, 20):
    x = i / 10
    y = f(x)
    P.append((x, y))
    
x_values = [point[0] for point in P]
y_values = [point[1] for point in P]

st.set_option('deprecation.showPyplotGlobalUse', False)  # Deprecated warningの抑制
st.title('Graph of f(x)')

fig = plt.figure()
plt.plot(x_values, y_values)
st.pyplot(fig)


