# Channel Menu Overview

The Channel Menu configures per-position (VFO) operating parameters that affect how the radio receives and transmits on the selected frequency or channel.

---

## Bandwidth

Sets the FM receive bandwidth for the active position (VFO).

**Options:**

- **Wide** – 12.5 kHz  
- **Narrow** – 6.25 kHz  
- **Automatic** – Uses the default bandwidth defined by the band plan for the current frequency  

See:
- [Main Menu → Band Plan → Bandwidth](https://github.com/nicsure/RMS880/wiki/Band-Plan-Menu#bandwidth)
- [RMS → Band Plan](https://github.com/nicsure/RMS880/wiki/Band-Plan-Tab)

---

## Modulation

Configures the **receive modulation mode**.

> ⚠️ **Transmission Note**  
> The radio is only capable of native **FM transmission**. When set to **AM** or **USB**, the radio attempts to simulate AM transmission by over-modulation and frequency offset.  
> This may partially work, but results in poor audio quality and significant adjacent-channel interference. **AM transmission is not recommended.**

**Options:**

- **FM**
- **AM**
- **DSB**
- **Automatic** – Uses the default modulation defined by the band plan for the current frequency  

See:
- [Main Menu → Band Plan → Modulation](https://github.com/nicsure/RMS880/wiki/Band-Plan-Menu#modulation)
- [RMS → Band Plan](https://github.com/nicsure/RMS880/wiki/Band-Plan-Tab)
- [Menu → Advanced → AM Hacks](https://github.com/nicsure/RMS880/wiki/Advanced-Menu#am-emulation-notes)

---

## TX CTCSS

Sets the **CTCSS tone** used during transmission (commonly for repeater access).

- Range: **0.1 to 300.0 Hz**
- Exact values (including non-standard tones) may be entered manually  
  - Use `*` to enter a decimal point
- Standard tones can be browsed using `UP/DOWN`

When enabled, a **`CT`** indicator appears on the VFO display.

See:
- [Main Menu → VFO → Tone Monitor](https://github.com/nicsure/RMS880/wiki/VFO-Menu#tone-monitor)

---

## TX DCS

Sets the **DCS code** used during transmission.

- Range: **D001N to D777I**
- Exact values (including non-standard codes) may be entered manually
- Standard codes can be browsed using `UP/DOWN`
- Press `#` to toggle between **normal** and **inverted** polarity

When enabled, a **`DT`** indicator appears on the VFO display.

See:
- [Main Menu → VFO → Tone Monitor](https://github.com/nicsure/RMS880/wiki/VFO-Menu#tone-monitor)

---

## RX CTCSS

Sets the **CTCSS tone required for reception**.

- Range: **0.1 to 300.0 Hz**
- Exact values (including non-standard tones) may be entered manually
- Standard tones can be browsed using `UP/DOWN`
- A special value of `105.0` enables NOAA alert monitoring

When set:
- Squelch will only open if the received signal includes the matching tone
- A **`CR`** indicator appears on the VFO display

See:
- [Radio → NOAA](https://github.com/nicsure/RMS880/wiki/NOAA)
- [Main Menu → VFO → Tone Monitor](https://github.com/nicsure/RMS880/wiki/VFO-Menu#tone-monitor)
- [Main Menu → Calibration → XTAL 671](https://github.com/nicsure/RMS880/wiki/Calibration-Menu#xtal-671)

---

## RX DCS

Sets the **DCS code required for reception**.

- Range: **D001N to D777I**
- Exact values (including non-standard codes) may be entered manually
- Standard codes can be browsed using `UP/DOWN`
- Press `#` to toggle between **normal** and **inverted** polarity

When set:
- Squelch will only open if the received signal includes the matching code
- A **`DR`** indicator appears on the VFO display

See:
- [Main Menu → VFO → Tone Monitor](https://github.com/nicsure/RMS880/wiki/VFO-Menu#tone-monitor)
- [Main Menu → Calibration → XTAL 671](https://github.com/nicsure/RMS880/wiki/Calibration-Menu#xtal-671)

---

## Busy Lock

Controls transmit lockout while a signal is present.

- When **On**, PTT cannot be engaged while a signal is being received
- A received signal may still be present even if squelch is closed due to RX CTCSS/DCS filtering

When enabled, a **padlock** icon appears on the VFO display.

---

## PTT ID

Controls transmission of a **DTMF identification sequence** at the beginning and/or end of a transmission.

The sequence transmitted is defined by **DTMF preset slot #99**.

**Options:**

- **Off** – PTT ID disabled
- **BoT** – Send sequence at the beginning of transmission
- **EoT** – Send sequence at the end of transmission
- **Both** – Send sequence at both beginning and end

When enabled, the standard **PTT-ID icon** appears on the VFO display.

See:
- [RMS → DTMF](https://github.com/nicsure/RMS880/wiki/DTMF-Tab)
- [Radio → Main Menu → DTMF](https://github.com/nicsure/RMS880/wiki/DTMF-Menu)

---

## TX Power

Sets the RF output power for the active position (VFO).

Actual output levels depend on the configured power table.

**Options:**

- **N/T** – No transmit (PTT disabled)
- **ZERO** – Transmit enabled with near-zero output (useful for testing)
- **VLO** – Very low power
- **LOW** – Low power
- **MID** – Medium power
- **HIGH** – High power
- **VHI** – Very high power

This setting is always displayed on the VFO.

> ⚠️ **Note**  
> The band plan may override this setting if a frequency range defines a maximum allowed transmit power.

See:
- [Radio → Main Menu → Band Plan](https://github.com/nicsure/RMS880/wiki/Band-Plan-Menu)
- [RMS → Power](https://github.com/nicsure/RMS880/wiki/Power-Tab)
- [RMS → Band Plan](https://github.com/nicsure/RMS880/wiki/Band-Plan-Tab)

---

## Reversed

Swaps the RX and TX frequencies.

- When active, an **`R`** indicator appears on the VFO display

See:  
[Radio → Main Menu → Reverse RX TX](https://github.com/nicsure/RMS880/wiki/Radio-Mode#reverse-tx--rx)

---

## Clarifier

Applies a fine frequency offset (in kHz) without changing the displayed frequency.

Useful for tuning signals that are slightly off-frequency.

- Use `*` to enter a decimal point
- Use `#` to toggle between positive and negative offset

---

## Scrambler

Applies simple audio scrambling to transmitted and received audio.

When active an `S` icon will appear on the display.

> ⚠️ **Legal Notice**  
> Audio scrambling is **illegal** on amateur and public-access bands in many regions.  
> This feature is intended for **commercial use only** and provides **no real privacy**, as it is easily decoded.

- Adjustable range: **2600 Hz to 4500 Hz**

---

## Channel Name

**Channel and Group modes only.**

Allows customization of the channel name. Because the maximum channel length of 30 characters cannot fit in the menu in a single line, the text is split into two lines of 15 characters.

See:
- [Main Menu → Advanced → Name Scroll](https://github.com/nicsure/RMS880/wiki/Advanced-Menu#name-scroll)
- [Radio → T9 Text Entry](https://github.com/nicsure/RMS880/wiki/T9-Text-Entry)
- [RMS → UI](https://github.com/nicsure/RMS880/wiki/UI-Tab)
- [RMS → Channels](https://github.com/nicsure/RMS880/wiki/Channel-Tab)