import os
import secrets
from PIL import Image
from flask import current_app


def save_picture(form_picture):
    """ save picture in picture_path """
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = f"{random_hex}{f_ext}"
    picture_path = os.path.join(
        current_app.root_path, 'static/profile_pics', picture_fn)

    # resizing using Pillow
    # output_size = (125, 125)
    img = Image.open(form_picture)
    # img.thumbnail(output_size, Image.ANTIALIAS)

    img.save(picture_path)
    return picture_fn