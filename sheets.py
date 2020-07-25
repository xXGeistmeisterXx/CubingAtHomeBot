import stats
import output
import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials

def importtimes(client, url, event, ldata):
  fsheet = client.open_by_url(url)
  
  rs = None
  try:
    rs = fsheet.add_worksheet(title=event, rows=str(1000), cols="14")
  except:
    rs = fsheet.worksheet(event)
  data = rs.get_all_records()
  
  start = 0
  if data:
    start = len(data)
 
  return output.results(rs, start, ldata)

def getscrambles(client, url, name, event):
  fsheet = client.open_by_url(url)
  sheet = fsheet.worksheet(name)
  data = sheet.get_all_records()
  
  scrambles = []
  images = []
  ind = list(data[0]).index(event)
  skey = list(data[0])[ind + 1]
  ikey = list(data[0])[ind + 2]
  
  for row in data:
    scrambles.append(row[skey])
    images.append(row[ikey])
    
  return scrambles, images

def geteventsn(client, url, name): 
  fsheet = client.open_by_url(url) 
  sheet = fsheet.worksheet(name)

  data = sheet.get_all_records() 
  active = [] 
  for key in list(data[0].keys()):
      if data[0][key] == "ON": 
          active.append(key) 
          
  return active

def inevent(client, url, name, event, email): 
  fsheet = client.open_by_url(url)
  sheet = fsheet.worksheet(name) 
  data = sheet.get_all_records() 
  
  emails = [] 
  for row in data:
    row[event] = str(row[event])
    if(not row[event].isspace() and row[event] and data.index(row) > 0): 
      emails.append(row[event].lower()) 
  return email.lower() in emails

def checkemail(client, url, event, email): 
  fsheet = client.open_by_url(url)
  try: 
    sheet = fsheet.worksheet(event) 
  except: 
    return False 
  data = sheet.get_all_records() 
  
  emails = [] 
  for row in data:
    emails.append(str(row["EMAIL"]).lower())
  return str(email).lower() in emails

def formatrun(client, url, name): 
    
  fsheet = client.open_by_url(url) 
  sheet = fsheet.worksheet(name)
  data = sheet.get_all_records()

  rs = None 
  try: 
    rs = fsheet.add_worksheet(title=sheet.title + "(r)", rows=str(sheet.row_count), cols="10") 
  except: 
    rs = fsheet.worksheet(sheet.title + "(r)")

  fdata = stats.getSortedStats(data) 
  output.outdat(rs, fdata)

  return "success"

def check(client, url, name):
  return 1
  while True: 
    flag = True 
    try: 
      fsheet = client.open_by_url(url) 
    except: 
      flag = False 
    if flag: 
      break 
    return(-2)

  while True: 
    flag = True 
    try: 
      sheet = fsheet.worksheet(name) 
    except: 
      flag = False 
    if flag: 
      break 
    return(-1)

  return(1)
