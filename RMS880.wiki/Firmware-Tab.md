# Firmware Tab Overview

The **Firmware** tab provides tools for updating the radio’s firmware, as well as backing up and restoring the radio’s internal storage memory.

A video guide on performing firmware flashing and storage backup operations can be viewed here: [Video Guide](https://www.patreon.com/posts/137941085?collection=1537808)

---

# Firmware Flashing

## Select Radio Model
- Under **Select Radio Model**, choose the radio model you are using:
  - **Radtel RT-880**
  - **iRadio UV-98**
  > **Note:**  
  > For Radtel radios with a serial number **below 300**, you must select **iRadio UV-98**.

## Select Firmware File
Under **Select Firmware File**, click **Browse** and select the firmware binary (`.bin`) file you wish to flash.

## Preparation
Before flashing:  
- Ensure the radio is connected to the computer using an approved **RT-880 or UV-98 programming cable**
- Select the correct **COM port** for your radio in the bottom-right corner of the RMS window  
  > **Note:** The baud rate setting is **not used** for firmware flashing

## Enter Flash Mode

1. Turn **off** the radio  
2. Power it **on while holding the PTT button**  
3. The radio’s screen should remain black and the **green LED** should illuminate  

## Flashing

Click **Flash Firmware** and wait for the process to complete.

> **Important:**  
> When flashing **nicFW**, the progress bar will reach **100%** and then **timeout**.  
> This is normal behaviour. Simply power the radio off and back on to boot into the new firmware.
>
> When flashing **stock firmware**, the radio will automatically reboot when flashing completes.

---

# Storage Backup

## Taking a Backup

It is **strongly recommended** to take a full backup of the radio’s storage chip **immediately after installing nicFW**, before pressing any buttons or interacting with the radio in any way. This backup allows you to fully restore the radio to its original state later.

1. After nicFW boots for the first time, **do not press any buttons**
2. Select a reasonably fast baud rate  
   - This is a long operation; values around **345,600** are typically suitable  
   - Reliable baud rates may vary between radios and may require experimentation
3. Click **Read Flash Image**  
4. Wait for the block counter in the status bar to count down to zero
5. Click **Save Flash Image** and store the backup file in a safe location

> **Important:**  
> After completing a flash backup, **close the RMS completely and restart it** before continuing.

---

## Restoring a Backup

To restore a previously saved flash image:

1. Ensure the radio is powered on and running **nicFW**
2. Click **Load Flash Image** and select your saved backup file
3. Click **Write Flash Image** and wait for the block counter to reach zero
4. Power off the radio

You may now flash the **stock firmware** back onto the radio (see *Firmware Flashing* above).  
Once complete, the radio will be fully restored to its factory state.

If you did not take a backup image, you can download ones that I have taken from new radios here:
- [Flash Backup Images](https://www.patreon.com/posts/141763099?collection=1727030)