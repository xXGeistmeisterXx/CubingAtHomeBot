#import stats
import output
import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

def formatrun(client, url, name):
  os.system("clear")

  fsheet = client.open_by_url(url)
  sheet = fsheet.worksheet(name)

  data = sheet.get_all_records()

  rs = None
  try:
    rs = fsheet.add_worksheet(title=sheet.title + "(r)", rows=str(sheet.row_count), cols="9")
  except:
    rs = fsheet.worksheet(sheet.title + "(r)")

  print()

  fdata = stats.getSortedStats(data)

  #pprint(fdata)
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

  formatrun(client, url, name)
  print("done")

if __name__ == "__main__":
  stuff()