import streamlit as st

st.set_page_config(page_title="SI to CGS Unit Converter", page_icon="📏")

st.title("📏 SI to CGS Unit Converter")

conversion = st.selectbox(
    "Choose Conversion",
    [
        "Length (m → cm)",
        "Mass (kg → g)",
        "Force (N → dyne)",
        "Energy (J → erg)",
        "Pressure (Pa → Ba)"
    ]
)

value = st.number_input("Enter Value", value=0.0)

if st.button("Convert"):

    if conversion == "Length (m → cm)":
        result = value * 100
        unit = "cm"

    elif conversion == "Mass (kg → g)":
        result = value * 1000
        unit = "g"

    elif conversion == "Force (N → dyne)":
        result = value * 100000
        unit = "dyne"

    elif conversion == "Energy (J → erg)":
        result = value * 10000000
        unit = "erg"

    elif conversion == "Pressure (Pa → Ba)":
        result = value * 10
        unit = "Ba"

    st.success(f"Converted Value: **{result} {unit}**")
