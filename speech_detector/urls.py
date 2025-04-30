
## Speech Detector Urls


from django.urls import path
from speech_detector.views  import SpeechDetectorView


urlpatterns = [
    path('v1/speech-detect/', SpeechDetectorView.as_view())
]