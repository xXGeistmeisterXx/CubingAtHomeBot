from flask import Flask, request, render_template, redirect, url_for
import sheets as sh
import stats as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
pname = "VCB"

app = Flask(__name__)

@app.route('/freevbucks',  methods=['POST', 'GET'])
def rickroll():
  return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

@app.route('/',  methods=['POST', 'GET'])
def home():
  return redirect(url_for("events"))

@app.route('/events',  methods=['POST', 'GET'])
def events():
  global pname
  if request.method == 'POST':

    if(request.form.get("1")):
      url = request.form.get("url")
      name = request.form.get("name")
      newurl = "https://cubething.kikoho.xyz/events?url=" + url + "&name=" + name
      return render_template("link.html", url="<a target='_blank' href=" + newurl + ">" + newurl + "</a>", name=pname)

    elif(request.form.get("2")):

      scope = ["https://spreadsheets.google.com/feeds"]
      creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
      client = gspread.authorize(creds)

      url = request.args.get('url')
      name = request.args.get('name')

      ans = checkall(client, url, name)
      if(ans): return ans

      if(sh.checkemail(client, url, request.form.get("event"), request.form.get("email"))):
        return render_template("error.html", error="already submitted", name=pname)

      if(request.form.get("email").lower() != request.form.get("temail").lower()):
        return render_template("error.html", error="emails do not match", name=pname)

      times = [0, 0, 0, 0, 0]
      pens = ["DNF", "DNF", "DNF", "DNF", "DNF"]

      for i in range(1,6):
        times[i - 1] = st.minstosecs(request.form.get("time" + str(i)))
        if(times[i - 1] < 240):
          pens[i - 1] = request.form.get("pen" + str(i))
      
      ldata = [request.form.get("email"), request.form.get("fname"), request.form.get("lname"), request.form.get("wcaid"), times[0], pens[0], times[1], pens[1], times[2], pens[2], times[3], pens[3], times[4], pens[4]]
      sh.importtimes(client, url, request.form.get("event"), ldata)
      return render_template("success.html", name=pname)

    else:
      event = request.form.get("events")
      email = request.form.get("email")
      scope = ["https://spreadsheets.google.com/feeds"]
      creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
      client = gspread.authorize(creds)

      url = request.args.get('url')
      name = request.args.get('name')

      ans = checkall(client, url, name)
      if(ans): return ans
      
      auth = sh.inevent(client, url, name, event, email)
      if(auth):
        scrambles, images = sh.getscrambles(client, url, name, event)

        return render_template("input.html", scrambles=scrambles, images=images, email=email, event=event, name=pname)

      else:
        return render_template("error.html", error="email not found", name=pname)

  else:

    url = request.args.get('url')
    name = request.args.get('name')

    if(not url or not name):
      return render_template("gen.html", name=pname)

    scope = ["https://spreadsheets.google.com/feeds"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
    client = gspread.authorize(creds)

    ans = checkall(client, url, name)
    if(ans): return ans

    events = sh.geteventsn(client, url, name)
	
    items = ""
    for event in events:
      items += '<option value="%s">%s</option> ' % (event, event)
    return render_template("form.html", select=items, name=pname)

@app.route('/url',  methods=['POST', 'GET'])
def url():
  if request.method == 'POST':
    url = request.form.get("url")
    name = request.form.get("name")
    newurl = "https://CubingBot--tylergeist1.repl.co/events?url=" + url + "&name=" + name
    return render_template("link.html", url="<a target='_blank' href=" + newurl + ">" + newurl + "</a>", name=pname)
  else:
	  return render_template("gen.html", name=pname)

@app.route('/format',  methods=['POST', 'GET'])
def format():
  global pname
  if request.method == 'POST':
    url = request.form.get("url")
    name = request.form.get("name")
    return out(url, name)
  else:
	  return render_template("format.html", name=pname)

def out(url, name):
  global pname
  scope = ["https://spreadsheets.google.com/feeds"]
  creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
  client = gspread.authorize(creds)

  ans = checkall(client, url, name)
  if(ans): return ans

  sh.formatrun(client, url, name)
  return render_template("fsuccess.html", name=pname)

def checkall(client, url, name):
  global pname
  while True:
    flag = True
    if(sh.check(client, url, "test") > -2):
      break
    return render_template("error.html", error="bad module link", name=pname)

  while True:
    flag = True
    if(sh.check(client, url, name) > -1):
      break
    return render_template("error.html", error="bad sheet name", name=pname)

  return None

if __name__ == '__main__':
    app.run('0.0.0.0','80')

