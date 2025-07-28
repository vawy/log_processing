import json
from datetime import datetime
from typing import Any

from app.interfaces import LogReaderInterface


class FileLogReader(LogReaderInterface):
    def __init__(self, file_paths: list[str], date_filter=None):
        self.file_paths = file_paths
        self.date_filter = date_filter

    def read_logs(self) -> list[dict[str, Any]]:
        logs = []
        for file_path in self.file_paths:
            with open(file_path, 'r') as file:
                for line in file:
                    try:
                        log_entry = json.loads(line.strip())
                        if self.date_filter:
                            log_date = datetime.fromisoformat(log_entry['@timestamp']).date()
                            if log_date != self.date_filter:
                                continue
                        logs.append(log_entry)
                    except (json.JSONDecodeError, KeyError) as e:
                        print(f"Error processing line: {line.strip()}. Error: {e}")
        return logs