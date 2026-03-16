import time

from injection_detector import InjectionDetector
from pii_detector import PIIDetector
from policy_engine import PolicyEngine


detector = InjectionDetector()
pii_detector = PIIDetector()
policy_engine = PolicyEngine()


def security_gateway(user_input):

    start_time = time.time()

    # Step 1: Injection Detection
    injection_result = detector.detect(user_input)

    # Step 2: PII Detection
    pii_results = pii_detector.analyze(user_input)

    # Step 3: Policy Decision
    decision = policy_engine.decide(injection_result, pii_results)

    # Step 4: Apply Policy
    if decision == "BLOCK":

        output = "Request blocked due to prompt injection attempt."

    elif decision == "MASK":

        output = pii_detector.anonymize(user_input, pii_results)

    else:

        output = user_input

    latency = time.time() - start_time

    return decision, output, latency


if __name__ == "__main__":

    while True:

        user_input = input("\nEnter prompt: ")

        decision, output, latency = security_gateway(user_input)

        print("\nDecision:", decision)
        print("Output:", output)
        print("Latency:", latency)