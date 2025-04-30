
from rest_framework import (
    generics,
    response,
    status
)
from speech_detector.serializers import SpeechDetectSerializer
from speech_detector.detect import SpeechDetector


class SpeechDetectorView(generics.GenericAPIView):
    
    # No authentication/permission required for this view
    permission_classes = ()
    
    # Use the custom serializer to validate input
    serializer_class = SpeechDetectSerializer

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to detect sentiment from a web URL's headline.
        Validates input using serializer, then uses SpeechDetector to process it.
        """

        # Deserialize and validate incoming JSON data
        serializer = SpeechDetectSerializer(data=request.data)

        if serializer.is_valid():
            # If data is valid, extract the cleaned/validated input
            validated_data = serializer.validated_data

            # Call SpeechDetector to perform translation and sentiment detection
            result = SpeechDetector.detect(validated_data['web_url'])

            # Return successful response with analysis result
            return response.Response({
                "Result": result
            }, status=status.HTTP_200_OK)
        
        # If validation fails, return error messages
        return response.Response({
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
