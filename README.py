import streamlit as st
import math

st.set_page_config(page_title="SI ↔ CGS Converter", page_icon="🧲", layout="centered")

st.title("🧲 SI ↔ CGS Magnetic Unit Converter")
st.write("Convert Magnetic Quantities between SI and CGS Units")

quantity = st.selectbox(
    "Select Magnetic Quantity",
    [
        "Magnetic Flux",
        "Magnetic Flux Density",
        "Magnetic Field Strength",
        "Magnetization",
        "Magnetic Moment",
        "Magnetic Susceptibility"
    ]
)

direction = st.radio(
    "Conversion",
    ["SI → CGS", "CGS → SI"]
)

value = st.number_input("Enter Value", value=0.0, format="%.6f")

result = None
formula = ""
unit = ""

if st.button("Convert"):

    if quantity == "Magnetic Flux":
        if direction == "SI → CGS":
            result = value * 1e8
            unit = "Maxwell (Mx)"
            formula = "1 Wb = 10⁸ Mx"
        else:
            result = value / 1e8
            unit = "Weber (Wb)"
            formula = "1 Mx = 10⁻⁸ Wb"

    elif quantity == "Magnetic Flux Density":
        if direction == "SI → CGS":
            result = value * 10000
            unit = "Gauss (G)"
            formula = "1 Tesla = 10⁴ Gauss"
        else:
            result = value / 10000
            unit = "Tesla (T)"
            formula = "1 Gauss = 10⁻⁴ Tesla"

    elif quantity == "Magnetic Field Strength":
        if direction == "SI → CGS":
            result = value / 79.57747
            unit = "Oersted (Oe)"
            formula = "Oe = A/m ÷ 79.57747"
        else:
            result = value * 79.57747
            unit = "A/m"
            formula = "A/m = Oe × 79.57747"

    elif quantity == "Magnetization":
        if direction == "SI → CGS":
            result = value / 1000
            unit = "emu/cm³"
            formula = "1 A/m = 0.001 emu/cm³"
        else:
            result = value * 1000
            unit = "A/m"
            formula = "1 emu/cm³ = 1000 A/m"

    elif quantity == "Magnetic Moment":
        if direction == "SI → CGS":
            result = value * 1000
            unit = "emu"
            formula = "1 A·m² = 1000 emu"
        else:
            result = value / 1000
            unit = "A·m²"
            formula = "1 emu = 0.001 A·m²"

    elif quantity == "Magnetic Susceptibility":
        if direction == "SI → CGS":
            result = value / (4 * math.pi)
            unit = "CGS"
            formula = "χ(CGS) = χ(SI) / (4π)"
        else:
            result = value * (4 * math.pi)
            unit = "SI"
            formula = "χ(SI) = 4π × χ(CGS)"

    st.success("Conversion Completed")

    st.metric("Converted Value", f"{result:.6f} {unit}")

    st.info(f"Formula Used:\n\n{formula}")

st.markdown("---")
st.caption("Developed for SI ↔ CGS Magnetic Unit Conversion")
