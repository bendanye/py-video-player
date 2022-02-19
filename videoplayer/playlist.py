class Playlist:
    def __init__(self, playlist):
        self.playlist = playlist
        self.current_playing = -1

    def current(self):
        return self.playlist[self.current_playing]

    def next(self):
        self.current_playing = self.current_playing + \
            1 if self.current_playing + 1 <= len(self.playlist) else 0
        return self.playlist[self.current_playing]
