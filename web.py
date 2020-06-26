from flask import Flask, request, render_template
import sheets as sh
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask('')

@app.route('/',  methods=['POST', 'GET'])
def home():
  if request.method == 'POST':
    event = request.form.get("events")
    email = request.form.get("email")
    scope = ["https://spreadsheets.google.com/feeds"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
    client = gspread.authorize(creds)

    url = request.args.get('url')
    name = request.args.get('name')

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

    auth, password = sh.getemails(client, url, name, event, email)

    print(password)

    if auth: return password
    else: return "email not found"
  else:
    scope = ["https://spreadsheets.google.com/feeds"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
    client = gspread.authorize(creds)

    url = request.args.get('url')
    name = request.args.get('name')

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

    events = sh.getevents(client, url, name)

    items = ""
    for event in events:
      items += '<option value="%s">%s</option> ' % (event, event)
    return render_template("form.html", select=items)

@app.route('/url',  methods=['POST', 'GET'])
def url():
  if request.method == 'POST':
    url = request.form.get("url")
    name = request.form.get("name")
    print(url)
    print(name)
    newurl = "https://CubingBot--tylergeist1.repl.co/?url=" + url + "&name=" + name
    return "<a href=" + newurl + ">" + newurl + "</a>"
  else:
	  return render_template("gen.html")

@app.route('/format',  methods=['POST', 'GET'])
def format():
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

