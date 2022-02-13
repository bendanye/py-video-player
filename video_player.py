import pafy

# pip install youtube-dl==2020.12.2

import vlc


class VideoPlayer:

    def __init__(self):
        self.media_player = None

    def has_video_loaded(self):
        return self.media_player is not None

    def is_current_video_duration_enough(self, play_interval_secs):
        return self.get_current_time() + (play_interval_secs * 1000) <= self.media_player.get_length()

    def load(self, video_url):
        video = pafy.new(video_url)
        best = video.getbest()
        self.media_player = vlc.MediaPlayer(best.url)

    def play(self, start_from):
        self.media_player.play()
        self.media_player.set_time(start_from)

    def stop(self):
        self.media_player.stop()

    def get_current_time(self):
        return self.media_player.get_time()

    def get_state(self):
        return self.media_player.get_state()
