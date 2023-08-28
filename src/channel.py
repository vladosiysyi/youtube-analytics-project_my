import json
import os
import pprint

from googleapiclient.discovery import build
api_key: str = os.getenv('API_KEY')

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        youtube = self.get_service()
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        snippet = channel["items"][0]["snippet"]
        statistics = channel["items"][0]["statistics"]
        self.title = snippet["title"]
        # pprint.pprint(statistics)
        self.video_count = statistics["videoCount"]
        self.url = snippet["customUrl"]

    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self,file_name):
        date = {'title':self.title,'video_count':self.video_count,'url':self.url}
        with open(file_name, 'w') as file:
            json.dump(date,file)
    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        youtube = self.get_service()
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        printj = json.dumps(channel, indent=2, ensure_ascii=False)
        print(printj)
        pass
