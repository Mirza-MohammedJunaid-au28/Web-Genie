from fileinput import filename
from flask import Flask,render_template,redirect,session,request,send_file
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime
from io import BytesIO
import json

with open('config.json','r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)
app.secret_key = 'super-secret-key'

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail'],
    MAIL_PASSWORD = params['password']
)   # for mail
mail = Mail(app)

local_server = params['local_server']

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Discord Database Model
class Discord(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    discord_url = db.Column(db.String(255),unique=True,nullable=False)

# Whatsapp Database Model
class Whatsapp(db.Model):
    feilds = db.Column(db.String(50),primary_key=True)
    whatsapp_url = db.Column(db.String(255),unique=True,nullable=False)

# Contact Database Model
class Contact(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(120),nullable=False)
    phone = db.Column(db.String(15),nullable=False)
    message = db.Column(db.String(255),nullable=False)
    date = db.Column(db.String(255),nullable=False)

# Google Form Link Database Model
class Form(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    form_link = db.Column(db.String(255),nullable=False)

# Notes Databse Model
class Notes(db.Model):
    srno = db.Column(db.Integer,primary_key=True)
    contributerName = db.Column(db.String(50),nullable=False)
    department = db.Column(db.String(10),nullable=False)
    subject = db.Column(db.String(100),nullable=False)
    sem = db.Column(db.Integer,nullable=False)
    chapterNo = db.Column(db.Integer,nullable=False)
    topicName = db.Column(db.String(100),nullable=False)
    slug = db.Column(db.String(100),nullable=False)
    filename = db.Column(db.String(100),nullable=False)
    filedata = db.Column(db.LargeBinary)
    date = db.Column(db.String(255),nullable=False)

# Login Database Model
class Login(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(20),nullable=False)

# Index
@app.route("/")
def home():
    return render_template('index.html')

# Let's Talk
@app.route("/letsTalk")
def letsTalk():
    discord = Discord.query.filter_by().first()
    return render_template('lets talk/letsTalk.html',discord=discord)

# Chat
@app.route("/chat")
def chat():
    whatsapp = Whatsapp.query.filter_by().all()
    return render_template('chat/chat.html',whatsapp=whatsapp)

#Council's and Teams
@app.route("/councils")
def council():
    return render_template('council/councils.html')

# Syllabus
@app.route("/syllabus")
def syllabus():
    return render_template('syllabus/syllabus.html')

# Blogs
@app.route("/blogs")
def blogs():
    return redirect('https://medium.com/@crce')

#Notes
@app.route("/notes")
def notes():
    return render_template('notes/notes.html')

#Career
@app.route("/career")
def career():
    return render_template('career/carierOption.html')


@app.route("/career-CE")
def careerCE():
    return render_template('career/computerEngineering.html')
@app.route("/career-ME")
def careerME():
    return render_template('career/mechanicalEngineering.html')
@app.route("/career-ECS")
def careerECS():
    return render_template('career/electronicsEngineering.html')
@app.route("/career-AIDS")
def careerAIDS():
    return render_template('career/aids.html')
@app.route("/career-PE")
def careerPE():
    return render_template('career/productionEngineering.html')

# Contacts
@app.route("/contact",methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry = Contact(name=name,email=email,phone=phone,message=message,date= datetime.now())
        db.session.add(entry);
        db.session.commit();
        mail.send_message('New Message from Direct Secendo ' + name,sender=email,recipients = [params['gmail']],body="message : "+message + "\n" +"Email : "+email+"\n"+"Phone No : "+ phone)
    return render_template('contact us/contactUs.html')


#admin
@app.route("/admin",methods=['GET','POST'])
def login():

    discord = Discord.query.filter_by().first()
    whatsapp = Whatsapp.query.filter_by().all()
    form = Form.query.filter_by().first()

    if request.method == 'POST':
        global username
        username = request.form.get('username')
        userpass = request.form.get('password')
        login = Login.query.filter_by(email = username).first()
        if username == login.email and userpass == login.password:
            session['user'] = username
            params['admin_user'] = username
            return render_template('admin/AdminDashboard.html',discord=discord,whatsapp=whatsapp,form=form)
        else:
            return 'Invalid Credentials'
    
    elif  'user' in session and session['user'] == params['admin_user']:
        return render_template('admin/AdminDashboard.html',discord=discord,whatsapp=whatsapp,form=form)

    else:
        return render_template('admin/login.html')

# Edit    
@app.route("/edit/<string:feilds>",methods=['GET','POST'])
def editDiscord(feilds):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == "POST":
            if feilds == "discord":
                discord_url = request.form.get('discord-url')
                discord = Discord.query.filter_by(sno=1).first()
                discord.discord_url = discord_url
                db.session.commit()
                return redirect('/admin')

            elif feilds == "AIDSwhatsapp":
                whatsapp_url = request.form.get('AIDSwhatsaappURL')
                whatsapp = Whatsapp.query.filter_by(feilds='AIDS').first()
                whatsapp.whatsapp_url = whatsapp_url
                db.session.commit()

            elif feilds == "CEwhatsapp":
                whatsapp_url = request.form.get('CEwhatsaappURL')
                whatsapp = Whatsapp.query.filter_by(feilds='CE').first()
                whatsapp.whatsapp_url = whatsapp_url
                db.session.commit()

            elif feilds == "EXTCwhatsapp":
                whatsapp_url = request.form.get('EXTCwhatsaappURL')
                whatsapp = Whatsapp.query.filter_by(feilds='EXTC').first()
                whatsapp.whatsapp_url = whatsapp_url
                db.session.commit()

            elif feilds == "ITwhatsapp":
                whatsapp_url = request.form.get('ITwhatsaappURL')
                whatsapp = Whatsapp.query.filter_by(feilds='IT').first()
                whatsapp.whatsapp_url = whatsapp_url
                db.session.commit()

            elif feilds == "MECHwhatsapp":
                whatsapp_url = request.form.get('MECHwhatsaappURL')
                whatsapp = Whatsapp.query.filter_by(feilds='MECH').first()
                whatsapp.whatsapp_url = whatsapp_url
                db.session.commit()

            elif feilds == "PRODwhatsapp":
                whatsapp_url = request.form.get('PRODwhatsaappURL')
                whatsapp = Whatsapp.query.filter_by(feilds='PROD').first()
                whatsapp.whatsapp_url = whatsapp_url
                db.session.commit()
            
            elif feilds == "formlink":
                form_link = request.form.get('form-link')
                form = Form.query.filter_by(sno=1).first()
                form.form_link = form_link
                db.session.commit()

            elif feilds == "uploadNotes":
                department = request.form.get('select-feilds')
                document = request.files['fileUpload']
                sem = request.form.get('select-sem')
                subject = request.form.get('subject-name')
                chapter = request.form.get('chapter-no')
                topic = request.form.get('topic-name')
                name = request.form.get('contributer-name')
                
                entry = Contact(department=department,document=document,sem=sem,subject=subject,chapter=chapter,topic=topic,name=name)
                db.session.add(entry);
                db.session.commit();

        return redirect('/editLinks')

# Edit Links Page
@app.route("/editLinks")
def editLink():
    if ('user' in session and session['user'] == params['admin_user']):
        discord = Discord.query.filter_by().first()
        whatsapp = Whatsapp.query.filter_by().all()
        form = Form.query.filter_by().first()
        return render_template('admin/EditLink.html',discord=discord,whatsapp=whatsapp,form=form)
    else:
        return redirect('/Error')

# Send Link
@app.route("/sendlink",methods=['GET','POST'])
def sendLink():
    if ('user' in session and session['user'] == params['admin_user']):
        form = Form.query.filter_by().first()
        formURL = form.form_link
        gmail = request.form.get('send-mail')
        print(mail)
        try:
            message = "You Can Fill this Form and Upload Notes here , Once it is rechecked it will Uploaded to the Website"
            mail.send_message('New Message from Direct Secendo ',sender=params['gmail'],recipients =[gmail] ,body="message :"+message + "\n" +"Form Link :"+formURL)
            return redirect('/admin')
        except Exception:
            return redirect('/Error')
    else:
        return redirect('/')

# Upload Notes Page
@app.route("/uploadNotes")
def uploadNotes():
    if ('user' in session and session['user'] == params['admin_user']):
        form = Form.query.filter_by().first()
        return render_template('admin/uploadNotes.html',form=form)
    else:
        return redirect('/Error')

@app.route("/submitNotes", methods=['GET', 'POST'])
def SubmitNotes():
    if ('user' in session and session['user'] == params['admin_user']):
        try :
            if request.method == "POST":
                name = request.form.get('contributer_name')
                dept = request.form.get('dept')
                subject = request.form.get('subject')
                sem = request.form.get('sem')
                chapter = request.form.get('chapt')
                topic = request.form.get('topic')
                slug = request.form.get('slug')
                document = request.files['upload_file']
                entry = Notes(contributerName=name,department=dept,subject=subject,sem=sem,chapterNo=chapter,topicName=topic,slug=slug,filename=document.filename,filedata=document.read(),date=datetime.now())
                db.session.add(entry)
                db.session.commit()
            return redirect('/uploadNotes')
        except Exception:
            return redirect('/Error')
            

@app.route("/editNotes", methods=['GET', 'POST'])
def editNotes():
    if ('user' in session and session['user'] == params['admin_user']):
        notes = Notes.query.filter_by().all()
        return render_template('admin/EditNotes.html',notes=notes)
    else:
        return redirect('/Error')


@app.route("/deleteNotes/<string:slug>", methods=['GET', 'POST'])
def deleteNotes(slug):
    if ('user' in session and session['user'] == params['admin_user']):
        notes = Notes.query.filter_by(slug=slug).first()
        db.session.delete(notes)
        db.session.commit()
        return redirect('admin/EditNotes.html')

@app.route("/aidsNotes")
def aidsNotes():
    aidsnotes = Notes.query.filter_by(department="AIDS").all()
    return render_template('notes/aidsNotes.html',aidsnotes=aidsnotes)

@app.route("/download/<string:slug>")
def downloadNotes(slug):
    notes = Notes.query.filter_by(slug=slug).first()
    print("File Name :",notes.filename)
    return send_file(BytesIO(notes.filedata), as_attachment=True)

# Logout
@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/admin')

# Error
@app.route("/Error")
def error():
    return render_template('Error.html')

app.run(debug=True)