class InjectionDetector:

    def __init__(self, threshold=0.7):

        self.threshold = threshold

        # suspicious phrases with scores
        self.rules = {
            "ignore previous instructions": 0.6,
            "reveal system prompt": 0.7,
            "jailbreak": 0.8,
            "bypass security": 0.7,
            "act as": 0.3,
            "show hidden instructions": 0.6
        }

    def detect(self, text):

        score = 0

        for phrase, value in self.rules.items():

            if phrase in text.lower():
                score += value

        attack_detected = score >= self.threshold

        return {
            "score": score,
            "attack_detected": attack_detected
        }