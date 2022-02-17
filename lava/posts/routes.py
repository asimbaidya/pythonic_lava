from flask import (render_template,
    url_for,
    flash,
    redirect,
    Blueprint)
from flask_login import current_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from lava import db
from lava.models import Post
from lava.posts.forms import PostForm



posts = Blueprint('posts', __name__)

def save_picture(path):
    pass


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        picture_file = save_picture(form.picture.data)
        # current_user.image_file = picture_file
        # post = Post(title=form.title.data,
        #             content=form.content.data, author=current_user)
        # db.session.add(post)
        # db.session.commit()
        flash('Your post has been Created!', category='success')
        return redirect(url_for('index'))
    return render_template('create_post.html',
        title='New Post', form=form, legend='Update Post')


@posts.route('/post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)
