import pytest
from validador_email import validar_email

@pytest.mark.parametrize("email, resultado_esperado", [
    ("teste@exemplo.com", "E-mail válido"),
    ("usuario@dominio", "E-mail inválido"),           # sem ponto no domínio
    ("usuario@@dominio.com", "E-mail inválido"),      # dois @
    ("usuario dominio@com", "E-mail inválido"),       # espaço
    ("@dominio.com", "E-mail inválido"),              # começa com @
    ("usuario@", "E-mail inválido"),                  # termina com @
    (" usuario@dominio.com ", "E-mail válido"),       # espaços nas pontas
])
def test_validar_email(email, resultado_esperado):
    assert validar_email(email) == resultado_esperado
