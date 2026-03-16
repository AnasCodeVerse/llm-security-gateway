# analyzer.py

import importlib
import sys

# Temporarily remove presidio_analyzer module to avoid local file shadowing
_local_module = sys.modules.pop('presidio_analyzer', None)

# Import the installed package versions
AnalyzerEngine = importlib.import_module('presidio_analyzer').AnalyzerEngine
AnonymizerEngine = importlib.import_module('presidio_anonymizer').AnonymizerEngine

# Restore if needed
if _local_module:
    sys.modules['presidio_analyzer'] = _local_module

class PresidioAnalyzer:

    def __init__(self):
        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()

    def analyze(self, text):

        results = self.analyzer.analyze(
            text=text,
            entities=None,
            language="en"
        )

        return results

    def anonymize(self, text, results):

        anonymized = self.anonymizer.anonymize(
            text=text,
            analyzer_results=results
        )

        return anonymized.text
