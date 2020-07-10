from string import ascii_lowercase

def outdat(sheet, data):
  rdata = []
  rdata.append(["EMAIL", "POSITION", "AVERAGE", "NAME", "WCA ID", "SOLVE 1", "SOLVE 2", "SOLVE 3", "SOLVE 4", "SOLVE 5"])

  count = 0
  for row in data:
    count += 1
    rdata.append([row["EMAIL"], str(count), row["AVERAGE"], str(row["NAME"][0]) + " " + str(row["NAME"][1]), str(row["ID"]), row["TIMES"][0], row["TIMES"][1], row["TIMES"][2], row["TIMES"][3], row["TIMES"][4]])

  sheet.update("A1:J" + str(len(rdata)), rdata)

def results(sheet, start, ldata):
  rdata = []
  if(start < 1):
    rdata.append(["EMAIL", "FIRST", "LAST", "ID", "SOLVE 1", "PENALTY 1", "SOLVE 2", "PENALTY 2", "SOLVE 3", "PENALTY 3", "SOLVE 4", "PENALTY 4", "SOLVE 5", "PENALTY 5"])
    start -= 1

  start += 1
  rdata.append(ldata)
  sheet.update("A" + str(start + 1) + ":N" + str(len(rdata) + start), rdata)
  return "doned"