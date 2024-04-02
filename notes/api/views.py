from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

@api_view(['GET'])
def getRoutes(request):
    """
    View that returns a list of all available routes in the API
    Args:
        request: The request object
    Returns:
        A JSON response with a list of all available routes
    """
    routes = [
        {
            'Endpoint': '/notes/',
            'Method': 'GET',
            'Body': None,
            'Description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'Method': 'GET',
            'Body': None,
            'Description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'Method': 'POST',
            'Body': {'body': 'string', 'title': 'string'},
            'Description': 'Creates a new note with data sent in POST request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'Method': 'PUT',
            'Body': {'body': 'string', 'title': 'string'},
            'Description': 'Updates an existing note with data sent in POST request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'Method': 'DELETE',
            'Body': None,
            'Description': 'Deletes an existing note'
        },
    ]

    return Response(routes)


@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)

    return Response(serializer.data)
 
@api_view(['POST'])
def createNote(request):
    data = request.data

    note = Note.objects.create(
        body = data['body']
    )

    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data

    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data = request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()

    return Response('Note deleted')