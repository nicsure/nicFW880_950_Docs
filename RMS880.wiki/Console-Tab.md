# Console Tab Overview

The Console tab provides low-level serial communication with the radio. Two data modes are available: Text and Hex.  

This tab is primarily intended for developers and advanced users who wish to test CAT commands and programming packets. It may also be used as a debug console at the request of the developer to help diagnose difficult or intermittent issues.

Ensure the correct Serial Port is selected before starting a console session.

While a console session is active you may not switch tabs until you end the session.

---

## Text Console

To start a Text Console session, click the `Text Console` button. The border of the text console window will turn orange, and the text input box below will become active. You may then enter commands into the input box. The console window will display any text returned by the radio.
- See: [Technical Info → CAT Commands](https://github.com/nicsure/RMS880/wiki/CAT-Commands)

The developer may occasionally request that you activate this console and report any output for debugging purposes.

To terminate the session, click the `Text Console` button again. The orange border will disappear, and the text input box will be deactivated.

---

## Hex Console

To start a Hex Console session, click the `Hex Console` button. The border of the hex console window will turn orange, and the input box below will become active. You may then enter raw hexadecimal data to communicate directly with the radio.

Hexadecimal data must be entered as pairs of hexadecimal digits.  
Example: `94 A7 2B AF`

The console window will display data received from the radio in the same hexadecimal format.

- See [Technical Info → Serial Protocol](https://github.com/nicsure/RMS880/wiki/Serial-Protocol)

The developer may occasionally request that you activate this console and report any output for debugging purposes.

To terminate the session, click the `Hex Console` button again. The orange border will disappear, and the input box will be deactivated.

---