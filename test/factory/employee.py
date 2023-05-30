import pytest

from app import Employee

@pytest.fixture(name='employee_factory')
def _employee_factory(faker):
    def _factory(**kwargs):
        return Employee(
            id= kwargs.get('id', faker.pyint()),
            name= kwargs.get('name', faker.name()),
        )
    return _factory