## Band Plan Overview

nicFW provides **20 user-definable band slots** that can be used to define frequency ranges with associated default behavior. Each band slot can specify default modulation and bandwidth settings, which are used by other parts of the firmware when those settings are configured for **Automatic** operation. Band slots may also enforce **maximum transmit power limits** or disable transmit entirely.

When a new frequency is tuned, the band plan slots are evaluated sequentially from **slot 0 through slot 19**. The **first slot** where the tuned frequency lies between the configured `Start` (inclusive) and `End` (non-inclusive) frequencies is selected and applied.

If the tuned frequency does **not** match any configured band slot, a default fallback configuration is used:

- FM modulation  
- Wide bandwidth  
- No power limit  
- No frequency wrapping  

### Default Band Slots

On a newly flashed or factory-reset radio, two band slots are preconfigured:

- **Slot 0:** AM Aircraft Band (108–136 MHz)  
- **Slot 1:** FM Broadcast Band (88–108 MHz)  

Transmit is disabled on both of these bands.

---

## Band Plan Menu

The Band Plan menu allows configuration of individual band slots directly from the radio. While this menu is open, the **Extra Info** field displays information related to the currently selected slot number.

Band slots may also be configured using the RMS application.  
See: [RMS → Band Plan](https://github.com/nicsure/RMS880/wiki/Band-Plan-Tab)

---

### Plan Number

Selects the band slot that will be modified by the other settings in this menu.

- **Range:** 0 to 19

---

### Start

Sets the starting frequency of the selected band.  
This value is **inclusive**.

- **Range:** 18 to 1300 MHz

---

### End

Sets the ending frequency of the selected band.  
This value is **not inclusive**.

- **Range:** 18 to 1300 MHz

---

### Max Power

Defines a maximum transmit power limit for the selected band.  
Setting the value to `N/T` disables transmit entirely for that band.

- **Values:** `N/T`, `ZERO`, `VLOW`, `LOW`, `MID`, `HIGH`, `VHI`  
- **See:** [Main Menu → Channel → TX Power](https://github.com/nicsure/RMS880/wiki/Channel-Menu#tx-power)

---

### Modulation

Sets the default modulation for the selected band.  
This value is used when other modulation settings are configured as `Automatic`.
- Values: `FM` `AM` `DSB`
- **See:**  
  - [Main Menu → Channel → Modulation](https://github.com/nicsure/RMS880/wiki/Channel-Menu#modulation)  
  - [Main Menu → Scanning → VFO Modulation](https://github.com/nicsure/RMS880/wiki/Scanning-Menu#vfo-modulation)

---

### Bandwidth

Sets the default bandwidth for the selected band.  
This value is used when other bandwidth settings are configured as `Automatic`.
- Values: `Wide` `Narrow`
- **See:**  
  - [Main Menu → Channel → Bandwidth](https://github.com/nicsure/RMS880/wiki/Channel-Menu#bandwidth)  
  - [Main Menu → Scanning → VFO Bandwidth](https://github.com/nicsure/RMS880/wiki/Scanning-Menu#vfo-bandwidth)

---

### Wrap

When set to `On`, frequency stepping beyond the limits of the band (using the UP/DOWN keys in frequency mode) will wrap around to the opposite end of the band.

When set to `Off`, stepping past the band limits will continue into adjacent bands.

---

### Name

Allows a custom name of up to **17 characters** to be assigned to the selected band.

- **See:** [Radio → T9 Text Entry](https://github.com/nicsure/RMS880/wiki/T9-Text-Entry)

---

### Save

Changes made within the Band Plan menu are **not automatically saved**.  
Selecting this option writes all changes to flash storage.

- Skipping this step will cause all changes to be lost on power cycle  
- **Note:** The radio must be power-cycled after saving for changes to take full effect
