import os, json
from googleapiclient.discovery import build
from dotenv import load_dotenv

class Channel:
    """Класс для ютуб-канала"""

    load_dotenv()

    api_key = os.getenv('YT_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        channel = Channel.youtube.channels().list(id=self.__channel_id, part='snippet, statistics').execute()
        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = f"https://www.youtube.com/{channel['items'][0]['snippet']['customUrl']}"
        self.subscriber_count = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.view_count = channel['items'][0]['statistics']['viewCount']
    @staticmethod
    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = Channel.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        Channel.printj(channel)

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        return cls.youtube

    def to_json(self, filename):
        with open(filename, 'w') as file:
            data = {'ID': self.channel_id,
                    'Title': self.title,
                    'Descripstion': self.description,
                    'Channel url': self.url,
                    'Subscriber count': self.subscriber_count,
                    'Video count': self.video_count,
                    'View count': self.view_count}
            json.dump(data, file, ensure_ascii=False)