# NOAA Tone Detection

A special RX CTCSS tone value of **105.0** can be assigned to a channel to enable **NOAA alert-style tone detection**.

When this tone is configured:

- The channel’s squelch remains **closed** until a **1050 Hz tone** is detected on the received signal
- Once detected, the squelch **opens and remains open**
- The squelch will close again when:
  - The signal is lost, or
  - The user manually intervenes

When the channel is tuned to a designated **NOAA weather frequency**, this configuration effectively enables NOAA alert monitoring.

---

## Visual Indicator

When NOAA Tone Detection is active, a **raincloud icon** is displayed on the VFO.

---

## Detection Latency

The radio requires approximately **250 milliseconds** to detect the presence of a tone.

Because NOAA frequencies typically transmit a continuous carrier:
- The radio cannot immediately reject the signal
- It must wait the full detection period to determine whether the tone is present

As a result, when monitoring NOAA frequencies, particularly while **Multiwatch** is enabled, the radio may feel slightly less responsive.

---

## Configuration

See:  
[Radio → Main Menu → RX CTCSS](https://github.com/nicsure/RMS880/wiki/Channel-Menu#rx-ctcss)
