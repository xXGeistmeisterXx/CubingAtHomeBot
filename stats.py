def getSortedStats(data):

  fdata = []
  for row in data:
    nrow = {"EMAIL":row["EMAIL"], "NAME":(row["FIRST"], row["LAST"]), "ID":row["ID"], "AVERAGE":0, "TIMES":[0, 0, 0, 0, 0]}

    for i in range(5):
      if(row["PENALTY " + str(i + 1)] == "DNF"):
        nrow["TIMES"][i] = "DNF"
      elif(row["PENALTY " + str(i + 1)] == "2+"):
        nrow["TIMES"][i] = float('%.2f'%(row["SOLVE " + str(i + 1)] + 2))
      else:
        nrow["TIMES"][i] = float('%.2f'%(row["SOLVE " + str(i + 1)]))

    ltime = nrow["TIMES"][:]
    btime, stime = ltime[0], ltime[0]
    for time in ltime[1:]:
      if(time == "DNF"):
        btime = time
      elif(stime == "DNF"):
        stime = time
      elif btime != "DNF" and time > btime:
        btime = time
      elif stime != "DNF" and time < stime:
        stime = time
    
    #print(ltime)

    ltime.remove(stime)
    ltime.remove(btime)

    #print(ltime)

    if("DNF" in ltime):
      nrow["AVERAGE"] = "DNF"
    else:
      nrow["AVERAGE"] = float('%.2f'%(sum(ltime) / len(ltime)))

    for i in range(5):
      nrow["TIMES"][i] = mtos(nrow["TIMES"][i])
      

    fdata.append(nrow)

  for ind in range(len(fdata)):
    for row in fdata[ind + 1:]:
      if(fdata[ind]["AVERAGE"] == "DNF"):
        pass
      elif(row["AVERAGE"] == "DNF"):
        temp = row
        fdata[fdata.index(row)] = fdata[ind]
        fdata[ind] = temp
      elif(row["AVERAGE"] > fdata[ind]["AVERAGE"]):
        temp = row
        fdata[fdata.index(row)] = fdata[ind]
        fdata[ind] = temp
  
  fdata = fdata[::-1]

  for ind in range(len(fdata)):
    fdata[ind]["AVERAGE"] = mtos(fdata[ind]["AVERAGE"])

  return fdata


def mtos(ttime):
  if(ttime == "DNF"):
    return ttime
  secs = int(str(ttime)[:str(ttime).find(".")])
  rest = str(ttime)[str(ttime).find(".") + 1:]
  mins = 0
  while(secs >= 60):
    mins += 1
    secs -= 60
  ntime = ""
  if(mins > 0):
    if(len(str(secs)) < 2):
      secs = "0" + str(secs)
    ntime = str(mins) + ":" + str(secs)
  else:
    ntime = str(secs)
  if(rest):
    if(len(str(rest)) < 2):
      rest = str(rest) + "0"
    ntime += "." + rest
  return str(ntime)
    

def stom(ttime):
  if not ":" in ttime:
    return float(ttime)
  else:
    mins = ttime[:ttime.find(":")]
    secs = (int(mins) * 60) + float(ttime[ttime.find(":") + 1:])
    return secs
