from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


# LISTAR E CRIAR
class CursosAPIView(generics.ListCreateAPIView):

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

#ATUALIZA E DESTROI
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# LISTAR E CRIAR
class AvaliacaoAPIView(generics.ListCreateAPIView):

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

#ATUALIZA E DESTROI
class AvaliacoesAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer