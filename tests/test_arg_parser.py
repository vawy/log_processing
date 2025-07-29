from app.main import setup_arg_parser


def test_arg_parser_defaults():
    parser = setup_arg_parser()
    args = parser.parse_args(args=['--file', 'file1.log', 'file2.log', '--report', 'average'])

    assert args.file == ['file1.log', 'file2.log']
    assert args.report == 'average'
    assert args.output == 'console'
    assert args.date is None


def test_arg_parser_with_date():
    parser = setup_arg_parser()
    args = parser.parse_args(args=['--file', 'file.log', '--report', 'user_agent', '--date', '2025-22-06'])

    assert args.date.year == 2025
    assert args.date.day == 22
    assert args.date.month == 6
