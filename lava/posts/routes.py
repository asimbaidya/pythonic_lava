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
from lava.utils import save_picture



posts = Blueprint('posts', __name__)

@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        picture_file = 'default.jpg'
        post = Post(title=form.title.data,
            content=form.content.data,image=picture_file, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been Created!', category='success')
        return redirect(url_for('main.index'))
    return render_template('create_post.html',
        title='New Post', form=form, legend='Post | Post')


@posts.route('/post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)
