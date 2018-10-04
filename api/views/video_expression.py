from api.views.abstract_api_view import AbstractAPIView
from django.utils.translation import gettext_lazy as _
from api.helpers import markdown_parser
from api.forms.video_expression import VideoExpressionForm
from api.helpers.handle_upload_flle import handle_uploaded_file, remove_upload_file
from video_expression.predict_emoji import predict
import json

class VideoExpression(AbstractAPIView):
    """
        Auto-Tagging API form for handle request
    """
    success = _('Get expression succesfully.')
    failure = _('Get expression failed.')

    def post(self, request):
        form = VideoExpressionForm(request.POST, request.FILES)
        if not form.is_valid():
            return self.json_format(code=442, data=[], message=self.failure, errors = form.errors)
        video_path = handle_uploaded_file(form.cleaned_data.get('video'))
        results, nb_frames = predict(video_path)
        remove_upload_file(video_path)
        return self.json_format(code=200, data={"keyframes" : results, "nb_frames" : nb_frames}, message=self.success, errors=[])


