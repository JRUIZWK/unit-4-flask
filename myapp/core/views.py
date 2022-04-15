from flask import render_template, request, Blueprint
from myapp.models import FavSongs

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    song_posts = FavSongs.query.order_by(FavSongs.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', song_posts=song_posts)

@core.route('/info')
def info():
    return render_template('info.html')