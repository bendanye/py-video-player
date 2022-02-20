import pafy
import vlc


class VideoPlayer:

    def __init__(self):
        self.media_player = None
        self.current_video = None

    def play(self, video_url, start_from):
        self._load(video_url)
        self._play(start_from)

    def _load(self, video_url):
        self.current_video = video_url
        video = pafy.new(video_url)
        best = video.getbest()
        self.media_player = vlc.MediaPlayer(best.url)

    def _play(self, start_from):
        self.media_player.play()
        self.media_player.set_time(start_from)

    def stop(self):
        self.media_player.stop()

    def get_current_video(self):
        return self.current_video

    def get_current_time(self):
        return self.media_player.get_time()

    def get_state(self):
        return self.media_player.get_state()
