#Get all songs without audio_ID
curl "http://127.0.0.1:8000/song"

printf "\n"

#Get all songs with audio_ID
curl "http://127.0.0.1:8000/song/1"

printf "\n"

## Delete podcast by id
curl -X "DELETE" "http://127.0.0.1:8000/podcast/1"

printf "\n"

## Add song
curl -X "POST" "http://127.0.0.1:8000/" \
     -H 'Content-Type: application/json' \
     -d $'{
    "audioFileType": "audiobook",
    "audioFileMetadata": {
        "id": 2,
        "title": "Stephen Story",
        "duration": 340,
        "narrator": "Saurabh",
        "author": "Stephen Hawking"
    }
}'

printf "\n"

## Update audiobook
curl -X "PUT" "http://127.0.0.1:8000/audiobook/2" \
     -H 'Content-Type: application/json' \
     -d $'{
    "audioFileType": "audiobook",
    "audioFileMetadata": {
        "id": 2,
        "title": "Stephen Story",
        "duration": 340,
        "narrator": "Saurabh",
        "author": "Stephen Hawking"
    }
}'

printf "\n"

## Invalid audio format
curl -X "DELETE" "http://127.0.0.1:8000/podcast/1"