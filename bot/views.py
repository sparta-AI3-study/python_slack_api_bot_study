from rest_framework.views import APIView
from rest_framework.response import Response

class SendSlackAPI(APIView):
    def post(self, request):
        print(request.body)
        
        challenge = request.data.get('challenge')
        return Response(status=200, data=dict(challenge=challenge))
        