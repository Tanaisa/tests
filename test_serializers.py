import pytest 
import datetime
from model_bakery import baker 
from reserva.models import Petshop
from rest_api.serializers import AgendamentoModelSerializer

@pytest.fixture
def dados_agendamento_errado():
    ontem = datetime.date.today() - datetime.timedelta(days=1)
    Petshop = baker.make(Petshop)
    return {
        'nome': 'nome teste', 'email': 'email@gmail.com'
        'nome_pet': 'pet teste', 'data': ontem, 'turno': 'manhã',
        'tamanho':0, 'observacoes': '', 'petshop': petshop.pk,
    }
    @pytest.mark.django_db
    def test_data_agendamento_invalida(dados_agendamento_errado):
        serializer = AgendamentoModelSerializer(data=dados_agendamento_errado)
        assert not serializer_is_valid()