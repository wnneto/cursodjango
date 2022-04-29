import pytest
from django.test import Client
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = Client.get(reverse('base:home'))
    return resp

def test_status_code(resp):
    assert resp.status_code == 200

def test_title(resp):
    assert_contains(resp, '<title>Karol BanK</title>')

def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Karol BanK</a>')

