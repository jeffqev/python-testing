# Mock

Supongamos que tenemos una función llamada "calculate_average" que depende de una función "get_values" para obtener los valores a promediar. Queremos probar la función "calculate_average" de manera aislada, sin depender de la implementación de "get_values". Podemos utilizar mock para simular la función "get_values" y controlar su comportamiento en la prueba. Aquí hay un ejemplo:

``` python

# Código a probar
def get_values():
    # Obtener los valores de alguna manera
    return [1, 2, 3, 4, 5]

def calculate_average():
    values = get_values()
    return sum(values) / len(values)

# Prueba con mock
import pytest
from unittest.mock import patch

def test_calculate_average():
    with patch('__main__.get_values') as mock_get_values:
        mock_get_values.return_value = [10, 20, 30, 40, 50]  # Mockear los valores de get_values
        assert calculate_average() == 30  # Verificar que se calcule el promedio correctamente


```

Supongamos que tenemos una clase llamada "EmailSender" que depende de una biblioteca externa "send_email" para enviar correos electrónicos. Queremos probar el método "send_email" de la clase "EmailSender" sin depender de la implementación real de la biblioteca externa. Podemos utilizar patch con pytest y pytest-mock para reemplazar la función "send_email" durante la prueba. Aquí hay un ejemplo:
``` python
# Código a probar
import send_email

class EmailSender:
    def send_email(self, recipient, message):
        send_email.send(recipient, message)

# Prueba con patch y pytest-mock
import pytest
from unittest.mock import patch

def test_email_sender(mock):
    with patch('send_email.send') as mock_send:
        email_sender = EmailSender()
        email_sender.send_email('test@example.com', 'Hello, world!')
        mock_send.assert_called_once_with('test@example.com', 'Hello, world!')

```