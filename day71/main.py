from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from forms import RegisterForm, CreatePostForm, LoginForm, CommentForm
import os
# Import your forms from the forms.py
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
ckeditor = CKEditor(app)
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI', 'SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy()
db.init_app(app)


# TODO: Create a User table for all your registered users. 
class User(db.Model, UserMixin):
    # __bind_key__ = "usertable"
    __tablename__="users"
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    email = db.Column(db.String(100), unique = True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(300))
    posts = db.relationship("BlogPost", back_populates = "author")
    comments = db.relationship("Comment", back_populates = "author")

# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)

    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    author = db.relationship("User", back_populates="posts")
    comments = db.relationship("Comment", back_populates="post")

    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    author = db.relationship("User", back_populates="comments")
    post_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id'), nullable = False)
    post = db.relationship("BlogPost", back_populates="comments")


with app.app_context():
    db.create_all()


login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).filter_by(id=user_id).first()

def admin_only(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and current_user.id == 1:
            return func(*args, *kwargs)
        else:
            return abort(403)

    return decorated_function;
        

@app.route('/register', methods = ["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if not db.session.execute(db.select(User).where(User.email == form.email.data)).scalar():
            password = form.password.data
            hashed_pass = generate_password_hash(password, 'pbkdf2', salt_length=8)
            user = User(id = db.session.query(User.id).count()+1,
                        email = form.email.data,
                        name = form.name.data,
                        password = hashed_pass)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('get_all_posts'))
        else:
            flash("Email already registered")
            return redirect(url_for('register'))
    return render_template("register.html", form = form)

@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('get_all_posts'))
            else:
                flash("Wrong password, try again")
                return redirect(url_for('login'))
    return render_template("login.html", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))

@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, validated = current_user.is_authenticated)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods = ["GET", "POST"])
def show_post(post_id):
    form = CommentForm()
    curPost = db.session.query(BlogPost).filter_by(id = post_id).first()
    if form.validate_on_submit(): 
        if current_user.is_authenticated:
            newComment = Comment(
                content = form.body.data,
                author = current_user,
                post = curPost
            )
            db.session.add(newComment)
            db.session.commit()
            # print(curPost.comments)
        else:
            flash("You must log in before posting")
            return redirect(url_for("register"))
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post, form=form, comments=curPost.comments,
                           validated = current_user.is_authenticated)


# TODO: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    # app.run(debug=True, port=5000)
    app.run(debug=False)