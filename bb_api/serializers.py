from rest_framework import serializers
from bb_ap.models import Bb, Comment


class BbListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bb
        fields = ('id', 'title', 'content', 'price', 'created_at')


class BbCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bb
        fields = '__all__'


class BbUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bb
        fields = '__all__'


class BbDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bb
        fields = '__all__'


class BbDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bb
        fields = ('id', 'title', 'content', 'price', 'created_at', 'contacts', 'image')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('bb', 'author', 'content', 'created_at')

