# Radio Mode Overview

### Radio mode is the default state of the radio when first powered on, the classic “Walkie-Talkie” experience.

The radio mode operates utilising a Radio System on Chip, the Beken BK48x9. This chip has many capabilities and it is advised you skim the [Datasheet](https://alfaexploit.com/files/BK4819.pdf).

The frequency range of the radio in this operating mode is from **18 MHz** to **1300 MHz** , however there is a "Dead Spot" from 630 MHz to 756 MHz that the chip cannot receive or transmit on.

While Radio mode shares many similarities with other radio models and firmware, providing a familiar environment, there are some notable differences in how nicFW operates that may feel unfamiliar at first.

## Positions (VFOs)

The radio can operate on up to three frequencies or channels simultaneously. Historically, these “positions” are called VFOs (Variable Frequency Oscillators) and are labelled A, B, and C from top to bottom.

![alt](https://github.com/nicsure/RMS880/blob/main/vfo.jpg?raw=true)

Each VFO can operate in its own independent mode.

### VFO Modes
* Frequency Mode  
In Frequency Mode, any valid frequency can be manually entered and used. This mode provides full flexibility for direct frequency operation.
  - Valid frequencies are between **18 MHz** to **1300 MHz**

* Channel Mode  
The radio can store up to 999 pre-programmed channels. Channel Mode provides access to these stored channels for quick selection and operation.  
See: [Main Menu → Channels](https://github.com/nicsure/RMS880/wiki/Channel-Menu)

* Group Mode  
The pre-programmed channels can also be organized into groups (sometimes referred to as “zones” in other radios). Group Mode allows browsing and operating channels according to these groupings for easier management and navigation.  
See: [Radio → Channel Groups](https://github.com/nicsure/RMS880/wiki/Channel-Groups)

---

## Channel Names

When operating in **Channel Mode** or **Group Mode**, the channel’s configured name is displayed on the VFO.  
Each channel supports a name of up to **30 characters**, however the amount of text that can be shown on screen depends on the selected font and UI layout.

If a channel name exceeds the available display space, the text may be **scrolled horizontally** to allow the full name to be read. Scrolling behavior is configurable and can be adjusted or disabled entirely.

See:
- [Main Menu → Advanced → Name Scroll](https://github.com/nicsure/RMS880/wiki/Advanced-Menu#name-scroll)
- [RMS → UI](https://github.com/nicsure/RMS880/wiki/UI-Tab)

---

## Signal Meter

The signal meter displays the strength of incoming signals. It consists of a graphical bar and a numeric **S-unit** readout, as well as more precise **dBm values** for both the signal level and the signal floor.

A thin auxiliary bar indicates the amount of **Ex-Noise (external noise)** currently being received. The meter also displays the current radio state (**RX** or **TX**), and during transmission the signal meter doubles as a **power output meter**.

The signal meter is fully customizable by the user. By default, it appears as shown below:

![alt](https://github.com/nicsure/RMS880/blob/main/signalbar.jpg?raw=true)

See:
- [RMS → UI](https://github.com/nicsure/RMS880/wiki/UI-Tab)
- [Main Menu → Display → SBar Style](https://github.com/nicsure/RMS880/wiki/Display-Menu#sbar-style)

---

## Battery Level

The radio screen displays the current battery level. The style of the battery read out is configurable by [Main Menu → Display → Batt Style](https://github.com/nicsure/RMS880/wiki/Display-Menu#batt-style).

(**_RT-880 Only_**) A `Lightning Bolt` icon will be shown next to the battery readout when the battery is being charged.

---

# Controls
## SP-RED (_RT-880_) | SP-VM (_RT-950_)
Switches the active position (VFO) between Frequency, Channel, and Group modes.
* To switch to Channel Mode, at least one pre-programmed channel must exist.
* To switch to Group Mode, at least one pre-programmed channel must be assigned to a group.

## SP-# (_RT-880)_ | SP-ABC (_RT-950_)
Cycles the active position (VFO) between A, B, and C.

> Note: RT-880 only. nicFW has historically used the above key combinations consistently across all supported radios.
However, the RT-880’s native firmware implements these functions in reverse. To accommodate this difference, a setting is provided to swap the behavior of SP-RED and SP-#.  
See: [Main Menu → Advanced → #/Red Mode](https://github.com/nicsure/RMS880/wiki/Advanced-Menu#red-mode)

## `RT-880`:SP-GREEN / `RT-950-Pro`:SP-BLUE
Opens the Main Menu.

## `RT-880`:LP-GREEN / `RT-950-Pro`:LP-BLUE
Opens the Function Menu.

## UP / DOWN
Behaviour depends on the active mode:
* Frequency Mode : Increases or decreases the active position’s frequency by the configured step size.  
See: [Main Menu → VFO → Step](https://github.com/nicsure/RMS880/wiki/VFO-Menu#step)
* Channel Mode : Selects the next or previous pre-programmed channel.
* Group Mode : Selects the next or previous pre-programmed channel that is a member of the currently selected group.

## LEFT / RIGHT (_RT-950 Only_)
Behaviour depends on the active mode:
* Frequency Mode : Increases or decreases the active position’s frequency by 10 times the configured step size.  
See: [Main Menu → VFO → Step](https://github.com/nicsure/RMS880/wiki/VFO-Menu#step)
* Channel Mode : Skips 10 channels back or forward.
* Group Mode : Selects the next or previous group.

## PTT (or Muti-PTT)
If transmission is permitted, begins transmitting on the selected frequency or channel _(on the relevant VFO in the case of Multi-PTT)_.  
Also see: [Main Menu → VFO → Multi-PTT](https://github.com/nicsure/RMS880/wiki/VFO-Menu#multi-ptt)

## Numeric Keys (0–9)
(Note: 0 is not used for channel selection in Group Mode on the RT-880)
* Frequency Mode  
Begins entry of a new frequency. The first key pressed becomes the first digit; subsequent keys enter additional digits.  
Press * to enter a decimal point  
Press GREEN or # to confirm the entry  
Press RED to abort entry
* Channel Mode  
Begins entry of a channel number from 1 to 999.  
Press GREEN or # to confirm the selection.  
Press RED to abort entry.  
_If the entered channel does not exist, the closest configured channel is selected._
* Group Mode
Functions the same as Channel Mode. If the entered channel is not a member of the selected group, the closest channel within that group will be selected instead.

## 0 and * (_RT-880 Group Mode Only_)
Selects the previous or next group.

---

# Transmit Controls

While **PTT** is engaged, additional keys become available to perform transmit-specific functions.


## DTMF Transmission

When transmitting, the keypad can be used to send **DTMF tones**.

**Key mappings:**

- `0–9`, `*`, `#` → Send their respective DTMF tones
- **GREEN** → A
- **UP** → B
- **DOWN** → C
- **RED** → D

---

## Side Key S1 — Manual APRS Beacon

When **APRS** is enabled, pressing **S1** during transmission sends a **manual APRS beacon** on the **currently transmitting frequency**.

> ⚠️ **Important**  
> This does **not** transmit on the VFO assigned for APRS operation.  
> The beacon is sent strictly on the active transmit frequency.

See:  
[Radio → APRS](https://github.com/nicsure/RMS880/wiki/APRS-Menu)

---

## Side Key S2 — Repeater Tone

Pressing **S2** transmits a **legacy repeater access tone**.

- Default tone: **1750 Hz**
- The tone frequency is user-configurable

> ⚠️ **Note**  
> If you are transmitting using S1 or S2 with Multi-PTT, this key gets redefined to the main PTT key.

See:  
[Main Menu → Advanced → Repeater Tone](https://github.com/nicsure/RMS880/wiki/Advanced-Menu#repeater-tone)


---

# Key Functions and the Function Menu
Key Functions are accessed via LP-GREEN, which opens a dedicated menu containing radio-mode–specific functions.  
Each function in this menu may also be assigned directly to a key press and customized by the user.  
For more information on key customization, see: [RMS → User Keys](https://github.com/nicsure/RMS880/wiki/User-Keys-Tab) and [Main Menu → User Keys](https://github.com/nicsure/RMS880/wiki/User-Keys-Menu)  
When a function is selected in the menu, its currently assigned key (if any) is displayed beneath the menu for reference.

A video guide regarding the Function Menu can be viewed [HERE](https://www.patreon.com/posts/144892121?collection=1537808)

## Edit TX Frequency
Default Key: LP-RED  
Allows entry of a split (offset) transmit frequency. Frequency entry follows the same rules as RX frequency entry.  
Enter an absolute TX frequency by keying in the value directly.  
Enter an offset TX frequency by pressing UP or DOWN to indicate the entered value is relative to the RX frequency. When an offset is selected, a + or - symbol appears next to the input field.  
Press `*` to enter a decimal point  
Press `GREEN` or `#` to confirm entry  
Press `RED` to abort.  
Press `S2` to cancel split frequency mode and remove the TX offset.  

A video guide demonstrating how to do this can be viewed [HERE](https://www.patreon.com/posts/145799458?collection=1537808)

## Reverse TX / RX
Default Key: LP-5  
When operating with a split or offset TX frequency, this function swaps the RX and TX frequencies. When active, an R indicator appears in the VFO display. Activating the function again restores the original configuration.

## Busy Lock
Default Key: LP-6  
Prevents transmission when the squelch is open. When active, a padlock symbol is displayed on the VFO.

## Squelch Override
Default Key: SP-S1  
Forces the squelch open regardless of received signals or tones. While active, the RX/TX indicator area displays OV. Activate the function again to cancel the override.

## Multiwatch
Default Key: SP-9  

Toggles between Off, On and Group settings for Multi Watch.  
When enabled, the radio continuously monitors all three VFOs. Upon receiving a signal, the radio switches to the active VFO.
After the signal ends, the radio either:
* Remains on the detected VFO, or
* Returns to the previously active VFO  
* This behaviour is controlled by [Menu → VFO → MW Keep VFO](https://github.com/nicsure/RMS880/wiki/VFO-Menu#mw-keep-vfo).  

If the VFO being checked is in [Group Mode](https://github.com/nicsure/RMS880/wiki/Radio-Mode#vfo-modes) and Multiwatch is set to `Group` then all channels in the VFO's selected group will also be watched.
- This function is best used with smaller groups. Since each channel in the group must be scanned individually, larger groups will increase the scan cycle time and may significantly impact signal detection latency.

Multiwatch only monitors VFOs that are of the same HF or non-HF band. I.e. if the active VFO is set to a frequency over 70 MHz then only VFOs that are also over 70 MHz will be monitored. Similarly if the active VFO is less than 70 MHz only other VFOs that are also less than 70 MHz will be monitored.  

A circular arrow icon is shown when Multiwatch is active.  
If this setting is set to `Group` then the icon will have a letter `G` inside it.



## Key Lock
Default Key: LP-*  
Locks and unlocks the keypad. When locked, a key icon is displayed on the screen and only PTT and the key assigned to Key Lock remain functional.  
Note: If [Menu → Advanced → PIN](https://github.com/nicsure/RMS880/wiki/Advanced-Menu#pin) is enabled:
* PTT is disabled
* The configured PIN must be entered to unlock the keypad

## Edit RX Frequency
Default Key: LP-0  
In Channel and Group modes, numeric keys are assigned to other functions and cannot initiate RX frequency editing directly. This function must be used to begin editing the RX frequency of a channel.

## Enter Group
Default Key: LP-#  
Available in Group Mode. Allows direct entry of a group number:
* 1 = Group A
* 2 = Group B
* 3 = Group C etc..

## Scan (Menu)
Default Key: LP-3  
Starts a frequency (VFO) or channel scan.
* Frequency Mode: Scans frequencies using configured scan settings in the Main Menu.  
See: [Menu → Scanning](https://github.com/nicsure/RMS880/wiki/Scanning-Menu) and [Radio → Scanning → VFO Scan](https://github.com/nicsure/RMS880/wiki/Scanning#vfo-scanning)
* Channel Mode: Scans all channels that do not require switching to or from the HF band.
* Group Mode: Scans all channels in the selected group that do not require HF switching.  
(Essentially, if the active VFO is in the HF band, then the scanner will only scan other HF channels, if the active VFO is not in the HF band, then the scanner will only scan other non-HF channels)  
See : [Radio → Scanning → Channel/Group Scan](https://github.com/nicsure/RMS880/wiki/Scanning#channel-scanning)

## Scan (VFO)
Default Key: LP-4  
Available in Frequency Mode only. Starts a scan using the current VFO settings, rather than the scan settings defined in the menu.

## Shut Down (_RT-880 Only_)
Default Key: LP-EMG  
Places the radio into a safe shutdown state so it may be powered off. This is only required when the red flash deferral icon is displayed.  
See [Radio → Storage Deferral](https://github.com/nicsure/RMS880/wiki/Storage-Deferral)

## XB Repeater
Default Key: LP-S2  
Enables Cross-Band Repeater mode.  
Requirements:
* VFO A and VFO B must be set to different bands (VHF and UHF)
* Both VFOs must be permitted to transmit

Operation:
* Signals received on either VFO are retransmitted on the other
* Both VFOs appear active
* An XB icon is displayed while active

## Day / Night Mode
Default Key: SP-EMG  
Toggles the LCD between Day and Night display modes. Night mode is typically dimmer. Brightness levels for both modes are configurable.  
See: [Menu → Display → Day/Night Level](https://github.com/nicsure/RMS880/wiki/Display-Menu#day-level)  
A crescent moon icon is displayed in Night mode.

## Frequency Counter
Default Key: LP-7  
Also known as a Fast Frequency Scanner on other radios. Rapidly scans for strong signals and locks onto them quickly. The scan is limited to the band (HF or non-HF) on which it is initiated.  
[Main Menu → VFO → Tone Monitor](https://github.com/nicsure/RMS880/wiki/VFO-Menu#tone-monitor) will be temporarily set to 'Clone' if it not already set.

This function may only be started in `Frequency Mode`  
See: [Radio → VFO Modes](https://github.com/nicsure/RMS880/wiki/Radio-Mode#vfo-modes)

A video guide on using this feature can be found [HERE](https://www.patreon.com/posts/148366675)

## Invert LCD
Default Key: LP-S1  
Toggles the LCD between normal and inverted display modes. Inverted mode can improve readability in bright ambient light.  
See: [Main Menu → Display → Inverted](https://github.com/nicsure/RMS880/wiki/Display-Menu#inverted)

## Si4732 Tuner
Default Key: LP-8  
Enters Tuner mode. See: [Radio Modes → Tuner](https://github.com/nicsure/RMS880/wiki/Tuner-Mode)

## Spectrum Scope
Default Key: LP-2  
Enters Spectrum Scope mode. See: [Radio Modes → Scope](https://github.com/nicsure/RMS880/wiki/Spectrum-Scope-Mode)

## Scan Presets
Default Key: LP-1  
Displays a menu of pre-configured Frequency Mode scan presets.  
* Use UP/DOWN to browse presets
* Press RED to exit without starting a scan  
See: [RMS → Scanning](https://github.com/nicsure/RMS880/wiki/Scanning-Tab#presets-tab) and [Main Menu → Scanning](https://github.com/nicsure/RMS880/wiki/Scanning-Menu)

## DTMF Presets
Default Key: SP-S2  
Displays a menu of pre-configured DTMF tone sequences.
* Use UP/DOWN to browse sequences
* Press RED to exit without transmitting  
* LP-GREEN to edit the name of the selected sequence.
* PTT to begin transmitting and send the selected sequence.

See: [RMS → DTMF](https://github.com/nicsure/RMS880/wiki/DTMF-Tab) and [Main Menu → DTMF](https://github.com/nicsure/RMS880/wiki/DTMF-Menu)

## Chan 2 VFO
Default Key: None  
Available in Channel and Group modes only. Copies the currently selected channel into Frequency Mode on the VFO.

## DTMF Speed Dial
Default Key: None  
When assigned to LP-0 through LP-9, transmits the DTMF preset associated with the corresponding numeric slot.

## GPS
Default Key: None  
Enters GPS operating mode. See: [Operating Modes → GPS](https://github.com/nicsure/RMS880/wiki/GPS-Mode)

## Enter DTMF
Default Key: None  
Allows manual entry of a DTMF sequence for transmission.  
Key mapping:
* 0–9, *, # → Enter themselves
* GREEN = A
* UP = B
* DOWN = C
* RED = D
* PTT to transmit
* S2 to cancel

## Beacons
Default Key: None  
Displays a list of received APRS beacons.
* Beacons are numbered #1–#50. #1 is the most recently received
* Use UP/DOWN to browse
* Press RED to exit
* Press GREEN to set the beacon location as the current GPS navigation target.

See: [Radio → APRS](https://github.com/nicsure/RMS880/wiki/APRS-Menu)

## Weather
Default Key: None  
If a Weather APRS packet has been received, displays the decoded weather data. Press RED to exit.
See: [Radio → APRS](https://github.com/nicsure/RMS880/wiki/APRS-Menu)

## TX Power Up / TX Power Down
Default Key: None  
Increases or decreases the transmit power level of the active VFO.  
See: [Main Menu → Channel → TX Power](https://github.com/nicsure/RMS880/wiki/Channel-Menu#tx-power)

## Focus
Default Key: None  
Toggles Focus Mode on and off. Focus mode changes the layout of the main display so that only the active VFO is visible. The VFO is stretched to fill the whole screen.  
See [Main Menu → Display → VFO Dim Level](https://github.com/nicsure/RMS880/wiki/Display-Menu#vfo-dim-level)

## FM
Default Key: None  
Switch the modulation to **FM**.  
See: [Main Menu → Channel → Modulation](https://github.com/nicsure/RMS880/wiki/Channel-Menu#modulation)

## AM
Default Key: None  
Switch the modulation to **AM**.  
See: [Main Menu → Channel → Modulation](https://github.com/nicsure/RMS880/wiki/Channel-Menu#modulation)

## DSB
Default Key: None  
Switch the modulation to **DSB**.  
See: [Main Menu → Channel → Modulation](https://github.com/nicsure/RMS880/wiki/Channel-Menu#modulation)

## Modul Toggle
Default Key: None  
Cycle the modulation between **FM → AM → DSB** in that order.  
See: [Main Menu → Channel → Modulation](https://github.com/nicsure/RMS880/wiki/Channel-Menu#modulation)

## Freq Mode
Default Key: None  
Switches the active VFO directly into Frequency Mode.

## Channel Mode
Default Key: None  
Switches the active VFO directly into Channel Mode.  
Note: _At least one pre programmed channel must exist to enter Channel Mode._

## Group Mode
Default Key: None  
Switches the active VFO directly into Group Mode.  
Note: _At least one pre programmed channel must be a member of any group to enter Group Mode._

## KISS Mode
Default Key: None  
Switches the radio into KISS mode.  
See:
- [Operating Modes → KISS](https://github.com/nicsure/RMS880/wiki/KISS-Mode)

## Scan MGroups (Multiple Group Scan)
Default Key: None  
Starts a **Group Mode scan** that can operate across multiple groups simultaneously. Unlike the standard group scan, which scans only a single group, this function allows you to scan **up to four groups at once**.  
When started, you will be prompted to enter up to **four group letters (A–Z)**. The scanner will then cycle through each selected group in turn.  
This feature is useful for monitoring several related channel groups without needing to merge them into a single group.
- Notes
  - Channels may belong to **more than one group**.
  - If the selected groups share common channels, those channels will be scanned **more frequently**, as they appear in multiple group cycles.
  - Only valid (used) groups will be accepted.
  - Only groups that have at least one channel that matches the current VFO' frequency band, either below or above 70 MHz will be accepted.

See:
- [Radio → Scanning → Multi Group Scanning](https://github.com/nicsure/RMS880/wiki/Scanning#multi-group-scanning)
- [Radio → T9 Text Entry](https://github.com/nicsure/RMS880/wiki/T9-Text-Entry)

## APRS On/Off
Default Key: None  
Enables and Disables APRS & GPS operation with a single toggling function. When re-enabling, the function will restore the same APRS mode that was active when APRS was previously disabled using this function.  
See:
- [Main Menu → APRS → Enabled](https://github.com/nicsure/RMS880/wiki/APRS-Menu#enabled)

## Keypad LED
Default Key: None   
Enables/Disables the keypad backlight.  
See:
- [Main Menu → Advanced → Keypad LED](https://github.com/nicsure/RMS880/wiki/Advanced-Menu#keypad-led)

## Beacon NOW
Default Key: None  
Immediately sends an APRS beacon on the assigned APRS VFO or Channel 999.  

## Wipe Beacons
Default Key: None  
Erases all previously received APRS beacons from the radio's memory.  