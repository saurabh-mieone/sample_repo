from .models import *
from django.core import serializers
from django.http import JsonResponse, HttpResponse
import json


class songserializer:
    # data_object = Student.objects.all()
    # serialized_data = serializers.serialize("json", data_object)
    json_data = {
        # "data": json.loads(serialized_data)
    }
    response = HttpResponse("jadugar hai tu??")
    json_response = JsonResponse(json_data)
