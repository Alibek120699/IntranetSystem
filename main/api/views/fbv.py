from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import Subject
from api.serializers import SubjectSerializer
from api.constants import OFFICE_REGISTER


@api_view(['GET', 'POST'])
def subject_view(request):
    if request.method == 'GET':
        orders = Subject.objects.all()
        serializer = SubjectSerializer(orders, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        if request.user.role != OFFICE_REGISTER:
            return Response({'error': 'you are not office register'})
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    return Response({'error': 'bad request'})


@api_view(['GET', 'PUT', 'DELETE'])
def subject_detail_view(request, pk):
    try:
        order = Subject.objects.get(id=pk)
    except Subject.DoesNotExist as e:
        return Response({'error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubjectSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        if request.user.role != OFFICE_REGISTER:
            return Response({'error': 'you are not office register'})
        serializer = SubjectSerializer(instance=order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    if request.method == 'DELETE':
        if request.user.role != OFFICE_REGISTER:
            return Response({'error': 'you are not office register'})
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'bad request'})