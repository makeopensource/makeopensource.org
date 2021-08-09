from rest_framework import serializers
from .models import Project, Contributor


class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['title', 'description', 'contributors', 'release_date', 'github']

    # allows author to be displayed by name rather than id
    def to_representation(self, instance):
        contributor_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Contributor.objects.all(), default=[])

        return {
            "title": instance.title,
            "release_date": instance.release_date,
            "description": instance.description,
            "contributors": [_.name for _ in instance.contributor_set.all()],
            "github": instance.github
        }


class ContributorSerializer(serializers.ModelSerializer):
    # displays list of ideas per author
    project_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all(), default=[])

    class Meta:
        model = Contributor
        fields = ['name', 'email', 'project_set']
    
    # allows ideas to be listed by title instead of id
    def to_representation(self, instance):
        return {
            "name": instance.name,
            "email": instance.email,
            "idea_set": [_.title for _ in instance.project_set.all()]
        }

