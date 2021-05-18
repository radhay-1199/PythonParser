import os

import csv2string
import txt2csv2
from Utils import Dictionary, WriteCsv


def main_process():
    path = '/hyperlite/SOURCE/TECHNICIAN_TEMP'

    for filename in os.listdir(path):
          try:
              if ((filename.endswith('G') or filename.endswith('S') or filename.endswith('T') or
                filename.endswith('X')) and ((len(filename) == 14 and filename[3:13].isdigit() == True) or
                (len(filename) == 13 and filename[2:12].isdigit() == True)) and (filename.startswith('AP') or
                filename.startswith('SP') or filename.startswith('DP'))):

                  Dictionary.dict['techUploadSource'] = 'HST'
                  if len(filename) == 14:
                      Dictionary.dict['wtn'] = filename[3:13]
                      if filename[13] == 'G':
                          Dictionary.dict['techTestLocation'] = 'GATEWAY/MODEM'
                      elif filename[13] == 'S':
                          Dictionary.dict['techTestLocation'] = 'SNI/NI'
                      elif filename[13] == 'T':
                          Dictionary.dict['techTestLocation'] = 'TERMINAL'
                      elif filename[13] == 'X':
                          Dictionary.dict['techTestLocation'] = 'CROSSBOX'
                  elif len(filename) == 13:
                      Dictionary.dict['wtn'] = filename[2:12]
                      if filename[12] == 'G':
                          Dictionary.dict['techTestLocation'] = 'GATEWAY/MODEM'
                      elif filename[12] == 'S':
                          Dictionary.dict['techTestLocation'] = 'SNI/NI'
                      elif filename[12] == 'T':
                          Dictionary.dict['techTestLocation'] = 'TERMINAL'
                      elif filename[12] == 'X':
                          Dictionary.dict['techTestLocation'] = 'CROSSBOX'
                  print("Path",os.path.join(path, filename))
                  txt2csv2.txt_parser(os.path.join(path, filename))

                  for csvFile in os.listdir(path):
                      try:
                          if(csvFile.endswith('.csv') and (csvFile.startswith('AP') or
                            csvFile.startswith('SP') or csvFile.startswith('DP')) and ((len(csvFile) == 18 and
                            csvFile[3:13] == Dictionary.dict['wtn']) or (len(csvFile) == 17 and
                            csvFile[2:12] == Dictionary.dict['wtn']))):
                            Dictionary.dict['partialTestSetUpload'] = 'N'
                            csv2string.csv_parser(os.path.join(path, csvFile))
                          else:
                              if 'partialTestSetUpload' not in Dictionary.dict.keys():
                                  Dictionary.dict['partialTestSetUpload'] = 'Y'
                      except Exception as e: print(e)
                  WriteCsv.writeInCsv()
          except Exception as e: print(e)



if __name__ == '__main__':
    #print("hello")
    main_process()

