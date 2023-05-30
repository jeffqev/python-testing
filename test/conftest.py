import pytest
import faker

from .factory import _employee_factory

@pytest.fixture(name='faker')
def _faker():
    return faker.Faker()


