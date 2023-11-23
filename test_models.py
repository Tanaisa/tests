from reserva.models import ReservaDeBanho
from model_bakery import baker
from datetime import date
import pytest

def test_conf():
    assert 1 == 1

@pytest.mark.django_db
def test_str_reserva_retornar_string_formatada():
    data = date(2023, 11, 6)
    reserva = baker.make(
    ReservaDeBanho,
    nomeDoPet = 'Lulu',
    diaDaReserva = data, 
    turno = 'tarde'

)
assert str(reserva) == 'Nome do Pet:Lulu - Dia: 2023,11,6 - Turno:tarde'