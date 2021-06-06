from rest_framework import serializers
from .models import Idea, Author


class IdeaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Idea
        fields = ['title', 'release_date', 'description', 'author', 'approved', 'upvotes']

    # allows author to be displayed by name rather than id
    def to_representation(self, instance):
        return {
            "title": instance.title,
            "release_date": instance.release_date,
            "description": instance.description,
            "author": instance.author.name,
            "approved": instance.approved,
            "upvotes": instance.upvotes
        }


class AuthorSerializer(serializers.ModelSerializer):
    # displays list of ideas per author
    idea_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Idea.objects.all(), default=[])

    class Meta:
        model = Author
        fields = ['name', 'email', 'idea_set']
    
    # allows ideas to be listed by title instead of id
    def to_representation(self, instance):
        return {
            "name": instance.name,
            "email": instance.email,
            "idea_set": [_.title for _ in instance.idea_set.all()]
        }

