from flask import Flask, render_template
from controllers.lesson_controller import lessons_blueprint

app = Flask(__name__)

app.register_blueprint(lessons_blueprint)

@app.route('/')
def home():
    return render_template('index.html', title='Home')

if __name__ == '__main__':
    app.run(debug=True)