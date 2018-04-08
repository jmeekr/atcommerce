from rest_framework import views
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

"""
This file is not being used but should be extended out from
a frontend other than a Django Template for file uploads.

This snippet was taken from DRF documentation
"""

class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, filename, format='.py'):
        file_obj = request.data['file']
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204)
