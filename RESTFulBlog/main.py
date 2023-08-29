from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


#Make FlaskWTF Form
class MakeForm(FlaskForm):
    title = StringField('Blog Post Title',validators=[DataRequired()])
    subtitle = StringField('Subtitle',validators=[DataRequired()])
    author = StringField('Name',validators=[DataRequired()])
    img_url = URLField('Blog Image URL', validators=[DataRequired()])
    body = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField()

# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(250), nullable=False)
    
    
    


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.query(BlogPost).filter_by(id=post_id).one()
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=['GET', 'POST'])
def add_new_post():
    form = MakeForm()
    if form.validate_on_submit():
        newpost = BlogPost(id=db.session.query(BlogPost.id).count()+1,
                    title=form.title.data,
                    subtitle=form.subtitle.data,
                    date = datetime.now().strftime("%B %-d, %Y"),
                    body=form.body.data,
                    author=form.author.data,
                    img_url=form.img_url.data)
        db.session.add(newpost)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form = form)

# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<int:id>', methods=['POST', 'GET'])
def edit_post(id):
    post = db.session.query(BlogPost).filter_by(id=id).one()
    form = MakeForm(title=post.title,
                    subtitle=post.subtitle,
                    author=post.author,
                    img_url=post.img_url,
                    body=post.body)
    
    if form.validate_on_submit():
        newpost=BlogPost(id=id,
                    title=form.title.data,
                    subtitle=form.subtitle.data,
                    date = post.date,
                    body=form.body.data,
                    author=form.author.data,
                    img_url=form.img_url.data)
        db.session.delete(post)
        db.session.commit()
        db.session.add(newpost)
        db.session.commit()
        return redirect(url_for('show_post', post_id = id))
    return render_template('make-post.html',is_edit=True, id=id, form=form)
# TODO: delete_post() to remove a blog post from the database

@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post = db.session.query(BlogPost).filter_by(id=post_id).one()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
