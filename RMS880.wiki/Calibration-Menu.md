# Calibration Menu Overview

The Calibration Menu provides tools for calibrating battery measurements and correcting oscillator frequency error.

While this menu is open, the *Extra Info* field displays live diagnostic values to assist with calibration.

Calibration values can be set via the RMS. See [RMS → Calibration](https://github.com/nicsure/RMS880/wiki/Calibration-Tab)


---

## Batt V Cal

Calibrates the displayed battery voltage.

To set this value correctly:

1. Fully charge the battery
2. Adjust this value until the battery voltage shown in the *Extra Info* field reads **8.4 V**

This value is typically around **970**, but may vary slightly between radios.

---

## Batt Full

Defines the ADC value corresponding to a fully charged battery.

To calibrate:

1. Fully charge the battery
2. Note the **ADC** value shown in the *Extra Info* field
3. Set **Batt Full** to match that ADC value

This value is typically around **1400**, but may vary slightly between radios.

---

## Batt Flat

Defines the ADC value at which the battery is considered discharged.

This is typically the point where:
- The radio still powers on
- Transmission is no longer possible due to insufficient battery voltage

To calibrate:

1. Allow the battery to discharge to this flat state
2. Note the **ADC** value shown in the *Extra Info* field
3. Set **Batt Flat** to match that ADC value

This value is typically around **1000**, but may vary significantly between radios.

---

## Batt Low

Defines the ADC threshold at which the battery is considered **low**.

This level typically corresponds to the point where:

- The radio can still transmit  
- However, available battery capacity is nearly exhausted

To calibrate:

1. Allow the battery to discharge until it reaches the desired *low* state.
2. Note the **ADC value** shown in the **Extra Info** field.
3. Set **Batt Low** to match that ADC value.

This value is typically around **1050**, but may vary significantly between radios.

---

## Low Alarm

When enabled, an audible alert will sound **every 60 seconds** if the battery level is below the threshold defined by **Batt Low**.
If the battery level falls below **Batt Flat**, the audible alert will sound for **twice the normal duration**, providing a more urgent warning that the battery is critically low.

- This alarm also sounds if PTT is pressed while the battery is in a low state, however the PTT alarm sounds regardless of if this setting is enabled or not.

---

## XTAL 671

Compensates for manufacturing tolerances in the radio’s base crystal oscillator.

The reference oscillator should ideally produce **26.000000 MHz**, but in practice it will always be slightly high or low. This error is multiplied as operating frequency increases.

### Why this matters

Frequency error scales with frequency multiplication. For example:

- Target frequency: **442 MHz**
- Oscillator frequency: **25.99970 MHz**
- Multiplier: **17**
- Actual tuned frequency: **441.99490 MHz**

This results in a **5.1 kHz** error.

This is by far the most common cause of “non-bug” reports where:
- RX CTCSS fails to open squelch
- RX DCS fails entirely

CTCSS generally requires accuracy within **~1 kHz**, and DCS within **~500 Hz**, making proper calibration essential.

---

## XTAL 671 Quick Calibration Procedure

### Requirements

- A trusted reference signal:
  - Another radio known to be accurately on frequency, **or**
  - An external signal generator
  - A known accurate signal, such as from a repeater.
- The signal must transmit **CTCSS or DCS**
- Higher frequencies yield better accuracy

---

### Step-by-Step Calibration

1. Ensure [Main Menu → Advanced → Hunt STones](https://github.com/nicsure/RMS880/wiki/Advanced-Menu#hunt-stones) is turned off.

2. Acquire a trusted signal source, this can be from another radio, a signal generator or a broadcast source such as a repeater. This signal source must be sending a valid CTCSS or DCS.

3. Configure the VFO:
   - Set **RX CTCSS** or **RX DCS** to match the test signal
   - Set [Main Menu → VFO → Step](https://github.com/nicsure/RMS880/wiki/VFO-Menu#step) to **0.01 kHz**
   - Tune to the target frequency  
     Example: **450.00000 MHz**

4. Using `UP/DOWN`, adjust the frequency until squelch opens reliably.

5. Find the **lower limit**:
   - Step **down** until squelch no longer opens  
   Example: `450.00020 MHz`

6. Find the **upper limit**:
   - Step **up** until squelch no longer opens  
   Example: `450.00050 MHz`

7. Calculate the midpoint frequency:
   - (Lower + Upper) / 2  
   Example: (450.00020 + 450.00050) / 2 = 450.00035 MHz

8. Calculate frequency drift:
   - Drift = (Midpoint − Target) × 100,000  
   Example: (450.00035 − 450.00000) × 100,000 = 35
     - Note: The resulting value may be negative.

9. Calculate XTAL 671 value:
   - (Drift × 671) / Target Frequency  
   Example: (35 × 671) / 450 = 52.19 → 52

10. Set **XTAL 671** to **52**

---

### Notes

- If the calculated value is **negative**, enter it as a positive number and press `#` to flip the sign.

Proper XTAL calibration ensures reliable CTCSS/DCS decoding and accurate frequency display across all bands.

---

## Common Whinges

Q: My radio was on-frequency with the factory firmware, why is it off with nicFW?

A: When these radios are manufactured, each one can be tested on the production line and calibration data written to the radio's stock settings. I cannot do that can I? And I have no idea where this data is stored or what format it is in. So calibration has to be performed by the user, I cannot visit each one of you personally to tune your radios or use a time machine, teleport to China and insert myself into the factory to secretly write my own calibration data to new radios.

---

## Common Questions

**Q:** Why 671? That seems rather arbitrary.

**A:** It is anything but arbitrary. The value **671** was chosen for a very specific and practical reason.

To accurately correct oscillator drift, the calibration math requires a reference point. Several factors influenced the choice of this reference:

- Higher reference frequencies provide better adjustment resolution
- Values that are easy for processors to work with are preferred, especially powers of two
- A frequency close to a whole MHz simplifies user-side calculations
- The value must align cleanly with the radio’s internal frequency representation

Internally, the radio represents frequencies in **10 Hz units**.  
For example, a frequency of 423.12600 MHz is stored as the integer 42,312,600.

Now consider the frequency **671.08864 MHz**.

This value meets all of the design goals:

- It is reasonably high in frequency
- It is very close to a round MHz value (671 MHz)
- Internally it becomes 67,108,864
- 67,108,864 is a power of two

Perfect.

That is why the calibration constant is **671**.
