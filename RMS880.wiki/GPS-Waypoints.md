## GPS Waypoints Overview

nicFW can store up to **99 pre-programmed locations**, referred to as **Waypoints**. Waypoints may be used to:

- Save locations while navigating  
- Set navigation target locations  
- Spoof GPS coordinates  

**Waypoint #99** is reserved as the default spoofed location when the radio is powered on with GPS functionality disabled.  
See: [Main Menu → GPS → Enabled](https://github.com/nicsure/RMS880/wiki/GPS-Menu#enabled)

---

## Waypoint Browser

Waypoints can be browsed by executing the **Waypoints** function while in GPS Mode  
(default key: **SP-7**).

Each waypoint entry displays:

- Waypoint number  
- Waypoint name  
- Location in degrees/minutes  
- Location in decimal degrees  
- Maidenhead locator  

![alt](https://github.com/nicsure/RMS880/blob/main/waypoints.jpg?raw=true)

---

## Browser Controls

### SP-RED — Exit

Closes the Waypoint Browser and returns to the previous screen.


### SP-GREEN — Set to Target

Sets the currently selected waypoint as the active navigation target.


### LP-0 — Edit Name

Creates, edits, or changes the name of the selected waypoint.

See:  
- [Radio → T9 Text Entry](https://github.com/nicsure/RMS880/wiki/T9-Text-Entry)


### LP-1 — Edit Latitude

Edits the latitude of the selected waypoint.  
Input is in **decimal degrees** format.

Controls during entry:

- `*` — Enter a decimal point  
- `GREEN` or `#` — Confirm entry  
- `RED` — Cancel entry  


### LP-2 — Edit Longitude

Edits the longitude of the selected waypoint.  
Operation is identical to **Edit Latitude**, but applies to longitude.


### LP-4 — Invert Latitude

Flips the latitude sign between positive and negative  
(North ↔ South).


### LP-5 — Invert Longitude

Flips the longitude sign between positive and negative  
(East ↔ West).


### LP-RED — Spoof GPS

Sets the selected waypoint as the **spoofed GPS location**.  
[Main Menu → GPS → Enabled](https://github.com/nicsure/RMS880/wiki/GPS-Menu#enabled) must be set to `Off` for this function to operate.

The spoofed location will remain set until:
- GPS is re-enabled
- Another location is spoofed
- The radio is powered off.

