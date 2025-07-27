import argparse
from datetime import datetime
from app.processors.report_processor import ReportProcessor
from app.generators.report_generator import ReportGenerators


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%d-%m').date()
    except ValueError:
        raise argparse.ArgumentTypeError("Date must be in format YYYY-DD-MM")


def main():
    parser = argparse.ArgumentParser(description='Process log files and generate reports.')
    parser.add_argument('--file', required=True, nargs='+', help='Path to log file(s)')
    parser.add_argument('--report', required=True, choices=['average'], help='Type of report to generate')
    parser.add_argument('--date', type=parse_date, help='Filter logs by date (format: YYYY-DD-MM)')

    args = parser.parse_args()

    results = []
    for file_path in args.file:
        results.append(ReportProcessor.process_log_file(file_path, args.date))

    merged_data = ReportProcessor.merge_results(results)

    if args.report == 'average':
        report_data = ReportProcessor.generate_average_report(merged_data)
        print(ReportGenerators.average(report_data))


if __name__ == '__main__':
    main()
