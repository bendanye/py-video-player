from video_service import VideoService

from video_player import VideoPlayer
from playlist import Playlist

# url of the video
url = "https://www.youtube.com/watch?v=vG2PNdI8axo"

video_service = VideoService(player=VideoPlayer(), playlist=Playlist([url]))
video_service.play_video()

try:
    while True:
        print(video_service.get_player_state())
except KeyboardInterrupt:
    print('Interrupted')
    video_service.stop_video()
