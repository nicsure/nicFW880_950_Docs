## DTMF Menu Overview

The DTMF menu controls generation, timing, storage, and decoding of Dual-Tone Multi-Frequency (DTMF) signaling. These settings affect manually sent tones, preset sequences, and automatic PTT-ID operation.

Functions specific to DTMF operation are recommended for review:
- [Main Menu → Channel → PTT ID](https://github.com/nicsure/RMS880/wiki/Channel-Menu#ptt-id)
- [Key Functions → DTMF Presets](https://github.com/nicsure/RMS880/wiki/Radio-Mode#dtmf-presets)
- [Key Functions → DTMF SpeedDial](https://github.com/nicsure/RMS880/wiki/Radio-Mode#dtmf-speed-dial)
- [Key Functions → Enter DTMF](https://github.com/nicsure/RMS880/wiki/Radio-Mode#enter-dtmf)
- [Transmit Controls → DTMF](https://github.com/nicsure/RMS880/wiki/Radio-Mode#dtmf-transmission)

DTMF Sequences may also be configured from the RMS  
- See: [RMS → DTMF](https://github.com/nicsure/RMS880/wiki/DTMF-Tab)

---

### Deviation

Sets the transmit level (loudness) of generated DTMF tones.  
Units are specific to the BK4819 radio SoC; refer to the datasheet for conversion to dB.

- **Range:** 0 to 127  
- **Default:** 112

---

### Digit Time

Defines the duration of each individual DTMF digit in a sequence.

- **Range:** 0 to 999 ms  
- **Default:** 100 ms

---

### Gap Time

Defines the silent gap between consecutive DTMF digits in a sequence.

- **Range:** 0 to 999 ms  
- **Default:** 25 ms

---

### Start Pause

Defines the delay between PTT activation and the start of a DTMF sequence.

- **Range:** 0 to 3000 ms  
- **Default:** 1000 ms

---

### Preset

nicFW provides **99 preset slots** for storing pre-programmed DTMF sequences. This menu allows each slot to be populated with a custom sequence.

The **Extra Info** field indicates whether the selected slot is currently assigned.

> **Note:** The key mappings used to enter DTMF sequences differ from normal keypad input.

**Entry Keys:**

- `0–9`, `*`, `#` — Enter themselves  
- `GREEN` — A  
- `UP` — B  
- `DOWN` — C  
- `RED` — D  
- `PTT` — Confirm entry  
- `S2` — Abort entry  

**Special Slot:**

- **Slot 99** is reserved for configuration of the **PTT-ID** sequence.

DTMF presets may also be configured using the RMS application.

- **See:**  
  - [RMS → DTMF](https://github.com/nicsure/RMS880/wiki/DTMF-Tab)  
  - [Key Functions → DTMF Presets](https://github.com/nicsure/RMS880/wiki/Radio-Mode#dtmf-presets)

---

### Decoding

Controls the behaviour of the DTMF decoding system. When enabled, detected DTMF tones in received signals are decoded and displayed on screen.

| Mode | Description |
|-----|------------|
| Off | DTMF decoding disabled |
| On | Standard DTMF decoding |
| P-ID | Enables decoding and displays the name of a matching `Preset` slot when a received sequence matches a stored preset |

- **Default:** Off  
- **See:** [Main Menu → Channel → PTT ID](https://github.com/nicsure/RMS880/wiki/Channel-Menu#ptt-id)

---

### Display For

Defines how long decoded DTMF sequences remain visible on the display after the last tone is detected.

- **Range:** 1 to 99 seconds  
- **Default:** 7 seconds

---

### SeqEnd Pause

Defines the minimum gap between digits that the radio interprets as the **end of a DTMF sequence**. This is used by the PTT-ID matching system described above.

- **Range:** 0.1 to 9.9 seconds  
- **Default:** 1.0 second
