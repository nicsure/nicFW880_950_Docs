## GPS Mode Overview

For radios equipped with GPS capability, GPS Mode provides both a **diagnostic readout** and a **basic navigation environment**.

For GPS related settings see [Main Menu → GPS](https://github.com/nicsure/RMS880/wiki/GPS-Menu)

---

## Data Display Readout

The Data Display is shown first when entering GPS Mode. It presents real-time information received from the GPS chip in an easy-to-read format.

![alt](https://github.com/nicsure/RMS880/blob/main/gpsdata.jpg?raw=true)

Displayed fields:

- Latitude  
- Longitude  
- Altitude  
- Locked Satellites  
- Maidenhead Locator  
- Velocity  
- Course (heading)  
- Time  

Additionally, the bottom of the display shows:

- Target Latitude  
- Target Longitude  

---

## Navigation Environment

The Navigation environment is a simple direction-finding system. It displays a compass with a **blip** representing a target location, if one is selected. Beneath the compass are several informational fields (see image below for reference).

![alt](https://github.com/nicsure/RMS880/blob/main/gpsnavigate.jpg?raw=true)

The radio does **not** contain a magnetic compass. Direction is determined from motion, meaning the compass updates based on the direction of travel.

Two rotation modes are available:

- The compass needle remains fixed while the outer ring rotates  
  * A circular arrow icon is displayed top left.
- The outer ring remains fixed while the needle rotates  
  * No icon is displayed top left.

When a target location is set, a blip appears on the compass indicating the target’s **direction and distance**.  
If the target lies beyond the current compass radius, the blip is drawn on the outer ring to indicate direction only.

Target information is shown at the bottom of the display, including:

- Target name (if set via a waypoint)  
- Distance to target  
- Heading to target  

An satellite dish icon is displayed top right representing the current GPS status.

- Not Shown
  * GPS is disabled
- Dish Pointing Down
  * GPS is enabled but not locked
- Dish Pointing Up
  * GPS is enabled and locked

---

## Rudimentary Walkie-Talkie Operation

GPS Mode allows very limited radio operation. The VFO that was active when GPS Mode was entered remains active for receive and transmit.

Most Radio Mode features are unavailable. GPS Mode is **not intended for normal communication**; this functionality exists primarily for testing and diagnostic purposes.

---

## Controls

### SP-# — Data / Nav

Cycles between the GPS Data Display and the Navigation environment.


### SP-* — Rotate Mode

Cycles between compass ring rotation mode and compass needle rotation mode.

When ring rotation mode is active, a circular arrow icon appears in the top-left corner of the navigator screen.


### SP-7 — Waypoints

Opens the Waypoint browser.

See:  
- [Radio → GPS Waypoints](https://github.com/nicsure/RMS880/wiki/GPS-Waypoints)


### SP-RED — Exit

Exits GPS Mode and returns to Radio Mode.


### SP-9 — Units

Cycles the units used for distance, speed, and related measurements.

See:  
- [Main Menu → GPS → Units](https://github.com/nicsure/RMS880/wiki/GPS-Menu#units)


### LP-4 — Set Target

Sets the current GPS position as the navigation target.


### LP-5 — Clear Target

Clears the currently selected navigation target.


### LP-1 — Set Range

Allows editing of the compass radius.  
This defines the real-world distance represented by the compass ring.


### SP-6 — Beacons

Duplicate function. Opens the APRS beacon browser.  
Received beacons may be selected as navigation targets.

See:  
- [Key Functions → Beacons](https://github.com/nicsure/RMS880/wiki/Radio-Mode#beacons)


### SP-8 — Weather

Duplicate function. Opens the APRS weather information screen.

See:  
- [Key Functions → Weather](https://github.com/nicsure/RMS880/wiki/Radio-Mode#weather)


### LP-2 — MHL Target

Opens a text input field to enter a Maidenhead Locator string to be used as a navigation target.

See:  
- [Maidenhead Locator System](https://en.wikipedia.org/wiki/Maidenhead_Locator_System) 
- [Radio → T9 Text Entry](https://github.com/nicsure/RMS880/wiki/T9-Text-Entry)


### LP-3 — MHL Position

Opens a text input field to enter a Maidenhead Locator string to be used as a **spoofed GPS position**.  

[Main Menu → GPS → Enabled](https://github.com/nicsure/RMS880/wiki/GPS-Menu#enabled) must be set to `Off` for this function to work.

The spoofed location will remain set until:
- GPS is re-enabled
- Another location is spoofed
- The radio is powered off.

See: [Radio → T9 Text Entry](https://github.com/nicsure/RMS880/wiki/T9-Text-Entry)

### LP-0 — Dec / DegMin

Cycles the latitude and longitude display format between:

- Decimal degrees  
- Degrees and minutes  

### LP-GREEN - GPS Function Menu
Opens the GPS Function Menu. This menu lists and executes all available functions and displays a reminder of their activation key presses.