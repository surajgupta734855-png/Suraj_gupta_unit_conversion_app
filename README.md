import streamlit as st
import math

# --- CONFIGURATION (STUDENT DATA) ---
# Replace 'YourInitial' with the first two letters of your name (e.g., AB, RA, etc.)
STUDENT_INITIALS = "YOURINITIAL" 

# --- APP SETUP & DATA ---
PI = math.pi

magnetic_conversions = {
    "Magnetic Induction (B)": {"factor": 10**4, "si_unit": "tesla (T)", "cgs_unit": "gauss (G)"},
    "Magnetic Field (H)": {"factor": 4 * PI * (10**-3), "si_unit": "A m⁻¹", "cgs_unit": "oersted (Oe)"},
    "Magnetization (M)": {"factor": 10**-3, "si_unit": "A m⁻¹", "cgs_unit": "emu cm⁻³"},
    "Magnetic Polarization (J)": {"factor": (10**4) / (4 * PI), "si_unit": "T", "cgs_unit": "emu cm⁻³"},
    "Magnetic Moment (m)": {"factor": 10**-3, "si_unit": "A m²", "cgs_unit": "emu = G cm³"},
    "Magnetic Moment per unit mass (σ)": {"factor": 1, "si_unit": "A m² kg⁻¹", "cgs_unit": "emu g⁻¹"},
    "Volume Magnetic Susceptibility (χ)": {"factor": 4 * PI, "si_unit": "dimensionless (SI)", "cgs_unit": "dimensionless (CGS)"},
    "Mass Magnetic Susceptibility (χ)": {"factor": (10**3) / (4 * PI), "si_unit": "m³ kg⁻¹", "cgs_unit": "emu Oe⁻¹ g⁻¹"},
    "Molar Magnetic Susceptibility (χₘ)": {"factor": (10**3) / (4 * PI), "si_unit": "m³ mol⁻¹", "cgs_unit": "emu Oe⁻¹ g⁻¹ mol⁻¹"},
    "Magnetic Permeability (μ)": {"factor": (10**7) / (4 * PI), "si_unit": "H m⁻¹", "cgs_unit": "G Oe⁻¹"},
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

# --- UTILITY FUNCTION FOR LATEX FORMATTING ---
def format_to_latex(value, unit_text):
    """Formats a number and its unit into a professional LaTeX string."""
    if value == 0:
        val_str = "0"
    elif abs(value) < 0.01 or abs(value) >= 10000:
        # Standard scientific notation: 1.23 x 10^4
        exponent = int(math.floor(math.log10(abs(value))))
        mantissa = value / (10**exponent)
        val_str = f"{mantissa:.2f} \\times 10^{{{exponent}}}"
    else:
        # Standard decimal: 123.45
        val_str = f"{value:.4f}".rstrip('0').rstrip('.')
        if val_str == "": val_str = "0"

    # Clean up common unit symbols for LaTeX
    latex_unit = unit_text.replace("⁻¹", "^{-1}").replace("²", "^2").replace("³", "^3").replace("μ", "\\mu ").replace("Φ", "\\Phi ").replace("φ", "\\phi ").replace("χ", "\\chi ").replace("λ", "\\lambda ")
    
    # Text mode for units to keep them upright
    return f"{val_str} \\text{{ {latex_unit}}}"

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

# 2. Main Interface
col1, col2 = st.columns([2, 1])

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
        input_label = f"Enter SI value:"
        input_unit_display = details['si_unit']
    else:
        input_label = f"Enter CGS value:"
        input_unit_display = details['cgs_unit']
        
    input_value = st.number_input(input_label, value=1.0, format="%.6e")
    st.caption(f"Unit: {input_unit_display}")

# 3. Calculation & LaTeX Display
st.divider()
st.header("3. Mathematical Conversion Statement")

factor = details['factor']

if conversion_mode == "SI ➔ CGS":
    result = input_value * factor
    input_unit = details['si_unit']
    output_unit = details['cgs_unit']
else:
    result = input_value / factor
    input_unit = details['cgs_unit']
    output_unit = details['si_unit']

# --- KEY DISPLAY USING LATEX ---
# 1. Format both sides of the equation
latex_input = format_to_latex(input_value, input_unit)
latex_result = format_to_latex(result, output_unit)

# 2. Create the full conversion statement
full_statement = f"{latex_input} = {latex_result}"

# 3. Display with st.latex for professional math formatting
st.info(f"The conversion statement for **{selected_quantity}** is:")
st.latex(full_statement)

# 4. Reference Section
st.divider()
st.subheader("Conversion Reference Data")
col_ref1, col_ref2 = st.columns(2)
with col_ref1:
    st.write(f"**SI Unit:** {details['si_unit']}")
    st.write(f"**CGS Unit:** {details['cgs_unit']}")
with col_ref2:
    # Use LaTeX here too for the base factor
    base_factor_latex = format_to_latex(factor, details['cgs_unit'])
    st.latex(f"1 \\text{{ {details['si_unit']}}} = {base_factor_latex}")
