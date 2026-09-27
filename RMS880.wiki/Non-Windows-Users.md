# macOS and Linux

RMS builds for **macOS** and **Linux** are available and linked from the nicFW release posts.

Because the RMS is developed on Windows, packaging non-Windows releases with the correct file permissions and operating-system–specific flags is more complex. As a result, Linux and macOS releases are provided primarily as **`.zip` archives** containing the required binaries and libraries. After extracting these files, users must manually set the appropriate execution permissions.

This process is usually familiar to Linux users but can be less intuitive for macOS users. For this reason, macOS releases are also provided in a standard **App Bundle** format alongside the `.zip` files. However, Mac users must still deal with quarantining and third party app permissions. 

---

## Regarding macOS specifically

At present, the **ARM64 (Apple Silicon)** builds of the RMS for macOS are **not functional**. Users should instead use the **x64** version, which works correctly under Rosetta. ARM64 builds continue to be compiled and released in the hope that the issue can be identified, either by an experienced user or through future fixes in **Avalonia**, the application framework used by the RMS.

For reasons that are still under investigation, macOS Tahoe 26.3 or earlier currently operate **only at 38,400 baud**, however macOS Tahoe 26.4 or later fix this issue and faster speeds are available.

