import streamlit as st
import math

# Page Configuration
st.set_page_config(page_title="Magnetic Unit Converter", page_icon="🧲", layout="centered")

# App Header
st.title("🧲 Magnetic Unit Converter")
st.subheader("Course: Spintronics (NPH-605) | HBTU Kanpur")
st.write("Convert SI units to CGS units and vice-versa for magnetic quantities.")

# Conversion Factors & Metadata
# Factor converts 1 SI unit into CGS units
quantities = {
    "Magnetic induction (B)": {"si": "Tesla (T)", "cgs": "gauss (G)", "factor": 1e4},
    "Magnetic field (H)": {"si": "A m⁻¹", "cgs": "oersted (Oe)", "factor": 4 * math.pi * 1e-3},
    "Magnetization (M)": {"si": "A m⁻¹", "cgs": "emu cm⁻³", "factor": 1e-3},
    "Magnetic polarization (J)": {"si": "Tesla (T)", "cgs": "emu cm⁻³", "factor": 1e4 / (4 * math.pi)},
    "Magnetic moment (m)": {"si": "A m²", "cgs": "emu = G·cm³", "factor": 1e3},
    "Magnetic moment per unit mass (σ)": {"si": "A m² kg⁻¹", "cgs": "emu g⁻¹", "factor": 1.0},
    "Volume magnetic susceptibility (κ)": {"si": "Dimensionless (SI)", "cgs": "Dimensionless (CGS)", "factor": 1 / (4 * math.pi)},
    "Mass magnetic susceptibility (χ)": {"si": "m³ kg⁻¹", "cgs": "emu Oe⁻¹ g⁻¹", "factor": 1e3 / (4 * math.pi)},
    "Molar magnetic susceptibility (χm)": {"si": "m³ mol⁻¹", "cgs": "emu Oe⁻¹ g mol⁻¹", "factor": 1e3 / (4 * math.pi)},
    "Magnetic permeability (μ)": {"si": "H m⁻¹", "cgs": "G Oe⁻¹", "factor": 1e7 / (4 * math.pi)},
    "Magnetic flux (Φ)": {"si": "Weber (Wb)", "cgs": "maxwell (Mx)", "factor": 1e8},
    "Magnetic scalar potential / MMF (ϕ)": {"si": "Ampere (A)", "cgs": "gilbert", "factor": 4 * math.pi / 10},
    "Magnetic vector potential (A)": {"si": "Wb m⁻¹", "cgs": "emu = G cm", "factor": 1e6},
    "Magnetic pole strength (p)": {"si": "A m", "cgs": "emu = G cm²", "factor": 1e3},
    "Demagnetizing factor (N)": {"si": "Dimensionless (SI)", "cgs": "Dimensionless (CGS)", "factor": 4 * math.pi},
    "Magnetostriction constant (λ)": {"si": "Dimensionless (SI)", "cgs": "Dimensionless (CGS)", "factor": 1.0},
    "Anisotropy constant (K)": {"si": "J m⁻³", "cgs": "erg cm⁻³", "factor": 10.0},
    "Magnetostatic energy (Em)": {"si": "J m⁻³", "cgs": "erg cm⁻³", "factor": 10.0},
    "Energy product ((BH)max)": {"si": "J m⁻³", "cgs": "erg cm⁻³", "factor": 10.0}
}

# User Inputs
selected_qty = st.selectbox("Select Magnetic Quantity:", list(quantities.keys()))
mode = st.radio("Select Conversion Direction:", ["SI Unit ➔ CGS Unit", "CGS Unit ➔ SI Unit"])
val = st.number_input("Enter Value to Convert:", value=1.0, format="%.6e")

# Computation
item = quantities[selected_qty]

if mode == "SI Unit ➔ CGS Unit":
    result = val * item["factor"]
    from_unit = item["si"]
    to_unit = item["cgs"]
else:
    result = val / item["factor"]
    from_unit = item["cgs"]
    to_unit = item["si"]

# Display Result
st.markdown("---")
st.markdown(f"### Result:")
st.success(f"**{val:g} {from_unit}** = **{result:.6e} {to_unit}**")
st.caption(f"Standard decimal notation: **{result:.6f} {to_unit}**")
