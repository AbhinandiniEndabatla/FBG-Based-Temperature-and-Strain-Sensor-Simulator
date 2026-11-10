
import math
from numbers import Real


def calculate_wavelength_shift(
    reference_wavelength_nm,
    delta_temperature_c,
    strain_microstrain,
    temperature_sensitivity_pm_per_c,
    strain_sensitivity_pm_per_microstrain
):

    # Validate that all inputs are numeric and finite
    inputs = {
        "Reference wavelength": reference_wavelength_nm,
        "Temperature change": delta_temperature_c,
        "Strain": strain_microstrain,
        "Temperature sensitivity": temperature_sensitivity_pm_per_c,
        "Strain sensitivity": strain_sensitivity_pm_per_microstrain
    }

    for name, value in inputs.items():
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError(f"{name} must be a numeric value")

        if not math.isfinite(value):
            raise ValueError(f"{name} must be a finite value")

    # Validate reference wavelength
    if reference_wavelength_nm <= 0:
        raise ValueError("Reference wavelength must be positive")

    # Validate sensitivity coefficients
    if temperature_sensitivity_pm_per_c < 0:
        raise ValueError("Temperature sensitivity cannot be negative")

    if strain_sensitivity_pm_per_microstrain < 0:
        raise ValueError("Strain sensitivity cannot be negative")

    # Calculate temperature-induced wavelength shift
    temperature_shift_pm = (
        temperature_sensitivity_pm_per_c * delta_temperature_c
    )

    # Calculate strain-induced wavelength shift
    strain_shift_pm = (
        strain_sensitivity_pm_per_microstrain * strain_microstrain
    )

    # Calculate total wavelength shift
    total_shift_pm = temperature_shift_pm + strain_shift_pm

    # Convert picometres into nanometres
    new_wavelength_nm = (
        reference_wavelength_nm + total_shift_pm / 1000
    )

    # Validate calculated wavelength
    if new_wavelength_nm <= 0:
        raise ValueError("Calculated wavelength must be positive")

    return (
        temperature_shift_pm,
        strain_shift_pm,
        total_shift_pm,
        new_wavelength_nm
    )
