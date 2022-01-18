from hack import app,db,mongo
from flask import render_template,redirect,url_for,request,flash,abort
from flask_login import login_user,login_required,logout_user,current_user
from hack.models import User,Raw,Manufacture,Sell
from hack.forms import LoginForm, RawForm, ManufactureForm,SellForm
from sqlalchemy import desc , asc
from werkzeug.security import generate_password_hash,check_password_hash
import flask
from datetime import datetime
@app.route('/')
def home():
    # user = User(fname = "oompa_god",
    #              email = "oompa_god@oompa.com",
    #              roles = "god",
    #              password = "password")
    # db.session.add(user)
    # db.session.commit()
    return render_template('HomePage.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    mess = 'Please fill form to login'
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        try:
            if user.check_password(form.password.data) and user is not None:
                #Log in the user

                login_user(user)
                mess = 'Logged in successfully.'
                current_user = user
                next = request.args.get('next')
                if next == None or not next[0]=='/':
                    next = url_for('home')
                return redirect(next)
            else:
                mess = "Wrong Password"
        except AttributeError:
            mess = 'No such login.Pls Ask Manager to make account'
    print(mess)
    return render_template('Login.html', form=form,mess=mess)

@app.route('/raw', methods=['GET','POST'])
@login_required
def raw():
    if current_user.roles != "raw" and current_user.roles != "god":
        abort(403)
    form = RawForm()
    if form.validate_on_submit():
        raw = Raw(
            beans = form.beans.data,
            milk = form.milk.data,
            sugar = form.sugar.data,
            date = datetime.now()
        )
        db.session.add(raw)
        db.session.commit()
        now = datetime.now()
        return redirect(url_for('raw'))
    beans =[]
    milk = []
    sugar = []
    date= []
    user_collection = Raw.query.all()
    if user_collection:
        for i in user_collection:
            beans.append(i.beans)
            milk.append(i.milk)
            sugar.append(i.sugar)
            date.append(i.date)
    date.reverse()
    beans.reverse()
    milk.reverse()
    sugar.reverse()
    n = len(beans)
    user = User.query.filter_by(roles = 'raw').first()
    beans_gr = []
    milk_gr = []
    sugar_gr = []
    date_gr = []

    if user_collection:
        for i in user_collection:
            beans_gr.append(i.beans)
            milk_gr.append(i.milk)
            sugar_gr.append(i.sugar)
            date_gr.append(i.date.strftime('%Y-%m-%d %H:%M:%S.%f')[:-4])
    return render_template('raw.htm',form=form,n=n,date_gr = date_gr,beans = beans,milk=milk,sugar=sugar,beans_gr = beans_gr,milk_gr=milk_gr, sugar_gr=sugar_gr,date=date,user=user)

@app.route('/manufacture', methods=['GET','POST'])
@login_required
def manufacture():
    if current_user.roles != "manufacture" and current_user.roles != "god":
        abort(403)
    form = ManufactureForm()
    if form.validate_on_submit():
        manufacture = Manufacture(
            beans = form.beans.data,
            milk = form.milk.data,
            sugar = form.sugar.data,
            date = datetime.now(),
            defected = form.defected.data,
            perfect = form.perfect.data
        )
        db.session.add(manufacture)
        db.session.commit()
        now = datetime.now()
        return redirect(url_for('manufacture'))
    beans =[]
    milk = []
    sugar = []
    date= []
    defected = []
    perfect = []
    user_collection = Manufacture.query.all()
    if user_collection:
        for i in user_collection:
            beans.append(i.beans)
            milk.append(i.milk)
            sugar.append(i.sugar)
            date.append(i.date)
            defected.append(i.defected)
            perfect.append(i.perfect)
    date.reverse()
    beans.reverse()
    milk.reverse()
    sugar.reverse()
    defected.reverse()
    perfect.reverse()
    user = User.query.filter_by(roles = 'manufacture').first()
    n = len(milk)
    beans_gr = []
    milk_gr = []
    sugar_gr = []
    date_gr = []
    defected_gr = []
    perfect_gr = []
    if user_collection:
        for i in user_collection:
            beans_gr.append(i.beans)
            milk_gr.append(i.milk)
            sugar_gr.append(i.sugar)
            date_gr.append(i.date.strftime('%Y-%m-%d %H:%M:%S.%f')[:-4])
            defected_gr.append(i.defected)
            perfect_gr.append(i.perfect)

    return render_template('manufacture.htm',user=user,n=n, date_gr= date_gr,form=form,beans = beans,milk=milk,sugar=sugar,date=date, defected= defected,perfect=perfect,beans_gr = beans_gr,milk_gr=milk_gr,sugar_gr=sugar_gr, defected_gr= defected_gr,perfect_gr=perfect_gr)

@app.route('/sell', methods=['GET','POST'])
@login_required
def sell():
    if current_user.roles != "sell" and current_user.roles != "god":
        abort(403)
    form = SellForm()
    if form.validate_on_submit():
        sell = Sell(
            offline = form.offline.data,
            online = form.online.data,
            buisness = form.buisness.data,
            date = datetime.now()
        )
        db.session.add(sell)
        db.session.commit()
        now = datetime.now()
        return redirect(url_for('sell'))
    offline =[]
    online = []
    buisness = []
    date= []
    user_collection = Sell.query.all()
    if user_collection:
        for i in user_collection:
            offline.append(i.offline)
            online.append(i.online)
            buisness.append(i.buisness)
            date.append(i.date)
    offline.reverse()
    online.reverse()
    buisness.reverse()
    date.reverse()
    user = User.query.filter_by(roles = 'sell').first()
    n  = len(offline)
    offline_gr = []
    online_gr = []
    buisness_gr = []
    date_gr = []

    if user_collection:
        for i in user_collection:
            offline_gr.append(i.offline)
            online_gr.append(i.online)
            buisness_gr.append(i.buisness)
            date_gr.append(i.date.strftime('%Y-%m-%d %H:%M:%S.%f')[:-4])

    return render_template('sell.htm',user=user,form=form,offline = offline,online = online,buisness = buisness,date_gr= date_gr, n=n,date=date,offline_gr = offline_gr,online_gr = online_gr,buisness_gr = buisness_gr)

@app.route('/admin',methods = ['GET','POST'])
@login_required
def admin():
    n=2
    if current_user.roles != 'god':
        abort(403)
    offline = 0
    online = 0
    user = User.query.filter_by(roles='sell').first()
    buisness = 0
    sell = Sell.query.all()
    if sell:
        for i in sell:
            offline += i.offline
            online += i.online
            buisness += i.buisness
    milk = 0
    sugar = 0
    beans = 0
    raw = Raw.query.all()
    if raw:
        for i in raw:
            milk += i.milk
            sugar += i.sugar
            beans += i.beans
    defected = 0
    perfect = 0
    manu = Manufacture.query.all()
    sales   = (offline+online+buisness)*100
    raw_material_cost = milk*3+sugar*2+beans*5
    raw_material = milk+sugar+beans

    if manu:
        for i in manu:
            defected += i.defected
            perfect += i.perfect
    profit = (sales)-(((defected+perfect)*3)+raw_material_cost)
    return render_template('admin.htm',n=n, user = user, offline = offline,online = online,buisness = buisness,milk = milk,sugar=sugar,
                            beans =beans, raw_material_cost= raw_material_cost,raw_material= raw_material,sales=sales,defected = defected,perfect = perfect,profit=profit)
if __name__ == '__main__':
    app.run(debug=True)
