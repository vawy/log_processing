from abc import ABC

from app.interfaces import ReportGeneratorInterface


class BaseReportGenerator(ReportGeneratorInterface, ABC):
    pass
