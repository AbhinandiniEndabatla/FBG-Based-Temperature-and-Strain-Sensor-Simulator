
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from fbg_model import calculate_wavelength_shift


# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="FBG Sensor Simulator",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 FBG-Based Temperature and Strain Sensor Simulator")

st.write(
    """
    This application simulates how temperature and strain affect
    the Bragg wavelength of a Fiber Bragg Grating (FBG) sensor.
    Adjust the input parameters in the sidebar and observe the
    corresponding wavelength shift.
    """
)

st.divider()


# --------------------------------------------------
# 2. SIDEBAR INPUT PARAMETERS
# --------------------------------------------------

st.sidebar.header("Sensor Input Parameters")

st.sidebar.subheader("Reference Parameters")

reference_wavelength = st.sidebar.number_input(
    "Reference Bragg Wavelength (nm)",
    min_value=100.0,
    max_value=3000.0,
    value=1550.0,
    step=1.0
)

temperature = st.sidebar.slider(
    "Temperature Change (°C)",
    min_value=-50,
    max_value=150,
    value=30,
    step=1
)

strain = st.sidebar.slider(
    "Strain (microstrain, µε)",
    min_value=0,
    max_value=2000,
    value=500,
    step=10
)

st.sidebar.divider()

st.sidebar.subheader("Sensor Sensitivity")

temperature_sensitivity = st.sidebar.number_input(
    "Temperature Sensitivity (pm/°C)",
    min_value=0.1,
    max_value=100.0,
    value=10.3,
    step=0.1
)

strain_sensitivity = st.sidebar.number_input(
    "Strain Sensitivity (pm/µε)",
    min_value=0.1,
    max_value=10.0,
    value=1.2,
    step=0.1
)

st.sidebar.divider()

st.sidebar.subheader("Spectrum Settings")

peak_width = st.sidebar.slider(
    "Illustrative Peak Width (FWHM in nm)",
    min_value=0.05,
    max_value=1.0,
    value=0.2,
    step=0.05
)


# --------------------------------------------------
# 3. CALCULATE WAVELENGTH SHIFT
# --------------------------------------------------

try:
    (
        temperature_shift,
        strain_shift,
        total_shift,
        new_wavelength
    ) = calculate_wavelength_shift(
        reference_wavelength,
        temperature,
        strain,
        temperature_sensitivity,
        strain_sensitivity
    )

except (ValueError, TypeError) as error:
    st.error(f"Calculation error: {error}")
    st.stop()


total_shift_nm = total_shift / 1000


# --------------------------------------------------
# 4. DISPLAY CALCULATION RESULTS
# --------------------------------------------------

st.header("Simulation Results")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Reference Wavelength",
    f"{reference_wavelength:.3f} nm"
)

col2.metric(
    "Temperature Shift",
    f"{temperature_shift:.2f} pm"
)

col3.metric(
    "Strain Shift",
    f"{strain_shift:.2f} pm"
)

col4.metric(
    "New Bragg Wavelength",
    f"{new_wavelength:.3f} nm",
    delta=f"{total_shift_nm:.3f} nm"
)

st.info(
    f"Total wavelength shift: {total_shift:.2f} pm "
    f"({total_shift_nm:.4f} nm)"
)

st.divider()


# --------------------------------------------------
# 5. REFLECTION SPECTRUM
# --------------------------------------------------

st.header("1. FBG Reflection Spectrum")

st.write(
    """
    The graph shows the original reflection peak and the shifted
    reflection peak after applying temperature and strain.
    """
)

# Calculate Gaussian peak width
sigma = peak_width / (2 * np.sqrt(2 * np.log(2)))

# Set graph range to include both peaks
margin = max(
    4 * peak_width,
    abs(total_shift_nm) + 2 * peak_width,
    0.5
)

wavelength_range = np.linspace(
    min(reference_wavelength, new_wavelength) - margin,
    max(reference_wavelength, new_wavelength) + margin,
    1000
)

# Original reflection spectrum
original_spectrum = np.exp(
    -0.5 * ((wavelength_range - reference_wavelength) / sigma) ** 2
)

# Shifted reflection spectrum
shifted_spectrum = np.exp(
    -0.5 * ((wavelength_range - new_wavelength) / sigma) ** 2
)

fig1, ax1 = plt.subplots(figsize=(10, 4))

ax1.plot(
    wavelength_range,
    original_spectrum,
    label="Original FBG Spectrum",
    linewidth=2
)

ax1.plot(
    wavelength_range,
    shifted_spectrum,
    label="Shifted FBG Spectrum",
    linewidth=2
)

ax1.axvline(
    reference_wavelength,
    linestyle="--",
    label="Reference Wavelength"
)

ax1.axvline(
    new_wavelength,
    linestyle="--",
    label="New Wavelength"
)

ax1.set_xlabel("Wavelength (nm)")
ax1.set_ylabel("Normalized Reflectivity")
ax1.set_title("FBG Reflection Spectrum Before and After Shift")
ax1.legend()
ax1.grid(True, alpha=0.3)

st.pyplot(fig1)
plt.close(fig1)


# --------------------------------------------------
# 6. TEMPERATURE CONTRIBUTION GRAPH
# --------------------------------------------------

st.header("2. Temperature Effect")

st.write(
    "This graph shows the wavelength shift caused by temperature alone."
)

temperature_values = np.linspace(-50, 150, 100)

temperature_shifts = (
    temperature_sensitivity * temperature_values
)

fig2, ax2 = plt.subplots(figsize=(9, 4))

ax2.plot(
    temperature_values,
    temperature_shifts,
    linewidth=2,
    label="Temperature-induced Shift"
)

ax2.scatter(
    temperature,
    temperature_shift,
    s=80,
    label="Current Temperature"
)

ax2.set_xlabel("Temperature Change (°C)")
ax2.set_ylabel("Wavelength Shift (pm)")
ax2.set_title("Temperature vs Wavelength Shift")
ax2.legend()
ax2.grid(True, alpha=0.3)

st.pyplot(fig2)
plt.close(fig2)


# --------------------------------------------------
# 7. STRAIN CONTRIBUTION GRAPH
# --------------------------------------------------

st.header("3. Strain Effect")

st.write(
    "This graph shows the wavelength shift caused by strain alone."
)

strain_values = np.linspace(0, 2000, 100)

strain_shifts = (
    strain_sensitivity * strain_values
)

fig3, ax3 = plt.subplots(figsize=(9, 4))

ax3.plot(
    strain_values,
    strain_shifts,
    linewidth=2,
    label="Strain-induced Shift"
)

ax3.scatter(
    strain,
    strain_shift,
    s=80,
    label="Current Strain"
)

ax3.set_xlabel("Strain (µε)")
ax3.set_ylabel("Wavelength Shift (pm)")
ax3.set_title("Strain vs Wavelength Shift")
ax3.legend()
ax3.grid(True, alpha=0.3)

st.pyplot(fig3)
plt.close(fig3)


# --------------------------------------------------
# 8. CALCULATION BREAKDOWN
# --------------------------------------------------

st.header("4. Calculation Summary")

st.write("The total wavelength shift is calculated using:")

st.latex(
    r"\\Delta\\lambda_B = K_T\\Delta T + K_\\epsilon\\epsilon"
)

st.write("**Temperature contribution:**")

st.latex(
    rf"{temperature_sensitivity} \\times {temperature}"
    rf" = {temperature_shift:.2f}\\ \\mathrm{{pm}}"
)

st.write("**Strain contribution:**")

st.latex(
    rf"{strain_sensitivity} \\times {strain}"
    rf" = {strain_shift:.2f}\\ \\mathrm{{pm}}"
)

st.write("**Total wavelength shift:**")

st.latex(
    rf"{temperature_shift:.2f} + {strain_shift:.2f}"
    rf" = {total_shift:.2f}\\ \\mathrm{{pm}}"
)

st.write("**New Bragg wavelength:**")

st.latex(
    rf"{reference_wavelength:.3f} + "
    rf"\\frac{{{total_shift:.2f}}}{{1000}}"
    rf" = {new_wavelength:.3f}\\ \\mathrm{{nm}}"
)

st.divider()


# --------------------------------------------------
# 9. THEORY AND ASSUMPTIONS
# --------------------------------------------------

st.header("5. Theory Behind the Simulation")

with st.expander("What is a Fiber Bragg Grating (FBG)?"):
    st.write(
        """
        A Fiber Bragg Grating is an optical fiber sensor containing
        periodic variations in the refractive index of its core.

        It reflects a particular wavelength of light called the
        Bragg wavelength, while other wavelengths pass through.
        """
    )

    st.latex(
        r"\\lambda_B = 2n_{eff}\\Lambda"
    )

    st.write(
        """
        Here:

        - λB = Bragg wavelength
        - neff = Effective refractive index
        - Λ = Grating period
        """
    )

with st.expander("How do temperature and strain affect FBG?"):
    st.write(
        """
        When temperature changes, the refractive index and physical
        grating period can change.

        When strain is applied, the grating period and effective
        refractive index also change.

        These changes cause the reflected Bragg wavelength to shift.
        """
    )

with st.expander("Model Assumptions and Limitations"):
    st.write(
        """
        1. The simulator uses a simplified linear wavelength-shift model.
        2. Temperature and strain contributions are added independently.
        3. Sensitivity coefficients are treated as constant.
        4. The reflection spectrum is represented by an illustrative
           Gaussian curve.
        5. This is a numerical simulation, not a real experimental
           sensor measurement.
        6. A single FBG wavelength measurement cannot independently
           determine two unknowns (temperature and strain) without
           additional information or compensation.
        7. The spectrum is not calculated using Coupled Mode Theory
           or the Transfer Matrix Method.
        """
    )


# --------------------------------------------------
# 10. FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "FBG-Based Temperature and Strain Sensor Simulator | "
    "ECE Photonics Project"
)
