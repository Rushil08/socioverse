from flask import Flask, render_template, request, flash, url_for
import pickle
app = Flask(__name__)

#making a database file

'''f=open("UserDatabase","wb")
pickle.dump([['username@gmail.com','password',10,'username'],['rushil@gmail.com','rushil',5,'rushil']],f)
f.close()'''

'''f=open("EventDatabase","wb")
pickle.dump([['username','sample','sample','2022/03/11','2022/03/13',10,'text',1234567890,'abc@gmail.com']],f)
f.close()'''

try:
    f=open("EventDatabase","rb")
    event_database=pickle.load(f)
    f.close()
except:
    f.close()


#fetching the database file
try:
    f=open("UserDatabase","rb")
    user_database=pickle.load(f)
    f.close()
except: 
    f.close()

title=''
location=''
duration=''
participants=0
desc=''
mob=0
mail=''
pics=''
username=''
l=len(event_database)
eventnum=0

@app.route("/")
def start():
    return render_template('login.html')
    #return redirect(url_for('login'))

@app.route('/signin',methods=["POST","GET"])
def login():
    flag=0
    user=request.form.get('username')
    pwd=request.form.get('password')
    for i in range(len(user_database)):
        if (user==user_database[i][0] or user==user_database[i][3]) and user_database[i][1]==pwd:  
            flag=1
            global sociocoins,username,email
            sociocoins=user_database[i][2]
            email=user_database[i][0]
            username=user_database[i][3]
            global eventnum
            return render_template('homepage.html',event_database=event_database,eventnum=eventnum)
        else:
            continue
    if flag==0:
        return render_template('login.html')

@app.route('/register')       
def register():
    return render_template('register.html')

@app.route('/registerform',methods=["POST","GET"])
def registerform():
    global user_database
    username=request.form.get('username')
    password=request.form.get('password')
    password2=request.form.get('passconfirm')
    email=request.form.get('email')
    sociocoins=0
    flag=0
    for i in range(len(user_database)):
        if username==user_database[i][3]:
            flag=1
            return render_template('register.html',info="Username already exists.")
    if flag==0:    
        if username not in user_database and password==password2:
            f=open("UserDatabase","wb")
            user_database.append([email,password,sociocoins,username])
            pickle.dump(user_database,f)
            f.close()
            return render_template('login.html') 
        else:
            return render_template('register.html',info="Username already exists.")

@app.route("/homepage")
def home():
    global event_database
    global eventnum
    return render_template("homepage.html",event_database=event_database,length=len(event_database),eventnum=eventnum)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/eventpage')
def eventpage():
    return render_template('createevent.html')

@app.route('/status')
def status(eventnum=0):
    title=event_database[eventnum][1]
    location=event_database[eventnum][2]
    dur1=event_database[eventnum][3]
    dur2=event_database[eventnum][4]
    participants=event_database[eventnum][5]
    description=event_database[eventnum][6]
    mob=event_database[eventnum][7]
    mail=event_database[eventnum][8]

    return render_template('status.html',title=title,location=location,start=dur1,end=dur2,participants=participants,description=description,mob=mob,mail=mail)

@app.route('/profile')
def profile():
    return render_template('profile.html',username=username,email=email,sociocoins=sociocoins)

@app.route('/event',methods=["POST","GET"])
def event():
    global title,location,duration,participants,desc,mob,mail,pics,username,event_database
    title=request.form.get('title')
    location=request.form.get('location')
    duration=request.form.get('duration')
    duration2=request.form.get('duration2')
    participants=request.form.get('particips')
    desc=request.form.get('desc')
    mob=request.form.get('number')
    mail=request.form.get('email')
    participantnames=[]
    event_database.append([username,title,location,duration,duration2,participants,participantnames,desc,mob,mail]) 
    f=open("EventDatabase","wb")
    pickle.dump(event_database,f)
    f.close()
    return render_template('status.html',title=title,location=location,dur1=duration,dur2=duration2,participants=participants,desc=desc,mob=mob,mail=mail)

if __name__ == '__main__':
   app.run()