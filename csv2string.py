import pandas as pd
from Utils import Dictionary

def extractCsv(df):
    bits = []
    for i in range(1, 9000):
        try:
            temp = df.iat[i, 0]
            bits.append(temp)
        except:
            break
    converted_list = [str(element) for element in bits]
    bits_str = ",".join(converted_list)
    Dictionary.dict["bits"] = bits_str
    #print(bits_str)
    #print('--------------------------')

    snr = []
    for i in range(1, 9000):
        try:
            temp = df.iat[i, 1]
            snr.append(temp)
        except:
            break
    converted_list = [str(element) for element in snr]
    snr_str = ",".join(converted_list)
    Dictionary.dict["snr"]=snr_str
    #print(snr_str)
    #print('--------------------------')

    hlog = []
    for i in range(1, 9000):
        try:
            temp = df.iat[i, 2]
            hlog.append(temp)
        except:
            break
    converted_list = [str(element) for element in hlog]
    hlog_str = ",".join(converted_list)
    Dictionary.dict["hlog"] = hlog_str
    #print(hlog_str)
    #print('--------------------------')

    qln = []
    for i in range(1, 9000):
        try:
            temp = df.iat[i, 3]
            qln.append(temp)
        except:
            break
    converted_list = [str(element) for element in qln]
    qln_str = ",".join(converted_list)
    Dictionary.dict["qln"] = qln_str
    #print(qln_str)
    #print('--------------------------')


path = "C:\\Users\\ac80060\\Downloads\\DP12187442762S.csv"
try:
    df = pd.read_csv(path, header=None, skiprows=[1, 2, 3, 4, 5, 6, 7],
                 usecols=[2, 3, 4, 5], error_bad_lines=False)
    extractCsv(df)
except ValueError:
    count=1
    with open(path, 'r') as f:
        lines = f.read().splitlines()
        f.close()
    with open(path, "w") as fw:
        for line in lines:
            if count <= 7:
                fw.write(line + ",,,,,\n")
                count += 1
            else:
                fw.write(line + "\n")
        fw.close()
    df = pd.read_csv(path, header=None, skiprows=[1, 2, 3, 4, 5, 6, 7],
                     usecols=[2, 3, 4, 5], error_bad_lines=False)
    extractCsv(df)
