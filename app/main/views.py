from flask import render_template,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from ..models import Review,User,Pitch
from .forms import UpdateProfile,ReviewForm,PitchForm
from ..import db,photos


@main.route('/')
def index():
    '''
    View root page function that returns the index page 
    '''

    #Getting popular movi
    title = 'Home - Pitch'
    allPitches = Pitch.query.all()
    zee =  Review.query.all()

    return render_template( 'index.html', title = title, pitches = allPitches, zee = zee )

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitcher = Pitch.query.filter_by(user_id = user.id).order_by(Pitch.posted.desc())

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, Pitch = Pitch)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form,user=user)

@main.route('/user/<uname>/update/pic',methods= ['GET','POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/user/<uname>/pitch',methods= ['GET','POST'])
@login_required
def new_pitch(uname):
    '''
    Function to check Pitches form
    '''
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = PitchForm()
    pitch = Pitch()

    if form.validate_on_submit():
        pitch.category = form.category.data
        pitch.title = form.title.data
        pitch.pitch_statement = form.pitch.data
        pitch.user_id = current_user.id

        db.session.add(pitch)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('new_pitch.html',uname=uname, user = user, PitchForm = form)

@main.route('/category/<int:id>')
def pitcher(category):
    '''
    category route function returns a list of pitches in the category chosen
    '''
    pitcher = Pitch.query.filter_by(category = category).order_by(Pitch.posted.desc())

    return render_template("pitcher.html", pitches = pitches, category = category)

@main.route('/reviews/<pitch_id>')
@login_required
def reviews(pitch_id):
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    reviews = Review.query.filter_by(pitch_id = pitch.id).order_by(Review.posted.desc())

    return render_template('reviews.html', pitch = pitch, reviews = reviews)

@main.route('/pitch/review/new/<pitch_id>', methods = ['GET', 'POST'])
@login_required
def new_review(pitch_id):
    form = ReviewForm()
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    review = Review()

    if form.validate_on_submit():
        review.pitch_review_title = form.title.data
        review.pitch_review = form.review.data
        review.pitch_id = pitch_id
        review.user_id = current_user.id

        db.session.add(review)
        db.session.commit()

        return redirect(url_for('main.reviews', pitch_id=pitch.id ))

    return render_template('new_review.html', review_form = form)
