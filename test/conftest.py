import pytest

import faker

@pytest.fixture(name='faker')
def _faker():
    return faker.Faker()


