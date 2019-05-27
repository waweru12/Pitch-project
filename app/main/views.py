from flask import render_template,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from ..models import Comment,User,Pitch
from .forms import UpdateProfile,CommentForm
from ..import db,photos


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = "pitch"
    return render_template('index.hmtl',title=title)