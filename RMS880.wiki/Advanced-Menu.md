# Advanced Menu Overview

As the name implies, these are advanced settings intended for power users. It is strongly recommended that you become familiar with nicFW before making changes in this menu. *Here be dragons*.

---

## Repeater Tone

While transmitting, pressing side button **S2** will send a repeater access tone. This setting defines the frequency of that tone in Hz.

- **Default:** 1750 Hz  
- **See:** [Operating Modes → Radio → Transmit Controls](https://github.com/nicsure/RMS880/wiki/Radio-Mode#transmit-controls)

---

## TX Deviation

Sets the FM deviation width using the native units of the BK4819 radio SoC. Refer to the BK4819 datasheet for exact bandwidth conversion.

Most manufacturers using the BK4819 set this value to **64**, which is also the default. Beta testing suggests **70** is the upper practical limit before over-deviation becomes problematic.

Increasing this value effectively increases global TX audio gain, but it affects **all** transmitted audio, including tones, beeps, DTMF, CTCSS, and DCS.

- **Range:** 0–99  
- **Default:** 64

---

## Subtone Deviation

Controls how “loud” the transmitted CTCSS and DCS tones are. Increasing this value can help open repeaters in noisy environments.

Units are specific to the BK4819; refer to the datasheet for dB equivalents.

- **Range:** 0–127  
- **Default:** 74

---

## SPI Deferral _(RT-880 Only)_

Defines how long configuration and state changes remain cached before being written to persistent storage.

- **Range:** 0–250 seconds  
- **Default:** 10 seconds  
- **See:** [Radio → Storage Deferral](https://github.com/nicsure/RMS880/wiki/Storage-Deferral)

---

## Tone Monitor Time

Sets how long the detected tone readout remains visible after the signal or tone is lost.

- **Range:** 2–99 seconds  
- **Default:** 7 seconds  
- **See:** [Main Menu → VFO → Tone Monitor](https://github.com/nicsure/RMS880/wiki/VFO-Menu#tone-monitor)

---

## AM AGC Fix _(RT-880 Only)_

A common issue with the BK4819 occurs when receiving strong AM signals: the built-in AGC cannot attenuate the signal sufficiently, resulting in overdrive.

When enabled, this setting disables the chip’s AGC in AM mode and replaces it with a firmware-level RF gain control system. Strong signals may briefly begin with loud buzzing before attenuation takes effect.

- **Default:** On

---

## AM Emulation Notes

The radio chips used in the RT-880 & RT-950 are the Beken BK48x9. These chips are only capable of FM transmission.

### _(RT-880)_
The RT-880 attempts a crude emulation of AM transmission by combining frequency offset with heavily over-modulated FM.
This produces a large deviation in the carrier frequency as the signal is modulated. As the carrier swings above and below the AM receiver’s tuned frequency, the signal moves into and out of the receiver’s passband. This causes the apparent received signal strength to vary.
The AM receiver interprets these variations in signal strength as changes in amplitude, effectively recovering the original modulation from the FM signal.


While intelligible to a receiving station, audio quality is poor and adjacent-channel interference is likely.
This feature is **not recommended** for practical operation.
  
### _(RT-950 Pro)_ 
The RT-950-Pro does this differently. It doesn't use the FM adjacent trick that the 880 does. It modulates a carrier by adjusting the output power (and thus the amplitude). Meaning the 950 produces true AM rather than the hack the 880 uses.

---

## AM Hack Transpose _(RT-880 Only)_

Defines the frequency offset used for AM emulation.

- **Units:** 10 Hz  
- Use `#` to flip polarity  
- **Range:** −20,000 to +20,000  
- **Default:** +150

---

## AM Hack Displacement _(RT-880 Only)_

Defines the FM deviation used for AM emulation. Uses the same units as **TX Deviation**.

- **Range:** 0–127  
- **Default:** 99

---
## AM TX Range _(RT-950 Pro Only)_

Defines the vertical normalization window around the TX audio waveform used to control the modulation. In effect, it functions like an inverted microphone gain control: a smaller value produces a tighter window and therefore higher modulation, making the audio louder.

If the value is set too low for the TX audio level, the waveform will exceed the window and be clipped resulting in distortion.

- **Units:** 12 bit ADC units
- **Range:** 100 to 3,000  
- **Default:** 256

---


## Noise Gate

When enabled, this system mutes audio whenever noise reaches or exceeds the value set in  
[Main Menu → Squelch → Noise Ceiling](https://github.com/nicsure/RMS880/wiki/Squelch-Menu#noise-ceiling).

Using this in combination with fully open squelch provides the most sensitive static gating possible.

- **Values:** On / Off  
- **Default:** Off

---

## AF Filters

Selects which built-in hardware audio filters are applied to speaker output.

| Option          | Description                                  |
|-----------------|----------------------------------------------|
| None            | No filters applied                           |
| De-emf Only     | De-emphasis filter only                     |
| Lo Only         | Low-pass filter only                        |
| Lo + De-emf     | Low-pass + de-emphasis                      |
| Hi Only         | High-pass filter only                       |
| Hi + De-emf     | High-pass + de-emphasis                     |
| Hi + Lo         | High-pass + low-pass                        |
| All             | All filters enabled                         |
| FSK             | Optimized for data decoding                 |

- **Default:** All

---

## PIN

Sets a four-digit PIN required to unlock the radio.

- **Range:** 0001–9999  
- **Default:** 0000 (Disabled)  
- **See:** [Operating Modes → Radio → Keylock](https://github.com/nicsure/RMS880/wiki/Radio-Mode#key-lock)

---

## PIN Action

Defines when the PIN is required.

| Option   | Description                                      |
|----------|--------------------------------------------------|
| Unlock   | PIN required only when unlocking the keypad     |
| Startup  | PIN required at radio power-on                  |

- **Default:** Unlock

---

## Auto Lock

Automatically locks the keypad after a period of inactivity.

- **Range:** 0–999 seconds  
- **0 = Disabled**  
- **Default:** 0

---

## DAC Gain

Individual radios can exhibit different audio amplifier gain levels due to normal manufacturing tolerances. This setting adjusts the output level of the radio’s **DAC (Digital-to-Analog Converter)**, effectively changing the usable range of the volume control to make the volume range more consistent.

Increasing the value raises the maximum audio output, which can be helpful in noisy environments such as vehicles where the radio may be too quiet even at full volume. Lowering the value reduces overall output, providing finer control over volume levels in quieter environments.

- **Values:**  
  - `0–15` — Increasing output level  
- **Default:** `8`

---

## #/Red Mode _(RT-880 Only)_

Swaps the functions of `SP-#` and `SP-RED`.

- `nicFW` Normal behaviour:
  - `SP-#` cycles active VFOs
  - `SP-RED` switches between Frequency, Channel, and Group modes
- `Stock` Inverted behaviour; these functions are reversed.

- **Default:** `nicFW`  
- **See:** [Operating Modes → Radio → Controls](https://github.com/nicsure/RMS880/wiki/Radio-Mode#sp-red)

---

## LW Start

Defines the starting frequency of the **LW (Longwave) band** when operating in Tuner Mode. This setting allows the LW band stepping to be adjusted to match different regional and country-specific standards.

- **Range:** 103 kHz – 211 kHz  
- **Default:** 103 kHz  
- **See:** [Operating Modes → Tuner](https://github.com/nicsure/RMS880/wiki/Tuner-Mode)  
- **Note:** The radio must be power-cycled for changes to this setting to take effect.

---

## Name Scroll

Defines how the UI behaves when a channel name is too long to fit entirely on the display.

- **Values**
  - **0 (Disabled)**  
  No scrolling occurs. Channel names that exceed the available space are simply truncated.
  - **1–20**  
  Enables scrolling when the channel name exceeds the available display space by at least the specified number of characters. If the name is shorter than this threshold, scrolling does not occur, and the name will just be truncated (if needed).
- **Examples**
  - A value of **1** causes scrolling for _**any**_ channel name that does not fully fit on the display.  
  - A value of **3** causes scrolling only when the channel name is **three or more characters** longer than the available space.
#### See
- [RMS → UI](https://github.com/nicsure/RMS880/wiki/UI-Tab)
- [Main Menu → Channel → Channel Name](https://github.com/nicsure/RMS880/wiki/Channel-Menu#channel-name)

---

## T9 Advance

Defines the delay, in seconds, after the last key press during **T9 text entry** before the cursor automatically advances to the next character position.

When set to **Disabled**, the cursor will **not** advance automatically and must be moved manually by the user.

- **Values:** 0.0 seconds (Disabled) to 2.0 seconds  
- **Recommended:** 0.75 seconds
- **Default:** Disabled

See:
- [Radio → T9 Text Entry](https://github.com/nicsure/RMS880/wiki/T9-Text-Entry)

---

## Battery Save

To conserve battery power, the radio can periodically place the RF chip into a low-power state and put the main processor to sleep. While asleep, the radio temporarily reduces activity, then wakes up at regular intervals to check squelch status, perform MultiWatch cycles, and respond to user input.

The duration of this low-power sleep interval is controlled by this setting. Longer sleep periods result in improved battery life, but may make the radio feel less responsive when reacting to incoming signals or user interaction.

### Values
- **0.00** – Disabled  
- **0.01 to 2.00 seconds** – Increasing power-save aggressiveness  
- **Default:** Disabled

### Activation Conditions

Battery Save only becomes active when **all** of the following conditions are met:

- The radio is operating in **normal Radio Mode**
- **Squelch is closed**
- The **LCD has timed out** and is turned off
- The radio is **not transmitting**

When any of these conditions change, the radio immediately exits low-power mode and resumes full operation.

See
- [Main Menu → Display → Timeout](https://github.com/nicsure/RMS880/wiki/Display-Menu#timeout)

---

## Keypad LED

Controls whether the keypad backlight LED is enabled.

By default, the keypad illuminates in sync with the LCD backlight. When this setting is changed to `Off`, the keypad LED will remain off at all times, regardless of the LCD state.

This can help reduce power consumption slightly or prevent unwanted light in low-visibility environments.

- **Values:** `On`, `Off`  
- **Default:** `On`

See also:
- [Main Menu → Display → Timeout](https://github.com/nicsure/RMS880/wiki/Display-Menu#timeout)

---

## Hunt STones

Enables a more aggressive AFC (Automatic Frequency Control) system to help recover and correctly decode incoming **CTCSS tones** and **DCS codes** when the radio or transmitting station is too far off frequency for decoding to occur normally.

This enhanced AFC operates at the firmware level and can compensate for noticeable frequency error, improving tone decoding reliability, particularly on radios that have not been fully calibrated or when receiving slightly off-frequency transmitters.

Because this AFC system actively adjusts reception to “hunt” for the correct center frequency, it may very briefly make the radio feel slightly less responsive while it locks in. In practice, this effect is rarely noticeable and typically only occurs momentarily while the frequency correction is being established.

- **Values:** `On`, `Off`  
- **Default:** `On`

---

## Baud Delay

Controls an acknowledgement delay that radio introduces when changing BAUD rates.  
If higher speeds are not working correctly in the RMS, try increasing this value.

- **Values:** `100` to `2000` milliseconds  
- **Default:** `100`