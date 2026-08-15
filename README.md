<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>XX_PHYHBTU - Unit Converter</title>
    <style>
        * { box-sizing: border-box; font-family: Arial, sans-serif; }
        body { background-color: #f4f6f9; padding: 20px; margin: 0; }
        .card { max-width: 450px; margin: 0 auto; background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        h2 { text-align: center; color: #800000; margin-top: 0; font-size: 20px; }
        h4 { text-align: center; color: #555; margin-bottom: 20px; font-weight: normal; font-size: 13px; }
        label { font-weight: bold; color: #333; display: block; margin-top: 12px; margin-bottom: 5px; font-size: 14px; }
        select, input, button { width: 100%; padding: 12px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 8px; font-size: 15px; }
        select:focus, input:focus { border-color: #800000; outline: none; }
        button { background-color: #800000; color: white; border: none; font-weight: bold; cursor: pointer; transition: 0.2s; }
        button:hover { background-color: #600000; }
        .result-box { background: #eef2f7; padding: 15px; border-radius: 8px; border-left: 5px solid #800000; margin-top: 10px; }
        .result-title { font-size: 13px; color: #666; }
        .result-val { font-size: 18px; font-weight: bold; color: #111; word-break: break-all; }
    </style>
</head>
<body>

<div class="card">
    <h2>NPH-605: Magnetic Converter</h2>
    <h4>HBTU Kanpur - Physics Assignment</h4>

    <label for="quantity">Select Magnetic Quantity:</label>
    <select id="quantity">
        <option value="B">Magnetic Induction (B)</option>
        <option value="H">Magnetic Field (H)</option>
        <option value="M">Magnetization (M)</option>
        <option value="J">Magnetic Polarization (J)</option>
        <option value="m">Magnetic Moment (m)</option>
        <option value="sigma">Magnetic Moment per unit mass (σ)</option>
        <option value="kappa">Volume Magnetic Susceptibility (κ)</option>
        <option value="chi">Mass Magnetic Susceptibility (χ)</option>
        <option value="chi_m">Molar Magnetic Susceptibility (χm)</option>
        <option value="mu">Magnetic Permeability (μ)</option>
        <option value="Phi">Magnetic Flux (Φ)</option>
        <option value="phi">Magnetic Scalar Potential / MMF (ϕ)</option>
        <option value="A">Magnetic Vector Potential (A)</option>
        <option value="p">Magnetic Pole Strength (p)</option>
        <option value="N">Demagnetizing Factor (N)</option>
        <option value="lambda">Magnetostriction Constant (λ)</option>
        <option value="K">Anisotropy Constant (K)</option>
        <option value="Em">Magnetostatic Energy (Em)</option>
        <option value="BHmax">Energy Product ((BH)max)</option>
    </select>

    <label for="direction">Conversion Mode:</label>
    <select id="direction">
        <option value="si_to_cgs">SI Unit ➔ CGS Unit</option>
        <option value="cgs_to_si">CGS Unit ➔ SI Unit</option>
    </select>

    <label for="inputValue">Enter Value:</label>
    <input type="number" id="inputValue" placeholder="e.g. 1.5" step="any">

    <button onclick="convert()">CONVERT</button>

    <div class="result-box" id="resultContainer" style="display:none;">
        <div class="result-title" id="resultLabel">Converted Value:</div>
        <div class="result-val" id="resultValue">-</div>
    </div>
</div>

<script>
const data = {
    B: { si: "Tesla (T)", cgs: "Gauss (G)", factor: 1e4 },
    H: { si: "A m⁻¹", cgs: "Oersted (Oe)", factor: 4 * Math.PI * 1e-3 },
    M: { si: "A m⁻¹", cgs: "emu cm⁻³", factor: 1e-3 },
    J: { si: "Tesla (T)", cgs: "emu cm⁻³", factor: 1e4 / (4 * Math.PI) },
    m: { si: "A m²", cgs: "emu (G·cm³)", factor: 1e3 },
    sigma: { si: "A m² kg⁻¹", cgs: "emu g⁻¹", factor: 1 },
    kappa: { si: "Dimensionless (SI)", cgs: "Dimensionless (CGS)", factor: 1 / (4 * Math.PI) },
    chi: { si: "m³ kg⁻¹", cgs: "emu Oe⁻¹ g⁻¹", factor: 1e3 / (4 * Math.PI) },
    chi_m: { si: "m³ mol⁻¹", cgs: "emu Oe⁻¹ g mol⁻¹", factor: 1e3 / (4 * Math.PI) },
    mu: { si: "H m⁻¹", cgs: "G Oe⁻¹", factor: 1e7 / (4 * Math.PI) },
    Phi: { si: "Weber (Wb)", cgs: "Maxwell (Mx)", factor: 1e8 },
    phi: { si: "Ampere (A)", cgs: "Gilbert", factor: 4 * Math.PI / 10 },
    A: { si: "Wb m⁻¹", cgs: "emu (G·cm)", factor: 1e6 },
    p: { si: "A m", cgs: "emu (G·cm²)", factor: 1e3 },
    N: { si: "Dimensionless (SI)", cgs: "Dimensionless (CGS)", factor: 4 * Math.PI },
    lambda: { si: "Dimensionless (SI)", cgs: "Dimensionless (CGS)", factor: 1 },
    K: { si: "J m⁻³", cgs: "erg cm⁻³", factor: 10 },
    Em: { si: "J m⁻³", cgs: "erg cm⁻³", factor: 10 },
    BHmax: { si: "J m⁻³", cgs: "erg cm⁻³", factor: 10 }
};

function convert() {
    const qty = document.getElementById('quantity').value;
    const dir = document.getElementById('direction').value;
    const valInput = document.getElementById('inputValue').value;

    if (valInput === "" || isNaN(valInput)) {
        alert("Kripya sahi numeric value enter karein!");
        return;
    }

    const val = parseFloat(valInput);
    const item = data[qty];
    let res = 0;
    let fromUnit = "", toUnit = "";

    if (dir === "si_to_cgs") {
        res = val * item.factor;
        fromUnit = item.si;
        toUnit = item.cgs;
    } else {
        res = val / item.factor;
        fromUnit = item.cgs;
        toUnit = item.si;
    }

    document.getElementById('resultContainer').style.display = "block";
    document.getElementById('resultLabel').innerText = `${val} ${fromUnit} =`;
    document.getElementById('resultValue').innerText = `${res.toExponential(6).replace(/e\+?/, ' × 10^')} ${toUnit}\n(${res.toFixed(6)} ${toUnit})`;
}
</script>

</body>
</html>
