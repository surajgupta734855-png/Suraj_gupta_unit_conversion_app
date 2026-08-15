import streamlit as st

st.set_page_config(page_title="SI ↔ CGS Converter", page_icon="🧲")

st.title("🧲 SI ↔ CGS Unit Converter")
st.write("### Magnetic Quantities Conversion")

conversion = st.selectbox(
    "Select Conversion",
    [
        "Magnetic Flux (Wb ↔ Maxwell)",
        "Magnetic Flux Density (Tesla ↔ Gauss)",
        "Magnetic Field Strength (A/m ↔ Oersted)",
        "Magnetic Moment (A·m² ↔ erg/G)",
        "Inductance (Henry ↔ abHenry)"
    ]
)

direction = st.radio(
    "Conversion Type",
    ["SI → CGS", "CGS → SI"]
)

value = st.number_input("Enter Value", value=0.0)

result = None

if conversion == "Magnetic Flux (Wb ↔ Maxwell)":
    if direction == "SI → CGS":
        result = value * 1e8
        unit = "Maxwell"
    else:
        result = value / 1e8
        unit = "Weber"

elif conversion == "Magnetic Flux Density (Tesla ↔ Gauss)":
    if direction == "SI → CGS":
        result = value * 10000
        unit = "Gauss"
    else:
        result = value / 10000
        unit = "Tesla"

elif conversion == "Magnetic Field Strength (A/m ↔ Oersted)":
    if direction == "SI → CGS":
        result = value * 0.012566
        unit = "Oersted"
    else:
        result = value * 79.577
        unit = "A/m"

elif conversion == "Magnetic Moment (A·m² ↔ erg/G)":
    if direction == "SI → CGS":
        result = value * 1000
        unit = "erg/G"
    else:
        result = value / 1000
        unit = "A·m²"

elif conversion == "Inductance (Henry ↔ abHenry)":
    if direction == "SI → CGS":
        result = value * 1e9
        unit = "abHenry"
    else:
        result = value / 1e9
        unit = "Henry"

if st.button("Convert"):
    st.success(f"Converted Value = {result:.6f} {unit}")

st.markdown("---")
st.caption("Developed for M.Sc Physics Assignment")
