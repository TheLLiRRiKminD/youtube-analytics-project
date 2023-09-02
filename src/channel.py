import os
from googleapiclient.discovery import build
import json
from dotenv import load_dotenv


class Channel:
    """Класс для ютуб-канала"""

    load_dotenv()

    api_key = os.getenv('YT_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    @staticmethod
    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = Channel.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        Channel.printj(channel)
