from Utils import Dictionary

def getInitialData(datafile):
    assetManufacture=datafile[0].replace("\n","")
    assetModel=datafile[1].replace("\n","")
    assetUniqueId=datafile[2].replace("\n","")
    assetSwVersion=datafile[3].replace("\n","")

def getXDSLAutoxTURConfiguration(line):
    vectoring = phyR = sra = dslInterface = ''
    if ':' in line:
        var, val = (line.split(":"))
        if var == 'Standard':  Dictionary.dict[var]=val.strip()
        if var == 'PhyR':  phyR = Dictionary.dict[var]=val.strip()
        if var == 'SRA':  sra = Dictionary.dict[var]=val.strip()
        if var == 'DSL Interface':  Dictionary.dict[var]=val.strip()
        print(line)

def getADSLSummary(line):
    print(line)

def get
