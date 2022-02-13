from playlist import Playlist


class VideoService:
    def __init__(self, player, playlist, play_interval_secs=30):
        self.playlist = playlist
        self.player = player
        self.play_interval_secs = play_interval_secs
        self.last_stop_time = 0

    def play_video(self):
        if not self.player.has_video_loaded() or not self.player.is_current_video_duration_enough(self.play_interval_secs):
            self._load_video_into_player(self.playlist.next())

        self.player.play(self.last_stop_time)

    def _load_video_into_player(self, url):
        self.player.load(url)
        self.last_stop_time = 0

    def get_player_state(self):
        return self.player.get_state()

    def stop_video(self):
        self.last_stop_time = self.player.get_current_time()
        self.player.stop()
