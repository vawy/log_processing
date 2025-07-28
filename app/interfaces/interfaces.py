from abc import ABC, abstractmethod
from typing import Any


class LogReaderInterface(ABC):
    @abstractmethod
    def read_logs(self) -> list[dict[str, Any]]:
        pass


class ReportGeneratorInterface(ABC):
    @abstractmethod
    def generate(self, data: Any) -> Any:
        pass


class ReportExporterInterface(ABC):
    @abstractmethod
    def export(self, report: Any) -> None:
        pass
