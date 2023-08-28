from flask import Flask, request, render_template, redirect, flash,  jsonify, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Question, Survey, satisfaction_survey, surveys

app = Flask(__name__)
app.config['SECRET_KEY'] = "super-Duper-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)
app.debug = True

@app.route('/')
def index():
    """Return homepage."""

    if session.get("responses") == None:
        session["responses"] = []

    return render_template("index.html", survey=satisfaction_survey)


@app.route('/survey/questions/<int:number>')
def quiz(number):
    """Return the survey page."""

    if session.get("responses") == None:
        return redirect("/")
    
    if len(session["responses"]) >= len(satisfaction_survey.questions):
        flash('Survey already complete.', 'error')
        return redirect("/thankyou")
    elif number != len(session["responses"]):
        flash('Please take the survey in the intended order.', 'error')
        return redirect(f"/survey/questions/{len(session['responses'])}")
    else:
        return render_template("survey.html", number=number, survey=satisfaction_survey)


@app.route('/survey/send/<int:number>', methods=["POST"])
def add_quiz_answer(number):
    """Add answer to responses list and redirect to next question."""

    if session.get("responses") == None:
        return redirect("/")

    if len(session["responses"]) >= len(satisfaction_survey.questions):
        flash('Survey already complete.', 'error')
        return redirect("/thankyou")

    session["responses"] = session["responses"] + [request.form[f"question-{number}"]]
    print(session["responses"])

    if len(session["responses"]) >= len(satisfaction_survey.questions):
        return redirect("/thankyou")
    else:
        return redirect(f"/survey/questions/{len(session['responses'])}")

@app.route('/thankyou')
def thank_you():
    """Return end of survey page."""

    return render_template("thankyou.html", survey=satisfaction_survey)
