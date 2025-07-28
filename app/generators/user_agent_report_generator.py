from collections import defaultdict
from typing import Any

from .base_report_generator import BaseReportGenerator


class UserAgentReportGenerator(BaseReportGenerator):
    def generate(self, logs: list[dict[str, Any]]) -> list[dict[str, Any]]:
        user_agents = defaultdict(int)

        for log in logs:
            user_agent = log.get('http_user_agent', 'Unknown')
            user_agents[user_agent] += 1

        total_requests = sum(user_agents.values())
        report = []

        for ua, count in sorted(user_agents.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total_requests) * 100
            report.append({
                'User Agent': ua,
                'Requests': count,
                'Percentage': f"{percentage:.1f}%"
            })

        return report
