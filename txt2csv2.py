import re
from datetime import datetime
from Utils import ExtractData,Dictionary,WriteCsv

datetimestr = datetime.now().strftime('_%Y%m%d%H%M%S')
csv_file_name="HST"+datetimestr+".csv"

path = 'C:\\Users\\ac80060\\Downloads\\SP19708849479X.txt'
res=""
end_line = '#======================================='

with open('C:\\Users\\ac80060\\Downloads\\Headings.txt') as file:
    list = file.read().splitlines()
    file.close()

# with open(path, 'a+') as f:
#     f.seek(0)
#     data=f.read(100)
#     if len(data)>0:
#         f.write("\n")
#     f.write(end_line)
#     f.close()

with open(path, 'r') as f:
    line_num=0
    start_line_num=0
    datafile=f.readlines()
    ExtractData.getInitialData(datafile)
    for heading in list:
        for line in datafile:
            line_num += 1
            if heading in line:
                start_line_num = line_num
                hname = re.sub("[\s#()-]", "", heading)
            if ':' in line and (start_line_num != 0):
                eval("ExtractData.get" + hname + "(line)")
            if (end_line in line) and (start_line_num != 0):
                start_line_num = 0
    print(Dictionary.dict)
    WriteCsv.writeInCsv()


