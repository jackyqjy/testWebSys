import random
from flask import Blueprint, render_template, request, session, redirect, url_for
from utils import restful
from models.user import UserModel
from forms.user import loginForm


bp = Blueprint("user", __name__, url_prefix="/user")

@bp.route("/register")
def register():
    return render_template("front/register.html")

@bp.route("/mail/captcha")
def mail_captcha():
    try:
        email = request.arg.get("mail")
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        captcha = "".join(random.sample(digits, 4))
        subject = "注册验证码"
        body = f"您的注册验证为{captcha},请勿告诉他人"
        #current_app.celery.send_task("send_mail",(email, subject, body))
        #cache.set(email, captcha, timeout=100)
        return restful.ok()
    except Exception as e:
        print(e)
        return restful.server_error()
@bp.route("/login", methods=['GET','POST'])
def login():
    return redirect(url_for("front.index"))
    # if request.method == 'GET':
    #     return render_template('front/login.html')
    # else:
        # form = LoginForm(request.form)
        # if form.validate():
        #     email = form.email.data
        #     password = form.password.data
        #     remember = form.remember.data
        #     user = UserModel.query.filter_by(email=email).first()
        #     if user and user.checkpassword(password):
        #         session['user_id'] = user.id
        #         if remember:
        #             session.permanent = True
        #         return redirect("/")
        #     else:
        #         return redirect(url_for("user.login"))
        # else:
        #     return render_template("front/login.html")