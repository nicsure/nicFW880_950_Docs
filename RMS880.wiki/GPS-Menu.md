## GPS Menu Overview

The GPS menu controls aspects of the radio’s Global Positioning System functionality, including waypoint management, navigation targets, unit preferences, and hardware behaviour.

For a more detailed explanation of the radio’s GPS capabilities, see  
`Operating Modes → GPS`.

---

### Point Save
Saves the current navigation **Target** location as a GPS waypoint.  

Select one of the 99 available waypoint slots to save to. The **Extra Info** field indicates whether the selected slot is already in use or free.

- **See:**
  - [Operating Modes → GPS → Waypoints](https://github.com/nicsure/RMS880/wiki/GPS-Waypoints)
  - [Operating Modes → GPS → Navigation](https://github.com/nicsure/RMS880/wiki/GPS-Mode#navigation-environment)
  - [RMS → GPS/APRS → Waypoints](https://github.com/nicsure/RMS880/wiki/GPS-APRS-Tab#waypoints-tab)

---

### Point Load
Loads a previously saved GPS waypoint and sets it as the current navigation target.  

Select one of the 99 waypoint slots to load from. The **Extra Info** field indicates whether the selected slot contains a waypoint.

- **See:**
  - [Operating Modes → GPS → Waypoints](https://github.com/nicsure/RMS880/wiki/GPS-Waypoints)
  - [Operating Modes → GPS → Navigation](https://github.com/nicsure/RMS880/wiki/GPS-Mode#navigation-environment)
  - [RMS → GPS/APRS → Waypoints](https://github.com/nicsure/RMS880/wiki/GPS-APRS-Tab#waypoints-tab)

---

### Point Erase
Deletes a stored GPS waypoint.  

Select one of the 99 waypoint slots to erase. The **Extra Info** field indicates whether the selected slot is currently in use.

- **See:**
  - [Operating Modes → GPS → Waypoints](https://github.com/nicsure/RMS880/wiki/GPS-Waypoints)
  - [RMS → GPS/APRS → Waypoints](https://github.com/nicsure/RMS880/wiki/GPS-APRS-Tab#waypoints-tab)

---

### Enabled
Enables or disables GPS functionality.

When set to `Off`, the radio will not use the GPS hardware and will instead rely on spoofed location data. This setting defaults to `On` and must be manually set to `Off` on non-GPS radio variants.

When enabled, a GPS icon (satellite dish) is displayed on the screen:
- The dish **points downward** when no GPS lock has been acquired or when lock has been lost.
- The dish **points upward** when a valid GPS satellite lock is established.

While enabled, the radio will continuously attempt to acquire and maintain a GPS lock whenever the GPS hardware is powered.

- **Values:** On, Off  
- **Default:** On  
- **See:**
  - [Radio → GPS Waypoints](https://github.com/nicsure/RMS880/wiki/GPS-Waypoints)
  - [Operating Modes → GPS](https://github.com/nicsure/RMS880/wiki/GPS-Mode)

---

### Units
Selects the preferred measurement system for distance, speed, altitude, and temperature displays.

- **Values:** Imperial, Metric, Nautical  
- **Default:** Imperial

---

### Reduce QRM
Some radios experience audio interference caused by digital communication between the radio and the GPS chipset. This interference may be present during reception, transmission, or both.

This setting attempts to reduce QRM by temporarily disabling the GPS chip during affected operations.

- **Values:** None, RX, TX, Both  
- **Default:** None
