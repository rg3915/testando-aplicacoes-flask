from flask import Blueprint, render_template

page = Blueprint('page', __name__)


@page.route('/')
def home():
    from app.models import Curso

    cursos = Curso.query.all()

    return render_template('index.html', cursos=cursos)
