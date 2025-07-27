from tabulate import tabulate

class ReportGenerators:
    @staticmethod
    def average(data):
        headers = ['handler', 'total', 'avg_response_time']
        table_data = [[item['handler'], item['total'], item['avg_response_time']] for item in data]
        return tabulate(table_data, headers=headers, tablefmt='grid')
