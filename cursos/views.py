from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response



"""
     API V1
"""   

# LISTAR E CRIAR
class CursosAPIView(generics.ListCreateAPIView):

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

#ATUALIZA E DESTROI
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# LISTAR E CRIAR
class AvaliacoesAPIView(generics.ListCreateAPIView):

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()

#ATUALIZA E DESTROI
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(
                self.get_queryset(),
                curso_id=self.kwargs.get('curso_id'),
                pk=self.kwargs.get('avaliacao_pk')
            )
        return get_object_or_404(
            self.get_queryset(),
            pk=self.kwargs.get('avaliacao_pk')
        )
            
        return self.queryset.all()
    

"""
     API V2
"""   

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        self.pagination_class = 1
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
       
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
    

class AvaliacoesViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    

