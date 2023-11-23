from pytest_django.asserts import AssertTemplateUsed
from datetime import date, timedelta
import pytest
from reserva
def test_reserva_criar_view_restornado_template_corresto(client):
 response = client.get('/reserva/criar')
    
assert response.status_code == 200
AssertTemplateUsed(response, 'reserva_de_banho_html')

@pytest.fixture
def fixture_name(request):
    
def reserva_valida():

    def test_reserva_criando_corretamente(client):
        data = date.today() + timedelta(days=1)
        dados_reserva = {
        'nomeDoPet':'Lari',
        'telefone': '999999999',
        'email': 'lari@hotmail.com',
        'diaDaReserva':'amanha',
        'turno':'manha',
        'tamanho': 1,
        'observacoes':'sem obs..',
    
    }
    
    return dados_reserva

@pytest.mark.django.bd
def test_reserva_retornando_mensagem_de_sucesso(client, response_valida):
 client.post('/reserva/criar, dados_reserva', reserva_valida)

assert response.status_code == 200
assert 'Reserva feita com sucesso' in str(response.context)

@pytest.mark.django_db
def test_reserva_salvando_no_bd_corretamente(client, reserva_valida):
    response = client.post('/reserva/criar/', reserva_valida)

assert response.status_code == 200

first_reserva = ReservaDeBanho.objects.first()

@pytest.mark.django_db
def test_obter_agendamento_pelo_id(dados_agendamento_instancia):
    ReservaDeBanho.objects.create(**dados_agendamento_instancia)
    
    client = APIClient()
    resposta = client.get('/api/agendamento/:')
    json = resposta.json()
    assert json['nomeDoPet'] == 'Lari'
    