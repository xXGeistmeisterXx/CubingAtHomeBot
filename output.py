from string import ascii_lowercase

def outdat(sheet, data):
  rdata = []

  for row in data:
    rdata.append([row["EMAIL"], str(row["NAME"][0]) + " " + str(row["NAME"][1]), str(row["ID"]), row["AVERAGE"], row["TIMES"][0], row["TIMES"][1], row["TIMES"][2], row["TIMES"][3], row["TIMES"][4]])

  sheet.update("A1:I" + str(len(data)), rdata)
