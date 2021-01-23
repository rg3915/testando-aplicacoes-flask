from pytest import mark as m
from app.models import Curso
from app import db
from unittest.mock import patch, Mock


@m.it('deve retorna status code 200')
def test_home_status_code(client):
    response = client.get('/')
    assert response.status_code == 200


@m.it('deve conter ola mundo!')
def test_home_ola_mundo(client, data_regression):
    response = client.get('/')
    assert 'Olá, mundo!' in response.get_data(as_text=True)


@m.it('deve conter o título do curso!')
def test_home_titulo_do_curso(client):
    curso = Curso(name='Criando Websites Com Python e Django') #model
    db.session.add(curso)
    db.session.commit() # ele vai salvar este dado dentro do sqlite3

    response = client.get('/')
    assert 'Criando Websites Com Python e Django' in response.get_data(as_text=True)