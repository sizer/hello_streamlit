import streamlit as st

st.markdown('Streamlit is **_really_ cool**.')
st.markdown(
    "This text is : red[colored red], and this is **: blue[colored] ** and bold.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
