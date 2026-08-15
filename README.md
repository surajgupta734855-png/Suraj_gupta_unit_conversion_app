import math
import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Magnetic Units Converter - HBTU", page_icon="🧲", layout="wide"
)

# Header Section
st.title("🧲 Spintronics: SI ↔ CGS Magnetic Unit Converter")
st.markdown("### Department of Physics | HBTU Kanpur (Course: NPH-605)")
st.markdown("---")

# Conversion Data based on Assignment Table
# Factor definition: 1 SI Unit = (Factor) * CGS Unit
quantities = {
    "Magnetic induction (B)": {
        "symbol": "B",
        "si_unit": "Tesla (T)",
        "cgs_unit": "Gauss (G)",
        "factor": 1e4,
        "conversion_str": "1 T = 10⁴ G",
    },
    "Magnetic field (H)": {
        "symbol": "H",
        "si_unit": "A m⁻¹",
        "cgs_unit": "Oersted (Oe)",
        "factor": 4 * math.pi * 1e-3,
        "conversion_str": "1 A m⁻¹ = 4π × 10⁻³ Oe",
    },
    "Magnetization (M)": {
        "symbol": "M",
        "si_unit": "A m⁻¹",
        "cgs_unit": "emu cm⁻³",
        "factor": 1e-3,
        "conversion_str": "1 A m⁻¹ = 10⁻³ emu cm⁻³",
    },
    "Magnetic polarization (J)": {
        "symbol": "J",
        "si_unit": "Tesla (T)",
        "cgs_unit": "G (or emu cm⁻³)",
        "factor": 1e4 / (4 * math.pi),
        "conversion_str": "1 T = 10⁴/(4π) emu cm⁻³",
    },
    "Magnetic moment (m)": {
        "symbol": "m",
        "si_unit": "A m²",
        "cgs_unit": "emu (= G cm³)",
        "factor": 1e3,
        "conversion_str": "1 A m² = 10³ emu",
    },
    "Magnetic moment per unit mass (σ)": {
        "symbol": "σ",
        "si_unit": "A m² kg⁻¹",
        "cgs_unit": "emu g⁻¹",
        "factor": 1.0,
        "conversion_str": "1 A m² kg⁻¹ = 1 emu g⁻¹",
    },
    "Volume magnetic susceptibility (χ)": {
        "symbol": "χ",
        "si_unit": "dimensionless",
        "cgs_unit": "dimensionless",
        "factor": 1 / (4 * math.pi),
        "conversion_str": "1 (SI) = 1/(4π) (CGS)",
    },
    "Mass magnetic susceptibility (χ_g)": {
        "symbol": "χ_g",
        "si_unit": "m³ kg⁻¹",
        "cgs_unit": "emu Oe⁻¹ g⁻¹",
        "factor": 1e3 / (4 * math.pi),
        "conversion_str": "1 m³ kg⁻¹ = 10³/(4π) emu Oe⁻¹ g⁻¹",
    },
    "Molar magnetic susceptibility (χ_m)": {
        "symbol": "χ_m",
        "si_unit": "m³ mol⁻¹",
        "cgs_unit": "emu Oe⁻¹ mol⁻¹",
        "factor": 1e6 / (4 * math.pi),
        "conversion_str": "1 m³ mol⁻¹ = 10⁶/(4π) emu Oe⁻¹ mol⁻¹",
    },
    "Magnetic permeability (μ)": {
        "symbol": "μ",
        "si_unit": "H m⁻¹",
        "cgs_unit": "G Oe⁻¹",
        "factor": 1e7 / (4 * math.pi),
        "conversion_str": "1 H m⁻¹ = 10⁷/(4π) G Oe⁻¹",
    },
    "Magnetic flux (Φ)": {
        "symbol": "Φ",
        "si_unit": "Weber (Wb)",
        "cgs_unit": "Maxwell (Mx)",
        "factor": 1e8,
        "conversion_str": "1 Wb = 10⁸ Mx",
    },
    "Magnetic scalar potential / Magnetomotive force (ϕ)": {
        "symbol": "ϕ",
        "si_unit": "Ampere (A)",
        "cgs_unit": "gilbert",
        "factor": 0.4 * math.pi,
        "conversion_str": "1 A = 4π/10 gilbert",
    },
    "Magnetic vector potential (A)": {
        "symbol": "A",
        "si_unit": "Wb m⁻¹",
        "cgs_unit": "emu (= G cm)",
        "factor": 1e6,
        "conversion_str": "1 Wb m⁻¹ = 10⁶ emu",
    },
    "Magnetic pole strength (p)": {
        "symbol": "p",
        "si_unit": "A m",
        "cgs_unit": "emu (= G cm²)",
        "factor": 1e3,
        "conversion_str": "1 A m = 10³ emu",
    },
    "Demagnetizing factor (N)": {
        "symbol": "N",
        "si_unit": "dimensionless",
        "cgs_unit": "dimensionless",
        "factor": 4 * math.pi,
        "conversion_str": "1 (SI) = 4π (CGS)",
    },
    "Magnetostriction constant (λ)": {
        "symbol": "λ",
        "si_unit": "dimensionless",
        "cgs_unit": "dimensionless",
        "factor": 1.0,
        "conversion_str": "1 (SI) = 1 (CGS)",
    },
    "Anisotropy constant (K)": {
        "symbol": "K",
        "si_unit": "J m⁻³",
        "cgs_unit": "erg cm⁻³",
        "factor": 10.0,
        "conversion_str": "1 J m⁻³ = 10 erg cm⁻³",
    },
    "Magnetostatic energy (Em)": {
        "symbol": "Em",
        "si_unit": "J m⁻³",
        "cgs_unit": "erg cm⁻³",
        "factor": 10.0,
        "conversion_str": "1 J m⁻³ = 10 erg cm⁻³",
    },
    "Energy product ((BH)max)": {
        "symbol": "(BH)max",
        "si_unit": "J m⁻³",
        "cgs_unit": "erg cm⁻³",
        "factor": 10.0,
        "conversion_str": "1 J m⁻³ = 10 erg cm⁻³",
    },
}

# Sidebar for App Settings
st.sidebar.header("⚙️ Converter Settings")
selected_q = st.sidebar.selectbox(
    "Choose Magnetic Quantity:", list(quantities.keys())
)
direction = st.sidebar.radio("Conversion Direction:", ["SI to CGS", "CGS to SI"])

data = quantities[selected_q]

# Main Interface
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"Convert: {selected_q}")
    st.info(
        f"**Symbol:** `{data['symbol']}` | **Standard Relation:** `{data['conversion_str']}`"
    )

    if direction == "SI to CGS":
        input_label = f"Enter Value in SI Unit ({data['si_unit']})"
        val = st.number_input(
            input_label, value=1.0, format="%.6e", key="input_val"
        )
        converted = val * data["factor"]
        st.success(
            f"**Result:** `{val:g}` {data['si_unit']} = **`{converted:.6e}` {data['cgs_unit']}**"
        )
    else:
        input_label = f"Enter Value in CGS Unit ({data['cgs_unit']})"
        val = st.number_input(
            input_label, value=1.0, format="%.6e", key="input_val"
        )
        converted = val / data["factor"]
        st.success(
            f"**Result:** `{val:g}` {data['cgs_unit']} = **`{converted:.6e}` {data['si_unit']}**"
        )

with col2:
    st.markdown("### ℹ️ Units Summary")
    st.write(f"**SI Unit:** {data['si_unit']}")
    st.write(f"**CGS Unit:** {data['cgs_unit']}")

st.markdown("---")

# Full Reference Table Display
st.subheader("📋 Complete Magnetic Units Reference Table")
table_data = []
for k, v in quantities.items():
    table_data.append(
        {
            "Magnetic Quantity": k,
            "Symbol": v["symbol"],
            "SI Unit": v["si_unit"],
            "CGS Unit": v["cgs_unit"],
            "Conversion Factor": v["conversion_str"],
        }
    )

df = pd.DataFrame(table_data)
st.dataframe(df, use_container_width=True)
