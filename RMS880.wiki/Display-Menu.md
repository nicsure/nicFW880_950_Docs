# Display Menu Overview

The Display menu controls all visual aspects of the LCD, including brightness behavior, battery indicators, signal bars, and power-saving features. These settings allow the display to be optimized for different lighting conditions, usage patterns, and personal preferences.

---

## Batt Style

Sets the visual appearance of the on-screen battery indicator.

| Option   | Description                                   |
|----------|-----------------------------------------------|
| Off      | Battery readout is hidden                     |
| Percent  | Displays remaining charge as a percentage     |
| Icon     | Displays a graphical bar-style icon           |
| Voltage  | Displays battery voltage (up to 8.4 V)        |

**Default:** Icon

---

## Timeout

Defines the period of inactivity (in seconds) before the LCD backlight turns off or dims, depending on the **Dimmed Level** setting.  
The keypad backlight also turns off when timed out.

- **Values:** 0 (Disabled) to 999 seconds  
- **Default:** Disabled

When the LCD is turned off, battery saving features are enabled if configured:
- [Main Menu → Advanced → Battery Save](https://github.com/nicsure/RMS880/wiki/Advanced-Menu#battery-save)

The Keypad LED will also light in sync with the LCD backlight. This can be disabled however:
- [Main Menu → Advanced → Keypad LED](https://github.com/nicsure/RMS880/wiki/Advanced-Menu#keypad-led)

---

## Heartbeat

When the LCD is turned off, this setting controls whether the radio periodically flashes an LED to indicate that it is still powered on.

- **Values:** 0 (Off) to 500 seconds  
- **Default:** 10 seconds

---

## Heartbeat Style

Selects which LEDs are used for the heartbeat indication.  
If set to flash the RX/TX LED, the following behaviour applies
| Battery Level | LED Colour |
|---|---|
| Over 80% | GREEN |
| Below 80%, Above [Batt Low](https://github.com/nicsure/RMS880/wiki/Calibration-Menu#batt-low) | YELLOW |
| Below [Batt Low](https://github.com/nicsure/RMS880/wiki/Calibration-Menu#batt-low) | RED |

- **Values:** Keypad LED, RX/TX LEDs, Both  
- **Default:** Keypad LED

---

## Inverted

When enabled, the LCD colors are inverted. This can improve visibility in bright ambient light conditions.

- **Default:** Off

See Also: [Key Functions → Invert LCD](https://github.com/nicsure/RMS880/wiki/Radio-Mode#invert-lcd)

---

## Gamma

Adjusts the gamma correction of the LCD (similar to contrast).

- **Values:** 0 (Least) to 3 (Most)  
- **Default:** 0

---

## SBar Style

Defines the visual style of the signal strength bar.

| Option        | Description                                           |
|---------------|-------------------------------------------------------|
| Stepped       | Segmented bar, stepped per S-unit                     |
| Solid Step    | Solid bar with visible S-unit steps                   |
| Solid         | Plain solid bar (recommended for inverted mode)       |
| Segmented     | Straight segmented bar                                |

**Default:** Stepped

---

## Day Level

Sets the LCD brightness level when display **Mode** is set to *Day*. This should generally be a bright setting.

- **Values:** 1 (Dimmest) to 31 (Brightest)  
- **Default:** 31

See Also: [Key Functions → Day/Night Mode](https://github.com/nicsure/RMS880/wiki/Radio-Mode#day--night-mode)

---

## Night Level

Sets the LCD brightness level when display **Mode** is set to *Night*. This should generally be a dimmer setting.

- **Values:** 1 (Dimmest) to 31 (Brightest)  
- **Default:** 5

See Also: [Key Functions → Day/Night Mode](https://github.com/nicsure/RMS880/wiki/Radio-Mode#day--night-mode)

---

## Dimmed Level

Defines the LCD brightness level used after the inactivity **Timeout** expires.

- **Values:**  
  - 0: Disabled (screen turns completely off)  
  - 1–31: Brightness level  
- **Recommended:** 1  
- **Default:** Disabled

---

## Mode

Selects the current LCD brightness mode.

- **Values:** Day, Night  
- **Default:** Day

See Also: [Key Functions → Day/Night Mode](https://github.com/nicsure/RMS880/wiki/Radio-Mode#day--night-mode)

---

## VFO Dim Level

Controls how much inactive VFOs are dimmed relative to the active VFO.

- **Values:**  
  - 0: No dimming  
  - 1–9: Increasing dim level  
  - 10: **Focus Mode**

**Focus Mode:**  
When set to 10, inactive VFOs are not drawn at all and the active VFO expands to fill the display.

See Also: [Key Functions → Focus Mode](https://github.com/nicsure/RMS880/wiki/Radio-Mode#focus)

---

## Wake LCD On

Defines which events will wake the LCD when it has timed out.

| Option      | Description                                                  |
|-------------|--------------------------------------------------------------|
| TX          | Wake on transmit or keypad interaction                      |
| RX          | Wake on received signal or keypad interaction               |
| Keys Only   | Wake only on keypad interaction                             |
| All         | Wake on all events                                          |

**Default:** All

---

## S-Meter Perm

- **Values:** `On`, `Off`  
- **Default:** `Off`

When set to `On`, the signal meter is displayed **permanently**, rather than only appearing when the squelch is open.

Because the dBm readout shares the same screen position as the clock, enabling this option **disables the clock display** on the main radio screen. The clock is not lost, it will still be shown whenever the **Main Menu** is opened providing the clock display is enabled.

See: [Main Menu → Time → Enabled](https://github.com/nicsure/RMS880/wiki/Time-Menu#enabled)

