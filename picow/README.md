# Raspberry Pico W

One of the challenges of the server.home is that the mainboard EVGA Z170 classified 4-way is optimized for overclocking. This results in a hardware implementation that does seem to have WOL (Wake on Lan), its part of the BIOS and in S5 (powered off) of the machine both NIC i210 and i219. Yet in suspend (S3) the power to the I210 is cut! Here the hardware:

```sh
$ lspci
00:1f.6 Ethernet controller: Intel Corporation Ethernet Connection (2) I219-V (rev 31)
08:00.0 Ethernet controller: Intel Corporation I210 Gigabit Network Connection (rev 03)
```

## Intel i210

- a **discrete PCIe NIC**
- connected via a PCIe slot
- powered by PCIe AUX / slot standby power
- EVGA often cuts AUX in S5

```sh
$ $ lspci -vv -s 08:00.0
08:00.0 Ethernet controller: Intel Corporation I210 Gigabit Network Connection (rev 03)
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 18
        Region 0: Memory at df100000 (32-bit, non-prefetchable) [size=512K]
        Region 2: I/O ports at d000 [disabled] [size=32]
        Region 3: Memory at df180000 (32-bit, non-prefetchable) [size=16K]
        Capabilities: <access denied>
        Kernel driver in use: igb
        Kernel modules: igb
```

Well, there is more:

```sh
$ sudo lspci -vv -s 08:00.0
08:00.0 Ethernet controller: Intel Corporation I210 Gigabit Network Connection (rev 03)
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 18
        Region 0: Memory at df100000 (32-bit, non-prefetchable) [size=512K]
        Region 2: I/O ports at d000 [disabled] [size=32]
        Region 3: Memory at df180000 (32-bit, non-prefetchable) [size=16K]
        Capabilities: [40] Power Management version 3
                Flags: PMEClk- DSI+ D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
                Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=1 PME-
        Capabilities: [50] MSI: Enable- Count=1/1 Maskable+ 64bit+
                Address: 0000000000000000  Data: 0000
                Masking: 00000000  Pending: 00000000
        Capabilities: [70] MSI-X: Enable+ Count=5 Masked-
                Vector table: BAR=3 offset=00000000
                PBA: BAR=3 offset=00002000
        Capabilities: [a0] Express (v2) Endpoint, MSI 00
                DevCap: MaxPayload 512 bytes, PhantFunc 0, Latency L0s <512ns, L1 <64us
                        ExtTag- AttnBtn- AttnInd- PwrInd- RBE+ FLReset+ SlotPowerLimit 0W
                DevCtl: CorrErr+ NonFatalErr+ FatalErr+ UnsupReq+
                        RlxdOrd+ ExtTag- PhantFunc- AuxPwr- NoSnoop+ FLReset-
                        MaxPayload 256 bytes, MaxReadReq 512 bytes
                DevSta: CorrErr+ NonFatalErr- FatalErr- UnsupReq+ AuxPwr+ TransPend-
                LnkCap: Port #0, Speed 2.5GT/s, Width x1, ASPM L0s L1, Exit Latency L0s <2us, L1 <16us
                        ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
                LnkCtl: ASPM Disabled; RCB 64 bytes, Disabled- CommClk+
                        ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
                LnkSta: Speed 2.5GT/s, Width x1
                        TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
                DevCap2: Completion Timeout: Range ABCD, TimeoutDis+ NROPrPrP- LTR-
                         10BitTagComp- 10BitTagReq- OBFF Not Supported, ExtFmt- EETLPPrefix-
                         EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                         FRS- TPHComp- ExtTPHComp-
                         AtomicOpsCap: 32bit- 64bit- 128bitCAS-
                DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis- LTR- 10BitTagReq- OBFF Disabled,
                         AtomicOpsCtl: ReqEn-
                LnkCtl2: Target Link Speed: 2.5GT/s, EnterCompliance- SpeedDis-
                         Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                         Compliance Preset/De-emphasis: -6dB de-emphasis, 0dB preshoot
                LnkSta2: Current De-emphasis Level: -6dB, EqualizationComplete- EqualizationPhase1-
                         EqualizationPhase2- EqualizationPhase3- LinkEqualizationRequest-
                         Retimer- 2Retimers- CrosslinkRes: unsupported
        Capabilities: [100 v2] Advanced Error Reporting
                UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                UESvrt: DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
                CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr-
                CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr+
                AERCap: First Error Pointer: 00, ECRCGenCap+ ECRCGenEn- ECRCChkCap+ ECRCChkEn-
                        MultHdrRecCap- MultHdrRecEn- TLPPfxPres- HdrLogCap-
                HeaderLog: 00000000 00000000 00000000 00000000
        Capabilities: [140 v1] Device Serial Number 00-1f-bc-ff-ff-0f-36-20
        Capabilities: [1a0 v1] Transaction Processing Hints
                Device specific mode supported
                Steering table in TPH capability structure
        Kernel driver in use: igb
        Kernel modules: igb
```

Now the other card:

## I219

The other gigabit adapter is the i219: **PCH-integrated NIC**.

- Depends heavily on BIOS policy
- ErP often cripples it

```sh
$ lspci -vv -s 00:1f.6
00:1f.6 Ethernet controller: Intel Corporation Ethernet Connection (2) I219-V (rev 31)
        Subsystem: Intel Corporation Ethernet Connection (2) I219-V
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0
        Interrupt: pin A routed to IRQ 141
        Region 0: Memory at df300000 (32-bit, non-prefetchable) [size=128K]
        Capabilities: <access denied>
        Kernel driver in use: e1000e
        Kernel modules: e1000e
```

And verbose:

```sh
$ sudo lspci -vv -s 00:1f.6
00:1f.6 Ethernet controller: Intel Corporation Ethernet Connection (2) I219-V (rev 31)
        Subsystem: Intel Corporation Ethernet Connection (2) I219-V
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0
        Interrupt: pin A routed to IRQ 141
        Region 0: Memory at df300000 (32-bit, non-prefetchable) [size=128K]
        Capabilities: [c8] Power Management version 3
                Flags: PMEClk- DSI+ D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
                Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=1 PME-
        Capabilities: [d0] MSI: Enable+ Count=1/1 Maskable- 64bit+
                Address: 00000000fee02000  Data: 0024
        Capabilities: [e0] PCI Advanced Features
                AFCap: TP+ FLR+
                AFCtrl: FLR-
                AFStatus: TP-
        Kernel driver in use: e1000e
        Kernel modules: e1000e
```

## The WOL problem

Both have in `Capabilities: [40] Power Management version 3`:

```sh
Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=1 PME-
```

No Power Management Event allowed to create!

So there is something to do.

In S3 (suspend) a single key (even the left shift key) can wake up the server from hibernating. The difference in power consumption? Good you asked, I measured:

- (S5) Power off: 3.3 Watt
- (S3) Suspend: 4.8 Watt

It wakes up very fast! It's so easy to invoke:

```sh
sudo systemctl suspend
```

And in BIOS I can set that a power cycle just restarts the computer, so it automatically turns on. And an inactivity script powers it off when not in use.

Plus, I can still power it off with the remote Tuya switch. From my smartphone.
