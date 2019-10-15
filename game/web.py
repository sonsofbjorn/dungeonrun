from flask import Flask, render_template
from dungeon import Map
from forms import SubmitForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'blabla'

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = SubmitForm()
    if form.mapsize.data:
        dungeon = Map(form.mapsize.data)
    else:
        dungeon = Map(4)
    return render_template('home.html', dungeon=dungeon, form=form)

if __name__ == '__main__':
    app.run(debug=True)
