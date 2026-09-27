# Scanning Overview

The radio supports multiple scanning modes depending on the active operating mode. Scanning can be performed in **Frequency (VFO) Mode**, **Channel Mode**, or **Group Mode**, each with specialized behaviours.

While scanning, the radio steps through frequencies/channels until it detects a signal that is strong enough to break the current squelch settings. At which point the scan stops and the radio begins monitoring the detected signal.  
See: [Main Menu → Squelch](https://github.com/nicsure/RMS880/wiki/Squelch-Menu)

A scan icon (a radio antenna) is shown on the display during scanning.

During signal scanning, the display **DOES NOT** update for every scanned channel or frequency. This is because updating the screen takes time and would slow the scan down significantly. To compromise, the display updates every tenth of a second instead, this provides a fast enough visual reference without slowing down the scanner too much. nicFW scans much faster than this however, so it may appear as though channels and frequencies are being missed, this is NOT the case.

There are various menu settings that configure the performance and behaviour of scanning.  
See: [Main Menu → Scanning](https://github.com/nicsure/RMS880/wiki/Scanning-Menu)

---

# VFO/Frequency Scanning

VFO/Frequency Scanning is used when a scan is initiated in **Frequency Mode**. A continuous range of frequencies is scanned. The frequencies scanned depend on the function used to start the scan:
- See [Main Menu → User Keys](https://github.com/nicsure/RMS880/wiki/User-Keys-Menu)

## Scan (Menu) – Default key: `LP-3` 
Scans a range of frequencies defined in the **Main Menu**.  
- [Main Menu → Scanning → VFO Start](https://github.com/nicsure/RMS880/wiki/Scanning-Menu#vfo-start) defines the frequency the scan starts from in MHz.
- [Main Menu → Scanning → VFO Range](https://github.com/nicsure/RMS880/wiki/Scanning-Menu#vfo-range) defines the range of the scan in MHz. The scan will run up to: VFO Start + VFO Range
- [Main Menu → Scanning → VFO Step](https://github.com/nicsure/RMS880/wiki/Scanning-Menu#vfo-step) sets in kHz the gap between scanned frequencies.
- [Main Menu → Scanning → VFO Modul](https://github.com/nicsure/RMS880/wiki/Scanning-Menu#vfo-modulation) sets the modulation mode of the scan, FM, AM or DSB or Automatic for whatever the band plan defines.
- [Main Menu → Scanning → VFO Bandw](https://github.com/nicsure/RMS880/wiki/Scanning-Menu#vfo-bandwidth) sets the receive bandwidth of the scan, Wide, Narrow or Automatic for whatever the band plan defines.
  - Note: See [Main Menu → Band Plan](https://github.com/nicsure/RMS880/wiki/Band-Plan-Menu) and [RMS → Band Plan](https://github.com/nicsure/RMS880/wiki/Band-Plan-Tab) for more information on the above automatic settings. 

## Scan (VFO) – Default key: `LP-4`  

Uses the **current VFO’s frequency, modulation, bandwidth and step size** instead of the menu-defined scan parameters. The scan range is however still defined by [Main Menu → Scanning → VFO Range](https://github.com/nicsure/RMS880/wiki/Scanning-Menu#vfo-range).

## Scan Presets – Default key: `LP-1`

Scans a **pre-configured frequency range** selected from a menu.  
- See: [Operating Modes → Radio → Scan Presets](https://github.com/nicsure/RMS880/wiki/Radio-Mode#scan-presets)

---

## Ultra Scan

An acceleration system for VFO scanning that can **increase scan speed by up to 10×**.  
- See: [Main Menu → Scanning → Ultra Scan Level](https://github.com/nicsure/RMS880/wiki/Scanning-Menu#ultra-scan-level)

---

## Smart Scan

Remembers previously active frequencies and revisits them periodically.

Smart scan is not recommended to be used with [Monitor Time](https://github.com/nicsure/RMS880/wiki/Scanning-Menu#monitor-time) enabled, as their root purposes conflict. Neither is it ideal for users who regularly skip detected frequencies by pressing UP/DOWN during monitoring. That use-case is incompatible with the fundamental idea of the smart scan system.

- Results in **more hits** but can **slow overall scan speed** as memory builds.  
- See: [Main Menu → Scanning → Smart Scan](https://github.com/nicsure/RMS880/wiki/Scanning-Menu#smart-scan)

---

## Why does the frequency mode scan start lower than the start frequency I configured?

When performing a **frequency (VFO) mode scan** with **Ultra Scan** enabled, the scanner must first establish a reliable **noise floor** so it can correctly identify potential signals.

Ultra Scan does this by maintaining a **rolling minimum** of the noise levels from the **last 16 scanned frequencies**. This keeps the noise floor local and relevant to the part of the spectrum currently being scanned, which greatly improves detection accuracy and speed.

However, this approach has a small side effect:  
at the very beginning of a scan, the noise floor has not yet been fully initialized or localized. The first 16 frequencies would otherwise be evaluated using incomplete or inaccurate noise data.

To avoid this, the scanner automatically **shifts the effective start frequency downward by 16 steps**. This gives Ultra Scan enough data to establish a proper noise baseline *before* reaching your configured start frequency.

As a result, the scan appears to begin slightly below the start frequency you set, but by the time it reaches your configured range, the noise floor is fully settled and signal detection is accurate.


---

# Channel Scanning

Used when a scan is initiated in **Channel Mode** (default: `LP-3`).  

- Steps through each pre-programmed channel at approximately **30 channels per second**.

---

# Group Scanning

Used when a scan is initiated in **Group Mode** (default: `LP-3`).  

- Functions identically to Channel Scanning, **except only channels in the selected group are scanned**.

---

# Multi Group Scanning

Started by the User Key function `Scan MGroups`.  
- The scan toggles between up to four groups entered by the user.  
- The `*` and `0` keys used to change groups during a group scan do not function in multi group scan.  
- When stopping a scan, the VFO will switch to channel mode. This is because you might not stop the scan on the right group for the channel `Scan Return` will set.

See:
- [Operating Modes → Radio → Scan MGroups](https://github.com/nicsure/RMS880/wiki/Radio-Mode#scan-mgroups-multiple-group-scan)
- [Main Menu → Scanning → Scan Return](https://github.com/nicsure/RMS880/wiki/Scanning-Menu#scan-return)

---

# Scanning Controls

While a scan is running the following keys perform scanning-specific functions.

| Control | Function |
|---------|---------|
| `UP` / `DOWN` | Change scan direction. During monitoring, skips the monitor and continues the scan. |
| | Note: When skipping, the monitored frequency is **temporarily** ignored. This prevents the same active frequency being immediately detected again. |
| `#` | Place the current or last detected frequency into the **ignore (exclusion) list**. |
| `RED` | Stop the scan immediately. |
| `*` / `0` | Group scan only, change group during scanning (single group scan only) |
| `Any Other Key` | If [Main Menu → Scanning → Stop Any Key](https://github.com/nicsure/RMS880/wiki/Scanning-Menu#stop-any-key) is `On`, also stops the scan |

---

# Scanning Exclusions

- A list of **excluded frequencies** can be maintained to ignore nuisance signals.  
- The list can be set to:
  - **Persistent** – Saves exclusions between scans  
  - **Temporary** – Cleared each time a scan is started (configured via [Main Menu → Scanning → Save Ignores](https://github.com/nicsure/RMS880/wiki/Scanning-Menu#save-ignores) )  
- Exclusions can also be manually cleared: [Main Menu → Scanning → Clear Ignores](https://github.com/nicsure/RMS880/wiki/Scanning-Menu#clear-ignores)
- The exclusion list may also be managed via the RMS. See: [RMS → Scanning → Exclusions](https://github.com/nicsure/RMS880/wiki/Scanning-Tab#exclusions-tab)

---

# Scanning Limitations

- The radio uses a **mechanical relay** to switch in the **HF band (<70 MHz)**.  
- Rapid switching between HF and non-HF channels during a scan can **stress the relay**.  
- To protect the relay, **Channel and Group Mode scans will only scan channels that match the band of the VFO** when the scan is started.
- When group scanning, you cannot switch to a group that only contains channels that are in the other band.

---

# Frequency Counter / Fast Frequency Scan

A special scanning mode designed to find very strong signals over a wide frequency range very quickly.  
See: [Operating Modes → Radio → Frequency Counter](https://github.com/nicsure/RMS880/wiki/Radio-Mode#frequency-counter)