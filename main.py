from videoplayer.video_service import VideoService

from videoplayer.video_player import VideoPlayer
from videoplayer.playlist import Playlist
from videoplayer.video import Video

url = "https://www.youtube.com/watch?v=vG2PNdI8axo"
duration = 95000

video_service = VideoService(
    player=VideoPlayer(), playlist=Playlist([Video(url, duration)]))
video_service.play_video()

try:
    while True:
        print(video_service.get_player_state())
except KeyboardInterrupt:
    print('Stopping the video...')
    video_url, timing = video_service.stop_video()
    print(f"{video_url} - {timing}")
