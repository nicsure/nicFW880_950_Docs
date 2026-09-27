# Codeplug Tab Overview

The **Codeplug** tab allows multiple RMS configuration sections to be combined into a single file. The following tabs are included:

- Channels  
- Groups  
- User Keys  
- Band Plan  
- Scanning  
- DTMF  
- GPS / APRS  
- Settings  

This makes it possible to perform a **complete backup or restore** of most radio configuration data in one step, which is significantly faster and more convenient than managing each tab individually.

---

## Excluded Tabs

The following tabs are **not** included in the Codeplug:

- Power  
- Calibration  
- Fonts  
- UI  

These sections are excluded because they either:
- Contain binary data that is not compatible with the `.csv` format  
- Store device-specific calibration values  
- Control visual or aesthetic preferences rather than operational configuration  

This separation helps ensure Codeplugs remain portable, safe to share, and broadly compatible across devices.