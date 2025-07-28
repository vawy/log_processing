from abc import ABC
from app.interfaces import ReportExporterInterface


class BaseReportExporter(ReportExporterInterface, ABC):
    pass
