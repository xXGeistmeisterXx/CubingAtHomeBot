from flask import Flask, request, render_template
import sheets as sh
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask('')

@app.route('/',  methods=['POST', 'GET'])
def home():
  if request.method == 'POST':
    url = request.form.get("url")
    name = request.form.get("name")
    print(url)
    print(name)
    return out(url, name)
  else:
	  return render_template("index.html")

def out(url, name):
  scope = ["https://spreadsheets.google.com/feeds"]
  creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
  client = gspread.authorize(creds)

  while True:
    flag = True
    if(sh.check(client, url, "test") > -2):
      print("Module Found")
      break
    return "bad module"

  while True:
    flag = True
    if(sh.check(client, url, name) > -1):
      print("Sheet found")
      break
    return "bad sheet name"

  return sh.formatrun(client, url, name)


app.run(host='0.0.0.0',port=8080)

