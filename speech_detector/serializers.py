

from rest_framework import serializers


class SpeechDetectSerializer(serializers.Serializer):

    # Define a required URL field for user input
    web_url = serializers.URLField(required=True)

    
    def validate_website(self, value):

        """
        Custom validator for the 'web_url' field.
        Note: This method should be named 'validate_web_url' to match the field name,
        otherwise it will not be automatically triggered by DRF.
        """
        
        if not value:
            raise serializers.ValidationError("This field is required and must be a valid URL.")
        # If the value is not a valid URL, Django REST Framework will raise the error automatically
        return value

