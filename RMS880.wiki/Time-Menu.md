# Time Menu Overview

The radio includes a clock capable of displaying the **time of day** and, optionally, the **day of the week** on the screen. The radio does **not retain time information when powered off**. As a result, if the clock is required, it must be set each time the radio is powered on.  
  
The clock and received signal dBm indicator share the same screen position. Under normal conditions (squelch closed), the time is displayed. When a signal is received and the squelch opens, the display temporarily switches to show the signal strength in dBm.  
  
The clock can be set in the following ways:

- **GPS**  
  If GPS is enabled, a successful GPS lock will automatically set the clock.  
  See [Radio > Operating Modes → GPS](https://github.com/nicsure/RMS880/wiki/GPS-Mode)

- **FM Broadcast (RDS)**  
  When in Tuner mode, tuning to an FM broadcast station that supports **RDS** will automatically set the clock.  
  See [Operating Modes → Tuner](https://github.com/nicsure/RMS880/wiki/Tuner-Mode)

- **Manual Configuration**  
  The clock can be set manually using the menu options described below.

---

## Time Zone

When set automatically via GPS, the clock is synchronized to **GMT (UTC)**.  
This setting applies a positive or negative offset to convert GMT to local time.

- Range: **−12 to +14 hours**

---

## Day of Week

Manually sets the current day of the week.

- Available values: **MON** through **SUN**

---

## Hours

Manually sets the current hour of the day.

- Range: **0 to 23**

---

## Minutes

Manually sets the current minute.

- Range: **0 to 59**

---

## Format

Selects how the time is displayed on the screen.

- **24 Hour**  
  Displays the weekday and time in 24-hour format.  
  Example: `MON 23:21`

- **12 Hour**  
  Displays the time in 12-hour format with an AM/PM suffix.  
  Example: `4:20 PM`

---

## Enabled

Turns the clock display **on or off**.  
Note: When [Main Menu → Display → S-Meter Perm](https://github.com/nicsure/RMS880/wiki/Display-Menu#s-meter-perm) is `On`, the clock is not shown on the main radio display, instead it is shown under the `Main Menu` when it is open.

- When **Enabled** is `Off`, no time or weekday information is shown on the display or under the `Main Menu`.
