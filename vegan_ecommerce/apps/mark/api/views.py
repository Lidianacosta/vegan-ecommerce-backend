from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response


from apps.mark.api.serializers import MarkSerializer
from apps.mark.service import MarkService
from apps.shared.custom_api_exception import CustomApiException


class MarkViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            marks = MarkService.list_all_instances()
            serializer = MarkSerializer(instance=marks, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except CustomApiException as e:
            return Response(data=e.detail, status=e.status_code)

    def retrieve(self, request, pk):
        try:
            mark = MarkService.retrieve_instance(instance_id=pk)
            serializer = MarkSerializer(instance=mark)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except CustomApiException as e:
            return Response(data=e.detail, status=e.status_code)
