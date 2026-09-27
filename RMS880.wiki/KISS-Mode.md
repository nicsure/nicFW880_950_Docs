# KISS Mode Overview

When **KISS Mode** is enabled, the radio operates as a **TTNC (Transceiver and Terminal Node Controller)**. This mode requires a 38,400 baud serial connection to a host system using the standard programming cable and software capable of communicating via the **KISS protocol**.

See: [Main Menu → APRS → KISS Mode](https://github.com/nicsure/RMS880/wiki/APRS-Menu#kiss-mode)

---

# Operation

When KISS Mode is active, the radio’s display switches to a simplified layout showing:

- A text indicator confirming **KISS Mode** is active  
- The current **working frequency**
- _Settings Values_
  - **TX-Delay** in milliseconds
  - **Persist** probability (0-255)
  - **Slot-Time** delay in milliseconds
  - **TX Power** level
- Debug Messages

---

# Control

### Working Frequency
The working frequency may be changed by keying in a new frequency, using the same method as in [VFO Frequency Mode](https://github.com/nicsure/RMS880/wiki/Radio-Mode#vfo-modes).

### TX-Delay, Persist and Slot-Time
Initially these settings inherit radio mode values
- **TX-Delay** inherits [Main Menu → DTMF → Start Pause](https://github.com/nicsure/RMS880/wiki/DTMF-Menu#start-pause)
- **Persist** inherits [Main Menu → APRS → Persist](https://github.com/nicsure/RMS880/wiki/APRS-Menu#persist--slot-timee)
- **Slot-Time** inherits [Main Menu → APRS → Slot Time](https://github.com/nicsure/RMS880/wiki/APRS-Menu#persist--slot-time)

They can later be adjusted by the HOST using KISS commands.

### TX Power
Inherits the power level of the currently active VFO when KISS mode starts. The level can be changed by pressing the `UP` and `DOWN` buttons on the keypad.

### Backlight
The LCD backlight may be turned off to preserve battery charge by pressing `#`

---

# Note about Audio

Regardless of the setting configured in  
[Main Menu → APRS → Hear Tones](https://github.com/nicsure/RMS880/wiki/APRS-Menu#hear-tones),  
**no audible tones** are produced while operating in KISS Mode, the radio is fully muted.

---

# Packet Handling

- Incoming **AX.25 packets** received on the working frequency are decoded by the radio and forwarded to the host system using standard **KISS encoding**
- The host system may send **KISS-encoded AX.25 packets** to the radio, which are then transmitted on the working frequency

---

# Exiting KISS Mode

To exit KISS Mode and return to normal radio operation, press the **RED** key on the radio.  
THe HOST may also terminate KISS mode by sending the _"Exit"_ KISS command.

---

# More Information

For a technical description of the KISS protocol see the `PDF` link below  
[Kiss-TNC PDF](https://nicsure.github.io/RMS880/kiss-tnc.pdf)
