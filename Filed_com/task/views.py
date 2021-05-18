from django.http import HttpResponse, JsonResponse
import json
from datetime import datetime
from .models import *
from django.core import serializers


def verify(request, audioFileType):
    return router(request, audioFileType, audio_ID=None)


def router(request, audioFileType, audio_ID=None):
    if request.method == "DELETE":
        return delete(audioFileType, audio_ID)
    elif request.method == "GET":
        return get(audioFileType, audio_ID)
    elif request.method == "PUT":
        return put(request, audioFileType, audio_ID)
    else:
        return HttpResponse("Not Found", status=404)


# Create your views here.
def create(request):
    recv_json = json.loads(request.body)
    filetype = recv_json["audioFileType"]
    metadata = recv_json["audioFileMetadata"]

    # if filetype is song
    if filetype == "song":
        data_object = song(id=metadata["id"], name=metadata["name"], duration=metadata["duration"],
                           )
        data_object.save()

    # if file type is podcast
    elif filetype == "podcast":
        participants = "#".join(metadata["participants"])
        data_object = podcast(id=metadata["id"], name=metadata["name"], duration=metadata["duration"],
                               host=metadata["host"], participants=participants)
        data_object.save()

    # if filetype is audiobook
    elif filetype == "audiobook":
        data_object = audiobook(id=metadata["id"], title=metadata["title"], duration=metadata["duration"],
                                 narrator=metadata["narrator"],
                                author=metadata["author"])
        data_object.save()
    # in case of any wrong filetype
    else:
        return HttpResponse("BAD REQUEST :Invalid filetype system", status=400)
    return HttpResponse("Done")


def delete(audioFileType, audio_id):
    if audioFileType == "song":
        song.objects.filter(id=audio_id).delete()

    elif audioFileType == "podcast":
        podcast.objects.filter(id=audio_id).delete()

    elif audioFileType == "audiobook":
        audiobook.objects.filter(id=audio_id).delete()

    else:
        return HttpResponse("BAD REQEST : Invalid Format provided", status=400)

    return HttpResponse("Deleted")


def get(audioFileType=None, audio_id=None):
    if audioFileType == "song":
        if audio_id == None:
            data_object = serializers.serialize("json", song.objects.all())
        else:
            data_object = serializers.serialize("json", song.objects.filter(id=audio_id))

    elif audioFileType == "podcast":
        if audio_id == None:
            data_object = serializers.serialize("json", podcast.objects.all())
        else:
            data_object = serializers.serialize("json", podcast.objects.filter(id=audio_id))

    elif audioFileType == "audiobook":
        if audio_id == None:
            data_object = serializers.serialize("json", audiobook.objects.all())
        else:
            data_object = serializers.serialize("json", audiobook.objects.filter(id=audio_id))
    else:
        return HttpResponse("BAD REQUEST : Invalid audio format", status=400)

    return JsonResponse(data_object, safe=False)


def put(request, audioFileType, audio_id):
    recv_json = json.loads(request.body)
    metadata = recv_json["audioFileMetadata"]

    if audioFileType == "song":
        data_object = song.objects.filter(id=audio_id)

    elif audioFileType == "podcast":
        data_object = podcast.objects.filter(id=audio_id)

    elif audioFileType == "audiobook":
        data_object = audiobook.objects.filter(id=audio_id)

    else:
        return HttpResponse("BAD REQUEST :Invalid filetype system", status=400)

    data_object.update_or_create(defaults=metadata)

    return HttpResponse("Done")