class PolicyEngine:

    def decide(self, injection_result, pii_results):

        if injection_result["attack_detected"]:
            return "BLOCK"

        if len(pii_results) > 0:
            return "MASK"

        return "ALLOW"