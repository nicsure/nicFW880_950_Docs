# User Keys Menu Overview

The User Keys menu allows the user to assign custom functions to keypad and side-button presses. Both short and long presses can be configured, enabling quick access to commonly used features.

User key assignments can also be configured using the RMS application.  
See: [RMS → User Keys](https://github.com/nicsure/RMS880/wiki/User-Keys-Tab)

---

## Key

Selects the physical key and press type to be configured by the **Function** menu below.

- The selected key is shown as a numeric value from **0 to 21** in the standard menu value field
- The *Extra Info* field displays:
  - The friendly name of the selected key
  - The function currently assigned to it

### Key Friendly Names

Each key entry is prefixed with a press type:

- **SP** — Short Press (pressed and released quickly)
- **LP** — Long Press (pressed and held for approximately one second)

The press type is followed by the key identifier:

- `Grn` — Green key (top-left of the keypad)
- `Red` — Red key (top-right of the keypad)
- `0–9`, `*`, `#` — Standard keypad keys
- `S1` — Side button under main PTT
- `S2` — `RT-880`:Bottom side button / `RT-950`:Second from bottom
- `S3` — `RT-950 Only`:Bottom side button
- `EMG` — `RT-880 Only`:Top round orange button

---

## Function

Assigns a function to the key selected in the **Key** menu.

For a complete list and detailed descriptions of available functions, see:  
[Operating Modes → Radio → Key Functions](https://github.com/nicsure/RMS880/wiki/Radio-Mode#key-functions-and-the-function-menu)

---

## Save

Unlike most menu settings, user key assignments are **not** saved automatically.

After completing any changes, select **Save** to commit the new key mappings to storage.  
If this step is skipped, all changes will be lost when powering off the radio.
