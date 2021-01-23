import pytest
from app import create_app, db


@pytest.fixture
def app():
    return create_app()


@pytest.fixture(autouse=True)
def create_database(app):
    with app.app_context():
        db.create_all()       
        yield db
    db.session.remove()
    db.drop_all()