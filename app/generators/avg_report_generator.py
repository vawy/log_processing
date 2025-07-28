from collections import defaultdict
from typing import Any

from .base_report_generator import BaseReportGenerator


class AverageReportGenerator(BaseReportGenerator):
    def generate(self, logs: list[dict[str, Any]]) -> dict[str, dict[str, float]]:
        handlers = defaultdict(lambda: {'count': 0, 'total_time': 0.0})

        for log in logs:
            url = log['url']
            response_time = log['response_time']
            handlers[url]['count'] += 1
            handlers[url]['total_time'] += response_time

        return handlers
