from collections import defaultdict
from datetime import datetime
import json


class ReportProcessor:
    @staticmethod
    def process_log_file(file_path, date_filter=None):
        handlers = defaultdict(lambda: {'count': 0, 'total_time': 0.0})

        with open(file_path, 'r') as file:
            for line in file:
                try:
                    log_entry = json.loads(line.strip())
                    if date_filter:
                        log_date = datetime.fromisoformat(log_entry['@timestamp']).date()
                        if log_date != date_filter:
                            continue

                    url = log_entry['url']
                    response_time = log_entry['response_time']

                    handlers[url]['count'] += 1
                    handlers[url]['total_time'] += response_time
                except (json.JSONDecodeError, KeyError) as e:
                    print(f"Error processing line: {line.strip()}. Error: {e}")

        return handlers

    @staticmethod
    def merge_results(results):
        merged = defaultdict(lambda: {'count': 0, 'total_time': 0.0})
        for result in results:
            for url, data in result.items():
                merged[url]['count'] += data['count']
                merged[url]['total_time'] += data['total_time']
        return merged

    @staticmethod
    def generate_average_report(endpoints_data):
        report = []
        for url, data in endpoints_data.items():
            avg_time = data['total_time'] / data['count'] if data['count'] > 0 else 0
            report.append({
                'handler': url,
                'total': data['count'],
                'avg_response_time': f"{avg_time:.3f} sec"
            })
        return report
