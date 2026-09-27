# Scanning Tab Overview

The **Scanning** tab provides tools for configuring and managing scan-related behaviour used by the radio. It allows you to define reusable scan ranges, manage ignored (excluded) frequencies, and inspect the frequency memory used by the Smart Scan system.

This tab is divided into three sub-tabs:

- **Presets** — pre-configured frequency scan ranges  
- **Exclusions** — the scan ignore list  
- **Smart List** — frequencies remembered by Smart Scan  

For detailed information on how scanning behaves on the radio itself, see:
- [Radio → Operation → Scanning](https://github.com/nicsure/RMS880/wiki/Scanning)

---

# Presets Tab

The **Presets** tab manages the **99 available scan presets**.

A list of all presets appears on the left side of the tab. Selecting a preset populates the controls on the right with that preset’s configuration.

## Preset Controls
For more details on these scan settings see:
[Main Menu → Scanning](https://github.com/nicsure/RMS880/wiki/Scanning-Menu)

### Active

Enables or disables the selected scan preset.

- Unticking this option effectively deletes the preset

### Name

A descriptive name for the scan preset.

- Maximum length: **14 characters**

### Start

The starting frequency of the scan range, in **MHz**.

### End

The ending frequency of the scan range, in **MHz**.

### Step

Defines the spacing between scanned frequencies, in **kHz**.

### Mode

Selects the modulation mode used during the scan.

### Bandwidth

Selects the bandwidth setting used during the scan.

### Ultra Scan

Controls the sensitivity of the **Ultra Scan** acceleration system.

### Monitor Time

Defines how long (in seconds) a detected frequency will be monitored before the scan continues.

- A value of **0** causes the scan to remain on the frequency until the signal drops

### Hold Time

Defines how long (in seconds) the scan will pause **after a signal is lost** before resuming.  
This can be useful for catching replies during conversations.

# Exclusions Tab

The **Exclusions** tab displays the list of up to **50 ignored frequencies or channels** currently stored in the radio.

Ignored frequencies or channels are added automatically when the user presses `#` on the radio during a scan. Once added, these are skipped during future scans, which is useful for avoiding nuisance signals.

Selecting a slot allows the frequency or channel to be edited, created, or cleared using the controls on the right.

- Setting a slot’s frequency & channel to **0** disables it and frees the slot for reuse
- [Main Menu → Scanning → Save Ignores](https://github.com/nicsure/RMS880/wiki/Scanning-Menu#save-ignores) must be set to `On` for this tab to function.

---

# Smart List Tab

When **Smart Scan** is enabled, the radio remembers frequencies that were detected as busy during scans and revisits them more frequently. This can significantly increase the number of scan hits across large frequency ranges.

The **Smart List** tab allows these remembered frequencies to be:

- Read from the radio  
- Inspected and exported  
- Copied and pasted into the **Channels** tab  

This provides a convenient way to turn frequently active scan hits into permanent channels.
