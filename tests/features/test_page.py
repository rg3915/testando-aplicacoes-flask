from pytest import mark as m


@m.it('deve retorna status code 200')
def test_home_status_code(client, data_regression):
    response = client.get('/')
    data_regression.check({'status_code': response.status_code})


@m.it('deve conter ola mundo!')
def test_home_ola_mundo(client, data_regression):
    response = client.get('/')
    data_regression.check(response.get_data(as_text=True))
