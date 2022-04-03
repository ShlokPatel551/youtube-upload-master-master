# youtube upload api
from youtube_upload.client import YoutubeUploader

uploader = YoutubeUploader()
uploader = YoutubeUploader('youtube_upload/client_secret_699175412021-96qlf64he0fimns5bsu7odkmtc5fhtm8.apps.googleusercontent.com.json')
uploader.authenticate()
# Video options
options = {
    "title": "Example title",  # The video title
    "description": "Example description",  # The video description
    "tags": ["tag1", "tag2", "tag3"],
    "categoryId": "22",
    "privacyStatus": "private",  # Video privacy. Can either be "public", "private", or "unlisted"
    "kids": False,  # Specifies if the Video if for kids or not. Defaults to False.
    "thumbnailLink": "https://cdn.havecamerawilltravel.com/photographer/files/2020/01/youtube-logo-new-1068x510.jpg"
    # Optional. Specifies video thumbnail.
}
uploader.upload(file_path='client secret/test.mp4')
uploader.close()
