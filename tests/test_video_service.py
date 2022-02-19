import pytest

from videoplayer.video_service import VideoService
from videoplayer.playlist import Playlist
from videoplayer.video import Video


def test_should_play_first_video_in_playlist(playlist, mock_player):
    video_service = VideoService(player=mock_player, playlist=playlist)
    video_service.play_video()

    mock_player.play.assert_called_with('abc', 0)


def test_should_play_specified_video_in_playlist(playlist, mock_player):
    video_service = VideoService(player=mock_player, playlist=playlist)
    video_service.play_video(video_url='def')

    mock_player.play.assert_called_with('def', 0)


def test_should_play_video_from_specified_timing(playlist, mock_player):
    video_service = VideoService(player=mock_player, playlist=playlist)
    video_service.play_video(start_from=3000)

    mock_player.play.assert_called_with('abc', 3000)


def test_should_continue_play_video_from_where_it_stop(playlist, mock_player):
    video_service = VideoService(player=mock_player, playlist=playlist)
    expected_video = 'abc'
    expected_start_from = 3000
    mock_player.get_current_time.return_value = expected_start_from
    mock_player.get_current_video.return_value = expected_video
    video_service.play_video()
    video_service.stop_video()

    video_service.play_video()

    mock_player.play.assert_called_with(expected_video, expected_start_from)


def test_should_play_next_video_if_current_video_is_finished(playlist, mock_player):
    video_service = VideoService(player=mock_player, playlist=playlist)
    mock_player.get_current_time.return_value = 60000
    mock_player.get_current_video.return_value = 'abc'
    video_service.play_video()
    video_service.stop_video()

    video_service.play_video()

    mock_player.play.assert_called_with('def', 0)


def test_should_play_first_video_if_last_video_is_finished(playlist, mock_player):
    video_service = VideoService(player=mock_player, playlist=playlist)
    mock_player.get_current_time.return_value = 50000
    mock_player.get_current_video.return_value = 'aabb'
    video_service.play_video('aabb')
    video_service.stop_video()

    video_service.play_video()

    mock_player.play.assert_called_with('abc', 0)


@pytest.fixture
def playlist():
    return Playlist([Video('abc', 60000), Video('def', 30000), Video('aabb', 50000)])


@pytest.fixture
def mock_player(mocker):
    mock_client_class = mocker.Mock()
    return mock_client_class.return_value
