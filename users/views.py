from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
import csv
import io
from .serilizers import UserSerializer
from .models import User
from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.


@api_view(['POST'])
def upload_csv(request):
    try:
        csv_file = request.FILES.get('file')

        if not csv_file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not csv_file.name.endswith(".csv"):
            return Response({"error": "Only CSV Files accepted"}, status=status.HTTP_400_BAD_REQUEST)
        
        data = csv_file.read().decode('UTF-8')
        to_string = io.StringIO(data)
        data_dict = csv.DictReader(to_string)

        count = 0
        errors = []
        for i , val in enumerate(data_dict, start=1):
            serializer = UserSerializer(data=val)
            if serializer.is_valid():
                email = serializer.validated_data['email']
                if not User.objects.filter(email=email).exists():
                    serializer.save()
                    count += 1
                else:
                    errors.append({"row": i, "error": f"Duplicate Email {email}"})
            else:
                errors.append({"row": i, "error": serializer.errors})

        return JsonResponse({"saved_records": count, "rejected_records": len(errors), "errors": errors})

    except Exception as e:
        return Response({"error": f"Something went wrong: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)