## Calibration Tab Overview

The **Calibration** tab contains radio-specific settings used to fine-tune behaviour that can vary slightly between individual devices due to manufacturing tolerances.

These settings are intended for **advanced users** and should be adjusted with care.

---

## Battery and Oscillator Options

Battery calibration and oscillator calibration options mirror those available on the radio itself and are documented in the Radio Mode manual.

See:  
- [Main Menu → Calibration](https://github.com/nicsure/RMS880/wiki/Calibration-Menu)

---

## Band (Hz Offset)

Band offset calibration is **only configurable through the RMS**.

These settings apply a fine-grained **frequency correction in Hertz** on a per-band basis. Each band spans a **50 MHz range**, starting at **0 MHz** and extending up to **1300 MHz**.

The defined offset is applied to **all frequencies** that fall within the selected band.

### Example

Setting a value of `-300` in the band labelled **`<150 MHz`** applies a **−300 Hz frequency correction** to any tuned frequency between 145 MHz and 150 MHz.

This feature allows precise correction for band-specific frequency drift that cannot be accurately resolved using a single global oscillator adjustment.

---

## RSSI Floors

Defines the signal floor for specific frequency ranges. These floor values are used as the reference point for calculating S-meter readings.

Because receiver sensitivity can vary slightly across different frequency bands, nicFW allows separate floor values to be configured per range. Setting these correctly ensures that S-meter readings are consistent and meaningful across the spectrum.

The values entered here correspond to the **internal register units of the BK4819**.

### Converting to dBm

To convert the configured value to dBm:

1. Divide the value by **2**
2. Subtract **160**

**Example**

For a setting of `100`:

- `100 ÷ 2 = 50`  
- `50 − 160 = -110 dBm`

So a value of **100** corresponds to **–110 dBm**.

### S-Meter Scaling

Each **S-Unit** on the signal meter represents **6 dBm above the configured noise floor** defined in this section.

Accurate floor calibration ensures that:
- S-meter readings align with expected signal strengths  
- S-levels remain consistent across different frequency bands  

The radio will display the current received signal level in the same units while the [Squelch](https://github.com/nicsure/RMS880/wiki/Squelch-Menu) menu is open. This can be useful for quick reference.
