import streamlit as st
import math

# --- CONFIGURATION (STUDENT DATA) ---
# Replace 'YourInitial' with the first two letters of your name (e.g., AB, RA, etc.)
STUDENT_INITIALS = "YOURINITIAL" 

# --- APP SETUP & DATA ---
# (Pichhle code se magnetic conversions data waise hi hai)
PI = math.pi

magnetic_conversions = {
    "Magnetic Induction (B)": {"factor": 10**4, "si_unit": "tesla (T)", "cgs_unit": "gauss (G)"},
    "Magnetic Field (H)": {"factor": 4 * PI * (10**-3), "si_unit": "A m⁻¹", "cgs_unit": "oersted (Oe)"},
    "Magnetization (M)": {"factor": 10**-3, "si_unit": "A m⁻¹", "cgs_unit": "emu cm⁻³"},
    "Magnetic Polarization (J)": {"factor": (10**4) / (4 * PI), "si_unit": "T", "cgs_unit": "emu cm⁻³"},
    "Magnetic Moment (m)": {"factor": 10**-3, "si_unit": "A m²", "cgs_unit": "emu = G cm³"},
    "Magnetic Moment per unit mass (σ)": {"factor": 1, "si_unit": "A m² kg⁻¹", "cgs_unit": "emu g⁻¹"},
    "Volume Magnetic Susceptibility (χ)": {"factor": 4 * PI, "si_unit": "dimensionless (SI)", "cgs_unit": "dimensionless (CGS)"},
    "Mass Magnetic Susceptibility (χ = κ/ρ)": {"factor": (10**3) / (4 * PI), "si_unit": "m³ kg⁻¹", "cgs_unit": "emu Oe⁻¹ g⁻¹"},
    "Molar Magnetic Susceptibility (χₘ = χM*)": {"factor": (10**3) / (4 * PI), "si_unit": "m³ mol⁻¹", "cgs_unit": "emu Oe⁻¹ g⁻¹ mol⁻¹"},
    "Magnetic Permeability (μ = B/H)": {"factor": (10**7) / (4 * PI), "si_unit": "H m⁻¹", "cgs_unit": "G Oe⁻¹"},
    "Magnetic Flux (Φ)": {"factor": 10**8, "si_unit": "Weber (Wb)", "cgs_unit": "maxwell (Mx)"},
    "Magnetic Scalar Potential (φ)": {"factor": 4 * PI / 10, "si_unit": "A", "cgs_unit": "gilbert"},
    "Magnetic Vector Potential (A)": {"factor": 10**6, "si_unit": "Wb m⁻¹", "cgs_unit": "emu = G cm"},
    "Magnetic Pole Strength (p)": {"factor": 10, "si_unit": "A m", "cgs_unit": "emu = G cm²"},
    "Demagnetizing Factor (N)": {"factor": 1 / (4 * PI), "si_unit": "dimensionless (SI)", "cgs_unit": "dimensionless (CGS)"},
    "Magnetostriction Constant (λ)": {"factor": 1, "si_unit": "dimensionless (SI)", "cgs_unit": "dimensionless (CGS)"},
    "Anisotropy Constant (K)": {"factor": 10, "si_unit": "J m⁻³", "cgs_unit": "erg cm⁻³"},
    "Magnetostatic Energy (Eₘ)": {"factor": 10, "si_unit": "J m⁻³", "cgs_unit": "erg cm⁻³"},
    "Energy Product (BH)ₘₐₓ": {"factor": 10, "si_unit": "J m⁻³", "cgs_unit": "erg cm⁻³"}
}

quantity_list = list(magnetic_conversions.keys())

# --- APP LAYOUT ---

# 1. Header and Assignment Details
st.title("HBTU Magnetic Unit Converter")
st.subheader(f"Assignment-I Demonstration by {STUDENT_INITIALS}_PHYHBTU")
st.markdown("""
**Harcourt Butler Technical University, Kanpur**  
*Department of Physics, School of Basic and Applied Sciences*  
ODD Semester, 2026-2027, M.Sc. Physics II Year  
Spintronics: Fundamentals and Applications (Course Code: NPH-605)
""")
st.divider()

# 2. Main Interface in 3 columns
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.header("1. Selection")
    selected_quantity = st.selectbox("Select Magnetic Quantity:", quantity_list)
    
    conversion_mode = st.radio(
        "Select Conversion Direction:",
        ("SI ➔ CGS", "CGS ➔ SI")
    )

    details = magnetic_conversions[selected_quantity]

with col2:
    st.header("2. Input")
    if conversion_mode == "SI ➔ CGS":
        input_label = f"Enter SI value ({details['si_unit']}):"
    else:
        input_label = f"Enter CGS value ({details['cgs_unit']}):"
        
    input_value = st.number_input(input_label, value=1.0, format="%.6e")

# 3. Calculation & Display "Equal To" Result
st.divider()
st.header("3. Conversion Statement")

factor = details['factor']

if conversion_mode == "SI ➔ CGS":
    result = input_value * factor
    input_unit = details['si_unit']
    output_unit = details['cgs_unit']
else:
    result = input_value / factor
    input_unit = details['cgs_unit']
    output_unit = details['si_unit']

# Formatting for display
input_val_fmt = "{:.6e}".format(input_value)
result_fmt = "{:.6e}".format(result)

# --- KEY DISPLAY ---
# Use an info box for better visibility. Inside is a large, bold mathematical statement.
# Format: [Input Value] [Input Unit] = [Result] [Output Unit]
st.info(f"The conversion statement for **{selected_quantity}** is:")
st.markdown(f"""
<div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #ddd;">
    <span style="font-size: 28px; font-weight: bold; color: #1f77b4;">
        {input_val_fmt} <span style="font-size: 20px; color: #333;">{input_unit}</span>
    </span>
    <span style="font-size: 36px; font-weight: bold; color: #333; margin: 0 15px;">
        =
    </span>
    <span style="font-size: 28px; font-weight: bold; color: #2ca02c;">
        {result_fmt} <span style="font-size: 20px; color: #333;">{output_unit}</span>
    </span>
</div>
""", unsafe_allow_html=True)

# 4. Reference Section
st.divider()
st.subheader("Conversion Reference Data")
col_ref1, col_ref2 = st.columns(2)
with col_ref1:
    st.write(f"**SI Unit:** {details['si_unit']}")
    st.write(f"**CGS Unit:** {details['cgs_unit']}")
with col_ref2:
    st.write(f"**Base Factor (1 SI unit to CGS):** {factor:.6e}")
