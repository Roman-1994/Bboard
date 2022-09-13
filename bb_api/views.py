from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.decorators import permission_classes
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.permissions import *
from django_filters.rest_framework import DjangoFilterBackend

from bb_ap.models import Bb, Comment
from bb_api.serializers import BbListSerializer, BbDetailSerializer, CommentSerializer, BbCreateSerializer, BbUpdateSerializer, BbDeleteSerializer
from .service import BbFilter, BbPagination

#pip instal -r requirements.txt

@api_view(['GET'])
def bbs(request):
    if request.method == 'GET':
        bbs = Bb.objects.filter(is_active=True)[:10]
        serializer = BbListSerializer(bbs, many=True)
        return Response(serializer.data)


class BbListView(ListAPIView):
    queryset = Bb.objects.all()
    serializer_class = BbListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BbFilter
    pagination_class = BbPagination
    permission_classes = [IsAuthenticated]


class BbCreateView(CreateAPIView):
    serializer_class = BbCreateSerializer


class BbUpdateView(UpdateAPIView):
    queryset = Bb.objects.all()
    serializer_class = BbUpdateSerializer


class BbDeleteView(DestroyAPIView):
    queryset = Bb.objects.all()
    serializer_class = BbDeleteSerializer


class BbDetailView(RetrieveAPIView):
    queryset = Bb.objects.filter(is_active=True)
    serializer_class = BbDetailSerializer


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def comments(request, pk):
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    else:
        comments = Comment.objects.filter(is_active=True, bb=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

