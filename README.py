import streamlit as st

st.title("SI to CGS Unit Converter")

conversion = {
    "Length (m → cm)": (100, "cm"),
    "Mass (kg → g)": (1000, "g"),
    "Force (N → dyne)": (100000, "dyne"),
    "Energy (J → erg)": (10000000, "erg"),
    "Pressure (Pa → Ba)": (10, "Ba"),
    "Power (W → erg/s)": (10000000, "erg/s"),
    "Velocity (m/s → cm/s)": (100, "cm/s")
}

choice = st.selectbox("Select Quantity", list(conversion.keys()))
value = st.number_input("Enter Value", value=1.0)

if st.button("Convert"):
    factor, unit = conversion[choice]
    result = value * factor
    st.success(f"{value} = {result} {unit}")
