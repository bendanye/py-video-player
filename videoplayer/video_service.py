class VideoService:
    def __init__(self, player, playlist):
        self.playlist = playlist
        self.player = player

        self.last_played_video = None
        self.last_stop_time = 0

    def play_video(self, video_url=None, start_from=None):
        to_play_video = self._determine_video_to_play(video_url)
        to_start_from = self._determine_video_to_start_from(start_from)
        self.player.play(to_play_video, to_start_from)

    def _determine_video_to_play(self, video_url):
        if video_url:
            return video_url
        else:
            if self.last_played_video:
                current_video = self.playlist.current()
                if current_video.duration > self.last_stop_time:
                    return self.last_played_video

            self.last_played_video = None
            self.last_stop_time = 0
            return self.playlist.next().url

    def _determine_video_to_start_from(self, start_from):
        return start_from if start_from else self.last_stop_time

    def get_player_state(self):
        return self.player.get_state()

    def stop_video(self):
        self.last_stop_time = self.player.get_current_time()
        self.last_played_video = self.player.get_current_video()
        self.player.stop()
        return self.last_played_video, self.last_stop_time
