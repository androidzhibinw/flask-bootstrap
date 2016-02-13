from flask import Blueprint


mod_post = Blueprint('post', __name__, url_prefix='/post')


@mod_post.route('/all')
def posts():
    return 'posts'
