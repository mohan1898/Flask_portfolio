from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///testb'

db=SQLAlchemy(app)
class ContactUser(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100),primary_key=True)
    email=db.Column(db.String(100), primary_key=True)
    message=db.Column(db.String(100), primary_key=True)
@app.route('/')
def home():
    email='mohanyelamarthi5@gmail.com'
    return render_template('home/home.html', email=email)
@app.route('/about')
def about():
    return render_template('home/about.html')
@app.route('/contact',methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        id = request.form['id']
        name=request.form['name']
        email=request.form['email']
        message=request.form['message']
        new_contact=ContactUser(id=id,name=name,email=email,message=message)
        db.session.add(new_contact)
        db.session.commit()
        return redirect(url_for('thanks',name=name))
    return render_template('home/contact.html')
@app.route('/thanks/<name>')
def thanks(name):
    return render_template('home/thanks.html',name=name)    
@app.route('/github')
def github():
    github='https://github.com/mohan1898'
    lawyer='https://test-auwa.onrender.com/'
    insta='https://www.instagram.com/mohan.yelamarthi/'
    facebook='https://www.facebook.com/sai.mohan.507464'
    linkedin='https://www.linkedin.com/in/mohan-sai18/'
    return render_template('home/github.html',github=github,insta=insta,facebook=facebook,linkedin=linkedin,lawyer=lawyer)

if __name__ == '__main__':
    app.run(debug=True)