from unittest.mock import patch, MagicMock

from app.main import main


def test_full_workflow_average_report(sample_logs, capsys):
    test_args = ["main.py", "--file", str(sample_logs), "--report", "average"]

    with patch('sys.argv', test_args):
        main()

    captured = capsys.readouterr()
    assert '/api/homeworks/...' in captured.out
    assert '2' in captured.out


@patch('builtins.open', new_callable=MagicMock)
def test_full_workflow_file_export(mock_open, sample_logs):
    test_args = [
        "main.py", "--file", str(sample_logs), "--report", "user_agent", "--output", "file", "--output-file", "report.txt"
    ]

    with patch('sys.argv', test_args):
        main()

    mock_open.assert_called_with("report.txt", 'w')
