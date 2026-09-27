# Scanning Menu Overview

For a general overview of scanning behaviour and modes, see:  
[Radio → Scanning](https://github.com/nicsure/RMS880/wiki/Scanning)

This menu defines the parameters used for **Frequency (VFO) Scanning**, as well as global scan behaviour.

---

## VFO Start

Sets the **start frequency**, in MHz, used when a Frequency Mode scan is initiated.

---

## VFO Range

Defines the **width of the scan range**, in MHz.

The scan end frequency is calculated as: End Frequency = Start + Range  
The End Frequency is displayed in the 'Extra Info' field of the menu.


---

## VFO Step

Sets the **step size**, in kHz, between each scanned frequency.

---

## Scan Return

Defines which frequency the VFO will be set to when a scan is stopped.

Available options:

- **Last Signal**  
  Sets the VFO to the last detected active signal.

- **Last Scanned**  
  Sets the VFO to the last frequency checked by the scanner.

- **Start**  
  Returns the VFO to the scan start frequency.

---

## VFO Modulation

Sets the modulation mode used during a Frequency Mode scan.

Available options:
- **FM**
- **AM**
- **DSB**
- **Automatic**

When set to **Automatic**, the modulation is selected based on the **band plan default** for the start frequency.

See:
- [Main Menu → Band Plan → Modulation](https://github.com/nicsure/RMS880/wiki/Band-Plan-Menu#modulation)
- [RMS → Band Plan](https://github.com/nicsure/RMS880/wiki/Band-Plan-Tab)

---

## VFO Bandwidth

Sets the receiver bandwidth used during a Frequency Mode scan.

Available options:
- **Wide**
- **Narrow**
- **Automatic**

When set to **Automatic**, the bandwidth is selected based on the **band plan default** for the start frequency.

See:
- [Main Menu → Band Plan → Bandwidth](https://github.com/nicsure/RMS880/wiki/Band-Plan-Menu#bandwidth)
- [RMS → Band Plan](https://github.com/nicsure/RMS880/wiki/Band-Plan-Tab)

---

## Save Ignores

Controls whether the scan exclusion list persists.

- **On**  
  Excluded frequencies are saved between scans and power cycles.

- **Off**  
  The exclusion list is cleared at the start of each new scan.

See:  
- [Radio → Scanning → Exclusions](https://github.com/nicsure/RMS880/wiki/Scanning#scanning-exclusions)
- [RMS → Scanning → Exclusions Tab](https://github.com/nicsure/RMS880/wiki/Scanning-Tab#exclusions-tab)

---

## Clear Ignores

Immediately clears the current scan exclusion list.

See:  
[Radio → Scanning → Exclusions](https://github.com/nicsure/RMS880/wiki/Scanning#scanning-exclusions)

---

## Ultra Scan Level

Controls how aggressively the **Ultra Scan** acceleration system operates.

- The default value of **12** is suitable for most environments.
- In noisy RF environments, this value may require adjustment.

### Tuning Guidance

Perform a frequency scan and observe the **green LED** on top of the radio:

- **Mostly slow flashes** → Value is too low
- **Constant fast flashes** → Value is too high
- **Mostly fast flashes with occasional slow flashes** → Optimal

See:  
[Radio → Scanning → Ultra Scan](https://github.com/nicsure/RMS880/wiki/Scanning#ultra-scan)

---

## Ultra Scan Time

Sets the analysis time, in **microseconds**, that Ultra Scan spends evaluating each frequency.

- Default: **1500**
- This is an **advanced setting** and should only be adjusted by experienced users.

Notes:
- If set too low, Ultra Scan may never detect active signals.
- If set too high, Ultra Scan performance will degrade significantly.
- This setting directly affects how **Ultra Scan Level** behaves.

---

## Smart Scan

Applies to **Frequency Mode scans only**.

When enabled:
- Active frequencies are remembered
- The scanner revisits these frequencies more frequently

This can significantly increase scan hits over large frequency ranges, but as the list grows, overall scan speed will decrease.

See:
- [RMS → Scanning → Smart List](https://github.com/nicsure/RMS880/wiki/Scanning-Tab#smart-list-tab)
- [Radio → Scanning → Smart Scan](https://github.com/nicsure/RMS880/wiki/Scanning#smart-scan)

---

## Smart Select

Allows the user to browse the Smart Scan frequency memory list.

Each slot contains a remembered frequency along with its **Heat** value (activity score).

When browsing:  
The selected slot’s **frequency** and **heat value** are shown in the **Extra Info** field.  
If a slot is empty, the display will show **"NOT SET"**.

- **Values:** `0–49`  
- **Default:** N/A  


---

## Smart 2 Chan

Creates a new channel using the frequency stored in the Smart Scan slot selected in `Smart Select` above.

After selecting this option:
1. Browse to the desired channel number (1–999).
2. Press **`GREEN`** to confirm and write the channel.
3. Press **`RED`** to cancel.

While selecting a channel number, the **Extra Info** field will indicate whether the chosen channel slot is already in use. If a used channel slot is selected, the existing channel will be overwritten.

- **Values:** `0 (Cancel)`, `1–999`  
- **Default:** `Cancel`

---

## Monitor Time

Defines how long, in seconds, the scanner will monitor a detected signal.

- A value of **0** monitors indefinitely
- Monitoring ends when:
  - This time expires (if non zero)
  - The signal drops
  - The user manually resumes scanning with `UP` or `DOWN`
  - The user adds the detected frequency to the exclusions by pressing `#`

---

## Hold Time

Defines how long, in seconds, the scan will pause **after a signal is lost** before continuing.

This allows the scanner to briefly “hang around” to catch replies or follow-up transmissions.

---

## Scan TX Too?

Applies to **Channel Mode scans**.

- **Off** (default):  
  Only the receive frequency of a channel is scanned.

- **On**:  
  If a channel has a split or offset TX frequency, that frequency will also be scanned.

---

## Save Preset

Saves the current VFO scan settings as a **scan preset**.

- Up to **99 preset slots** are available
- Select a slot and press **GREEN** to save
- The menu’s *Extra Info* field indicates whether a slot is **Free** or **In Use**

See:  
[RMS → Scanning → Presets](https://github.com/nicsure/RMS880/wiki/Scanning-Tab#presets-tab)

---

## Load Preset

Loads a saved scan preset into the current VFO scanning settings.

- Select the desired preset slot
- Press **GREEN** to load

---

## Erase Preset

Deletes a scan preset.

- Select the preset slot to erase
- Press **GREEN** to confirm deletion

---

## Stop Any Key

Enables additional keys to stop a scan in progress.  
When `On`, any key not assigned to a function while scanning will act like `RED` and stop the scan.

