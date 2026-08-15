import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.metrics import dp

# Define conversion factors based on the assignment sheet (image_1.png)
# Conversions are SI -> CGS. Reverse (CGS -> SI) is 1/factor.
import math
PI = math.pi

conversions = {
    "Magnetic Induction (B)": {"factor": 10**4, "si_unit": "tesla (T)", "cgs_unit": "gauss (G)"},
    "Magnetic Field (H)": {"factor": 4 * PI * (10**-3), "si_unit": "A m⁻¹", "cgs_unit": "oersted (Oe)"},
    "Magnetization (M)": {"factor": 10**-3, "si_unit": "A m⁻¹", "cgs_unit": "emu cm⁻³"},
    "Magnetic Polarization (J)": {"factor": (10**4) / (4 * PI), "si_unit": "T", "cgs_unit": "emu cm⁻³"},
    "Magnetic Moment (m)": {"factor": 10**-3, "si_unit": "A m²", "cgs_unit": "emu = G cm³"},
    "Magnetic Moment per unit mass (σ)": {"factor": 1, "si_unit": "A m² kg⁻¹", "cgs_unit": "emu g⁻¹"},
    "Volume Magnetic Susceptibility (χ = M/H)": {"factor": 4 * PI, "si_unit": "dimensionless (SI)", "cgs_unit": "dimensionless (CGS)"},
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

quantity_names = list(conversions.keys())

# --- APP LAYOUT ---
class UnitConverterLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(UnitConverterLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(20)
        self.spacing = dp(15)

        # 1. Header with University and Course Info
        self.add_widget(Label(text="[b]Harcourt Butler Technical University, Kanpur[/b]", markup=True, font_size='20sp', size_hint_y=None, height=dp(40)))
        self.add_widget(Label(text="Assignment-I: Magnetic Unit Converter (NPH-605)", font_size='16sp', size_hint_y=None, height=dp(30)))
        
        # 2. Quantity Selector
        self.add_widget(Label(text="1. Select Magnetic Quantity:", size_hint_y=None, height=dp(30), halign='left'))
        self.quantity_spinner = Spinner(
            text='-- Select --',
            values=quantity_names,
            size_hint_y=None, height=dp(50)
        )
        self.quantity_spinner.bind(text=self.on_quantity_change)
        self.add_widget(self.quantity_spinner)

        # 3. Unit Info Labels
        unit_info_layout = BoxLayout(orientation='horizontal', spacing=dp(10), size_hint_y=None, height=dp(30))
        self.si_unit_label = Label(text="SI Unit: -", font_size='14sp')
        self.cgs_unit_label = Label(text="CGS Unit: -", font_size='14sp')
        unit_info_layout.add_widget(self.si_unit_label)
        unit_info_layout.add_widget(self.cgs_unit_label)
        self.add_widget(unit_info_layout)

        # 4. Conversion Direction & Input
        conv_layout = BoxLayout(orientation='horizontal', spacing=dp(10))
        
        # Left side: Input value
        input_vbox = BoxLayout(orientation='vertical', spacing=dp(5))
        input_vbox.add_widget(Label(text="2. Enter Value", size_hint_y=None, height=dp(25)))
        self.input_value = TextInput(text='', multiline=False, input_type='number', size_hint_y=None, height=dp(50))
        input_vbox.add_widget(self.input_value)
        conv_layout.add_widget(input_vbox)
        
        # Center: Direction Switch button
        self.direction_btn = Button(text="SI ➔ CGS", size_hint=(0.3, None), height=dp(80), pos_hint={'center_y': 0.5})
        self.direction_btn.bind(on_press=self.toggle_direction)
        conv_layout.add_widget(self.direction_btn)
        self.conversion_direction = "si_to_cgs"
        
        # Right side: Result
        result_vbox = BoxLayout(orientation='vertical', spacing=dp(5))
        result_vbox.add_widget(Label(text="3. Result", size_hint_y=None, height=dp(25)))
        self.result_value = Label(text='', font_size='24sp', bold=True)
        result_vbox.add_widget(self.result_value)
        conv_layout.add_widget(result_vbox)

        self.add_widget(conv_layout)

        # 5. Convert Button
        self.convert_btn = Button(text="[b]CONVERT[/b]", markup=True, font_size='22sp', size_hint_y=None, height=dp(60), background_color=(0, 0.5, 0, 1))
        self.convert_btn.bind(on_press=self.perform_conversion)
        self.add_widget(self.convert_btn)

        # Filler at the bottom
        self.add_widget(Label())

    # --- APP LOGIC ---
    def on_quantity_change(self, spinner, text):
        if text != '-- Select --':
            self.si_unit_label.text = f"SI Unit: {conversions[text]['si_unit']}"
            self.cgs_unit_label.text = f"CGS Unit: {conversions[text]['cgs_unit']}"
            self.result_value.text = "" # Clear previous result

    def toggle_direction(self, instance):
        if self.conversion_direction == "si_to_cgs":
            self.conversion_direction = "cgs_to_si"
            self.direction_btn.text = "CGS ➔ SI"
        else:
            self.conversion_direction = "si_to_cgs"
            self.direction_btn.text = "SI ➔ CGS"
        self.result_value.text = "" # Clear previous result

    def perform_conversion(self, instance):
        quantity = self.quantity_spinner.text
        
        # Validation
        if quantity == '-- Select --':
            self.result_value.text = "Select Quantity"
            return
        if not self.input_value.text:
            self.result_value.text = "Enter Value"
            return
        
        try:
            value = float(self.input_value.text)
        except ValueError:
            self.result_value.text = "Invalid Value"
            return

        factor = conversions[quantity]['factor']
        
        # Calculation
        if self.conversion_direction == "si_to_cgs":
            result = value * factor
            unit_display = conversions[quantity]['cgs_unit']
        else:
            result = value / factor
            unit_display = conversions[quantity]['si_unit']

        # Formatting large/small numbers
        if result == 0:
            formatted_result = "0"
        elif abs(result) < 0.001 or abs(result) > 10000:
            formatted_result = "{:.3e}".format(result)
        else:
            formatted_result = "{:.4f}".format(result)

        self.result_value.text = f"{formatted_result}\n{unit_display}"

# --- MAIN APP CLASS ---
# Replace 'YourInitial' with the first two letters of your name
class YOURINITIAL_PHYHBTU(App): 
    def build(self):
        self.title = 'HBTU Magnetic Unit Converter'
        return UnitConverterLayout()

if __name__ == '__main__':
    # When testing on your PC, you can use a phone-like screen size.
    # from kivy.core.window import Window
    # Window.size = (360, 640)
    YOURINITIAL_PHYHBTU().run()
