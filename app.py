from flask import Flask, redirect, request, render_template, Markup
import pickle

app = Flask(__name__)
app.config['SECRET_KEY'] = "SUPER_SECRET"

def store_in_database(user_object):
   """
   Dummy function.
   """
   pass

posts = []

@app.route("/")
def index():
   output = """
      <link rel="stylesheet" href="/static/site.css">
      <h1>Hacky Message Board</h1>
      <h2>POSTS</h2>
      <div>
         <form action='sendmsg' method='post'>
            <input type='text' name='person' value='Name'>
            <input type='text' name='msg' autofocus value='Your message'>
            <input type='submit' value='Submit'>
         </form>
         <form action='refresh'>
            <input type='hidden' name='next' value='/'>
            <input type='submit' value='Refresh'>
         </form>
      </div>
   """
   for post in posts:
      output += "<p>" + post + "</p>"
   return output

@app.route("/sendmsg", methods=["POST"])
def post():

   # Add message to the list of posts and go back to the main page
   person = request.form["person"]
   msg = request.form["msg"]


   posts.append(f"{person} says {msg}")
   return redirect("/")

@app.route("/refresh")
def refresh():
   nexturl = request.args.get("next").lower()
   return redirect(nexturl)
   # return redirect("/")

@app.route("/buy", methods=["POST", "GET"])
def buy():
   if request.method == 'POST':

      pet = request.form["pet"]
      amount = int(request.form["amount"])

      cost = 100
      msg = f"You just bought {amount} {pet}(s) for {cost*amount} CZK!"
   else:
      msg = "Mythical Pets for 100 CZK"

   return render_template("buyer.html", mesg=msg)

@app.route("/upload", methods=['POST'])
def import_object():
   for f in list(request.files.keys()):
      ff = request.files[f]
   user_object = pickle.load(ff)
   store_in_database(user_object)
   return 'OK'

if __name__ == "__main__":
   app.run(debug=True)
