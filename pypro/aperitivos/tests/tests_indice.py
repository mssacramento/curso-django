import pytest
from django.urls import reverse
from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titulo',
    [
        'Vídeo Aperitivo : Motivação',
        'Passo I : Criando Sala Virtual',
        'Passo II : Adicionando Professor',
        'Passo III : Criando Fórum',
        'Passo IV : Criando Tópicos',
        'Passo V : Tarefas e Testes',
        'Bônus : App Classroom',
    ]
)
def test_titulo_video(resp, titulo):
    assert_contains(resp, titulo)


@pytest.mark.parametrize(
    'slug',
    [
        'motivacao',
        'criando-sala-virtual',
        'adicionando-professor',
        'criando-forum',
        'criando-topicos',
        'tarefas-testes',
        'app-classroom',
    ]
)
def test_link_video(resp, slug):
    video_link = reverse('aperitivos:video', args=(slug,))
    assert_contains(resp, f'href="{video_link}"')
