## RMS Serial Ports & Baud Rate

Communication between the **RMS** and the radio occurs over a **serial programming cable**.

* _(RT-880 Only)_ Although the RT-880 includes a USB-C port, a standard USB-C to USB-A cable **only supports battery charging** and **cannot be used for data communication**.

A **USB cable specifically designed for the RT-880 or RT-950** is required. These are available from Radtel and various online marketplaces.  
Search for:  [RT-880 Programming Cable](https://www.google.com/search?q=rt-880+programming+cable).
[RT-950 Pro Programming Cable](https://www.google.com/search?q=rt-950+pro+programming+cable).  
Note: The RT-950 Pro generally comes supplied with a programming cable in the box.

It is recommended to use cables with **quality chipsets**, such as **CH340**.  
Avoid cheaper cables using **Prolific** chipsets, as they are often unreliable.

---

## Port / Baud Controls

The **bottom-right corner** of the RMS application window contains the serial configuration controls.  
These are labeled **`Port/Baud`** and consist of two drop-down selectors.

![text](https://github.com/nicsure/RMS880/blob/main/portbaud.jpg?raw=true)

### Port Dropdown

Displays all serial ports currently detected by your computer.

Select the port associated with your RT-880 programming cable.

If multiple ports are listed, an easy way to identify the correct one is:

1. Open the port dropdown  
2. Unplug the programming cable  
3. Note which port disappears  
4. Plug the cable back in and select that port  



### Baud Dropdown

Allows selection of the communication speed used between RMS and the radio.

Available baud rates range from:

- **38,400** up to **518,400**

The maximum reliable speed depends on:

- Cable quality  
- Radio tolerances  
- Computer hardware and drivers  

Some experimentation may be required to determine the fastest stable setting.

---

## Firmware Flashing Note

The configurable baud rate **does not apply to firmware flashing**.  
Firmware flashing always uses a **fixed baud rate of 115,200**.

---

## macOS Note

⚠ **Important for macOS users**

On macOS versions **Tahoe 26.3** or earlier, **38,400 baud** is the **only working speed**.

Faster speeds are working with **Tahoe 26.4** or later. You may need to experiment to find the fastest reliable speed for your system.

