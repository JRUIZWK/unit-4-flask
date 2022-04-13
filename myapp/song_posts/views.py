from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import FavSongs
from myapp.song_posts.forms import FavSongsForm

song_posts = Blueprint('song_posts', __name__)