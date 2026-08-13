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
         "Power (watt→ HP)"
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
 

st.title("Horsepower (hp) to Watt Converter")

hp_type = st.selectbox(
    "Select Horsepower Type",
    ["Mechanical hp", "Metric hp"]
)

hp = st.number_input("Enter Horsepower (hp)", min_value=0.0, value=1.0)

if st.button("Convert"):
    if hp_type == "Mechanical hp":
        watt = hp * 745.7
    else:
        watt = hp * 735.5

    st.success(f"{hp} {hp_type} = {watt:.2f} W")

    st.success(f"Converted Value: **{result} {unit}**")
