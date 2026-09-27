# UI Tab Overview

The **UI** tab is the most complex section of the RMS. It allows you to completely redesign the appearance of the radio’s main display by repositioning visual elements, selecting fonts, and defining colors.

The process of designing or editing the radio’s interface is referred to as **skinning**. UI designs, along with the `.csv` files saved and loaded by this tab, are commonly called **skins**.

Several example skins are included in the `extras.zip` file available from the RMS release page.

Skinning is not an easy task. It can be very time consuming, fiddly and tedious, so be warned before diving into this rabbit hole.

---

# Color Palette

On the left side of the tab is a scrollable list of **predefined color functions**. These colors do not simply represent static colors, they represent **logical functions** that change based on the radio’s state.

Each color entry is labeled with the function it represents.

### Example

The colors **RX Idle**, **RX Open**, and **TX** define the state colors for the active VFO:

- **RX Idle** — Squelch closed  
- **RX Open** — Squelch open (receiving)  
- **TX** — Transmitting  

Any UI element whose foreground or background color is set to **VFO State** will automatically use the appropriate color based on the current radio state.

To change a color, click on the example color box to open a color editor dialog.

---

# Preview

To the right of the color palette is the **preview display**. This is a live mock-up of the radio’s screen.

As you change colors, positions, fonts, or modes, the preview updates immediately to show how the display will look under different operating conditions.

---

# Element List

To the right of the preview is a scrollable list containing **all visual elements** that make up the display.

- Click an element to select it
- Once selected, all of its properties are loaded into the control panel on the right
- Only one element may be edited at a time

---

# Control Panel

The far-right section of the tab is the **control panel**. This is where the selected element’s properties are edited and where various preview simulation options are available.

## Control Panel Items

### Name Label

At the top of the control panel is the name of the currently selected element.

### Cursor Arrows

Convenience buttons used to move the selected element left, right, up, or down.  
These are often easier to use than manually editing coordinates.

### X

The horizontal position of the element.

> **Note:**  
> For VFO child elements, this value is relative to the parent **VFO Box** element’s X position.

### Y

The vertical position of the element.

> **Note:**  
> For VFO child elements, this value is relative to the parent **VFO Box** element’s Y position.

### Width & Height

These values are rarely required for text-based elements, as their size is usually fixed by the font.

Some elements, such as **VFO Box** and **User Rects** do require explicit width and height values.

- Setting **Width** to `0` disables the element entirely and prevents it from being drawn

### FG Color & BG Color (Default)

Defines the default foreground and background colors for the element.

- Setting a color to **Alpha** makes it transparent.
  - Note: Transparency is a bit of a misnomer, it merely means to use the same color as the the VFO's background color.
- These colors are used when no color function is defined or when the radio state does not match a defined function (for example, inactive VFOs)
- To change, click the color example box to open a color editing dialog. 

### FG Color Function & BG Color Function

Causes the element's background or foreground color to change based on a particular radio state. Use the pulldown list to select the particular radio state to associate with the element. The colors for each individual state can be edited using the color palette on the left hand side of the tab.

### Justification

For text-based elements, defines whether the text is **left-justified** or **right-justified**.

### Font

Selects which font is used to render the selected text-based element.

### Signal / Power Level

Controls the signal level or TX power level displayed by the preview’s signal meter.

### Noise / Mod Level

Controls the noise bar level shown in the preview.

### Battery Level

Sets the battery level displayed in the preview.

The battery element respects the **battery-level color functions** when rendering.


### VFO Status

Changes the preview to simulate different radio states:

- **Squelch Closed** — Idle state  
- **Squelch Open** — Receiving a signal  
- **TX** — Transmitting  
- **Scanning** — Active scan  
- **Scan Monitor** — Monitoring a detected scan hit  

### VFO Mode

Changes how the preview represents different VFO operating modes:

- **VFO** — Frequency mode  
- **Channel** — Channel mode  
- **Group** — Group mode  

### Channel Name Length

Defines the maximum number of characters that the **Channel Name** element can display without overlapping other elements or running off the right of the screen. 

This is particularly important when using **right justification**. It is also crucial for the correct operation of [scrolling channel names](https://github.com/nicsure/RMS880/wiki/Advanced-Menu#name-scroll).

### Menu Open

Simulates the appearance of the main menu in the preview.

### Menu Selected

When the menu is displayed, simulates how the UI looks while editing a menu option.

### Reset Button

Discards all changes and restores the UI to the **default layout**.

---

## Important Notes

- **Do not read UI data from the radio unless a skin has already been written to it**
- Reading UI data from a radio without a skin will return invalid data
- There is no need to read the default UI from the radio, as the RMS starts with the same default skin preloaded
