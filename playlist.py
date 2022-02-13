class Playlist:
    def __init__(self, playlist):
        self.playlist = playlist
        self.current_playlist = -1

    def next(self):
        self.current_playlist = self.current_playlist + \
            1 if self.current_playlist + 1 <= len(self.playlist) else 0
        return self.playlist[self.current_playlist]
