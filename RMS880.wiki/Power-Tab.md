# Power Tab Overview

The **Power** tab provides advanced control over the radio’s RF output characteristics. It allows experienced users to fine-tune the **five transmit power levels** across different frequency ranges.

The available power levels are:

- Very Low  
- Low  
- Medium  
- High  
- Very High  

See [Main Menu → Channel → TX Power](https://github.com/nicsure/RMS880/wiki/Channel-Menu#tx-power)

---

## Frequency Slots

Frequency coverage is divided into **5 MHz slots**, spanning from **0 MHz to 1300 MHz**. These slots are listed on the left side of the interface.

You do **not** need to configure every slot. When transmitting, the radio automatically selects the **closest configured slot** relative to the tuned frequency. In practice, assigning a single slot near the centre of the band you wish to adjust is usually sufficient.

---

## Power Parameters

Once a frequency slot is selected, the following parameters can be adjusted independently for each of the five power levels.

### Bias

Controls the power amplifier (PA) bias voltage.

- Range:
  - `0` = 0.0 V  _to_
  - `255` = 3.2 V  


### Gain 1 & Gain 2

Adjusts the RF gain tuning stages used by the power amplifier.

- Range: 0 to 7

### Technical Info

The Bias and Gain values map directly to internal BK4819 registers. Refer to the [BK4819 Application Notes](https://nicsure.github.io/RMS880/BK4819ApplicationNote1.0.pdf), specifically **Register 0x36**.

---

## Usage Notes

Correctly tuning these values requires **experimentation and measurement** using appropriate test equipment, such as a **dummy load** and **power meter**.

For most users, it is strongly recommended to **retain the default values** provided after a fresh firmware flash or factory reset. Improper configuration can result in poor performance, distortion, or hardware stress.
