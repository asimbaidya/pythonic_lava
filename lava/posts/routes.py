from unicodedata import category
from flask import (render_template,
    url_for,
    flash,
    redirect,
    Blueprint,
    request
    )
from flask_login import current_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from lava import db
from lava.models import Post,Comment
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

@posts.route('/create_comment/<int:post_id>', methods=['POST'])
@login_required
def create_comment(post_id):
    post = Post.query.filter_by(id=post_id)
    if not post:
        flash("Post does not exist!",category='danger')
        return redirect(url_for('main.index'))
    else:
        print("Post exist-")
        content = request.form.get('text')
        if content is None:
            flash("Please enter something!",category='danger')
            return redirect(url_for('posts.post',post_id=post_id))
        else:
            comment = Comment(content=content,
                author=current_user,post_id=post_id)
            db.session.add(comment)
            db.session.commit()
    return redirect(url_for('posts.post',post_id=post_id))


@posts.route('/post_up/<int:post_id>', methods=['POST','GET'])
@login_required
def up_vote(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if not post:
        flash("Post does not exist!",category='danger')
        return redirect(url_for('main.index'))
    else:
        post.up = post.up + 1
        db.session.commit()
    return redirect(url_for('posts.post',post_id=post_id))


@posts.route('/post_down/<int:post_id>', methods=['POST','GET'])
@login_required
def down_vote(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if not post:
        flash("Post does not exist!",category='danger')
        return redirect(url_for('main.index'))
    else:
        post.down = post.down + 1
        db.session.commit()
    return redirect(url_for('posts.post',post_id=post_id))