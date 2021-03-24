from app import workout 
from form import Details
import flask 

# app = flask.Flask(__name__, template_folder='/users/gursi/desktop/other/FRC/flask_app')
app = flask.Flask(__name__, template_folder='C:/Users/prash/VSCodeProjects/FRC/FRC-8235-2021-innov-chal/flask_app')
app.config['SECRET_KEY'] = '7584938n457987f3n984'

msgs = []

@app.route('/home', methods=['GET','POST'])
def home():
    form = Details()
    time_map = {
        'M':'MORNING',
        'A':'AFTERNOON',
        'E':'EVENING'
    }
    part_map = {
        'U':'UPPER BODY',
        'C':'CORE',
        'L':'LOWER BODY'
    }

    if form.validate_on_submit():
        workout_buddies = workout(
            name=form.name.data,
            bodypart=form.bodypart.data,
            loc = form.location.data,
            budget=form.budget.data,
            times=form.time.data
        )
        msgs.append('Possible workout homies : ')
        for buddy in workout_buddies :
            name, loc, part, budget, time = buddy
            location = 'OUTDOORS' if loc else 'INDOORS'
            msg = f'{name} also likes to workout their {part_map[part]} {location} in the {time_map[time]}.'
            msgs.append(msg)
        
        return flask.redirect(flask.url_for('output'))

    return flask.render_template('flask_form.html', title='Home', form=form, times=time_map.keys(), parts = part_map.keys())

@app.route('/output')
def output():
    return flask.render_template('output.html', title='Output', msgs=msgs)