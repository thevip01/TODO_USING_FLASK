from flask import Flask, redirect, url_for, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
db = SQLAlchemy(app)
app.secret_key = 'NONE'


class ToDo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f'{self.sno} - {self.title}'

# with app.app_context():
#     db.create_all()


@app.route('/', methods=["GET", "POST"])  # Create Routes
def startView():
    if request.method == "POST":
        title = request.form['title']
        description = request.form['description']

        todo = ToDo(title=title, description=description)

        db.session.add(todo)
        db.session.commit()

        flash("Task Added Successfully", 'info')

    ToDoList = ToDo.query.all()
    return render_template('Home.html', ToDoList=ToDoList)


@app.route('/update/<int:sno>', methods=["GET", "POST"])
def update(sno):
    if request.method == "POST":
        title = request.form['title']
        description = request.form['description']

        todo = ToDo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.description = description

        db.session.add(todo)
        db.session.commit()
        
        flash("Task Updated Successfully", 'info')

        return redirect(url_for('startView'))
    else:
        item = ToDo.query.get(sno)
        return render_template('Home.html', Data=item)


@app.route('/delete/<int:sno>', methods=["GET"])
def delete(sno):
    item = ToDo.query.get(sno)
    db.session.delete(item)
    db.session.commit()

    flash("Task Deleted Successfully", 'info')

    return redirect(url_for('startView'))


if __name__ == '__main__':
    app.run(debug=True, port=7041)
