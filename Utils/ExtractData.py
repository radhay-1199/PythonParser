from Utils import Dictionary

bondedAdslErrorFlag = False
bondedVdslErrorFlag = False
bondedAdslSummaryFlag = False
bondedVdslSummaryFlag = False
bondedAdslPerformanceFlag = False
bondedVdslPerformanceFlag = False
bondedAdslSignalFlag = False
bondedVdslSignalFlag = False
bondedVdslBandStatisticsFlag = False

def getInitialData(datafile):
    Dictionary.dict["assetManufacturer"] = datafile[0].replace("\n","")
    Dictionary.dict["assetModel"] = datafile[1].replace("\n","")
    Dictionary.dict["assetUniqueId"] = datafile[2].replace("\n","")
    Dictionary.dict["assetSwVersion"] = datafile[3].replace("\n","")

def getXDSLAutoxTURConfiguration(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if var == 'PhyR':  Dictionary.dict["phyR"] = val.strip()
        if var == 'SRA':  Dictionary.dict["sra"] = val.strip()
        if var == 'Vectoring Mode':  Dictionary.dict["vectoring"] = val.strip()
        if var == 'DSL Interface':  Dictionary.dict["dslInterface"] = val.strip()

def getBondedADSLATURConfiguration(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if var == 'PhyR':  Dictionary.dict["phyR"] = val.strip()
        if var == 'SRA':  Dictionary.dict["sra"] = val.strip()
        if var == 'Vectoring Mode':  Dictionary.dict["vectoring"] = val.strip()
        if var == 'DSL Interface':  Dictionary.dict["dslInterface"] = val.strip()

def getBondedVDSL2VTURConfiguration(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if var == 'PhyR':  Dictionary.dict["phyR"] = val.strip()
        if var == 'SRA':  Dictionary.dict["sra"] = val.strip()
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

def getVDSLSummary(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if var == 'Modem temperature':  Dictionary.dict["modemTemp"] = val.strip()
        if var == 'Upstream  Capacity':  Dictionary.dict["pair1capacityUp"] = val.strip()
        if var == 'Downstream  Capacity':  Dictionary.dict["pair1capacityDn"] = val.strip()
        if var == 'Upstream  Noise Margin':  Dictionary.dict["pair1marginUp"] = val.strip()
        if var == 'Downstream  Noise Margin':  Dictionary.dict["pair1marginDn"] = val.strip()

def getBondedADSLSummary(line):
    global bondedAdslSummaryFlag
    if 'Pair 2 State' in line:
        bondedAdslSummaryFlag = True
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if not bondedAdslSummaryFlag:
            if var == 'Modem temperature':  Dictionary.dict["modemTemp"] = val.strip()
            if var == 'Upstream Group Max Rate':  Dictionary.dict["upGrpMaxRate"] = val.strip()
            if var == 'Upstream  Group Capacity':  Dictionary.dict["upGrpMaxCap"] = val.strip()
            if var == 'Downstream Group Max Rate':  Dictionary.dict["dnGrpMaxRate"] = val.strip()
            if var == 'Downstream  Group Capacity':  Dictionary.dict["dnGrpMaxCap"] = val.strip()
            if var == 'Lapse Time':  Dictionary.dict["lapseTime"] = val.strip()
            if var == 'Upstream  Capacity':  Dictionary.dict["pair1capacityUp"] = val.strip()
            if var == 'Downstream  Capacity':  Dictionary.dict["pair1capacityDn"] = val.strip()
            if var == 'Upstream  Noise Margin':  Dictionary.dict["pair1marginUp"] = val.strip()
            if var == 'Downstream  Noise Margin':  Dictionary.dict["pair1marginDn"] = val.strip()
        elif bondedAdslSummaryFlag:
            if var == 'Upstream  Capacity':  Dictionary.dict["pair2capacityUp"] = val.strip()
            if var == 'Downstream  Capacity':  Dictionary.dict["pair2capacityDn"] = val.strip()
            if var == 'Upstream  Noise Margin':  Dictionary.dict["pair2marginUp"] = val.strip()
            if var == 'Downstream  Noise Margin':  Dictionary.dict["pair2marginDn"] = val.strip()

def getBondedVDSLSummary(line):
    global bondedVdslSummaryFlag
    if 'Pair 2 State' in line:
        bondedVdslSummaryFlag = True
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if not bondedVdslSummaryFlag:
            if var == 'Modem temperature':  Dictionary.dict["modemTemp"] = val.strip()
            if var == 'Upstream Group Max Rate':  Dictionary.dict["upGrpMaxRate"] = val.strip()
            if var == 'Upstream  Group Capacity':  Dictionary.dict["upGrpMaxCap"] = val.strip()
            if var == 'Downstream Group Max Rate':  Dictionary.dict["dnGrpMaxRate"] = val.strip()
            if var == 'Downstream  Group Capacity':  Dictionary.dict["dnGrpMaxCap"] = val.strip()
            if var == 'Lapse Time':  Dictionary.dict["lapseTime"] = val.strip()
            if var == 'Upstream  Capacity':  Dictionary.dict["pair1capacityUp"] = val.strip()
            if var == 'Downstream  Capacity':  Dictionary.dict["pair1capacityDn"] = val.strip()
            if var == 'Upstream  Noise Margin':  Dictionary.dict["pair1marginUp"] = val.strip()
            if var == 'Downstream  Noise Margin':  Dictionary.dict["pair1marginDn"] = val.strip()
        elif bondedVdslSummaryFlag:
            if var == 'Upstream  Capacity':  Dictionary.dict["pair2capacityUp"] = val.strip()
            if var == 'Downstream  Capacity':  Dictionary.dict["pair2capacityDn"] = val.strip()
            if var == 'Upstream  Noise Margin':  Dictionary.dict["pair2marginUp"] = val.strip()
            if var == 'Downstream  Noise Margin':  Dictionary.dict["pair2marginDn"] = val.strip()

def getADSLErrors(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if (var == 'Local(Dn) LOSS') and ("pair1losErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1losErrorDn'] = val.strip()
        if (var == 'Local(Dn) FEC/min') and ("pair1fecMinErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1fecMinErrorDn'] = val.strip()
        if (var == 'Local(Dn) CRC/min') and ("pair1crcMinErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1crcMinErrorDn'] = val.strip()
        if (var == 'Local(Dn) LOFS') and ("pair1lofErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1lofErrorDn'] = val.strip()
        if (var == 'Local(Dn) LOMS') and ("pair1lomErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1lomErrorDn'] = val.strip()
        if (var == 'Remote(Up) FLOSS') and ("pair1fLossUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1fLossUp'] = val.strip()
        if (var == 'Remote(Up) FEC/min') and ("pair1fecMinErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1fecMinErrorUp'] = val.strip()
        if (var == 'Remote(Up) CRC/min') and ("pair1crcMinErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1crcMinErrorUp'] = val.strip()
        if (var == 'Remote(Up) LOFS') and ("pair1lofErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1lofErrorUp'] = val.strip()
        if (var == 'Remote(Up) LOMS') and ("pair1lomErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1lomErrorUp'] = val.strip()

def getVDSLErrors(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if (var == 'Local(Dn) LOSS') and ("pair1losErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1losErrorDn'] = val.strip()
        if (var == 'Local(Dn) FEC/min') and ("pair1fecMinErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1fecMinErrorDn'] = val.strip()
        if (var == 'Local(Dn) CRC/min') and ("pair1crcMinErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1crcMinErrorDn'] = val.strip()
        if (var == 'Local(Dn) LOFS') and ("pair1lofErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1lofErrorDn'] = val.strip()
        if (var == 'Local(Dn) LOMS') and ("pair1lomErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1lomErrorDn'] = val.strip()
        if (var == 'Remote(Up) FLOSS') and ("pair1fLossUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1fLossUp'] = val.strip()
        if (var == 'Remote(Up) FEC/min') and ("pair1fecMinErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1fecMinErrorUp'] = val.strip()
        if (var == 'Remote(Up) CRC/min') and ("pair1crcMinErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1crcMinErrorUp'] = val.strip()
        if (var == 'Remote(Up) LOFS') and ("pair1lofErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1lofErrorUp'] = val.strip()
        if (var == 'Remote(Up) LOMS') and ("pair1lomErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1lomErrorUp'] = val.strip()

def getBondedADSLErrors(line):
    global bondedAdslErrorFlag
    if 'Pair 2' in line:
        bondedAdslErrorFlag = True
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if not bondedAdslErrorFlag:
            if (var == 'Local(Dn) LOSS') and ("pair1losErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1losErrorDn'] = val.strip()
            if (var == 'Local(Dn) FEC/min') and ("pair1fecMinErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1fecMinErrorDn'] = val.strip()
            if (var == 'Local(Dn) CRC/min') and ("pair1crcMinErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1crcMinErrorDn'] = val.strip()
            if (var == 'Local(Dn) LOFS') and ("pair1lofErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1lofErrorDn'] = val.strip()
            if (var == 'Local(Dn) LOMS') and ("pair1lomErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1lomErrorDn'] = val.strip()
            if (var == 'Remote(Up) FLOSS') and ("pair1fLossUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1fLossUp'] = val.strip()
            if (var == 'Remote(Up) FEC/min') and ("pair1fecMinErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1fecMinErrorUp'] = val.strip()
            if (var == 'Remote(Up) CRC/min') and ("pair1crcMinErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1crcMinErrorUp'] = val.strip()
            if (var == 'Remote(Up) LOFS') and ("pair1lofErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1lofErrorUp'] = val.strip()
            if (var == 'Remote(Up) LOMS') and ("pair1lomErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1lomErrorUp'] = val.strip()
        elif bondedAdslErrorFlag:
            if (var == 'Local(Dn) LOSS') and ("pair2losErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair2losErrorDn'] = val.strip()
            if (var == 'Local(Dn) FEC/min') and ("pair2fecMinErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair2fecMinErrorDn'] = val.strip()
            if (var == 'Local(Dn) CRC/min') and ("pair2crcMinErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair2crcMinErrorDn'] = val.strip()
            if (var == 'Local(Dn) LOFS') and ("pair2lofErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair2lofErrorDn'] = val.strip()
            if (var == 'Local(Dn) LOMS') and ("pair2lomErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair2lomErrorDn'] = val.strip()
            if (var == 'Remote(Up) FLOSS') and ("pair2fLossUp" not in Dictionary.dict.keys()): Dictionary.dict['pair2fLossUp'] = val.strip()
            if (var == 'Remote(Up) FEC/min') and ("pair2fecMinErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair2fecMinErrorUp'] = val.strip()
            if (var == 'Remote(Up) CRC/min') and ("pair2crcMinErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair2crcMinErrorUp'] = val.strip()
            if (var == 'Remote(Up) LOFS') and ("pair2lofErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair2lofErrorUp'] = val.strip()
            if (var == 'Remote(Up) LOMS') and ("pair2lomErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair2lomErrorUp'] = val.strip()

def getBondedVDSLErrors(line):
    global bondedVdslErrorFlag
    if 'Pair 2' in line:
        bondedVdslErrorFlag = True
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if not bondedVdslErrorFlag:
            if (var == 'Local(Dn) LOSS') and ("pair1losErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1losErrorDn'] = val.strip()
            if (var == 'Local(Dn) FEC/min') and ("pair1fecMinErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1fecMinErrorDn'] = val.strip()
            if (var == 'Local(Dn) CRC/min') and ("pair1crcMinErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1crcMinErrorDn'] = val.strip()
            if (var == 'Local(Dn) LOFS') and ("pair1lofErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1lofErrorDn'] = val.strip()
            if (var == 'Local(Dn) LOMS') and ("pair1lomErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1lomErrorDn'] = val.strip()
            if (var == 'Remote(Up) FLOSS') and ("pair1fLossUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1fLossUp'] = val.strip()
            if (var == 'Remote(Up) FEC/min') and ("pair1fecMinErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1fecMinErrorUp'] = val.strip()
            if (var == 'Remote(Up) CRC/min') and ("pair1crcMinErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1crcMinErrorUp'] = val.strip()
            if (var == 'Remote(Up) LOFS') and ("pair1lofErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1lofErrorUp'] = val.strip()
            if (var == 'Remote(Up) LOMS') and ("pair1lomErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1lomErrorUp'] = val.strip()
        elif bondedVdslErrorFlag:
            if (var == 'Local(Dn) LOSS') and ("pair2losErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair2losErrorDn'] = val.strip()
            if (var == 'Local(Dn) FEC/min') and ("pair2fecMinErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair2fecMinErrorDn'] = val.strip()
            if (var == 'Local(Dn) CRC/min') and ("pair2crcMinErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair2crcMinErrorDn'] = val.strip()
            if (var == 'Local(Dn) LOFS') and ("pair2lofErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair2lofErrorDn'] = val.strip()
            if (var == 'Local(Dn) LOMS') and ("pair2lomErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair2lomErrorDn'] = val.strip()
            if (var == 'Remote(Up) FLOSS') and ("pair2fLossUp" not in Dictionary.dict.keys()): Dictionary.dict['pair2fLossUp'] = val.strip()
            if (var == 'Remote(Up) FEC/min') and ("pair2fecMinErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair2fecMinErrorUp'] = val.strip()
            if (var == 'Remote(Up) CRC/min') and ("pair2crcMinErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair2crcMinErrorUp'] = val.strip()
            if (var == 'Remote(Up) LOFS') and ("pair2lofErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair2lofErrorUp'] = val.strip()
            if (var == 'Remote(Up) LOMS') and ("pair2lomErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair2lomErrorUp'] = val.strip()

def getADSLPerformance(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if (var == 'Local(Dn) ES') and ("pair1esErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1esErrorDn'] = val.strip()
        if (var == 'Remote(Up) ES') and ("pair1esErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1esErrorUp'] = val.strip()
        if (var == 'Local(Dn) SES') and ("pair1sesErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1sesErrorDn'] = val.strip()
        if (var == 'Remote(Up) SES') and ("pair1sesErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1sesErrorUp'] = val.strip()
        if (var == 'Local(Dn) UAS') and ("pair1uasErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1uasErrorDn'] = val.strip()
        if (var == 'Remote(Up) UAS') and ("pair1uasErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1uasErrorUp'] = val.strip()

def getVDSLPerformance(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if (var == 'Local(Dn) ES') and ("pair1esErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1esErrorDn'] = val.strip()
        if (var == 'Remote(Up) ES') and ("pair1esErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1esErrorUp'] = val.strip()
        if (var == 'Local(Dn) SES') and ("pair1sesErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1sesErrorDn'] = val.strip()
        if (var == 'Remote(Up) SES') and ("pair1sesErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1sesErrorUp'] = val.strip()
        if (var == 'Local(Dn) UAS') and ("pair1uasErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1uasErrorDn'] = val.strip()
        if (var == 'Remote(Up) UAS') and ("pair1uasErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1uasErrorUp'] = val.strip()

def getBondedADSLPerformance(line):
    global bondedAdslPerformanceFlag
    if 'Pair 2' in line:
        bondedAdslPerformanceFlag = True
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if not bondedAdslPerformanceFlag:
            if (var == 'Local(Dn) ES') and ("pair1esErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1esErrorDn'] = val.strip()
            if (var == 'Remote(Up) ES') and ("pair1esErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1esErrorUp'] = val.strip()
            if (var == 'Local(Dn) SES') and ("pair1sesErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1sesErrorDn'] = val.strip()
            if (var == 'Remote(Up) SES') and ("pair1sesErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1sesErrorUp'] = val.strip()
            if (var == 'Local(Dn) UAS') and ("pair1uasErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1uasErrorDn'] = val.strip()
            if (var == 'Remote(Up) UAS') and ("pair1uasErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1uasErrorUp'] = val.strip()
        elif bondedAdslPerformanceFlag:
            if (var == 'Local(Dn) ES') and ("pair2esErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair2esErrorDn'] = val.strip()
            if (var == 'Remote(Up) ES') and ("pair2esErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair2esErrorUp'] = val.strip()
            if (var == 'Local(Dn) SES') and ("pair2sesErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair2sesErrorDn'] = val.strip()
            if (var == 'Remote(Up) SES') and ("pair2sesErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair2sesErrorUp'] = val.strip()
            if (var == 'Local(Dn) UAS') and ("pair2uasErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair2uasErrorDn'] = val.strip()
            if (var == 'Remote(Up) UAS') and ("pair2uasErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair2uasErrorUp'] = val.strip()

def getBondedVDSLPerformance(line):
    global bondedVdslPerformanceFlag
    if 'Pair 2' in line:
        bondedVdslPerformanceFlag = True
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if not bondedVdslPerformanceFlag:
            if (var == 'Local(Dn) ES') and ("pair1esErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1esErrorDn'] = val.strip()
            if (var == 'Remote(Up) ES') and ("pair1esErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1esErrorUp'] = val.strip()
            if (var == 'Local(Dn) SES') and ("pair1sesErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1sesErrorDn'] = val.strip()
            if (var == 'Remote(Up) SES') and ("pair1sesErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1sesErrorUp'] = val.strip()
            if (var == 'Local(Dn) UAS') and ("pair1uasErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair1uasErrorDn'] = val.strip()
            if (var == 'Remote(Up) UAS') and ("pair1uasErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair1uasErrorUp'] = val.strip()
        elif bondedVdslPerformanceFlag:
            if (var == 'Local(Dn) ES') and ("pair2esErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair2esErrorDn'] = val.strip()
            if (var == 'Remote(Up) ES') and ("pair2esErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair2esErrorUp'] = val.strip()
            if (var == 'Local(Dn) SES') and ("pair2sesErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair2sesErrorDn'] = val.strip()
            if (var == 'Remote(Up) SES') and ("pair2sesErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair2sesErrorUp'] = val.strip()
            if (var == 'Local(Dn) UAS') and ("pair2uasErrorDn" not in Dictionary.dict.keys()): Dictionary.dict['pair2uasErrorDn'] = val.strip()
            if (var == 'Remote(Up) UAS') and ("pair2uasErrorUp" not in Dictionary.dict.keys()): Dictionary.dict['pair2uasErrorUp'] = val.strip()

def getADSLSignal(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if (var == '1MHz Attenuation') and ("pair1oneMhzAtten" not in Dictionary.dict.keys()): Dictionary.dict['pair1oneMhzAtten'] = val.strip()
        if (var == 'Num Syncs') and ("pair1syncCount" not in Dictionary.dict.keys()): Dictionary.dict['pair1syncCount'] = val.strip()
        if (var == 'Sync Time') and ("pair1syncTime" not in Dictionary.dict.keys()): Dictionary.dict['pair1syncTime'] = val.strip()
        if (var == 'Training Time') and ("pair1trainTime" not in Dictionary.dict.keys()): Dictionary.dict['pair1trainTime'] = val.strip()
        if (var == 'Estimated Length') and ("pair1estLoopLength" not in Dictionary.dict.keys()): Dictionary.dict['pair1estLoopLength'] = val.strip()
        if (var == 'Upstream Connected Method') and ("pair1usConnMethod" not in Dictionary.dict.keys()): Dictionary.dict['pair1usConnMethod'] = val.strip()
        if (var == 'Downstream Connected Method') and ("pair1dsConnMethod" not in Dictionary.dict.keys()): Dictionary.dict['pair1dsConnMethod'] = val.strip()

def getVDSLSignal(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if (var == '1MHz Attenuation') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1oneMhzAtten'] = val.strip()
        if (var == 'Num Syncs') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1syncCount'] = val.strip()
        if (var == 'Sync Time') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1syncTime'] = val.strip()
        if (var == 'Training Time') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1trainTime'] = val.strip()
        if (var == 'Estimated Length') and (var not in Dictionary.dict.keys()): Dictionary.dict['pair1estLoopLength'] = val.strip()

def getBondedADSLSignal(line):
    global bondedAdslSignalFlag
    if 'Pair 2' in line:
        bondedAdslSignalFlag = True
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if not bondedAdslSignalFlag:
            if (var == '1MHz Attenuation') and ("pair1oneMhzAtten" not in Dictionary.dict.keys()): Dictionary.dict['pair1oneMhzAtten'] = val.strip()
            if (var == 'Num Syncs') and ("pair1syncCount" not in Dictionary.dict.keys()): Dictionary.dict['pair1syncCount'] = val.strip()
            if (var == 'Sync Time') and ("pair1syncTime" not in Dictionary.dict.keys()): Dictionary.dict['pair1syncTime'] = val.strip()
            if (var == 'Training Time') and ("pair1trainTime" not in Dictionary.dict.keys()): Dictionary.dict['pair1trainTime'] = val.strip()
            if (var == 'Estimated Length') and ("pair1estLoopLength" not in Dictionary.dict.keys()): Dictionary.dict['pair1estLoopLength'] = val.strip()
            if (var == 'Upstream Connected Method') and ("pair1usConnMethod" not in Dictionary.dict.keys()): Dictionary.dict['pair1usConnMethod'] = val.strip()
            if (var == 'Downstream Connected Method') and ("pair1dsConnMethod" not in Dictionary.dict.keys()): Dictionary.dict['pair1dsConnMethod'] = val.strip()
        elif bondedAdslSignalFlag:
            if (var == '1MHz Attenuation') and ("pair2oneMhzAtten" not in Dictionary.dict.keys()): Dictionary.dict['pair2oneMhzAtten'] = val.strip()
            if (var == 'Num Syncs') and ("pair2syncCount" not in Dictionary.dict.keys()): Dictionary.dict['pair2syncCount'] = val.strip()
            if (var == 'Sync Time') and ("pair2syncTime" not in Dictionary.dict.keys()): Dictionary.dict['pair2syncTime'] = val.strip()
            if (var == 'Training Time') and ("pair2trainTime" not in Dictionary.dict.keys()): Dictionary.dict['pair2trainTime'] = val.strip()
            if (var == 'Estimated Length') and ("pair2estLoopLength" not in Dictionary.dict.keys()): Dictionary.dict['pair2estLoopLength'] = val.strip()
            if (var == 'Upstream Connected Method') and ("pair2usConnMethod" not in Dictionary.dict.keys()): Dictionary.dict['pair2usConnMethod'] = val.strip()
            if (var == 'Downstream Connected Method') and ("pair2dsConnMethod" not in Dictionary.dict.keys()): Dictionary.dict['pair2dsConnMethod'] = val.strip()

def getBondedVDSLSignal(line):
    global bondedVdslSignalFlag
    if 'Pair 2' in line:
        bondedVdslSignalFlag = True
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if not bondedVdslSignalFlag:
            if (var == '1MHz Attenuation') and ("pair1oneMhzAtten" not in Dictionary.dict.keys()): Dictionary.dict['pair1oneMhzAtten'] = val.strip()
            if (var == 'Num Syncs') and ("pair1syncCount" not in Dictionary.dict.keys()): Dictionary.dict['pair1syncCount'] = val.strip()
            if (var == 'Sync Time') and ("pair1syncTime" not in Dictionary.dict.keys()): Dictionary.dict['pair1syncTime'] = val.strip()
            if (var == 'Training Time') and ("pair1trainTime" not in Dictionary.dict.keys()): Dictionary.dict['pair1trainTime'] = val.strip()
            if (var == 'Estimated Length') and ("pair1estLoopLength" not in Dictionary.dict.keys()): Dictionary.dict['pair1estLoopLength'] = val.strip()
        elif bondedVdslSignalFlag:
            if (var == '1MHz Attenuation') and ("pair2oneMhzAtten" not in Dictionary.dict.keys()): Dictionary.dict['pair2oneMhzAtten'] = val.strip()
            if (var == 'Num Syncs') and ("pair2syncCount" not in Dictionary.dict.keys()): Dictionary.dict['pair2syncCount'] = val.strip()
            if (var == 'Sync Time') and ("pair2syncTime" not in Dictionary.dict.keys()): Dictionary.dict['pair2syncTime'] = val.strip()
            if (var == 'Training Time') and ("pair2trainTime" not in Dictionary.dict.keys()): Dictionary.dict['pair2trainTime'] = val.strip()
            if (var == 'Estimated Length') and ("pair2estLoopLength" not in Dictionary.dict.keys()): Dictionary.dict['pair2estLoopLength'] = val.strip()

def getADSLIdentity(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if var == 'Modem Firmware':  Dictionary.dict["modemFirmVersion"] = val.strip()
        if var == 'DSL Version':  Dictionary.dict["dslVersion"] = val.strip()
        if var == 'Modem Chipset':  Dictionary.dict["modemChipset"] = val.strip()
        if var == 'Remote Vendor Name':  Dictionary.dict["vendorName"] = val.strip()
        if var == 'Remote Vendor ID':  Dictionary.dict["vendorId"] = val.strip()

def getBondedADSLIdentity(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if var == 'Modem Firmware':  Dictionary.dict["modemFirmVersion"] = val.strip()
        if var == 'DSL Version':  Dictionary.dict["dslVersion"] = val.strip()
        if var == 'Modem Chipset':  Dictionary.dict["modemChipset"] = val.strip()
        if var == 'Remote Vendor Name':  Dictionary.dict["vendorName"] = val.strip()
        if var == 'Remote Vendor ID':  Dictionary.dict["vendorId"] = val.strip()

def getVDSLIdentity(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if var == 'Modem Firmware':  Dictionary.dict["modemFirmVersion"] = val.strip()
        if var == 'DSL Version':  Dictionary.dict["dslVersion"] = val.strip()
        if var == 'Modem Chipset':  Dictionary.dict["modemChipset"] = val.strip()
        if var == 'Remote Vendor Name':  Dictionary.dict["vendorName"] = val.strip()
        if var == 'Remote Vendor ID':  Dictionary.dict["vendorId"] = val.strip()

def getBondedVDSLIdentity(line):
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

def getVDSLDataSummary(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if var == 'Data Mode':  Dictionary.dict["dslDataMode"] = val.strip()
        if var == 'Data Link':  Dictionary.dict["dslDataLink"] = val.strip()
        if var == 'Emulation Type':  Dictionary.dict["dslEmulationType"] = val.strip()
        if var == 'Rx Bytes':  Dictionary.dict["dslRxBytes"] = val.strip()
        if var == 'Rx Frames':  Dictionary.dict["dslRxFrames"] = val.strip()
        if var == 'Rx Errors':  Dictionary.dict["dslRxErrors"] = val.strip()
        if var == 'Tx Bytes':  Dictionary.dict["dslTxBytes"] = val.strip()
        if var == 'Tx Frames':  Dictionary.dict["dslTxFrames"] = val.strip()
        if var == 'Tx Errors':  Dictionary.dict["dslTxErrors"] = val.strip()

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
        if var == 'WAN VLAN ID':  Dictionary.dict["wanVlanId"] = val.strip()

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
        if var == 'Delay Current':  Dictionary.dict["pingCurrDelay"] = val.strip().replace("    "," ")
        if var == 'Delay Ave':  Dictionary.dict["pingAvgDelay"] = val.strip().replace("    "," ")
        if var == 'Delay Max':  Dictionary.dict["pingMaxDelay"] = val.strip().replace("    "," ")
        if var == 'Delay Min':  Dictionary.dict["pingMinDelay"] = val.strip().replace("    "," ")
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

def getVDSLVectoring(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if var == 'Vectored Bands':  Dictionary.dict["vectorBand"] = val.strip()
        if var == 'Vector State':  Dictionary.dict["vectorState"] = val.strip()
        if var == 'Error Samples Sent':  Dictionary.dict["errSampleSent"] = val.strip()
        if var == 'Error Samples Dropped':  Dictionary.dict["errSampleDrop"] = val.strip()
        if var == 'Error Status Sent':  Dictionary.dict["errStatusSent"] = val.strip()
        if var == 'Error Status Dropped':  Dictionary.dict["errStatusDrop"] = val.strip()

def getBondedVDSLVectoring(line):
    if ':' in line:
        var, val, *rest = (line.split(":"))
        if var == 'Vectored Bands':  Dictionary.dict["vectorBand"] = val.strip()
        if var == 'Vector State':  Dictionary.dict["vectorState"] = val.strip()
        if var == 'Error Samples Sent':  Dictionary.dict["errSampleSent"] = val.strip()
        if var == 'Error Samples Dropped':  Dictionary.dict["errSampleDrop"] = val.strip()
        if var == 'Error Status Sent':  Dictionary.dict["errStatusSent"] = val.strip()
        if var == 'Error Status Dropped':  Dictionary.dict["errStatusDrop"] = val.strip()

def getVDSLBandStatistics(line):
    if "US0   Loop" in line:
        list = line.split("=")
        Dictionary.dict["pair1up0Latn"] = list[1].split("   ")[0]
        Dictionary.dict["pair1up0Satn"] = list[2].split("   ")[0]
        Dictionary.dict["pair1up0Margin"] = list[3].split("   ")[0]
        Dictionary.dict["pair1up0TxPower"] = list[4]
    if "US1   Loop" in line:
        list = line.split("=")
        Dictionary.dict["pair1up1Latn"] = list[1].split("   ")[0]
        Dictionary.dict["pair1up1Satn"] = list[2].split("   ")[0]
        Dictionary.dict["pair1up1Margin"] = list[3].split("   ")[0]
        Dictionary.dict["pair1up1TxPower"] = list[4]
    if "DS1   Loop" in line:
        list = line.split("=")
        Dictionary.dict["pair1dn1Latn"] = list[1].split("   ")[0]
        Dictionary.dict["pair1dn1Satn"] = list[2].split("   ")[0]
        Dictionary.dict["pair1dn1Margin"] = list[3].split("   ")[0]
        Dictionary.dict["pair1dn1TxPower"] = list[4]
    if "DS2   Loop" in line:
        list = line.split("=")
        Dictionary.dict["pair1dn2Latn"] = list[1].split("   ")[0]
        Dictionary.dict["pair1dn2Satn"] = list[2].split("   ")[0]
        Dictionary.dict["pair1dn2Margin"] = list[3].split("   ")[0]
        Dictionary.dict["pair1dn2TxPower"] = list[4]
    if "DS3   Loop" in line:
        list = line.split("=")
        Dictionary.dict["pair1dn3Latn"] = list[1].split("   ")[0]
        Dictionary.dict["pair1dn3Satn"] = list[2].split("   ")[0]
        Dictionary.dict["pair1dn3Margin"] = list[3].split("   ")[0]
        Dictionary.dict["pair1dn3TxPower"] = list[4]

def getBondedVDSLBandStatistics(line):
    global bondedVdslBandStatisticsFlag
    if 'Pair 2' in line:
        bondedVdslBandStatisticsFlag = True
    if not bondedVdslBandStatisticsFlag:
        if "US0   Loop" in line:
            list = line.split("=")
            Dictionary.dict["pair1up0Latn"] = list[1].split("   ")[0]
            Dictionary.dict["pair1up0Satn"] = list[2].split("   ")[0]
            Dictionary.dict["pair1up0Margin"] = list[3].split("   ")[0]
            Dictionary.dict["pair1up0TxPower"] = list[4]
        if "US1   Loop" in line:
            list = line.split("=")
            Dictionary.dict["pair1up1Latn"] = list[1].split("   ")[0]
            Dictionary.dict["pair1up1Satn"] = list[2].split("   ")[0]
            Dictionary.dict["pair1up1Margin"] = list[3].split("   ")[0]
            Dictionary.dict["pair1up1TxPower"] = list[4]
        if "DS1   Loop" in line:
            list = line.split("=")
            Dictionary.dict["pair1dn1Latn"] = list[1].split("   ")[0]
            Dictionary.dict["pair1dn1Satn"] = list[2].split("   ")[0]
            Dictionary.dict["pair1dn1Margin"] = list[3].split("   ")[0]
            Dictionary.dict["pair1dn1TxPower"] = list[4]
        if "DS2   Loop" in line:
            list = line.split("=")
            Dictionary.dict["pair1dn2Latn"] = list[1].split("   ")[0]
            Dictionary.dict["pair1dn2Satn"] = list[2].split("   ")[0]
            Dictionary.dict["pair1dn2Margin"] = list[3].split("   ")[0]
            Dictionary.dict["pair1dn2TxPower"] = list[4]
    if bondedVdslBandStatisticsFlag:
        if "US0   Loop" in line:
            list = line.split("=")
            Dictionary.dict["pair2up0Latn"] = list[1].split("   ")[0]
            Dictionary.dict["pair2up0Satn"] = list[2].split("   ")[0]
            Dictionary.dict["pair2up0Margin"] = list[3].split("   ")[0]
            Dictionary.dict["pair2up0TxPower"] = list[4]
        if "US1   Loop" in line:
            list = line.split("=")
            Dictionary.dict["pair2up1Latn"] = list[1].split("   ")[0]
            Dictionary.dict["pair2up1Satn"] = list[2].split("   ")[0]
            Dictionary.dict["pair2up1Margin"] = list[3].split("   ")[0]
            Dictionary.dict["pair2up1TxPower"] = list[4]
        if "DS1   Loop" in line:
            list = line.split("=")
            Dictionary.dict["pair2dn1Latn"] = list[1].split("   ")[0]
            Dictionary.dict["pair2dn1Satn"] = list[2].split("   ")[0]
            Dictionary.dict["pair2dn1Margin"] = list[3].split("   ")[0]
            Dictionary.dict["pair2dn1TxPower"] = list[4]
        if "DS2   Loop" in line:
            list = line.split("=")
            Dictionary.dict["pair2dn2Latn"] = list[1].split("   ")[0]
            Dictionary.dict["pair2dn2Satn"] = list[2].split("   ")[0]
            Dictionary.dict["pair2dn2Margin"] = list[3].split("   ")[0]
            Dictionary.dict["pair2dn2TxPower"] = list[4]
        if "DS3   Loop" in line:
            list = line.split("=")
            Dictionary.dict["pair2dn3Latn"] = list[1].split("   ")[0]
            Dictionary.dict["pair2dn3Satn"] = list[2].split("   ")[0]
            Dictionary.dict["pair2dn3Margin"] = list[3].split("   ")[0]
            Dictionary.dict["pair2dn3TxPower"] = list[4]
