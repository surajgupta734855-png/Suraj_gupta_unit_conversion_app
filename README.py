import streamlit as st
import math

# --- CONFIGURATION (STUDENT DATA) ---
# Replace 'YourInitial' with the first two letters of your name (e.g., AB, RA, etc.)
STUDENT_INITIALS = "YOURINITIAL" 

# --- APP SETUP ---
# Defining conversion factors based on image_1.png
# Format: SI_value * factor = CGS_value
# Reversing: CGS_value / factor = SI_value

PI = math.pi

magnetic_conversions = {
    "Magnetic Induction (B)": {
        "factor": 10**4, 
        "si_unit": "tesla (T)", 
        "cgs_unit": "gauss (G)"
    },
    "Magnetic Field (H)": {
        "factor": 4 * PI * (10**-3), 
        "si_unit": "A m⁻¹", 
        "cgs_unit": "oersted (Oe)"
    },
    "Magnetization (M)": {
        "factor": 10**-3, 
        "si_unit": "A m⁻¹", 
        "cgs_unit": "emu cm⁻³"
    },
    "Magnetic Polarization (J)": {
        "factor": (10**4) / (4 * PI), 
        "si_unit": "T", 
        "cgs_unit": "emu cm⁻³"
    },
    "Magnetic Moment (m)": {
        "factor": 10**-3, 
        "si_unit": "A m²", 
        "cgs_unit": "emu = G cm³"
    },
    "Magnetic Moment per unit mass (σ)": {
        "factor": 1, 
        "si_unit": "A m² kg⁻¹", 
        "cgs_unit": "emu g⁻¹"
    },
    "Volume Magnetic Susceptibility (χ = M/H)": {
        "factor": 4 * PI, 
        "si_unit": "dimensionless (SI)", 
        "cgs_unit": "dimensionless (CGS)"
    },
    "Mass Magnetic Susceptibility (χ = κ/ρ)": {
        "factor": (10**3) / (4 * PI), 
        "si_unit": "m³ kg⁻¹", 
        "cgs_unit": "emu Oe⁻¹ g⁻¹"
    },
    "Molar Magnetic Susceptibility (χₘ = χM*)": {
        "factor": (10**3) / (4 * PI), 
        "si_unit": "m³ mol⁻¹", 
        "cgs_unit": "emu Oe⁻¹ g⁻¹ mol⁻¹"
    },
    "Magnetic Permeability (μ = B/H)": {
        "factor": (10**7) / (4 * PI), 
        "si_unit": "H m⁻¹", 
        "cgs_unit": "G Oe⁻¹"
    },
    "Magnetic Flux (Φ)": {
        "factor": 10**8, 
        "si_unit": "Weber (Wb)", 
        "cgs_unit": "maxwell (Mx)"
    },
    "Magnetic Scalar Potential (φ)": {
        "factor": 4 * PI / 10, 
        "si_unit": "A", 
        "cgs_unit": "gilbert"
    },
    "Magnetic Vector Potential (A)": {
        "factor": 10**6, 
        "si_unit": "Wb m⁻¹", 
        "cgs_unit": "emu = G cm"
    },
    "Magnetic Pole Strength (p)": {
        "factor": 10, 
        "si_unit": "A m", 
        "cgs_unit": "emu = G cm²"
    },
    "Demagnetizing Factor (N)": {
        "factor": 1 / (4 * PI), 
        "si_unit": "dimensionless (SI)", 
        "cgs_unit": "dimensionless (CGS)"
    },
    "Magnetostriction Constant (λ)": {
        "factor": 1, 
        "si_unit": "dimensionless (SI)", 
        "cgs_unit": "dimensionless (CGS)"
    },
    "Anisotropy Constant (K)": {
        "factor": 10, 
        "si_unit": "J m⁻³", 
        "cgs_unit": "erg cm⁻³"
    },
    "Magnetostatic Energy (Eₘ)": {
        "factor": 10, 
        "si_unit": "J m⁻³", 
        "cgs_unit": "erg cm⁻³"
    },
    "Energy Product (BH)ₘₐₓ": {
        "factor": 10, 
        "si_unit": "J m⁻³", 
        "cgs_unit": "erg cm⁻³"
    }
}

# --- MAIN APP LAYOUT ---

# 1. Title and Assignment Details
st.title("HBTU Magnetic Unit Converter")
st.subheader(f"Assignment-I: {STUDENT_INITIALS}_PHYHBTU")
st.markdown("""
**Department of Physics, School of Basic and Applied Sciences**  
ODD Semester, 2026-2027, M.Sc. Physics II Year  
*Spintronics: Fundamentals and Applications (Course Code: NPH-605)*
""")
st.divider()

# 2. Sidebar for Selection
st.sidebar.header("Conversion Settings")
quantity_list = list(magnetic_conversions.keys())
selected_quantity = st.sidebar.selectbox("1. Select Magnetic Quantity:", quantity_list)

# Get details of the selected quantity
details = magnetic_conversions[selected_quantity]

# 3. Mode Selection (SI to CGS or vice versa)
st.sidebar.markdown("---")
conversion_mode = st.sidebar.radio(
    "2. Select Conversion Direction:",
    ("SI to CGS", "CGS to SI")
)

# 4. Input Value
st.sidebar.markdown("---")
if conversion_mode == "SI to CGS":
    input_label = f"Enter value in SI Unit ({details['si_unit']}):"
else:
    input_label = f"Enter value in CGS Unit ({details['cgs_unit']}):"

input_value = st.sidebar.number_input(input_label, value=1.0, format="%.6e")

# 5. Perform Calculation
st.divider()
st.header("Conversion Result")

# We use the factor directly if SI to CGS, or divide by it if CGS to SI.
factor = details['factor']

if conversion_mode == "SI to CGS":
    result = input_value * factor
    from_unit = details['si_unit']
    to_unit = details['cgs_unit']
else:
    result = input_value / factor
    from_unit = details['cgs_unit']
    to_unit = details['si_unit']

# Displaying the result clearly
st.metric(
    label=f"{selected_quantity} ({conversion_mode})",
    value="{:.6e}".format(result),
    help=f"Conversion from {from_unit} to {to_unit}"
)

# Showing the formula
st.info(f"Formula used: {input_value} {from_unit} = {result:.6e} {to_unit}")

# Showing the standard conversion factors from the sheet
st.divider()
st.subheader("Reference Data")
st.write(f"**Magnetic Quantity:** {selected_quantity}")
st.write(f"**SI Unit:** {details['si_unit']}")
st.write(f"**CGS Unit:** {details['cgs_unit']}")
st.write(f"**Base Conversion Factor (1 SI unit to CGS):** {factor:.6e}")
