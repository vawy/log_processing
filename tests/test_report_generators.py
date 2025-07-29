import pytest

from app.generators import AverageReportGenerator, UserAgentReportGenerator


def test_average_report_generator(raw_logs):
    """Тестируем генератор отчета по среднему времени ответа"""
    generator = AverageReportGenerator()
    report = generator.generate(raw_logs)

    assert len(report) == 2

    assert report['/api/homeworks/...']['count'] == 2
    assert report['/api/homeworks/...']['total_time'] == pytest.approx(0.28)

    assert report['/api/context/...']['count'] == 4
    assert report['/api/context/...']['total_time'] == pytest.approx(0.064)


def test_user_agent_report_generator(raw_logs):
    """Тестируем генератор отчета по User-Agent"""
    generator = UserAgentReportGenerator()
    report = generator.generate(raw_logs)

    sorted_report = sorted(report, key=lambda x: x['User Agent'])

    assert len(sorted_report) == 2
    assert sorted_report[0]['User Agent'] == "Mozilla/5.0"
    assert sorted_report[0]['Requests'] == 3
    assert sorted_report[0]['Percentage'] == "50.0%"

    assert sorted_report[1]['User Agent'] == "curl/7.68.0"
    assert sorted_report[1]['Requests'] == 3
    assert sorted_report[1]['Percentage'] == "50.0%"
