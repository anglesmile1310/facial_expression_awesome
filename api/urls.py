from django.urls import path
from api.views.video_expression import VideoExpression

app_name = 'api'

urlpatterns = [
    path('video_expression', VideoExpression.as_view(), name = 'video-expression'),
]
