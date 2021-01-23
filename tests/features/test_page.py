from pytest import mark as m

@m.it('deve retorna status code 200')
def test_home_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

@m.it('deve conter ola mundo!')
def test_home_ola_mundo(client):
    response = client.get('/')
    assert 'Olá, mundo!' in response.get_data(as_text=True)

