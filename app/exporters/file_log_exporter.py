from .base_report_exporter import BaseReportExporter


class FileAverageExporter(BaseReportExporter):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def export(self, report: dict) -> None:
        with open(self.file_path, 'w') as f:
            for url, data in report.items():
                avg_time = data['total_time'] / data['count'] if data['count'] > 0 else 0
                f.write(f"{url}\t{data['count']}\t{avg_time:.3f} sec\n")


class FileUserAgentExporter(BaseReportExporter):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def export(self, report: list) -> None:
        with open(self.file_path, 'w') as f:
            for item in report:
                f.write(f"{item['User Agent']}\t{item['Requests']}\t{item['Percentage']}\n")
