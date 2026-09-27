## Tuner Mode Overview

Tuner Mode is a receive-only operating mode that utilizes the highly flexible **Si4732 tuner chip** built into the RT-880. This mode supports reception of **Broadcast FM**, **Long Wave (LW)**, **Medium Wave (MW)**, and **Short Wave (SW)** radio bands.  
Some bands require the use of a **secondary antenna**, as detailed below.

---

### Available Bands

| Band | Frequency Range | Modulation | Antenna |
|-----|-----------------|------------|---------|
| Broadcast FM | 64 – 108 MHz | Wideband FM | Primary Antenna |
| Long Wave (LW) | 103 – 522 kHz | AM / USB / LSB / CW | Secondary Antenna |
| Medium Wave (MW) | 530 – 1700 kHz | AM / USB / LSB / CW | Secondary Antenna |
| Short Wave 1 | 1.700 – 6.000 MHz | AM / USB / LSB / CW | Secondary Antenna |
| Short Wave 2 | 6.000 – 12.000 MHz | AM / USB / LSB / CW | Secondary Antenna |
| Short Wave 3 | 12.000 – 30.000 MHz | AM / USB / LSB / CW | Secondary Antenna |

Regionally, the Long Wave band can have different step points. This can be fixed by defining the start of the band.  
See: [Main Menu → Advanced → LW Start](https://github.com/nicsure/RMS880/wiki/Advanced-Menu#lw-start)

---

### Spectrum Scope

Tuner Mode can optionally display a **spectrum scope** showing activity around the tuned frequency while simultaneously receiving audio. This feature has several important limitations:

- On the **FM Broadcast band**, the scope functions correctly using only a single antenna.
- On **Short Wave 3**, the scope requires **dual antennas** and only operates correctly on frequencies **above 18 MHz**.
- The spectrum scope uses the **BK4819 radio SoC** to scan surrounding frequencies rather than the Si4732 tuner.

Because of this architecture, enabling the scope may introduce **audible interference**. The scope can be disabled if this interference becomes undesirable (see controls below).

---

### MultiWatch Interaction

If **MultiWatch** is enabled in Radio Mode, Tuner Mode reception may be interrupted:

- When a signal on the radio side opens squelch, tuner reception is paused.
- Once the signal is lost, operation automatically returns to Tuner Mode.

This functionality is **only available when the Spectrum Scope is disabled**, as the scope requires exclusive use of the radio-mode chip.

---

### Signal Meter

Tuner Mode uses the same **signal strength meter** as Radio Mode to display received signal strength. However, due to limitations of the Si4732:

- No noise bar is available
- No dBm readout is provided

Signal meter updates may also introduce audible interference (typically perceived as periodic beeping). The signal meter can be disabled if required (see controls below).

---

### RDS

The Si4732 supports RDS in FM Broadcast mode. Data such as the station name, category and status text will be displayed on screen when it is received. RDS Data is also used to set the radio's clock.

---

### Channels
The tuner mode supports channels just like the radio mode does. These channels can be programmed via the RMS or directly by the radio by opening the `Main Menu`  
See:
- [RMS → Channels](https://github.com/nicsure/RMS880/wiki/Channel-Tab)
- [Main Menu → CMS](https://github.com/nicsure/RMS880/wiki/CMS-Menu)
- [SP-RED](#sp-red)

---

## Controls

### Numeric Keys (0–9)

- **Frequency Mode:** Initiates entry of a new frequency
- **Channel Mode:** Initiates entry of a new channel number
- In **SW modes**, entering a frequency outside the current band automatically switches to the appropriate band (if applicable)

Additional entry keys:
- `*` — Enter a decimal point  
- `GREEN` or `#` — Confirm entry  
- `RED` — Abort entry  

---

### UP / DOWN

- Steps the tuned frequency up or down by the current **Step** value in Frequency Mode
- Stepping beyond the limits of the current band **wraps around** to the opposite end
- In Channel Mode, steps between programmed **Tuner Channels**

---

### `*` and `#` — BFO Adjustment

USB, LSB, and CW modes only.

- Adjusts the **BFO fine-tune (clarifier)**
  - `*` increases the offset
  - `#` decreases the offset
- Short press adjusts by one step
- Long press continuously steps

The current BFO value is displayed at the bottom of the display as `BFO: +000`.

---

### SP-GREEN
Opens the **Main Menu**

---

### LP-GREEN
Opens the **Tuner Function Menu**, which lists all available tuner functions along with their associated key presses.

- Functions may also be executed by selecting them and pressing `GREEN`
- Press `RED` to close the function menu

---

### LP-2 — Reset BFO
Resets the BFO fine-tune value back to zero.

---

### SP-RED
Toggles between **Frequency Mode** and **Channel Mode**.

- Tuner channels share the same 999 slots as Radio Mode channels
- Channels are **specific to Tuner Mode**
- At least one Tuner Channel must be programmed to switch to Channel Mode

---

### LP-3 — Seek Forward
Frequency Mode only.

Steps upward through frequencies until a sufficiently strong signal is detected.

- Works on all bands
- Most effective on the **FM Broadcast band**
- Limited effectiveness on LW, MW, and SW bands

---

### LP-1 — Seek Reverse
Same as Seek Forward, but in the opposite direction.

---

### LP-4 — Set Step
Allows entry of a new frequency step value.

The current step size is displayed at the bottom of the display as `Step: X kHz`.

---

### LP-5 — Signal Meter On / Off
Toggles the signal meter.

- When enabled, periodic meter updates may cause audible interference
- Interference is more noticeable on lower bands
- Usually not present on the FM Broadcast band

---

### LP-6 — Squelch On / Off
Enables or disables an automatic noise-gating system.

- Cuts static on empty frequencies
- Displays an `S` icon when active
- Works best on the FM Broadcast band
- Not recommended for sideband or CW reception

---

### LP-7 — Spectrum Scope On / Off
Enables or disables the spectrum scope.

- Disabling the scope eliminates scope-related audio interference
- Also reduces display clutter for users who find it distracting

---

### LP-8 — Power Line Filter On / Off
Toggles the Si4732 built-in **Power Line Filter**, which attempts to reduce interference from mains power lines.

The current state is displayed as `PLF: On` or `PLF: Off`.

---

### LP-9 — Toggle Bandwidth
AM reception only.

Cycles through available AM bandwidths from **1 kHz to 6 kHz**.

The current bandwidth is displayed as `BW: X kHz`.

---

### SP-EMG
Toggles between **Day** and **Night** display modes.  
Duplicate function of [Key Functions → Day / Night Mode](https://github.com/nicsure/RMS880/wiki/Radio-Mode#day--night-mode).

---

### LP-RED
Exits Tuner Mode and returns to Radio Mode.

---

### LP-0 — Spirit Box
Rapid audio cycling of the entire band.

This is not a scan; the tuner steps through the band as quickly as possible at the current step rate, providing a fast audio sweep. Useful for estimating band activity and locating potentially interesting signals.

This feature also replicates the function of the so called "Spirit Talker" device, a complete load of nonsense, but what the hell.

---

### SP-S1
Cycles between available bands: **FM, LW, MW, SW1, SW2, SW3**.  
The band name is displayed above the tuned frequency.

---

### SP-S2
Cycles between demodulation modes: **AM, USB, LSB, CW**.

- Has no effect on the FM Broadcast band
- The current modulation mode is displayed under the tuned frequency
