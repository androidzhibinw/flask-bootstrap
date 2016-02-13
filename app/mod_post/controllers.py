from flask import Blueprint,render_template


mod_post = Blueprint('post', __name__, url_prefix='/post')


@mod_post.route('/all')
def posts():
    return  render_template('post/all.html')
