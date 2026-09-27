# Fonts Tab Overview

The **Fonts** tab allows visual customization of the radio by assigning different textual fonts. These fonts are **bitmapped, monospaced fonts** encoded in **column-major** format. In this format, bit data is stored column by column, from left to right and top to bottom.

---

## Supported Font Sizes

The following font sizes can be customized:

- 8×8 (ASCII)
- 8×16 (ASCII)
- 16×16 (ASCII)
- 16×24 (ASCII)
- 24×24 (ASCII)
- 24×32 (ASCII)
- 16×16 Symbols (Custom Icons)

---

## Interface Layout

- The **left side** of the tab displays a live preview of all fonts currently loaded into the RMS.
- The **right side** contains the font control panel.

Each font entry is labelled with its pixel dimensions and includes two associated buttons.


## Font Controls

### Load

The **Load** button allows you to browse for a font file compatible with the selected font size.

- The RMS will reject files that do not match the expected file size
- Once loaded, the preview pane updates immediately
- This action loads the font into the RMS **only** and does not modify the radio


### Export

The **Export** button saves the currently loaded font from the RMS to the local machine.  
This can be used to back up fonts or share them with others.

---

## Radio Synchronization

Below the individual font controls are two general buttons used to synchronize fonts with the radio.

### Read

Reads all font data previously written to the radio into the RMS.

- The preview pane updates to reflect the fonts currently stored on the radio
- **Note:** Do not use this function if no custom fonts have been written to the radio  
  The radio’s default fonts are stored in ROM and are not readable.  
  The RMS starts with these default fonts loaded by default, so reading is unnecessary in that case.

### Write

Writes all currently selected fonts in the RMS to the radio.  
This overrides the default fonts or replaces any previously written custom fonts on the device.

---

## Codeplug Note

Fonts are stored as **binary data** and are therefore **not compatible with the combined Codeplug** format.
