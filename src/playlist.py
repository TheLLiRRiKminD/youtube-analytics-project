import datetime
import isodate

from src.channel import Channel

playlist_id = 'PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw'
playlist_videos = Channel.youtube.playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails', maxResults=50, ).execute()
video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]


class PlayList:

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.title = 'Moscow Python Meetup №81'
        self.url = 'https://www.youtube.com/playlist?list=' + self.playlist_id

    @property
    def total_duration(self):
        add_time = datetime.timedelta(minutes=0)
        video_response = Channel.youtube.videos().list(part='contentDetails,statistics',
                                                       id=','.join(video_ids)
                                                       ).execute()
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            add_time += duration

        return add_time

    @staticmethod
    def show_best_video():

        like: int = 0
        for video_id in video_ids:
            video_response = Channel.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                           id=video_id
                                                           ).execute()
            like_count: int = int(video_response['items'][0]['statistics']['likeCount'])

            if like < like_count:
                url_video = 'https://youtu.be/' + video_id
                like = like_count

        return url_video
