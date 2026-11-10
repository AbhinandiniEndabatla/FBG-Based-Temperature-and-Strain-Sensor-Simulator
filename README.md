# FBG-Based Temperature and Strain Sensor Simulator

## 1. Project Overview

The **FBG-Based Temperature and Strain Sensor Simulator** is a Python-based application that demonstrates how temperature variations and mechanical strain affect the Bragg wavelength of a Fiber Bragg Grating (FBG) sensor.

A Fiber Bragg Grating is an optical fiber sensor that reflects a specific wavelength of light, known as the Bragg wavelength. When temperature or strain changes, the grating properties change, resulting in a shift in the reflected wavelength.

This project uses a mathematical model to calculate the wavelength shift caused by temperature and strain. The calculated results are displayed through an interactive dashboard developed using Streamlit.

The project provides a simple way to understand the working principle of FBG sensors without requiring physical optical fiber sensing hardware.

## 2. Objectives

The main objectives of this project are:

- To understand the working principle of Fiber Bragg Grating sensors.
- To simulate the effect of temperature variations on the Bragg wavelength.
- To simulate the effect of mechanical strain on the Bragg wavelength.
- To calculate the combined wavelength shift caused by temperature and strain.
- To visualize wavelength changes using graphs.
- To develop an interactive dashboard for exploring different sensor conditions.

## 3. Features

The application provides the following features:

- **Reference Wavelength:** Allows the user to specify the initial Bragg wavelength.
- **Temperature Simulation:** Calculates the wavelength shift caused by temperature variations.
- **Strain Simulation:** Calculates the wavelength shift caused by applied strain.
- **Combined Effect:** Calculates the total wavelength shift due to both temperature and strain.
- **Interactive Dashboard:** Allows users to modify input parameters.
- **Reflection Spectrum Visualization:** Displays the original and shifted wavelength peaks using an illustrative Gaussian spectrum.
- **Temperature Contribution Graph:** Shows the wavelength shift caused by temperature.
- **Strain Contribution Graph:** Shows the wavelength shift caused by strain.
- **Input Validation:** Checks for invalid numerical inputs and physically invalid wavelength values.
- **Unit Testing:** Includes four test cases to verify the mathematical calculations.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Interactive web dashboard |
| NumPy | Numerical calculations and array generation |
| Matplotlib | Graphs and spectrum visualization |
| Unittest | Testing the mathematical model |

## 5. Working Principle

An FBG consists of periodic variations in the refractive index of the optical fiber core. These variations form a grating that reflects a particular wavelength of light.

The reflected wavelength is called the Bragg wavelength.

The Bragg wavelength is given by:

\[
\lambda_B = 2n_{\mathrm{eff}}\Lambda
\]

Where:

- \(\lambda_B\) = Bragg wavelength
- \(n_{\mathrm{eff}}\) = Effective refractive index
- \(\Lambda\) = Grating period

When temperature or mechanical strain is applied, the effective refractive index and grating period change. This causes a shift in the Bragg wavelength.

The simulator uses a simplified linear relationship to calculate this shift.

\[
\Delta\lambda_B =
K_T\Delta T + K_\epsilon\epsilon
\]

Where:

- \(\Delta\lambda_B\) = Total wavelength shift in picometres
- \(K_T\) = Temperature sensitivity in pm/°C
- \(\Delta T\) = Temperature change in °C
- \(K_\epsilon\) = Strain sensitivity in pm/µε
- \(\epsilon\) = Applied strain in microstrain

The new Bragg wavelength is calculated as:

\[
\lambda_{\mathrm{new}} =
\lambda_{\mathrm{reference}}+
\frac{\Delta\lambda_B}{1000}
\]

The division by 1000 converts the wavelength shift from picometres to nanometres.

## 6. Default Simulation Parameters

The application uses the following illustrative default values:

| Parameter | Default Value |
|---|---:|
| Reference wavelength | 1550 nm |
| Temperature change | 30 °C |
| Applied strain | 500 µε |
| Temperature sensitivity | 10.3 pm/°C |
| Strain sensitivity | 1.2 pm/µε |
| Illustrative spectrum FWHM | 0.2 nm |

These sensitivity coefficients are example values used for simulation. Actual values depend on the FBG sensor and its operating conditions.

## 7. Sample Calculation

For the default input values:

Temperature-induced wavelength shift:

\[
\Delta\lambda_T=10.3\times30=309\text{ pm}
\]

Strain-induced wavelength shift:

\[
\Delta\lambda_\epsilon=1.2\times500=600\text{ pm}
\]

Total wavelength shift:

\[
\Delta\lambda_B=309+600=909\text{ pm}
\]

New Bragg wavelength:

\[
\lambda_{\mathrm{new}}=1550+\frac{909}{1000}
\]

\[
\boxed{\lambda_{\mathrm{new}}=1550.909\text{ nm}}
\]

## 8. Project Structure

```text
FBG_PROJECT/
│
├── app.py
├── fbg_model.py
├── test_fbg_model.py
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
└── .venv/
```

**File descriptions:**

- `app.py`: Contains the Streamlit application, input controls, calculations display and graphs.
- `fbg_model.py`: Contains the mathematical model used to calculate temperature-induced, strain-induced and total wavelength shifts.
- `test_fbg_model.py`: Contains unit tests to verify the correctness of the mathematical model.
- `requirements.txt`: Lists the Python libraries required to run the application.
- `README.md`: Provides project information and instructions.
- `PROJECT_REPORT.md`: Contains the detailed technical documentation of the project.
- `.venv/`: Python virtual environment used for the project.

## 9. Installation and Setup

### Step 1: Install Python

Install Python 3.10 or a compatible newer version.

### Step 2: Open the Project Folder

Open the project folder in Visual Studio Code.

### Step 3: Create a Virtual Environment

Open the VS Code terminal and execute:

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

## 10. Running the Application

After installing the required libraries, execute:

```bash
streamlit run app.py
```

The Streamlit application will open in the browser.

If it does not open automatically, visit:

```text
http://localhost:8501
```

Use the sidebar controls to change the reference wavelength, temperature, strain and sensitivity coefficients.

The dashboard will display the calculated wavelength shifts and corresponding graphs.

## 11. Running Unit Tests

The project includes four unit tests to verify the mathematical model.

Run the following command in the VS Code terminal:

```bash
python -m unittest -v
```

The four test cases are:

1. Zero temperature and zero strain.
2. Temperature-only wavelength shift.
3. Strain-only wavelength shift.
4. Combined temperature and strain wavelength shift.

All four test cases have been executed successfully.

Expected result:

```text
Ran 4 tests

OK
```

## 12. Limitations

- The simulator uses a simplified linear mathematical model.
- The temperature and strain sensitivity coefficients are assumed to be constant.
- The displayed reflection spectrum is an illustrative Gaussian representation and not a complete physical FBG spectrum.
- The simulator does not currently implement Coupled Mode Theory or the Transfer Matrix Method.
- No physical FBG sensor or experimental laboratory measurements are used.
- A single wavelength measurement cannot independently determine both unknown temperature and strain without additional information or compensation.

## 13. Future Scope

The project can be extended in the following ways:

- Implementing Coupled Mode Theory for more detailed FBG spectrum modelling.
- Implementing the Transfer Matrix Method.
- Adding temperature compensation techniques.
- Studying the effect of different grating parameters.
- Comparing simulated results with experimental FBG sensor measurements.
- Extending the simulator to support additional sensing parameters.

## 14. Conclusion

The FBG-Based Temperature and Strain Sensor Simulator demonstrates how temperature variations and mechanical strain influence the Bragg wavelength of a Fiber Bragg Grating sensor.

The application combines mathematical modelling, numerical computation and interactive visualization to provide an understandable representation of FBG sensing behaviour.

The project successfully calculates individual and combined wavelength shifts and displays the results through an interactive Streamlit dashboard. The mathematical model has also been verified using four successful unit tests.

This project provides a foundation for further exploration of optical fiber sensors and advanced FBG simulation techniques.

## 15. References

1. K. O. Hill and G. Meltz, "Fiber Bragg Grating Technology Fundamentals and Overview," Journal of Lightwave Technology, Vol. 15, No. 8, 1997, pp. 1263–1276.

2. A. D. Kersey et al., "Fiber Grating Sensors," Journal of Lightwave Technology, Vol. 15, No. 8, 1997, pp. 1442–1463.