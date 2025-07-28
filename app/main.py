from datetime import datetime

import argparse

from app.interfaces import ReportGeneratorInterface, ReportExporterInterface
from app.readers.file_log_reader import FileLogReader
from app.generators import AverageReportGenerator, UserAgentReportGenerator
from app.exporters import ConsoleAverageExporter, ConsoleUserAgentExporter, FileAverageExporter, FileUserAgentExporter


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%d-%m').date()
    except ValueError:
        raise argparse.ArgumentTypeError("Date must be in format YYYY-DD-MM")


def setup_arg_parser():
    parser = argparse.ArgumentParser(description='Process log files and generate reports.')
    parser.add_argument(
        '--file',
        required=True,
        nargs='+',
        help='Path to log file(s)'
    )
    parser.add_argument(
        '--report',
        required=True,
        choices=['average', 'user_agent'],
        help='Type of report to generate'
    )
    parser.add_argument(
        '--date',
        type=parse_date,
        help='Filter logs by date (format: YYYY-DD-MM)'
    )
    parser.add_argument(
        '--output',
        choices=['console', 'file'],
        default='console',
        help='Output destination for the report'
    )
    parser.add_argument(
        '--output-file',
        help='Path to output file (if --output=file)'
    )
    return parser


def get_report_generator(report_type: str) -> ReportGeneratorInterface:
    generators = {
        'average': AverageReportGenerator(),
        'user_agent': UserAgentReportGenerator()
    }
    return generators[report_type]


def get_exporter(output_type: str, report_type: str, output_file: str = None) -> ReportExporterInterface:
    exporters = {
        'console': {
            'average': ConsoleAverageExporter(),
            'user_agent': ConsoleUserAgentExporter()
        },
        'file': {
            'average': FileAverageExporter(file_path=output_file),
            'user_agent': FileUserAgentExporter(file_path=output_file)
        }
    }

    return exporters[output_type][report_type]



def main():
    parser = setup_arg_parser()
    args = parser.parse_args()

    # Components initialization
    log_reader = FileLogReader(file_paths=args.file, date_filter=args.date)
    report_generator = get_report_generator(report_type=args.report)
    exporter = get_exporter(
        output_type=args.output,
        report_type=args.report,
        output_file=args.output_file
    )

    # Logs reading
    logs = log_reader.read_logs()

    # Report generation
    report = report_generator.generate(logs)

    # Export report
    exporter.export(report=report)


if __name__ == '__main__':
    main()
