import os
import subprocess
from typing import List
from test_report import TestReport

class TestRunner:
    def __init__(self, directory: str):
        self.directory = directory

    def run_tests(self) -> str:
        file_paths = self.scan_directory()
        report = ""
        for file_path in file_paths:
            syntax_check_passed = self.run_syntax_check(file_path)
            pylint_results = self.run_pylint(file_path)
            test_results = self.run_test_cases(file_path)
            report += self.generate_report(file_path, syntax_check_passed, pylint_results, test_results)
        return report

    def scan_directory(self) -> List[str]:
        file_paths = []
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                if file.endswith(".py"):
                    file_paths.append(os.path.join(root, file))
        return file_paths

    def run_syntax_check(self, file_path: str) -> bool:
        try:
            subprocess.check_output(["python", "-m", "py_compile", file_path], stderr=subprocess.STDOUT)
            return True
        except subprocess.CalledProcessError as e:
            return False

    def run_pylint(self, file_path: str) -> List[str]:
        pylint_output = subprocess.check_output(["pylint", file_path], stderr=subprocess.STDOUT)
        pylint_results = pylint_output.decode().splitlines()
        return pylint_results

    def run_test_cases(self, file_path: str) -> List[str]:
        # Run the test cases for the Python file and return the results
        pass

    def generate_report(self, file_path: str, syntax_check_passed: bool, pylint_results: List[str], test_results: List[str]) -> str:
        report = TestReport(file_path)
        if not syntax_check_passed:
            report.add_syntax_error("Syntax error")
        for result in pylint_results:
            if "error" in result:
                report.add_linting_warning(result)
        for result in test_results:
            report.add_test_failure(result)
        return report.get_report()