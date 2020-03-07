from rest_framework import viewsets, mixins, generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from .models import PennyChat, FollowUp
from .serializers import PennyChatSerializer, FollowUpSerializer
from users.models import UserProfile


class PennyChatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows penny chats to be viewed or edited.
    """
    queryset = PennyChat.objects.all().order_by('-date')
    serializer_class = PennyChatSerializer

    def perform_create(self, serializer):
        # TODO add participants and make request user's UserProfile as the Organizer
        serializer.save()


class ListCreateFollowUps(generics.GenericAPIView):
    """
    API endpoint that allows follow ups to be viewed or edited based on the foreign key of their associated chat.
    """
    queryset = FollowUp.objects.all().order_by('-date')
    serializer_class = FollowUpSerializer

    def get(self, request, pk, format=None):
        follow_ups = FollowUp.objects.filter(penny_chat_id=pk)
        queryset = self.filter_queryset(follow_ups)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        follow_up_data = dict(request.data)
        penny_chat_url = reverse('pennychat-detail', args=[pk], request=request)
        follow_up_data['penny_chat'] = penny_chat_url
        serializer = FollowUpSerializer(data=follow_up_data, context={'request': request})
        if serializer.is_valid():
            # TODO - if request.user is not anonymous then find the UserProfile corresponding to the request user
            # creating new follow ups will not work unless you uncomment these lines!
            # user, created = UserProfile.objects.get_or_create(
            #     real_name='Anonymous Profile',
            #     defaults={
            #         'email': 'anonymous@profile.com',
            #         'slack_team_id': '1'
            #     })
            # serializer.save(user=user)
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UpdateDeleteFollowUp(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    """
    API endpoint that allows follow ups to be updated or deleted.
    """
    queryset = FollowUp.objects.all()
    serializer_class = FollowUpSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
