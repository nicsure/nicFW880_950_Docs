# VFO Menu Overview

The VFO Menu contains settings that control frequency stepping, transmission behavior, audio handling, and multi-VFO operation for the active position.

---

## Step

Sets the frequency step size, in kHz, used when adjusting the VFO frequency with the `UP/DOWN` keys in Frequency Mode.

This value also determines:
- The spacing between bars in the Spectrum Scope
- The scanning interval used during VFO frequency scans (default scan key: `LP-4`)

**Default value:** `12.50 kHz`

---

## TX Timeout

Sets the maximum continuous transmission time, in seconds.

- A value of **0** disables the timeout and allows indefinite transmission

**Default value:** `120 seconds`

---

## Mic Gain

Adjusts the sensitivity of the radio’s microphone.

- Range: **0** (minimum gain) to **31** (maximum gain)
- This is a relative level with no physical unit

**Default value:** `25`

---

## MultiWatch
**Values:** `Off`, `On`, `Group`  
**Default value:** `Off`

When enabled, the radio continuously monitors all three VFOs.

Behaviour:
- Upon receiving a signal, the radio switches to the detected VFO
- After the signal ends, the radio either:
  - Remains on the detected VFO, or
  - Returns to the previously active VFO after the time defined by **MW Pause**
    - Note: if any user interaction occurs before this time elapses, the selection will remain on the detected VFO.
    - This behaviour is controlled by **MW Keep VFO**.
  - If the VFO being checked is in [Group Mode](https://github.com/nicsure/RMS880/wiki/Radio-Mode#vfo-modes), **Multiwatch** is set to `Group` and **G-Watch VFOs** permits the VFO to operate in Group-Watch mode, then all channels in the VFO's selected group will also be watched.
    - This function is best used with smaller groups. Since each channel in the group must be scanned individually, larger groups will increase the scan cycle time and may significantly impact signal detection latency.

Multiwatch only monitors VFOs that are of the same HF or non-HF band. I.e. if the active VFO is set to a frequency over 70 MHz then only VFOs that are also over 70 MHz will be monitored. Similarly if the active VFO is less than 70 MHz only other VFOs that are also less than 70 MHz will be monitored.

A **circular arrow** icon is displayed when MultiWatch is active.  
If this setting is set to `Group` then the icon will have a letter `G` inside it.

### Multiwatch Suspension
Certain conditions will cause Multiwatch to temporarily stop functioning. When suspended, the icon changes (_greyed-out circular arrows with a line through them_) to indicate this state.  
This happens when:

- A user interaction occurs (not PTT) or a signal is received.

  - Multiwatch resumes after the period of time defined in [MW Pause](https://github.com/nicsure/RMS880/wiki/VFO-Menu#mw-pause-multiwatch-pause)

- The radio is placed into transmit mode.

  - Once transmission is over, Multiwatch resumes when:

    - The user presses a key.

    - After 30 seconds of no signal reception.

---

## G-Watch VFOs (MultiWatch Group Mode VFOs)

Values: `A Only`, `B Only`, `A And B`, `C Only`, `C And A`, `C And B`, `All`  
Default: `All`

Selects which VFOs will perform group watch operations when **MultiWatch** is set to `Group` mode.

---

## G-Watch Fast

**Values:** `On`, `Off`  
**Default:** `On`

Controls the scan priority used during Group Watch operation.

When set to `On`, Group Watch prioritizes scanning the channels within the selected group over the other VFOs and APRS-999. This improves signal detection speed for larger groups but results in slower response times for the single VFOs and APRS-999.

When set to `Off`, the other single VFOs and APRS-999 are scanned more frequently, keeping them more responsive. The trade-off is that signal detection within the watched group slows down by approximately four times.

---

## MW Pause (MultiWatch Pause)

Defines the delay, in seconds, after a signal loss or user interaction before **MultiWatch** resumes scanning all VFOs.

**Default value:** `2.0 seconds`

---

## MW Keep VFO

Controls which VFO remains active after a detected signal from **MultiWatch** is lost.

- **On**  
  The detected VFO remains active after the signal ends.

- **Off**  
  The radio returns to the previously active VFO after the delay defined by **MW Pause**.
    - Note: if any user interaction occurs before this time elapses, the selection will remain on the detected VFO.

**Default value:** `Off`

---

## VOX Level

Enables and configures **VOX (Voice-Operated Transmit)**, allowing transmission without pressing PTT.

When active a `Speech Bubble` icon is shown on the display.

- Transmission occurs on the currently active VFO
- **Off** disables VOX
- Values **1–15** enable VOX
  - `1` = least sensitive
  - `15` = most sensitive

**Default value:** `Off`

---

## VOX Tail

Defines how long, in seconds, a VOX-triggered transmission continues after the user stops speaking.

**Default value:** `2.0 seconds`

---

## Tone Monitor

When enabled, any received signal containing a **CTCSS tone or DCS code** will display the detected tone/code on the screen.
When set on `Clone` in addition to displaying the detected tone, the active VFO will automatically set its TX Tone to match.

Please use `Clone` sparingly as it will overwrite your TX subtone settings for whatever channel you're tuned to. You'll be scratching your head as to why all your channels have different CTCSS/DCS settings from what you originally programmed.

*Vales:* `Off`, `On`, `Clone`  
**Default value:** `Off`

See:
- [Main Menu → Channel → TX Subtones](https://github.com/nicsure/RMS880/wiki/Channel-Menu#tx-ctcss)
- [Main Menu → Advanced → Tone Monitor Time](https://github.com/nicsure/RMS880/wiki/Advanced-Menu#tone-monitor-time)

---

## Key Frequency

Controls audible keypress feedback.

- **Off** disables key beeps
- When enabled, the value defines the beep frequency in Hz

**Default value:** `Off`

---

## Roger Beep

Controls transmission of a terminating **roger beep** when a transmission ends.

When active a `Music Note` icon is shown on the display.

- **Off** disables the roger beep
- Values from **1 to 9999** define the beep pattern

The pattern consists of a sequence of short tones (musical notes):
- Each digit represents a musical note.
  - 0 - B4
  - 1 - C5
  - 2 - D5
  - ..
  - 8 - C6
  - 9 - D6
- Tones are played in **reverse order**

**Examples:**
- `1234` → `F5 E5 D5 C5`
- `582` → `D5 C6 G5`
- `9` → `D6`

**Default value:** `Off`

---

## Roger Beep Time

Defines the duration, in milliseconds, of each tone in the roger beep pattern.

**Default value:** `100 ms`

---

## Multi PTT

Configures how PTT buttons map to VFOs.

- **Off**  
  Only the main (top) PTT button transmits on the currently active VFO.

- **On**  
  All three side buttons function as PTT buttons:
  - Top button → **VFO A**
  - Middle button → **VFO B**
  - Bottom button → **VFO C**

> ⚠️ **Note**  
> When Multi PTT is enabled, the short-press and long-press key functions assigned to **S1** and **S2** are unavailable.
>
> When using S1 or S2 for transmitting, the main PTT button becomes the key to send a repeater tone.  
> See: [Radio Operation → Repeater Tone](https://github.com/nicsure/RMS880/wiki/Radio-Mode#side-key-s2--repeater-tone)

**Default value:** `Off`
