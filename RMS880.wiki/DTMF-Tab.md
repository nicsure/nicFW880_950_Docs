# DTMF Tab Overview

The **DTMF** tab allows you to pre-configure up to **99 DTMF sequences** for later use.  
DTMF usage, transmission behaviour, and related radio-side settings are documented in detail here:

[Main Menu → DTMF](https://github.com/nicsure/RMS880/wiki/DTMF-Menu)

---

## Preset Slots

All **99 DTMF preset slots** are displayed in a list on the left side of the tab.

To create, edit, or delete a preset:

1. Select a slot from the list on the left by clicking on it. It will highlight to indicate it is selected.
2. The slot’s current information _(if any)_ will appear in the controls on the right  
3. Use the controls to configure the selected slot  

As changes are made, the slot list updates in real time to reflect the current configuration.

Slot **#99** is reserved and is used to define the DTMF PTT-ID to be used when PTT-ID is active.
- See: [Main Menu → Channel → PTT ID](https://github.com/nicsure/RMS880/wiki/Channel-Menu#ptt-id)

---

## Slot Controls

### Active

Enables or disables the selected preset slot.

- A slot must be **active** before it can be edited
- Deactivating a slot effectively deletes its contents


### Name

Sets a descriptive name for the preset.

- Maximum length: **14 characters**


### Digits

Defines the DTMF digit sequence for the preset.

- Valid characters: `0–9`, `*`, `#`, `A–D`
- Maximum length: **14 digits**

---

DTMF presets configured here are available for use throughout the radio wherever DTMF functions are supported.