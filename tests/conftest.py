import pytest
import json


@pytest.fixture
def raw_logs():
    """Фикстура возвращает сырые логи без привязки к файлу"""
    return [
        {
            "@timestamp": "2025-06-21T13:59:04+00:00",
            "status": 200,
            "url": "/api/homeworks/...",
            "request_method": "GET",
            "response_time": 0.224,
            "http_user_agent": "Mozilla/5.0"
        },
        {
            "@timestamp": "2025-06-22T13:59:28+00:00",
            "status": 200,
            "url": "/api/context/...",
            "request_method": "GET",
            "response_time": 0.04,
            "http_user_agent": "Mozilla/5.0"
        },
        {
            "@timestamp": "2025-06-22T13:59:29+00:00",
            "status": 200,
            "url": "/api/homeworks/...",
            "request_method": "GET",
            "response_time": 0.056,
            "http_user_agent": "curl/7.68.0"
        },
        {
            "@timestamp": "2025-06-22T13:59:36+00:00",
            "status": 200,
            "url": "/api/context/...",
            "request_method": "GET",
            "response_time": 0.008,
            "http_user_agent": "Mozilla/5.0"
        },
        {
            "@timestamp": "2025-06-22T13:59:37+00:00",
            "status": 200,
            "url": "/api/context/...",
            "request_method": "GET",
            "response_time": 0.008,
            "http_user_agent": "curl/7.68.0"
        },
        {
            "@timestamp": "2025-06-22T13:59:37+00:00",
            "status": 200,
            "url": "/api/context/...",
            "request_method": "GET",
            "response_time": 0.008,
            "http_user_agent": "curl/7.68.0"
        }
    ]


@pytest.fixture
def sample_logs(tmp_path, raw_logs):
    """Фикстура создает временный файл с логами"""
    log_file = tmp_path / "test.log"
    with open(log_file, 'w') as f:
        for log in raw_logs:
            f.write(json.dumps(log) + '\n')
    return log_file
