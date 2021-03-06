import csv
from datetime import datetime
from Utils import Dictionary


def writeInCsv():
    field_names = ['wtn', 'techUploadSource', 'techTestLocation', 'partialTestSetUpload', 'assetManufacturer',
                   'assetModel', 'assetUniqueId', 'assetSwVersion', 'vectoring', 'phyR', 'sra',
                   'dslInterface', 'mode', 'vdsl2Profile', 'status', 'modemTemp', 'pair1capacityUp', 'pair1capacityDn',
                   'pair1marginUp', 'totalBearerUpStream', 'pair1marginDn', 'totalBearerDnStream',
                   'pair1bearer0UpstreamRate', 'pair1maxUpstreamRate', 'pair1lAttnDbUp', 'pair1sAttnDbUp',
                   'pair1bearer0DownstreamRate', 'pair1maxDownstreamRate', 'pair1lAttnDbDown',
                   'pair1sAttnDbDown', 'pair2bearer1UpstreamRate', 'pair2maxUpstreamRate', 'pair2lAttnDbUp',
                   'pair2sAttnDbUp', 'pair2bearer1DownstreamRate', 'pair2maxDownstreamRate', 'pair2lAttnDbDown',
                   'pair2sAttnDbDown', 'pair1fecDnTtErrors', 'pair1crcDnTtErrors', 'pair1fecUpTtErrors',
                   'pair1crcUpTtErrors', 'pair2fecDnTtErrors', 'pair2crcDnTtErrors', 'pair2fecUpTtErrors',
                   'pair2crcUpTtErrors', 'pair1rtxtxDnRetransCount', 'pair1rtxcDnRetransCount',
                   'pair1rtxucDnRetransCount', 'pair1rtxtxUpRetransCount', 'pair1rtxcUpRetransCount',
                   'pair1rtxucUpRetransCount', 'pair1pwrDbmUp', 'pair1pwrDbmDown', 'pair1bearer0UpDelayCount',
                   'pair1bearer0DnDelayCount', 'pair1bearer0UpInpCount', 'pair1bearer0DnInpCount', 'pair2pwrDbmUp',
                   'pair2pwrDbmDown', 'pair2bearer1UpDelayCount', 'pair2bearer1DnDelayCount', 'pair2bearer1UpInpCount',
                   'pair2bearer1DnInpCount', 'upGrpMaxRate', 'upGrpMaxCap', 'dnGrpMaxRate', 'dnGrpMaxCap', 'lapseTime',
                   'vectorBand', 'vectorState', 'errSampleSent', 'errSampleDrop', 'errStatusSent', 'errStatusDrop',
                   'pair2capacityUp', 'pair2marginUp', 'pair2capacityDn', 'pair2marginDn', 'pair1losErrorDn',
                   'pair1fecMinErrorDn', 'pair1crcMinErrorDn', 'pair1lofErrorDn', 'pair1lomErrorDn', 'pair1fLossUp',
                   'pair1fecMinErrorUp', 'pair1crcMinErrorUp', 'pair1lofErrorUp', 'pair1lomErrorUp', 'pair2losErrorDn',
                   'pair2fecMinErrorDn', 'pair2crcMinErrorDn', 'pair2lofErrorDn', 'pair2lomErrorDn', 'pair2fLossUp',
                   'pair2fecMinErrorUp', 'pair2crcMinErrorUp', 'pair2lofErrorUp', 'pair2lomErrorUp', 'pair1esErrorDn',
                   'pair1esErrorUp', 'pair1sesErrorDn', 'pair1sesErrorUp', 'pair1uasErrorDn', 'pair1uasErrorUp',
                   'pair2esErrorDn', 'pair2esErrorUp', 'pair2sesErrorDn', 'pair2sesErrorUp', 'pair2uasErrorDn',
                   'pair2uasErrorUp', 'pair1oneMhzAtten', 'pair1syncCount', 'pair1syncTime', 'pair1trainTime',
                   'pair1estLoopLength', 'pair1usConnMethod', 'pair1dsConnMethod', 'pair2usConnMethod',
                   'pair2dsConnMethod', 'pair2oneMhzAtten', 'pair2syncCount', 'pair2syncTime', 'pair2trainTime',
                   'pair2estLoopLength', 'pair1up0Latn', 'pair1up0Satn', 'pair1up0Margin', 'pair1up0TxPower',
                   'pair1up1Latn', 'pair1up1Satn', 'pair1up1Margin', 'pair1up1TxPower', 'pair1dn1Latn', 'pair1dn1Satn',
                   'pair1dn1Margin', 'pair1dn1TxPower', 'pair1dn2Latn', 'pair1dn2Satn', 'pair1dn2Margin',
                   'pair1dn2TxPower', 'pair1dn3Latn', 'pair1dn3Satn', 'pair1dn3Margin', 'pair1dn3TxPower',
                   'pair2up0Latn', 'pair2up0Satn','pair2up0Margin', 'pair2up0TxPower', 'pair2up1Latn', 'pair2up1Satn',
                   'pair2up1Margin', 'pair2up1TxPower', 'pair2dn1Latn', 'pair2dn1Satn', 'pair2dn1Margin',
                   'pair2dn1TxPower', 'pair2dn2Latn', 'pair2dn2Satn', 'pair2dn2Margin', 'pair2dn2TxPower',
                   'pair2dn3Latn', 'pair2dn3Satn', 'pair2dn3Margin', 'pair2dn3TxPower','modemFirmVersion', 'dslVersion',
                   'modemChipset', 'vendorName', 'vendorId', 'dslDataMode', 'dslDataLink', 'dslEmulationType',
                   'dslPriVc', 'dslRxBytes', 'dslRxFrames', 'dslRxErrors', 'dslTxBytes', 'dslTxFrames', 'dslTxErrors',
                   'wanIpv4Ip', 'wanIpv4Mask', 'lanIpv4Ip', 'lanIpv4Mask', 'wanIpv4Gw', 'dnsServer0', 'wanMacAddress',
                   'ipv4State', 'wanVlanId', 'ethRxBytes', 'ethRxFrames', 'ethRxErrors', 'ethRxDropped', 'ethTxBytes',
                   'ethTxFrames', 'ethTxErrors', 'ethTxDropped', 'ethTxCollisions', 'ethLinkStatus', 'pingDestination',
                   'pingRequestsTx', 'pingRepliesRx', 'pingPercentLost', 'pingLostPerLostPerc', 'pingCurrDelay',
                   'pingAvgDelay', 'pingMaxDelay', 'pingMinDelay', 'pingMessage', 'pingLastPingIp',
                   'traceRtDestination', 'traceRtState', 'traceRtActive', 'traceRtNumHops', 'traceRtHop1Delay',
                   'traceRtHop1Ip', 'traceRtHop1Nm', 'traceRtHop2Delay', 'traceRtHop2Ip', 'traceRtHop2Nm',
                   'traceRtHop3Delay', 'traceRtHop3Ip', 'traceRtHop3Nm', 'traceRtHop4Delay', 'traceRtHop4Ip',
                   'traceRtHop4Nm', 'traceRtHop5Delay', 'traceRtHop5Ip', 'traceRtHop5Nm', 'bits', 'snr', 'hlog', 'qln']

    df = Dictionary.dict
    datetimestr = datetime.now().strftime('_%Y%m%d%H%M%S%f')
    csv_file_name = "HST" + datetimestr + ".csv"
    with open(csv_file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerow(df)
        csvfile.close()
    Dictionary.dict.clear()
