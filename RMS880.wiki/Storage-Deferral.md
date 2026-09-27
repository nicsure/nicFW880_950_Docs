# Storage Deferral Overview

## _Note: Only the RT-880 uses storage deferral. The RT-950 Pro does not need it as it has a software power on/off system. Thus this section is only relevant for the RT-880._

Like a PC, smartphone, or tablet, the radio contains non-volatile storage used to preserve its settings and operational state. Users generally expect the radio to return to the same state it was in when powered off, which means that nearly every user action must be saved, channel changes, frequency adjustments, and configuration updates.  
  
However, the storage device used in the radio has a limited write endurance, typically rated for approximately 100,000 write cycles. Exceeding this limit can result in permanent storage failure, rendering the radio unusable.  
  
To protect the storage device and extend the radio’s usable lifespan, nicFW employs an aggressive strategy to minimize write operations. This mechanism is referred to as Storage Deferral.
  
  
  
## How It Works

When a change would normally require a write to storage, the update is first placed into a temporary buffer rather than being written immediately. Multiple changes can then accumulate in this buffer and are later committed to storage in a single write operation.  
  
By consolidating many small writes into fewer large ones, Storage Deferral dramatically reduces the total number of write cycles over the lifetime of the device.  
  
The amount of time changes remain buffered before being written is user-configurable.  
See: [Main Menu → Advanced → SPI Deferral](https://github.com/nicsure/RMS880/wiki/Advanced-Menu#spi-deferral)
  
  
  
## Impact on User Experience

When there are pending changes waiting to be written to storage, a red warning triangle is displayed on the main screen.  
If the radio is powered off while this indicator is visible:
* The pending changes will be discarded
* No corruption or damage will occur
* The radio will simply revert to the last saved state on the next power-up

To ensure all changes are preserved, you may:
* Wait for the warning triangle to disappear, indicating that storage has been updated, or
* Use `Main Menu → Shut Down` to place the radio into a safe state before powering it off