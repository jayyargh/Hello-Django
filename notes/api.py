from rest_framework import serializers, viewsets
from .models import PersonalNote


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    """ Describe the model and fields we want to use. """

    def create(self, validated_data):
        # import pdb
        # pdb.set_trace()
        note = PersonalNote.objects.create(foo=12, **validated_data)
        return note

    class Meta:
        model = PersonalNote
        fields = ('title', 'content', 'url')


class PersonalNoteViewSet(viewsets.ModelViewSet):
    """ Describe the rows we want from the DB."""

    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()
