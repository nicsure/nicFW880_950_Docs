# Channels Tab Overview

The **Channels** tab provides advanced tools for configuring and organizing radio channels and channel groups.  
It is the RMS equivalent of the radio’s [Main Menu → CMS](https://github.com/nicsure/RMS880/wiki/CMS-Menu) section, but with significantly expanded capabilities.

---

## Channel List and Selection

On the left side of the tab is a scrollable list displaying all **999 channel slots**.

- Click a channel to select it
- Hold **CTRL** while clicking to select multiple individual channels
- Hold **SHIFT** while clicking to select a continuous range of channels

When **one channel** is selected, all of its settings are displayed in the controls on the right.  

When **multiple channels** are selected, only settings that are **common to all selected channels** are shown. Any setting that differs between channels will appear blank. Editing a setting will set all selected channels at once.

---

## Channel 999
This can be a special channel reserved for APRS use.  
This is the channel to configure with your APRS operating frequency.  
See: [Main Menu → APRS → Enabled](https://github.com/nicsure/RMS880/wiki/APRS-Menu#enabled) 

---

## CHIRP Import and Export

The RMS supports **importing from** and **exporting to** the CHIRP channel CSV format.

### CHIRP Import (CHIRP → RMS)

You may load a CHIRP-format channel `.csv` file into the RMS. When imported:

- The RMS converts the file for use with **nicFW**
- All channels defined in the file from **1 to 999** are loaded
- Channels outside this range are ignored

### CHIRP Export (RMS → CHIRP)

Exporting converts all currently defined channels in the RMS into a CHIRP-format `.csv` file.  
The exported file may then be loaded into **CHIRP** or any other application that supports the CHIRP CSV format.

This makes it easy to move channel data between RMS, CHIRP, and other compatible tools.

---

## Channel List Right-Click Menu

**The channel list provides a context (right-click) menu for managing channels efficiently.**  
Note that actions like **Insert** or **Delete** that shift blocks of channels up or down will not affect channel 999, this channel is always left alone.


### Up

Moves the selected channel(s) up by one slot.


### Down

Moves the selected channel(s) down by one slot.



### Cut

Erases the selected channel(s) and places them into the clipboard.



### Copy

Copies the selected channel(s) into the clipboard without removing them.



### Paste

Overwrites channel slots starting at the selected position with the contents of the clipboard.



### Insert

Shifts all channels from the selected slot **down by one position**, erasing channel **998** if necessary, and leaves the selected slot empty.



### Delete

Erases the selected channel and shifts all subsequent channels **up by one position**, leaving channel **998** empty.



### Sort Ascending / Descending

Reorders a **contiguous block of selected channels** based on RX frequency:

- **Ascending:** Low to high frequency  
- **Descending:** High to low frequency


---

## Channel Settings

For detailed explanations of these settings, see:  
[Main Menu → Channel](https://github.com/nicsure/RMS880/wiki/Channel-Menu)

---

### Active

Must be enabled for a channel to exist.

- Unticking this option effectively erases the channel

---

### Name

A descriptive name for the channel.

- Maximum length: **30 characters**
- The number of visible characters depends on the radio’s UI configuration

When **multiple channels** are selected, the `%` symbol may be used for automatic numbering:

- Example: `PMR %`  
  → Generates `PMR 1` through `PMR 5` for five selected channels
- Example: `GMRS %15`  
  → Starts numbering at 15 instead of 1

See:
- [RMS → UI](https://github.com/nicsure/RMS880/wiki/UI-Tab)
- [Main Menu → CMS → Channel Name](https://github.com/nicsure/RMS880/wiki/CMS-Menu#channel-name)

---

### RX / TX

Defines the receive and transmit frequencies (in MHz).

- Entering an RX frequency automatically updates TX to match, preserving any existing offset

When **multiple channels** are selected, a frequency step may be specified:

- Example: `144.00000+12.5`  
  → RX frequencies increment by 12.5 kHz per channel

For split TX frequencies:

- Absolute TX: enter full frequency (e.g. `146.520`)
- Relative offset:
  - `+1.5` → TX is 1.5 MHz above RX
  - `-2.75` → TX is 2.75 MHz below RX

---

### Clarifier / BFO

Dual-purpose setting:

- **Radio channels:** Fine frequency adjustment in kHz for off-frequency stations
- **Tuner channels:** BFO offset used for SSB and CW reception

---

### RX Tone / TX Tone

Configures receive and transmit squelch subtones.  
If RX Tone is set to the custom value `105.0` this enables [NOAA Tone Detection](https://github.com/nicsure/RMS880/wiki/NOAA) for the channel.

- Supports **CTCSS** and **DCS**
- Standard and non-standard tones may be entered manually
- Right-click the field to select from a predefined list

---

### Groups

Assigns group membership for the channel.

- Up to **four groups** per channel
- Groups are labeled **A–Z**

---

### Modulation

Dual-purpose setting:

- **Radio channels:** FM, AM, DSB, or Automatic  
  - Automatic uses the band plan default
- **Tuner channels:** WFM, AM, USB, LSB, CW

See:
- [RMS → Band Plan](https://github.com/nicsure/RMS880/wiki/Band-Plan-Tab)

---

### Bandwidth

Dual-purpose setting:

- **Radio channels:** Wide, Narrow, or Automatic  
  - Automatic uses the band plan default
- **Tuner channels:** 1–6 kHz

See:
- [RMS → Band Plan](https://github.com/nicsure/RMS880/wiki/Band-Plan-Tab)

---

### TX Power

Sets transmit output power for the channel.

Options:
- `N/T` (No Transmit)
- Zero
- Very Low
- Low
- Medium
- High
- Very High

**Zero** is a special diagnostic mode that performs a transmit cycle with little to no RF output. This is useful for testing transmit functions like PTT-ID or Roger Beep without actually broadcasting with any significant output.

---

### PTT ID

Controls whether the PTT-ID DTMF sequence (DTMF preset slot #99) is transmitted.

Options:
- Off
- Start of TX
- End of TX
- Both

---

### Busy Lock

When enabled, prevents transmission if the channel is currently busy.

---

### Reversed / AM Filter

Dual-purpose setting:

- **Radio channels:** Sets or clears the RX/TX reverse flag  
  - Note: This does *not* swap RX and TX values in the RMS; it only toggles the flag
- **Tuner channels:** Enables or disables the Si4732 power line filter

---

### Scrambler

Selects the split-and-invert frequency used by the built-in voice scrambler.

- Applied to transmitted audio
- Decoded on receive when enabled

> **Note:** Scrambling may be illegal on amateur or public-access bands. Use responsibly.
