import os

import csv2string
import txt2csv2
from Utils import Dictionary, WriteCsv


def main_process():
    path = '/hyperlite/SOURCE/TECHNICIAN_TEMP'

    for filename in os.listdir(path):
          try:
              if ((filename.endswith('.txt') and len(filename) is 14) and (filename.startswith('A') or
                      filename.startswith('S') or filename.startswith('D')) and filename[3:13].isdigit() == True and
                      (filename[13] == 'G' or filename[13] == 'S' or filename[13] == 'T' or filename[13] == 'X')):

                  Dictionary.dict['techUploadSource'] = 'HST'
                  Dictionary.dict['wtn'] = filename[3:13]
                  if filename[13] is 'G': Dictionary.dict['techTestLocation'] = 'GATEWAY/MODEM'
                  elif filename[13] is 'S': Dictionary.dict['techTestLocation'] = 'SNI/NI'
                  elif filename[13] is 'T': Dictionary.dict['techTestLocation'] = 'TERMINAL'
                  elif filename[13] is 'X': Dictionary.dict['techTestLocation'] = 'CROSSBOX'
                  txt2csv2.txt_parser(path + '/' + filename)

                  for csvFile in os.listdir(path):
                      try:
                          if((csvFile.endswith('.csv') and len(csvFile) is 14) and (csvFile.startswith('A') or
                            csvFile.startswith('S') or csvFile.startswith('D')) and csvFile[3:13].isdigit() == True and
                            csvFile[3:13] == filename[3:13] and (csvFile[13] == 'G' or csvFile[13] == 'S' or
                            csvFile[13] == 'T' or csvFile[13] == 'X')):
                            Dictionary.dict['partialTestSetUpload'] = 'N'
                            csv2string.csv_parser(path + '/' + csvFile)
                          else:
                            Dictionary.dict['partialTestSetUpload'] = 'Y'
                      except: pass
                  WriteCsv.writeInCsv()
          except: pass



if __name__ == '__main__':
    main_process()

