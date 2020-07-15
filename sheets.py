import stats
import output
import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

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
  print(data)
  scrambles = []
  images = []
  ind = list(data[0]).index(event)
  skey = list(data[0])[ind + 1]
  ikey = list(data[0])[ind + 2]
  print(skey)
  print(ikey)
  for row in data:
    scrambles.append(row[skey])
    images.append(row[ikey])
  print(scrambles)
  return scrambles, images

def getevents(client, url, name):
  fsheet = client.open_by_url(url)
  sheet = fsheet.worksheet(name)

  data = sheet.get_all_records()
  active = []
  for key in list(data[0].keys())[::2]:
    if data[0][key] == "ON":
      active.append(key)
  return active

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
      emails.append(row[event])
  return email in emails

def checkemail(client, url, event, email):
  fsheet = client.open_by_url(url)
  try: 
    sheet = fsheet.worksheet(event)
  except:
    return False
  data = sheet.get_all_records()
  emails = []
  for row in data:
    emails.append(str(row["EMAIL"]))
    
  print(emails)
  print(type(emails))
  print(email)
  print(type(email))
  return str(email) in emails

def getemails(client, url, name, event, email):
  fsheet = client.open_by_url(url)
  sheet = fsheet.worksheet(name)
  data = sheet.get_all_records()
  emails = []
  password = ""
  for row in data:
    if(not row[event].isspace() and row[event] and data.index(row) > 0):
      emails.append(row[event])
  password = list(list(data)[0])[list(list(data)[0]).index(event) + 1]
  return email in emails, password

def formatrun(client, url, name):
  os.system("clear")

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

def stuff(): 
  scope = ["https://spreadsheets.google.com/feeds"]
  creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
  client = gspread.authorize(creds)

  print("CubingBot Beta v2.0")
  url = input("Sheets link: ")

  while True:
    flag = True
    if(check(client, url, "test") > -2):
      print("Module Found")
      break
    print("\nModule Not Found")
    url = input("Sheets link: ")


  #fsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1UhmzRBjdG9KXssUr3gY57Nwz_dACHt9TTZ7pNqjJ0AM/edit?usp=sharing")

  name = input("Sheet name: ")

  while True:
    flag = True
    if(check(client, url, name) > -1):
      print("Sheet found")
      break
    print("\nSheet not found")
    name = input("Sheet name: ")

  fsheet = client.open_by_url(url)
  sheet = fsheet.worksheet(name)
  data = sheet.get_all_records()

  print(data)

  #formatrun(client, url, name)
  print("done")

#stuff()
