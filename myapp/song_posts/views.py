from turtle import title
from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import FavSongs
from myapp.song_posts.forms import FavSongsForm

song_posts = Blueprint('song_posts', __name__)

@song_posts.route('/create', method=['GET', 'POST'])
@login_required
def create_post():
  form = FavSongsForm()
  if form.validate_on_submit():
    song_post = FavSongs(title=form.title.data, text=form.text.data, user_id=current_user.id)
    db.session.add(song_post)
    db.session.commit()
    flash('Song Post Created')
    print('Song Post was Created')
    return redirect(url_for('core.index'))
  return render_template('create_post.html', form=form)