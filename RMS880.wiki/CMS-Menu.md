# CMS (Channel Management System) Menu

The Channel Management System (CMS) menu provides tools for creating, deleting, naming, and organizing channels and channel groups.
### Channel 999
This can be a special channel reserved for APRS use.  
This is the channel to configure with your APRS operating frequency.  
See: [Main Menu → APRS → Enabled](https://github.com/nicsure/RMS880/wiki/APRS-Menu#enabled)

---

## Write To

Saves the currently active VFO or Tuner configuration as a channel.

- The source may be:
  - A frequency-mode VFO configuration
  - An Si4732 Tuner Frequency. See [Operating Modes → Tuner](https://github.com/nicsure/RMS880/wiki/Tuner-Mode)
  - An existing currently selected channel (effectively copying it)
- Select a channel number from **1 to 999** and press **GREEN** to confirm
- The menu’s *Extra Info* field indicates whether the selected channel slot is **in use** or **free**
- If the source was a tuner frequency that supports RDS, the station name will be set as the new channel's name.

---

## Delete

Erases a stored channel and returns it to a free state.

- Operates in the same manner as **Write To**
- Select the channel number to erase and press **GREEN** to confirm
- The *Extra Info* field indicates whether the selected channel is currently in use

---

## Channel Name

Duplicate menu entry.

See:  
[Main Menu → Channel → Channel Name](https://github.com/nicsure/RMS880/wiki/Channel-Menu#channel-name)

---

## Add Group / Rem Group

**Channel and Group modes only**

Adds or removes group membership for the currently selected channel.

- Use the `UP/DOWN` keys to select a group letter (**A–Z**)
- Press **GREEN** to confirm the action

A channel may belong to multiple groups (up to 4) simultaneously.

Adding groups to Tuner based channels is pointless.

The extra info field will display the selected channel's current group membership.  

See: [Radio → Channel Groups](https://github.com/nicsure/RMS880/wiki/Channel-Groups)

---

## Group Name

**Group mode only**

Sets a custom name for the currently selected group.

- Maximum length: **12 characters**
- Press **GREEN** to confirm the new name

Note: Group names may also be configured with the RMS

See:  
- [Radio → T9 Text Entry](https://github.com/nicsure/RMS880/wiki/T9-Text-Entry)
- [Radio → Channel Groups](https://github.com/nicsure/RMS880/wiki/Channel-Groups)
- [RMS → Groups](https://github.com/nicsure/RMS880/wiki/Groups-Tab)