## APRS Overview

Automatic Packet Reporting System (APRS) allows the radio to send and receive digital position and status information.  

nicFW on the RT-880 can encode and decode APRS frames even on non-GPS models, which is functionality not offered by even the radio's manufacturer. When used with a GPS-capable radio, the device can function as a full APRS station.  

Non-GPS radios can still transmit and receive APRS packets, but positions must be manually configured ("spoofed").  
See [Operating Modes → GPS](https://github.com/nicsure/RMS880/wiki/GPS-Mode)

Received APRS beacons are saved in a list, this list can be browsed using [Key Functions → Beacons](https://github.com/nicsure/RMS880/wiki/Radio-Mode#beacons)

Received weather data is also saved, it can be viewed using [Key Functions → Weather](https://github.com/nicsure/RMS880/wiki/Radio-Mode#weather)

### Waypoints
See [Radio → GPS Waypoints](https://github.com/nicsure/RMS880/wiki/GPS-Waypoints) for a full description of GPS waypoints.  
Waypoint 99 is a special slot, it defines the default spoofed location loaded on startup when GPS is disabled or when using a non-GPS radio.  
Any selected waypoint can be used as a spoofed location by selecting [Waypoint Browser Functions → Spoof GPS](https://github.com/nicsure/RMS880/wiki/GPS-Waypoints#lp-red--spoof-gps) in the Waypoint browser.  
For configuration using the RMS see [RMS → GPS/APRS → Waypoints](https://github.com/nicsure/RMS880/wiki/GPS-APRS-Tab#waypoints-tab)

---

## APRS Menu Overview

The APRS menu controls transmission, reception, and decoding behaviour for APRS packets.  

---

### Deviation
Sets the volume (loudness) of transmitted APRS FSK tones. This overrides [Main Menu → Advanced → TX Deviation](https://github.com/nicsure/RMS880/wiki/Advanced-Menu#tx-deviation).  
- **Range:** 0 to 126  
- **Default:** 64

---

### Beacon Time
Interval between automatic APRS beacon transmissions of the current location.  
- **Range:** 0 (Disabled) to 9999 seconds  
- **Default:** Disabled  
- **See:** [Operating Modes → GPS](https://github.com/nicsure/RMS880/wiki/GPS-Mode)

---

### Beacon Distance
Minimum distance travelled when GPS is enabled, before a new APRS beacon is sent.  
- **Range:** 0 (Disabled) to 9999 meters  
- **Default:** Disabled  
- **See:** [Operating Modes → GPS](https://github.com/nicsure/RMS880/wiki/GPS-Mode)

---

### Beacon TX
Sends an APRS beacon at the start or end of a normal PTT transmission, or both. This operates on the current transmit VFO, not the dedicated APRS VFO.  
- **Values:** Off, BoT (Beginning of Transmission), EoT (End of Transmission), Both  
- **Default:** Off

---

### Beacon Comment
Custom comment string transmitted with APRS beacons. Up to 24 characters.  
- **See:** [Radio → T9 Text Entry](https://github.com/nicsure/RMS880/wiki/T9-Text-Entry)

---

### Beacon RX Override
When `On` and `APRS Enabled` is set to a VFO or `999` , scheduled APRS beacons can interrupt an active reception to transmit.  
- **Default:** Off

---

### Callsign
Set your amateur radio callsign for APRS transmission.  
- **See:** [Radio → T9 Text Entry](https://github.com/nicsure/RMS880/wiki/T9-Text-Entry)

---

### SSID
AX.25 secondary station identifier for APRS.  
- **Range:** 0–15  
- **Default:** 7 (Human)

| Value | Identifier |
|---|---|
| 0 | Primary |
| 1 | Vehicle |
| 2 | Mobile |
| 3 | Camper |
| 4 | Home |
| 5 | Portable |
| 6 | Special |
| 7 | Human |
| 8 | BBS |
| 9 | I-Gate |
| 10 | Weather |
| 11 | Satellite |
| 12 | Digipeater |
| 13 | Experiment |
| 14 | Truck |
| 15 | Emergency |

---

### Enabled
Controls if APRS is enabled or not and how APRS operation behaves.  
| Value | Description |
|-------|-------------|
| Off | APRS disabled |
| Active VFO | APRS uses the current active VFO (not recommended for use, mainly for testing, prevents side buttons working) |
| VFO-A | APRS operates exclusively on VFO-A* |
| VFO-B | APRS operates exclusively on VFO-B* |
| VFO-C | APRS operates exclusively on VFO-C* |
| | [Multiwatch](https://github.com/nicsure/RMS880/wiki/VFO-Menu#multiwatch) needs to be enabled for the exclusive VFO modes |
| 999 | APRS operates transparently on channel 999  |
| | [Multiwatch](https://github.com/nicsure/RMS880/wiki/VFO-Menu#multiwatch) is NOT required for 999 mode |

\*Except for `Beacon TX` and [TX Controls → Manual APRS Beacon](https://github.com/nicsure/RMS880/wiki/Radio-Mode#side-key-s1--manual-aprs-beacon).  

> Operating APRS on a dedicated VFO or 999 is recommended.

| APRS Mode | Icon Behaviour |
|---|---|
| Current VFO & No Automatic Beacons | Compass Icon appears in main icon area. No VFO icon |
| Current VFO & Automatic Beacons | Compass Icon with central dot appears in main icon area. No VFO icon |
| Specific VFO & No Automatic Beacons | Compass Icon appears in main icon area and on the selected VFO |
| Specific VFO & Automatic Beacons | Compass Icon with central dot appears in main icon area and on the selected VFO (without the dot) |
| Specific VFO | If `Hear Tones` is set to `Off` a Speaker Mute icon will also appear in the selected VFO |
| 999 & No Automatic Beacons | 999 Icon appears in main icon area. No VFO icon |
| 999 & Automatic Beacons | 999 Icon with outward arrows appears in main icon area. No VFO icon |

- **Default:** Off

---

### Hear Tones
Controls whether transmitted and received APRS FSK tones are audible.  
| Value | Description |
|-------|-------------|
| On | Tones audible; APRS VFO not muted |
| Off | Tones muted; APRS VFO muted with mute icon |

---

### Decode
Controls whether received APRS packets are decoded.  
| Value | Description |
|-------|-------------|
| Off | No decoding |
| On | Decodes packets and stores in beacon list |
| Popup | Same as `On`, but displays a popup on receipt |

- **See:** [Key Functions → APRS Beacons](https://github.com/nicsure/RMS880/wiki/Radio-Mode#beacons)  
- **Default:** Off

---

### Popup Time
Duration for which a popup is displayed when `Decode` is set to `Popup`.  
Popups can be dismissed by the user before the time limit by pressing any kay.  
- **Range:** 0.0 (indefinite) to 99.9 seconds  
- **Default:** 3.0 seconds

---

### Symbol
ASCII symbol used in APRS beacons to define station icon. Only standard/primary symbols are supported.  
- **See:** [APRS Symbols](https://www.aprs.org/symbols.html)  
- **Default:** `[` (🏃 - Person running)

---

### Status
Sets station status encoded in APRS beacons.  
| Value | Status Message |
|---|---|
| 0 | Emergency |
| 1 | Priority |
| 2 | Special |
| 3 | Committed |
| 4 | Returning | 
| 5 | In Service |
| 6 | En Route |
| 7 | Off Duty |
- **Range:** 0–7  
- **Default:** 7 (Off Duty)

---

### Digipeaters
Configures AX.25 digipeater paths.  
| Value | Description |
|-------|-------------|
| None | No digipeaters |
| WIDE1-1 | Generic WIDE1-1 path |
| WIDE2-2 | Uses WIDE1-1 and WIDE2-2 |
| Custom | Custom callsign and SSID via `Custom Digipeater` and `AX25 DP SSID` |

---

### Custom Digipeater
Callsign used when `Digipeaters` = `Custom`.  
- **See:** [Radio → T9 Text Entry](https://github.com/nicsure/RMS880/wiki/T9-Text-Entry)
Default: AR0ISS (The international space station)

---

### AX25 DP SSID
SSID used for the custom digipeater.  
- **Range:** 0–15  
- **Default:** 0

---

### Ambiguity
Defines location precision in transmitted APRS beacons.  
| Value | Description |
|-------|-------------|
| 20 m | High precision, best available |
| 200 m | Medium precision |
| 2 km | Low precision |

- **Default:** 20 m

---

### Filters
Overrides [Main Menu → Advanced → AF Filters](https://github.com/nicsure/RMS880/wiki/Advanced-Menu#af-filters) for APRS VFO and 999 reception.  
Recommended: Low Pass Only.  
_Note: A VFO must be assigned to APRS or APRS 999 mode be in use for this to function_  
- **Default:** Low Pass Only

---

### Noise Filter
Extra low-pass filtering for received APRS signals.  
- **Range:** None, 1–3 (increasingly aggressive)  
- **Default:** 2

---

### Noise Reject
Software-level phase hysteresis for APRS decoding.  
- **Range:** None, 1 (less), 2 (more)  
- **Default:** 1

---

### Ignore Own

Prevents the APRS decoder from recording and displaying your own transmitted packets when they are repeated back by digipeaters.

When APRS is in use, your transmitted beacon may be repeated by nearby digipeater stations and received again by your radio. With this setting enabled, those repeated copies of your own packets will be ignored and not added to the received beacon list. This helps keep the beacon log clean and focused on other stations.

- **Values:** `On`, `Off`  
- **Default:** `Off`

---

### KISS Mode
Enables KISS mode (TTNC) over the serial interface.
See:
- [Operating Modes → KISS](https://github.com/nicsure/RMS880/wiki/KISS-Mode)

---

### Persist & Slot Time
KISS-mode settings:  

- **Persist:** Randomized transmission probability, 1–255  
  - **Default:** 128  
- **Slot Time:** Delay in hundredths of a second before retry if `Persist` fails  
  - **Default:** 10 centiseconds