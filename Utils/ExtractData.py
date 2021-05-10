from Utils import Dictionary

adslErrorFlag = False

def getInitialData(datafile):
    Dictionary.dict["assetManufacturer"] = datafile[0].replace("\n","")
    Dictionary.dict["assetModel"] = datafile[1].replace("\n","")
    Dictionary.dict["assetUniqueId"] = datafile[2].replace("\n","")
    Dictionary.dict["assetSwVersion"] = datafile[3].replace("\n","")

def getXDSLAutoxTURConfiguration(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if var == 'PhyR':  Dictionary.dict["phyR"]=val.strip()
        if var == 'SRA':  Dictionary.dict["sra"]=val.strip()
        if var == 'Vectoring Mode':  Dictionary.dict["vectoring"] = val.strip()
        if var == 'DSL Interface':  Dictionary.dict["dslInterface"] = val.strip()

def getADSLSummary(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if var == 'Modem temperature':  Dictionary.dict["modemTemp"] = val.strip()
        if var == 'Upstream  Capacity':  Dictionary.dict["pair1capacityUp"] = val.strip()
        if var == 'Downstream  Capacity':  Dictionary.dict["pair1capacityDn"] = val.strip()
        if var == 'Upstream  Noise Margin':  Dictionary.dict["pair1marginUp"] = val.strip()
        if var == 'Downstream  Noise Margin':  Dictionary.dict["pair1marginDn"] = val.strip()

def getADSLErrors(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if (var == 'Local(Dn) LOSS') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1losErrorDn'] = val.strip()
        if (var == 'Local(Dn) FEC/min') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1fecMinErrorDn'] = val.strip()
        if (var == 'Local(Dn) CRC/min') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1crcMinErrorDn'] = val.strip()
        if (var == 'Local(Dn) LOFS') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1lofErrorDn'] = val.strip()
        if (var == 'Local(Dn) LOMS') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1lomErrorDn'] = val.strip()
        if (var == 'Remote(Up) FLOSS') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1fLossUp'] = val.strip()
        if (var == 'Remote(Up) FEC/min') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1fecMinErrorUp'] = val.strip()
        if (var == 'Remote(Up) CRC/min') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1crcMinErrorUp'] = val.strip()
        if (var == 'Remote(Up) LOFS') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1lofErrorUp'] = val.strip()
        if (var == 'Remote(Up) LOMS') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1lomErrorUp'] = val.strip()

def getADSLPerformance(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if (var == 'Local(Dn) ES') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1esErrorDn'] = val.strip()
        if (var == 'Remote(Up) ES') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1esErrorUp'] = val.strip()
        if (var == 'Local(Dn) SES') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1sesErrorDn'] = val.strip()
        if (var == 'Remote(Up) SES') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1sesErrorUp'] = val.strip()
        if (var == 'Local(Dn) UAS') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1uasErrorDn'] = val.strip()
        if (var == 'Remote(Up) UAS') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1uasErrorUp'] = val.strip()

def getADSLSignal(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if (var == '1MHz Attenuation') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1oneMhzAtten'] = val.strip()
        if (var == 'Num Syncs') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1syncCount'] = val.strip()
        if (var == 'Sync Time') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1syncTime'] = val.strip()
        if (var == 'Training Time') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1trainTime'] = val.strip()
        if (var == 'Estimated Length') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1estLoopLength'] = val.strip()
        if (var == 'Upstream Connected Method') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1usConnMethod'] = val.strip()
        if (var == 'Downstream Connected Method') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1dsConnMethod'] = val.strip()

def getADSLIdentity(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if var == 'Modem Firmware':  Dictionary.dict["modemFirmVersion"] = val.strip()
        if var == 'DSL Version':  Dictionary.dict["dslVersion"] = val.strip()
        if var == 'Modem Chipset':  Dictionary.dict["modemChipset"] = val.strip()
        if var == 'Remote Vendor Name':  Dictionary.dict["vendorName"] = val.strip()
        if var == 'Remote Vendor ID':  Dictionary.dict["vendorId"] = val.strip()

def getADSLDataSummary(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if var == 'Data Mode':  Dictionary.dict["dslDataMode"] = val.strip()
        if var == 'Data Link':  Dictionary.dict["dslDataLink"] = val.strip()
        if var == 'Emulation Type':  Dictionary.dict["dslEmulationType"] = val.strip()
        if var == 'Pri VC':  Dictionary.dict["dslPriVc"] = val.strip()

def getIPv4(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if var == 'WAN IP Address':  Dictionary.dict["wanIpv4Ip"] = val.strip()
        if var == 'WAN Net Mask':  Dictionary.dict["wanIpv4Mask"] = val.strip()
        if var == 'LAN IP Address':  Dictionary.dict["lanIpv4Ip"] = val.strip()
        if var == 'LAN Net Mask':  Dictionary.dict["lanIpv4Mask"] = val.strip()
        if var == 'Gateway':  Dictionary.dict["wanIpv4Gw"] = val.strip()
        if var == 'DNS':  Dictionary.dict["dnsServer0"] = val.strip()
        if var == 'MAC Address':  Dictionary.dict["wanMacAddress"] = val.strip()
        if var == 'State':  Dictionary.dict["ipv4State"] = val.strip()

def getEthernet(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if var == 'Rx Bytes':  Dictionary.dict["ethRxBytes"] = val.strip()
        if var == 'Rx Frames':  Dictionary.dict["ethRxFrames"] = val.strip()
        if var == 'Rx Errors':  Dictionary.dict["ethRxErrors"] = val.strip()
        if var == 'Rx Dropped':  Dictionary.dict["ethRxDropped"] = val.strip()
        if var == 'Tx Bytes':  Dictionary.dict["ethTxBytes"] = val.strip()
        if var == 'Tx Frames':  Dictionary.dict["ethTxFrames"] = val.strip()
        if var == 'Tx Errors':  Dictionary.dict["ethTxErrors"] = val.strip()
        if var == 'Tx Dropped':  Dictionary.dict["ethTxDropped"] = val.strip()
        if var == 'Tx Collisions':  Dictionary.dict["ethTxCollisions"] = val.strip()
        if var == 'Link Status':  Dictionary.dict["ethLinkStatus"] = val.strip()

def getPing(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if var == 'Destination':  Dictionary.dict["pingDestination"] = val.strip()
        if var == 'Echos Sent':  Dictionary.dict["pingRequestsTx"] = val.strip()
        if var == 'Echos Returned':  Dictionary.dict["pingRepliesRx"] = val.strip()
        if var == 'Lost / Lost %':  Dictionary.dict["pingPercentLost"] = val.strip()
        if var == 'Echos Received':  Dictionary.dict["pingLostPerLostPerc"] = val.strip()
        if var == 'Delay Current':  Dictionary.dict["pingCurrDelay"] = val.strip()
        if var == 'Delay Ave':  Dictionary.dict["pingAvgDelay"] = val.strip()
        if var == 'Delay Max':  Dictionary.dict["pingMaxDelay"] = val.strip()
        if var == 'Delay Min':  Dictionary.dict["pingMinDelay"] = val.strip()
        if var == 'Message':  Dictionary.dict["pingMessage"] = val.strip()
        if var == 'Last Pinger IP':  Dictionary.dict["pingLastPingIp"] = val.strip()

def getTraceRoute(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if var == 'Destination':  Dictionary.dict["traceRtDestination"] = val.strip()
        if var == 'State':  Dictionary.dict["traceRtState"] = val.strip()
        if var == 'Active':  Dictionary.dict["traceRtActive"] = val.strip()
        if var == 'Number of Hops':  Dictionary.dict["traceRtNumHops"] = val.strip()
        if var == '1':
            list = val.split("   ")
            Dictionary.dict["traceRtHop1Delay"] = list[0]
            Dictionary.dict["traceRtHop1Ip"] = list[1]
            Dictionary.dict["traceRtHop1Nm"] = list[2]
        if var == '2':
            list = val.split("   ")
            Dictionary.dict["traceRtHop2Delay"] = list[0]
            Dictionary.dict["traceRtHop2Ip"] = list[1]
            Dictionary.dict["traceRtHop2Nm"] = list[2]
        if var == '3':
            list = val.split("   ")
            Dictionary.dict["traceRtHop3Delay"] = list[0]
            Dictionary.dict["traceRtHop3Ip"] = list[1]
            Dictionary.dict["traceRtHop3Nm"] = list[2]
        if var == '4':
            list = val.split("   ")
            Dictionary.dict["traceRtHop4Delay"] = list[0]
            Dictionary.dict["traceRtHop4Ip"] = list[1]
            Dictionary.dict["traceRtHop4Nm"] = list[2]
        if var == '5':
            list = val.split("   ")
            Dictionary.dict["traceRtHop5Delay"] = list[0]
            Dictionary.dict["traceRtHop5Ip"] = list[1]
            Dictionary.dict["traceRtHop5Nm"] = list[2]
