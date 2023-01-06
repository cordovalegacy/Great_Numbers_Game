import random
from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'this is a secret key for the great number game assignement'


@app.route('/')
def index():
    if 'random_num' not in session:
        session['random_num'] = random.randint(1, 100)
    if 'attempts' not in session:
        session['attempts'] = 0
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def take_guess():
    session['guess'] = request.form['num']
    session['attempts'] += 1
    if session['attempts'] > 5:
        session.clear()
        return redirect('/')
    if int(session['random_num']) > int(session['guess']):
        session['answer'] = "Guess Higher!"
        print('Too Low')
    elif int(session['random_num']) < int(session['guess']):
        print('Too High')
        session['answer'] = "Guess Lower!"
    else:
        print('You got it!')
        session['answer'] = "You Guessed Correctly!"
    return redirect('/')


@app.route('/destroy_session')
def reset_count():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
