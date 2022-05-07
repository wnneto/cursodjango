import pytest
from django.urls import reverse
from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('loto:games'))


def test_status_code(resp):
    assert resp.status_code == 200

