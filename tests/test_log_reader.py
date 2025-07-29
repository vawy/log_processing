from datetime import date

from app.readers.file_log_reader import FileLogReader


def test_read_logs(sample_logs):
    reader = FileLogReader([sample_logs])
    logs = reader.read_logs()

    assert len(logs) == 6
    assert logs[0]['url'] == '/api/homeworks/...'
    assert logs[1]['status'] == 200
    assert logs[2]['response_time'] == 0.056
    assert logs[3]['request_method'] == 'GET'
    assert logs[4]['@timestamp'] == '2025-06-22T13:59:37+00:00'
    assert logs[5]['http_user_agent'] == 'curl/7.68.0'


def test_read_logs_with_date_filter(sample_logs):
    reader = FileLogReader([sample_logs], date_filter=date(2025, 6, 22))
    logs = reader.read_logs()

    assert len(logs) == 5
    assert any(log['url'] == '/api/homeworks/...' for log in logs)
