from flask import * 
import speech_recognition as sr import 
pyttsx3 
import pymysql 
from sqlalchemy import create_engine,text 
from sqlalchemy.orm import sessionmaker,scoped_session import os 
from gtts import gTTS 
engine = create_engine("mysql+pymysql://root@localhost:3306/voiceback") 
db=scoped_session(sessionmaker(bind=engine)) 
app = Flask(_name_) 
app.debug=True 
app.config["SECRET_KEY"] = "voicebackproject123" global 
account_balance 
# Initialize the speech recognizer and TTS engine recognizer 
= sr.Recognizer() 
tts_engine = pyttsx3.init() 
31 
@app.route('/balance') def 
balance(): 
if session.get('user') is not None: 
username = session['user'] 
account_balance = db.execute(text("SELECT account_balance FROM user 
WHERE username = :username"), {"username": username}).fetchone() 
db.commit() 
if account_balance: 
return jsonify({'account_balance': int(account_balance[0])}) else: 
return jsonify({'error': 'User not found'}), 404 return 
jsonify({'error': 'User not logged in'}), 403 
def get_account_balance(): 
response = balance() 
return response.get_json().get('account_balance', 0) 
# Function to convert text to speech using gTTS def 
speak_text(text): 
# tts_engine.say(text) 
# tts_engine.runAndWait() 
tts = gTTS(text=text, lang='en') 
audio_file = "temp.mp3" 
tts.save(audio_file) 
os.system(f"start {audio_file}") 
# Use "start" on Windows, "afplay" on 
32 
macOS, or "mpg321" on Linux 
def balanceUpdate(account_balance): if 
session.get('user') is not None: 
username=session['user'] 
print(username,account_balance) 
account_balance 
= 
db.execute(text("update 
user 
set 
account_balance=:amount WHERE username = :username"), {"username": 
username,"amount":account_balance}) 
db.commit() 
# Function to process the voice command 
def process_command(command,account_balance): response_text = 
"" 
if "balance" in command.lower(): 
response_text = f"Your account balance is {account_balance} dollars." elif 
"send" in command.lower(): 
words = command.lower().split() try: 
idx = words.index("send") recipient = 
words[idx + 1] amount = float(words[idx + 
2]) 
if amount <= int(account_balance): account_balance -= 
amount {recipient}. 
"print("update account_balance:",account_balance) 
33 
account_balance = balanceUpdate(account_balance) 
response_text=f"Successfully transferred {amount} dollars to 
else: 
response_text = "Insufficient balance to complete the transfer." except 
(ValueError, IndexError): 
response_text = "There was an error processing your transfer command." elif "dd" 
in command.lower(): 
words = command.lower().split() try: 
idx = words.index("to") recipient = 
words[idx + 1] amount = float(words[idx + 
2]) 
print(f'recipient {recipient}.amount {amount}') if amount 
<= account_balance: 
account_balance -= amount 
response_text 
{recipient}." 
else: 
= f"Successfully transferred {amount} dollars to 
response_text = "Insufficient balance to complete the transfer." except 
(ValueError, IndexError): 
response_text = "There was an error processing your transfer command." 
else: 
response_text = "Sorry, I didn't understand the command." 
return response_text 
34 
@app.route('/voice_command', methods=['POST']) def 
voice_command(): 
recognizer = sr.Recognizer() try: 
with sr.Microphone() as source: 
recognizer.adjust_for_ambient_noise(source) 
print("Listening for command...") audio_data = 
recognizer.listen(source) 
command = recognizer.recognize_google(audio_data) 
print(f"Received command: {command}") 
account_balance = get_account_balance() # Call the balance function to 
get the current balance 
response_text = process_command(command, account_balance) print(response_text) 
speak_text(response_text) # Call speak_text here data = { 
'request_text': command, 'response_text': 
response_text, 
} 
print(data) 
return jsonify(data) except 
sr.UnknownValueError: 
35 
return jsonify({'error': "Could not understand the audio."}) except 
sr.RequestError as e: 
return jsonify({'error': f"Speech Recognition service error: {e}"}) 
# Route to render the home page 
@app.route('/home') 
def home(): 
return render_template('home.html') 
@app.route('/') def 
index(): 
return render_template('index.html') 
@app.route('/login') def 
login(): 
return render_template('login.html') 
@app.route('/logincheck',methods=["POST","GET"]) def 
logincheck(): 
if request.method == "POST": 
us=request.form.get("username") 
pw=request.form.get("password") print(us,pw) 
ad = db.execute(text("select username from user where username=:us and 
36 
password=:pas"),{'us':us,'pas':pw}).fetchone() 
db.commit() 
print("initial",ad) if ad is 
None: 
print("ad",ad) session.pop('user', None) 
return render_template("login.html") else: 
print("ad",ad) session.pop('user', None) 
session['user']=us 
if us == "admin": 
return render_template("admindashbord.html",us=us) else: 
print("user redirect") 
return render_template("userdashbord.html",us=us) return 
render_template('login.html') 
@app.route('/userlist',methods=["POST","GET"]) def 
userlist(): 
if request.method == "GET": 
data = db.execute(text("select * from user")).fetchall() return 
render_template("adminuser.html",data=data) 
elif request.method == "POST": us=request.form.get("username") 
37 
pw=request.form.get("password") role=request.form.get("role") 
mob=request.form.get("mobile") 
acb=request.form.get("accountbalance") 
data 
= 
db.execute(text("insert 
user(username,password,role,mobile,account_balance) 
into 
values(:un,:pw,:role,:mob,:acb)"),{"un":us,'pw':pw,"role":role,"mob":mob,"acb":acb} 
) 
db.commit() 
print("Save Details Successfully") return 
redirect(url_for('userlist')) 
else: 
return render_template('login.html') 
@app.route('/acknow') def 
acknow(): 
if session.get('user') is not None: 
username = session['user'] 
user = db.execute(text("SELECT * FROM user WHERE username = 
:username"), {"username": username}).fetchone() 
db.commit() 
return render_template('downloadform.html',user=user) 
@app.route('/logout') def 
logout(): 
38 
session.pop('user', None) return 
redirect(url_for('login')) 
if _name_ == '_main_': 
app.run(debug=True)
