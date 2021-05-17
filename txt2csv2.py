import re
from Utils import ExtractData, Dictionary


def txt_parser(txt_path):
    headings_path = 'C:\\Users\\ac80060\\Downloads\\Headings.txt'
    #path = 'C:\\Users\\ac80060\\Downloads\\SP19708849479X.txt'
    end_line = '#======================================='

    with open(headings_path) as file:
        list = file.read().splitlines()
        file.close()

    with open(txt_path, 'a+') as f:
        f.seek(0)
        data = f.read(100)
        if len(data) > 0:
            f.write("\n")
        f.write(end_line)
        f.close()

    with open(txt_path, 'r') as f:
        line_num = 0
        start_line_num = 0
        datafile = f.readlines()
        ExtractData.getInitialData(datafile)
        for heading in list:
            for line in datafile:
                line_num += 1
                if heading in line:
                    start_line_num = line_num
                    hname = re.sub("[\s#()-]", "", heading)
                if (end_line not in line) and (start_line_num != 0):
                    try:
                        eval("ExtractData.get" + hname + "(line)")
                    except AttributeError:
                        start_line_num = 0
                        continue
                if (end_line in line) and (start_line_num != 0):
                    start_line_num = 0
        print(Dictionary.dict)
    # WriteCsv.writeInCsv()
