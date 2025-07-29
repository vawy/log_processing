from app.exporters import ConsoleAverageExporter, FileAverageExporter


def test_console_average_exporter(capsys):
    """Тестируем вывод средних значений в консоль"""
    report = {
        '/api/homeworks/...': {
            'count': 2,
            'total_time': 0.224 + 0.056
        },
        '/api/context/...': {
            'count': 4,
            'total_time': 0.04 + 0.008 + 0.008 + 0.008
        }
    }

    exporter = ConsoleAverageExporter()
    exporter.export(report)

    captured = capsys.readouterr()

    assert 'handler' in captured.out
    assert 'total' in captured.out
    assert 'avg_response_time' in captured.out

    assert '/api/homeworks/...' in captured.out
    assert '2' in captured.out
    assert '0.140 sec' in captured.out

    assert '/api/context/...' in captured.out
    assert '4' in captured.out
    assert '0.016 sec' in captured.out


def test_file_average_exporter(tmp_path):
    """Тестируем запись средних значений в файл"""
    report = {
        '/api/homeworks/...': {
            'count': 2,
            'total_time': 0.28
        },
        '/api/context/...': {
            'count': 4,
            'total_time': 0.064
        }
    }

    output_file = tmp_path / "report.txt"
    exporter = FileAverageExporter(str(output_file))
    exporter.export(report)

    content = output_file.read_text()

    lines = content.strip().split('\n')
    assert len(lines) == 2

    assert '/api/homeworks/...' in lines[0]
    assert '2' in lines[0]
    assert '0.140' in lines[0]

    assert '/api/context/...' in lines[1]
    assert '4' in lines[1]
    assert '0.016' in lines[1]
