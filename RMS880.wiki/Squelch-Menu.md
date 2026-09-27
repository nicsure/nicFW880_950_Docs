# Squelch Overview

Squelch is a system designed to mute the main speaker until a valid signal is received. nicFW’s squelch implementation is significantly more advanced than that of most radios and allows for fine-grained control over how and when audio is unmuted.

nicFW squelch operates based on **two independent factors**:

- **Signal strength** (RSSI)
- **Received noise level** (ExNoise)

For squelch to **open**, the signal strength must rise above a configured threshold *and* the noise level must fall below its threshold.  
For squelch to **close**, the signal must drop back below its threshold and the noise level must rise again.

While the **Squelch Menu** is open, the menu’s *Extra Info* field displays real-time numerical values for the current channel or frequency’s **RSSI** and **ExNoise** levels. These live readings can be used to determine optimal values for several squelch parameters and [Signal Floor](https://github.com/nicsure/RMS880/wiki/Calibration-Tab#rssi-floors) calibration.

---

# Squelch Menu Options

## Level

- **Available Values:** `0` (Off) to `9`
- **Default Value:** `2`

Controls the primary signal-strength requirement for opening squelch.

- `0 (Off)`  
  Disables squelch entirely; the speaker remains unmuted at all times.
- `1`  
  Special *noise-only* mode. This is the most sensitive setting, but also the most prone to false openings and closings.
- `2–9`  
  Correspond to S-levels:
  - `2` → Minimum of **S1**
  - `3` → Minimum of **S2**
  - `4` → Minimum of **S3**
  - and so on

---

## Noise Trigger

- **Available Values:** `0` to `127`
- **Default Value:** `48`

Defines the maximum noise level that must be met for squelch to open. Noise must fall *below* this value before audio is unmuted.

---

## Noise Hysteresis

- **Available Values:** `0` to `20`
- **Default Value:** `4`

Defines a buffer zone between squelch opening and closing based on noise level.

Example:
- Noise Trigger = `48`
- Noise Hysteresis = `4`

Squelch will:
- Open when noise drops to **44**
- Close when noise rises to **52**

This prevents rapid toggling in marginal conditions.

---

## RSSI Hysteresis

- **Available Values:** `0` to `20`
- **Default Value:** `4`

Defines a buffer zone between squelch opening and closing based on signal strength.

- Units are in **½ dBm**
- Example:
  - `Level` set to `3` (S2)
  - RSSI Hysteresis set to `4`

Squelch will:
- Open at **S2 + 2 dBm**
- Close at **S2 − 2 dBm**

---

## Throttle

- **Available Values:** `0` to `9`
- **Default Value:** `2`

Sets a minimum time, in **tenths of a second**, that must pass after a squelch state change before another change is allowed.

This prevents rapid squelch chatter in noisy environments.

---

## Noise Ceiling

- **Available Values:** `0` to `127`
- **Default Value:** `60`

Defines an absolute maximum allowable noise level.

- Any noise **at or above** this value will immediately close squelch
- Overrides hysteresis and tail settings

This setting is the primary reason for nicFW’s exceptionally fast squelch cutoff behavior.

---

## Squelch Tail Elimination

- **Available Values:** `Off`, `RX`, `TX`, `Both`
- **Default Value:** `Off`

Reduces squelch tail noise (static bursts) at the end of transmissions.

This system works by transmitting a special **55.0 Hz CTCSS tone** at the end of a transmission. If the receiving radio detects this tone, it immediately mutes the speaker before the carrier drops.

Options:
- `RX` – Respond to tail elimination tones
- `TX` – Transmit tail elimination tones
- `Both` – Enable both receive and transmit behaviour

This feature requires compatible settings on both stations.

---

## Tail

- **Available Values:** `0.0` to `5.0` seconds
- **Default Value:** `0.5`

Defines how long the speaker remains unmuted after a signal drops before squelch closes.

Although often overridden by **Noise Ceiling**, this setting can help prevent squelch chatter when signals hover near the threshold.
