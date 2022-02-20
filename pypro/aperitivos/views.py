from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, titulo, youtube_id):
        self.slug = slug
        self.titulo = titulo
        self.youtube_id = youtube_id


def get_absolute_url(self):
    return reverse('aperitivos:video', args=(self.slug,))


videos = [
    Video('motivacao', 'Vídeo Aperitivo : Motivação', '3WRbMPA1p1Q'),
    Video('criando-sala-virtual', 'Passo I : Criando Sala Virtual', 'Lh3oqLMiFus'),
    Video('adicionando-professor', 'Passo II : Adicionando Professor', 'YLBy5GuyDpk'),
    Video('criando-forum', 'Passo III : Criando Fórum', 'qMeq0HSnQV4'),
    Video('criando-topicos', 'Passo IV : Criando Tópicos', 'aFF26rw22Us'),
    Video('tarefas-testes', 'Passo V : Tarefas e Testes', 'S6RoA19lcCw'),
    Video('app-classroom', 'Bônus : App Classroom', '3nS73hwupnE'),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
