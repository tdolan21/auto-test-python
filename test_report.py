class TestReport:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.syntax_errors = []
        self.linting_warnings = []
        self.test_failures = []

    def add_syntax_error(self, error: str):
        self.syntax_errors.append(error)

    def add_linting_warning(self, warning: str):
        self.linting_warnings.append(warning)

    def add_test_failure(self, failure: str):
        self.test_failures.append(failure)

    def get_report(self) -> str:
        report = f"Testing report for file: {self.file_path}\n"
        if self.syntax_errors:
            report += "Syntax errors:\n"
            for error in self.syntax_errors:
                report += f"- {error}\n"
        if self.linting_warnings:
            report += "Linting warnings:\n"
            for warning in self.linting_warnings:
                report += f"- {warning}\n"
        if self.test_failures:
            report += "Test failures:\n"
            for failure in self.test_failures:
                report += f"- {failure}\n"
        return report