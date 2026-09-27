## Spectrum Scope Mode Overview

The Spectrum Scope provides a graphical view of signal activity across a range of frequencies.

It can be started by executing  
[Key Functions → Scope](https://github.com/nicsure/RMS880/wiki/Radio-Mode#spectrum-scope) (default key: **LP-2**)  
while in **frequency mode**.

![alt](https://github.com/nicsure/RMS880/blob/main/scope.jpg?raw=true)

---

## Frequency Entry

### 0–9 — Enter Centre Frequency

Begins entry of a new centre frequency in MHz.

- `*` enters a decimal point  
- `GREEN` or `#` confirms entry  
- `RED` cancels entry  

---

## General Controls

### SP-RED — Exit Scope

Exits Spectrum Scope and returns to Radio Mode.

### SP-GREEN — Main Menu

Opens the main menu.

### LP-GREEN — Function Menu

Opens the Scope Function Menu.  
The menu lists all available scope functions and their associated key shortcuts.  
Functions may also be executed directly from this menu.

---

## Navigation

### UP — Roll Left

Increments the centre frequency upward by the current step value.

- Short press: one step  
- Long press: continuous stepping  

### DOWN — Roll Right

Same as **Roll Left**, but in the opposite direction.

### SP-# — Set Strongest

Sets the centre frequency to the currently strongest detected signal.

---

## Monitoring Functions

Certain actions and events will pause the scope display and switch the radio into receive mode on a user request or detected signal. Reception continues until the the user intervenes or the signal is lost in the case of trigger events.

### SP-S2 — Monitor High

Opens the squelch and receives on the strongest signal currently visible on the scope.

### SP-S1 — Monitor Centre

Opens the squelch and receives on the current centre frequency.

### LP-1 to LP-9 — Set Trigger Level

Sets the signal strength threshold required to trigger monitoring.

A horizontal blue line appears on the scope display indicating the trigger level.

- **1** – Lowest trigger threshold  
- **9** – Highest trigger threshold  

### LP-0 — Cancel Trigger

Removes the active monitor trigger.  
The blue trigger line will disappear.

### SP-# — Set Ignore

Adds the currently monitored frequency to the ignore list so it will not trigger again.

### LP-RED — Clear Ignores

Clears all entries from the ignore list.

---

## Scope Configuration

### LP-# — Bar Count

Toggles the number of bars displayed in the scope, which also controls the visible frequency span.

**Values:** 16, 24, 48, 60, 80, 120

### LP-* — Edit Step

Allows entry of a new frequency step value in kHz.

- `*` enters a decimal point  
- `GREEN` or `#` confirms entry  
- `RED` cancels entry  

---

## Modulation Selection

### LP-S1 — Set FM

Sets modulation mode to FM.

### LP-S2 — Set AM

Sets modulation mode to AM.

### LP-EMG — Set DSB

Sets modulation mode to DSB.

---

## VFO Interaction

### PTT — Frequency to VFO

Sets the active VFO in Radio Mode to the current center frequency.  
This action does **not** exit Spectrum Scope Mode.
