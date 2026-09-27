# GPS / APRS Tab Overview

The **GPS / APRS** tab is divided into two sub-tabs:

- **Waypoints** — for managing pre-programmed GPS locations  
- **Beacons** — for viewing received APRS packets  

Together, these tabs provide tools for navigation, location spoofing, and APRS monitoring.

# Waypoints Tab

Waypoints are **pre-programmed GPS coordinates** that can be used as:

- Navigation targets  
- Spoofed GPS locations  
- Saved points of interest while navigating  

The radio supports **99 waypoint slots**, displayed in a scrollable list on the left side of the tab.

- Click a slot to select it  
- When selected, the controls on the right populate with that waypoint’s data  

### Reserved Slot
**Slot #99** is reserved as the default **spoofed location**.  
When the radio starts with GPS functionality disabled, waypoint **#99** is automatically used as the radio’s GPS position.

## Waypoint Tab Controls

### Active

Enables or disables the waypoint.

- Unticking this box effectively deletes the waypoint

### Latitude

The waypoint’s latitude in **degrees**.

### Longitude

The waypoint’s longitude in **degrees**.

### Name

Assigns a descriptive name to the waypoint.

- Maximum length: **14 characters**

### MH Locator

The **Maidenhead Locator** for the waypoint.

- Editing this field with a valid locator automatically updates the Latitude and Longitude
- Editing Latitude or Longitude updates the Maidenhead Locator
- Maidenhead locators are **less precise** than direct coordinate entry

## Waypoint List Right-Click Menu

### Copy / Cut / Paste

Standard clipboard operations for copying, moving, or deleting waypoints.

### Browse

Opens a web browser centered on the selected waypoint’s location using **OpenStreetMap**.

## Additional Resources

A video guide covering the Waypoints tab is available here:

- [Waypoints Guide](https://www.patreon.com/posts/139897694)

For more information, see:
- [Main Menu → GPS](https://github.com/nicsure/RMS880/wiki/GPS-Menu)

---

# Beacons Tab

The **Beacons** tab displays APRS beacons received by the radio.

- Beacons are listed on the left side of the tab
- The most recent beacon appears in **slot #1**
- Older beacons follow in chronological order

Beacons can be selected and **copied into the Waypoints tab**, allowing received APRS locations to be saved as navigation targets.

Beacons are not editable, you may only read them from the radio. You can however erase them all from the radio by pressing the `Wipe` button.

For more information on APRS beacons, see:
- [APRS → Beacons](https://github.com/nicsure/RMS880/wiki/APRS-Menu#waypoints)
