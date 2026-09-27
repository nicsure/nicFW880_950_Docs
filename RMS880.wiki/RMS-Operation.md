# RMS Overview

The **RMS (Radio Management System)** is the companion desktop application for the radio firmware. It provides a powerful and user-friendly way to configure, manage, and back up virtually every aspect of the radio without needing to navigate menus on the device itself.

Using the RMS, you can configure channels, groups, scanning behavior, band plans, APRS/GPS features, power output, UI skins, key mappings, and more. Changes are made on the computer and then written to the radio over a serial connection, making complex configuration tasks faster, clearer, and far less error-prone than performing them directly on the radio.

RMS versions are tightly coupled to firmware versions. Unless explicitly stated otherwise in a release post, users should always download and use the **matching RMS version** that corresponds to the firmware installed on the radio. Mismatched versions may result in missing features or incorrect behaviour.

Download links for the RMS are provided alongside firmware releases and are available for **Microsoft Windows**, **Linux**, and **macOS**.

---

# RMS Operation Overview

The RMS is organized into a series of tabs, with each tab responsible for configuring a specific aspect of radio operation. You can work with each tab independently, adjusting only the settings you are interested in.

There is also a **Codeplug** tab, which allows you to combine many common configurations into a single file. This is useful for creating backups, sharing configurations, or moving a complete setup between radios.  
See: [RMS → Codeplug](https://github.com/nicsure/RMS880/wiki/Codeplug-Tab)

An important concept is that the RMS does **not** immediately apply changes to the radio. Instead, it maintains its own internal copy of the radio’s storage, think of this as a **working draft**.

As you change settings in the RMS, you are modifying this draft copy, not the radio itself. To apply those changes to the radio, you must explicitly write them.

---

# Configuration Files

All configuration files loaded and saved by the RMS use the **`.csv` (Comma-Separated Values)** format. This is a plain-text format that can be opened and viewed with common tools such as spreadsheet applications or text editors.

Using a text-based format was a deliberate design choice. Files with clearly labeled, human-readable fields are far easier to inspect, edit, back up, and troubleshoot than opaque binary files.

For power users, this makes advanced manipulation and automation straightforward. For everyday users, these files behave just like any other configuration file; load them, save them, and move them around as needed, without requiring any special knowledge of how they work internally.

---

# RMS Tabs – Common Controls

Most RMS tabs include the same four buttons. Understanding what these do will make using the RMS much easier.

## Load
Loads a previously saved `.csv` file into the RMS. This updates the RMS’s working copy and the on-screen settings, but **does not** change anything on the radio.

## Save
Creates a `.csv` file from the current RMS working copy. This is useful for backups or sharing settings. This action **does not** read anything from the radio.

## Read
Reads the relevant settings from the radio into the RMS. This synchronizes the RMS working copy with what is currently stored on the radio.

## Write
Writes the RMS working copy back to the radio. This is the step that actually applies your changes to the device.

---

# Common Tab Tasks

Here's some examples of common tasks you might perform with the RMS tabs.

## Backup of tab configuration
- Switch to the tab responsible for the settings you wish to backup.
- Click `Read` to synchronize the RMS to the radio.
- Click `Save` to create and save a `.csv` file to your computer.

## Restoring tab configuration from backup
- Switch to the tab responsible for the settings you wish to restore.
- Click `Load` and select the `.csv` file created previously.
- Click `Write` to apply the backup to the radio.



