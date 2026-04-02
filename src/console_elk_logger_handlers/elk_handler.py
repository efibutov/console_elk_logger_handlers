from datetime import datetime, timezone
from logging import Handler, LogRecord
import requests
from requests.auth import HTTPBasicAuth


class ELKHandler(Handler):
    def __init__(
        self,
        index='logs',
        host='docker-elk-elasticsearch-1',
        port=9200,
        password='changeme'
    ):
        super().__init__()
        self.url = f"http://{host}:{port}/{index}/_doc"
        self.auth = HTTPBasicAuth('elastic', password)

    def emit(self, record: LogRecord):
        try:
            doc = {
                'timestamp': datetime.now(timezone.utc).isoformat(),
                'message': record.getMessage(),
                'level': record.levelname,
                'logger': record.name,
                'lineno': record.lineno,
                'filename': record.filename,
                'module': record.module,
                'msg': record.msg,
                'name': record.name,
                'pathname': record.pathname,
            }
            requests.post(self.url, json=doc, auth=self.auth)
        except Exception as e:
            print(f"ELK error: {e}")
