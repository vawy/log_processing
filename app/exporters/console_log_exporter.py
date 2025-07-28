from tabulate import tabulate

from .base_report_exporter import BaseReportExporter


class ConsoleAverageExporter(BaseReportExporter):
    def export(self, report: dict) -> None:
        table_data = [
            [url, data['count'], f"{data['total_time']/data['count']:.3f} sec"]
            for url, data in report.items()
        ]
        print(tabulate(table_data, headers=['handler', 'total', 'avg_response_time']))


class ConsoleUserAgentExporter(BaseReportExporter):
    def export(self, report: list) -> None:
        print(tabulate(
            [[item['User Agent'], item['Requests'], item['Percentage']] for item in report],
            headers=['User Agent', 'Requests', 'Percentage'],
            maxcolwidths=[50, None, None]
        ))
