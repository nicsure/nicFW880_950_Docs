# All values are little endian

# Current Magic Value Is: 0xABC6
  - Note: Magic values are subject to change, but I try not to do this if I can help it.

## `channelInfo` Structure Definition

```c

#define CHANNAME_MAX_LENGTH 30

typedef struct __attribute__((packed))
{
    u32 rxFrequency; // 0
    u32 txFrequency; // 4 - 10Hz units
    u32 groups; // 8 - each 8 bits represents a group number 1-26 or 0 (slot not filled)
    u16 rxSubtone; // 12 -- 0.1 Hz units for CTCSS
    u16 txSubtone; // 14 -- DCS code | 0x8000 ( | 0x4000 as well for inverted codes)
    s16 clarifier; // 16
    u8 modulation; // 18 - 0 FM, 1 AM, 2 DSB, 3 Auto
    u8 bandwidth; // 19 - 0 Wide, 1 Narrow
    u8 busyLock; // 20 Bool
    u8 txPower; // 21
    u8 reversed; // 22 Bool
    u8 pttID; // 23
    u16 magic; // 24 - If valid, channel is active, if invalid channel is inactive.
    u8 scrambler; // 26
    u8 reserved[5]; // 27
    char name[CHANNAME_MAX_LENGTH]; // 32
} channelInfo;
```

There are a total of 1002 of these structs stacked in the CHANNEL section of the flash memory. Slots 0,1 & 2 are the VFOs, slots 3 to 1001 are the 999 channels.


---

## `settingsInfo` Structure Definition

```c
typedef struct __attribute__((packed, aligned(4)))
{
    u16 magic;
    u16 sigbarStyle;

    u16 squelch;
    u16 squelchNoiseLev;

    u16 noiseCeiling;
    u16 noiseHysteresis;

    u16 squelchThrottle;
    u16 step;

    u16 txTimeout;
    u16 micGain;

    u16 multiWatch;
    u16 multiWatchDelay;

    u16 battStyle;
    u16 lcdTimeout;

    u16 heartbeat;
    u16 lcdInverted;

    u16 lcdGamma;
    u16 scrambleFreqDEFUNCT;

    u16 vox;
    u16 voxTail;

    u16 squelchTailElim;
    u16 txDeviation;

    u16 stDeviation;
    u16 keyLock;

    struct {
        u16 groupChannel[27];
        u8 lastUsedGroup;
        u8 lastGroup;
        u8 isVfo;
        u8 padding[3];
    } groupMem[3];

    u16 spiDeferralTime;
    u16 toneMonitor;

    u16 toneTime;
    u8 activeVfo;
    u8 savedDimLevel;

    u32 scanStart;
    u32 scanRange;

    u16 scanStep;
    u16 ultraScan;

    u16 scanModulation;
    u16 scanBandwidth;

    u16 scanMonitorTime;
    u16 amAgc;

    u16 scanReversed;
    u16 lcdDayLevel;

    u16 lcdNightLevel;
    u16 lcdMode;

    u16 dtmfDev;
    u16 repeaterTone;

    u16 scanPersist;
    u16 noiseGate;

    u16 afFilters;
    u16 lcdDimLevel;

    u16 keyFreq;
    u16 rogerBeep;

    u16 rogerBeepTime;
    u16 multiWatchSwitch;
    
    u16 timeZone;
    u16 gpsSync;    

    u16 gps_unitType;
    u16 gps_rotate;

    u16 gps_range;
    u16 swapHashRed;

    tunerBandInfo tunerBands[6];

    u16 tunerLastChannel;
    u16 aprsHysteresis;

    u8 fmTunerSquelch;
    u8 fmTunerScope;
    u8 tunerBand;
    u8 foobargyy11;

    u16 rssiHysteresis;
    u16 squelchTail;

    s16 amHackTransform;
    u16 amHackDisplacement;

    u16 vfoDimLevel;
    u16 dtmfDigitTime;

    u16 dtmfGapTime;
    u16 dtmfStartPause;

    u16 dtmfDecoding;
    u16 dtmfDisplay4;

    u16 dtmfEndSeq;
    u16 timeFormat;

    u16 wakeLcdOn;
    u16 pinCode;

    u16 pinAction;
    u16 timeEnabled;

    u16 fskDeviation;
    u16 beaconTime;

    u16 beaconDistance;
    u16 beaconTx;

    char beaconComment[25];
    char aprsCallsign[7];

    u16 aprsMonitor;
    u16 aprsSsid;

    u16 aprsDecode;
    u16 audioBoost;

    u16 PERSIST;
    u16 SLOTTIME;

    u16 micEabc;
    u16 micEdigipeat;

    u16 micEstdSymbol;
    u16 micEambiguity;

    u16 popupTime;
    u16 aprsVFO;
    
    u16 aprsAfFilters;
    u16 ax25DigipeaterSSID;

    u16 aprsLowPass;
    u16 multiPTT;

    u16 autoLock;

    char ax25Digipeater[7];
    
    u8 gpsCoordType;

    u16 gpsReduceQRM;

    u16 heartbeatStyle;

    u16 saveIgnores;

    u16 scanReturn;

    u16 ultraScanDelay;

    u16 smartScan;

    u16 aprsBeaconRxOverride;

    u16 lwStartFreq;

    u16 scanAbortAnyKey;

    u16 scrollTrigger;

    u16 alwaysOnRssi;

    u16 last;
} settingsInfo;
```

## `tunerBandInfo` struct

```c
typedef struct __attribute__((packed, aligned(4)))
{
    u32 freq;
    u32 step;
    s16 bfo;
    u8 mode;
    struct {
        u8 bw: 7;
        u8 plfilt: 1;
    } bwConfig;
} tunerBandInfo;
```