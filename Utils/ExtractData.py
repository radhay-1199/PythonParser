from Utils import Dictionary

adslErrorFlag = False

def getInitialData(datafile):
    assetManufacture=datafile[0].replace("\n","")
    assetModel=datafile[1].replace("\n","")
    assetUniqueId=datafile[2].replace("\n","")
    assetSwVersion=datafile[3].replace("\n","")

def getXDSLAutoxTURConfiguration(line):
    if ':' in line:
        var, val = (line.split(":"))
        if var == 'PhyR':  Dictionary.dict["phyR"]=val.strip()
        if var == 'SRA':  Dictionary.dict["sra"]=val.strip()
        if var == 'Vectoring Mode':  Dictionary.dict["vectoring"] = val.strip()
        if var == 'DSL Interface':  Dictionary.dict["dslInterface"] = val.strip()

def getADSLSummary(line):
    if ':' in line:
        var, val = (line.split(":"))
        if var == 'Modem temperature':  Dictionary.dict["modemTemp"]=val.strip()
        if var == 'Upstream  Capacity':  Dictionary.dict["capacityUp"]=val.strip()
        if var == 'Downstream  Capacity':  Dictionary.dict["capacityDn"] = val.strip()
        if var == 'Upstream  Noise Margin':  Dictionary.dict["marginUp"] = val.strip()
        if var == 'Downstream  Noise Margin':  Dictionary.dict["marginDn"] = val.strip()

def getADSLErrors(line):
    if ':' in line:
        var, val = (line.split(":"))
        if (var == 'Local(Dn) LOSS') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1LosErrorDn'] = val.strip()
        if (var == 'Local(Dn) FEC/min') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1FecMinErrorDn'] = val.strip()
        if (var == 'Local(Dn) CRC/min') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1CrcMinErrorDn'] = val.strip()
        if (var == 'Local(Dn) LOFS') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1LofErrorDn'] = val.strip()
        if (var == 'Local(Dn) LOMS') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1LomErrorDn'] = val.strip()
        if (var == 'Remote(Up) FLOSS') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1FLossUp'] = val.strip()
        if (var == 'Remote(Up) FEC/min') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1FecMinErrorUp'] = val.strip()
        if (var == 'Remote(Up) CRC/min') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1CrcMinErrorUp'] = val.strip()
        if (var == 'Remote(Up) LOFS') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1LofErrorUp'] = val.strip()
        if (var == 'Remote(Up) LOMS') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1LomErrorUp'] = val.strip()

def getADSLPerformance(line):
    if ':' in line:
        var, val = (line.split(":"))
        if (var == 'Local(Dn) ES') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1EsErrorDn'] = val.strip()
        if (var == 'Remote(Up) ES') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1EsErrorUp'] = val.strip()
        if (var == 'Local(Dn) SES') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1SesErrorDn'] = val.strip()
        if (var == 'Remote(Up) SES') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1SesErrorUp'] = val.strip()
        if (var == 'Local(Dn) UAS') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1UasErrorDn'] = val.strip()
        if (var == 'Remote(Up) UAS') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1UasErrorUp'] = val.strip()

def getADSLSignal(line):
    if ':' in line:
        var, val = (line.split(":"))
        if (var == '1MHz Attenuation') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1OneMhzAtten'] = val.strip()
        if (var == 'Num Syncs') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1SyncCount'] = val.strip()
        if (var == 'Sync Time') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1SyncTime'] = val.strip()
        if (var == 'Training Time') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1TrainTime'] = val.strip()
        if (var == 'Estimated Length') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1EstLoopLength'] = val.strip()
        if (var == 'Upstream Connected Method') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1UsConnMethod'] = val.strip()
        if (var == 'Downstream Connected Method') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1DsConnMethod'] = val.strip()

def getADSLIdentity(line):
    if ':' in line:
        var, val = (line.split(":"))
        if var == 'Modem Firmware':  Dictionary.dict["modemFirmVersion"]=val.strip()
        if var == 'DSL Version':  Dictionary.dict["dslVersion"]=val.strip()
        if var == 'Modem Chipset':  Dictionary.dict["modemChipset"] = val.strip()
        if var == 'Remote Vendor Name':  Dictionary.dict["vendorName"] = val.strip()
        if var == 'Remote Vendor ID':  Dictionary.dict["vendorId"] = val.strip()

def getADSLDataSummary(line):
    if ':' in line:
        var, val = (line.split(":"))
        if var == 'Data Mode':  Dictionary.dict["dslDataMode"]=val.strip()
        if var == 'Data Link':  Dictionary.dict["dslDataLink"]=val.strip()
        if var == 'Emulation Type':  Dictionary.dict["dslEmulationType"] = val.strip()
        if var == 'Pri VC':  Dictionary.dict["dslPriVc"] = val.strip()

def getIPv4(line):
    if ':' in line:
        var, val = (line.split(":"))
        if var == 'WAN IP Address':  Dictionary.dict["wanIpv4Ip"]=val.strip()
        if var == 'WAN Net Mask':  Dictionary.dict["wanIpv4Mask"]=val.strip()
        if var == 'LAN IP Address':  Dictionary.dict["lanIpv4Ip"] = val.strip()
        if var == 'LAN Net Mask':  Dictionary.dict["lanIpv4Mask"] = val.strip()
        if var == 'Gateway':  Dictionary.dict["wanIpv4Gw"] = val.strip()
        if var == 'DNS':  Dictionary.dict["dnsServer0"] = val.strip()
        if var == 'MAC Address':  Dictionary.dict["wanMacAddress"] = val.strip()
        if var == 'State':  Dictionary.dict["ipv4State"] = val.strip()