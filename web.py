from flask import Flask, request, render_template
import sheets as sh
import stats as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask('')

@app.route('/test',  methods=['POST', 'GET'])
def test():
  return('<button onclick="window.history.back()">back?</button>')

@app.route('/new',  methods=['POST', 'GET'])
def new():
  if request.method == 'POST':
    if(request.form.get("2")):

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

      if(sh.checkemail(client, url, request.form.get("event"), request.form.get("email"))):
        return "already submitted"

      if(request.form.get("email") != request.form.get("temail")):
        return "emails do not match"

      times = [0, 0, 0, 0, 0]
      pens = ["DNF", "DNF", "DNF", "DNF", "DNF"]

      for i in range(1,6):
        times[i - 1] = st.stom(request.form.get("time" + str(i)))
        if(times[i - 1] < 240):
          pens[i - 1] = request.form.get("pen" + str(i))
      
      ldata = [request.form.get("email"), request.form.get("fname"), request.form.get("lname"), request.form.get("wcaid"), times[0], pens[0], times[1], pens[1], times[2], pens[2], times[3], pens[3], times[4], pens[4]]
      return sh.importtimes(client, url, request.form.get("event"), ldata)
      return("k")
    else:
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
      
      auth = sh.inevent(client, url, name, event, email)
      if(auth):
        scrambles, images = sh.getscrambles(client, url, name, event)

      return render_template("input.html", scrambles=scrambles, images=images, email=email, event=event)

      return "hi"

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

    events = sh.geteventsn(client, url, name)

    items = ""
    for event in events:
      items += '<option value="%s">%s</option> ' % (event, event)
    return render_template("form.html", select=items)

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

