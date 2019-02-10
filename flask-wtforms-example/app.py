#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, redirect
from wtforms import Form
from wtforms.fields import core
from wtforms.fields import html5
from wtforms.fields import simple
from wtforms import validators
from wtforms import widgets

app = Flask(__name__, template_folder='templates')
app.debug = True

"""
Form继承了FormMeta(type),执行FormMeta的__init__然后
LoginForm._unbound_fields = None
LoginForm._wtforms_meta = None
"""
class LoginForm(Form):
    name = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired(message='用户名不能为空.'),
            validators.Length(min=6, max=18, message='用户名长度必须大于%(min)d且小于%(max)d')
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}

    )
    pwd = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.'),
            validators.Length(min=8, message='用户名长度必须大于%(min)d'),
            validators.Regexp(regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}",
                              message='密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符')

        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )
"""
StringField和PasswordField都继承了Field,在实例化时调用了Field中的__new__方法执行了return UnboundField(cls, *args, **kwargs)
当LoginForm解释完后
LoginForm._unbound_fields = None
LoginForm._wtforms_meta = None
LoginForm.name = UnboundField(creation_counter=1,simple.StringField)
LoginForm.pwd = UnboundField(creation_counter=2,simple.PasswordField)
"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html', form=form)
    else:
        form = LoginForm(formdata=request.form)
        if form.validate():
            print('用户提交数据通过格式验证，提交的值为：', form.data)
        else:
            print(form.errors)
        return render_template('login.html', form=form)


class RegisterForm(Form):
    name = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired()
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'},
        default='alex'
    )

    pwd = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    pwd_confirm = simple.PasswordField(
        label='重复密码',
        validators=[
            validators.DataRequired(message='重复密码不能为空.'),
            validators.EqualTo('pwd', message="两次密码输入不一致")
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    email = html5.EmailField(
        label='邮箱',
        validators=[
            validators.DataRequired(message='邮箱不能为空.'),
            validators.Email(message='邮箱格式错误')
        ],
        widget=widgets.TextInput(input_type='email'),
        render_kw={'class': 'form-control'}
    )

    gender = core.RadioField(
        label='性别',
        choices=(
            (1, '男'),
            (2, '女'),
        ),
        coerce=int,
        default=2
    )
    city = core.SelectField(
        label='城市',
        choices=(
            ('bj', '北京'),
            ('sh', '上海'),
        )
    )

    hobby = core.SelectMultipleField(
        label='爱好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        coerce=int
    )

    favor = core.SelectMultipleField(
        label='喜好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput(),
        coerce=int,
        default=[1, 2]
    )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.favor.choices = ((1, '篮球'), (2, '足球'), (3, '羽毛球'))

    def validate_pwd_confirm(self, field):
        """
        自定义pwd_confirm字段规则，例：与pwd字段是否一致
        :param field: 
        :return: 
        """
        # 最开始初始化时，self.data中已经有所有的值

        if field.data != self.data['pwd']:
            # raise validators.ValidationError("密码不一致") # 继续后续验证
            raise validators.StopValidation("密码不一致")  # 不再继续后续验证


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        form = RegisterForm(data={'gender': 1})  # 传参数或者在相应字段中设置默认值
        # form = RegisterForm()
        return render_template('register.html', form=form)
    else:
        form = RegisterForm(formdata=request.form)
        if form.validate():
            print('用户提交数据通过格式验证，提交的值为：', form.data)
        else:
            print(form.errors)
        return render_template('register.html', form=form)


USER_LIST = []


@app.route('/users', methods=['GET'])
def users():
    return render_template('users.html', user_list=USER_LIST)


class UserForm(Form):
    name = core.StringField(label='用户名', validators=[validators.DataRequired()])
    email = core.StringField(label='邮箱', validators=[validators.DataRequired()])


@app.route('/add_user', methods=['GET', "POST"])
def add_user():
    if request.method == 'GET':
        form = UserForm()
        return render_template('add_user.html', form=form)
    else:
        form = UserForm(formdata=request.form)
        if form.validate():
            print(form.data)
            USER_LIST.append(form.data)
            return redirect('/users')
        return render_template('add_user.html', form=form)


@app.route('/edit_user/<int:nid>', methods=['GET', "POST"])
def edit_user(nid):
    if request.method == 'GET':
        obj = USER_LIST[nid]
        form = UserForm(data=obj)
        return render_template('add_user.html', form=form)
    else:
        form = UserForm(formdata=request.form)
        if form.validate():
            print(form.data)
            USER_LIST.append(form.data)
            return redirect('/users')
        return render_template('add_user.html', form=form)


if __name__ == '__main__':
    app.run()
