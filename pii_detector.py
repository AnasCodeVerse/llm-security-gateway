from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from custom_recognizers import get_custom_recognizers


class PIIDetector:

    def __init__(self):

        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()

        custom_recognizers = get_custom_recognizers()

        for recognizer in custom_recognizers:
            self.analyzer.registry.add_recognizer(recognizer)

    def analyze(self, text):

        results = self.analyzer.analyze(
            text=text,
            language="en"
        )

        return results

    def anonymize(self, text, results):

        anonymized = self.anonymizer.anonymize(
            text=text,
            analyzer_results=results
        )

        return anonymized.text