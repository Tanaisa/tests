import pytest 
from rest_framework.test import APIClient 

@pytest.mark.django_db
def test_todos_petshops():
    cliente = APIClient()
    resposta = cliente.get('/api/petshop')
    assert len(resposta.data['results']) == 0
    
    @pytest.fixture
    def dados_agendamento_instancia():
        petshop = baker.make(petshop)
        
        hoje = date.today()
        agendamento = {
            
        }
        