# Presidio-Based LLM Security Mini Gateway

## Overview

This project implements a **security gateway for Large Language Model (LLM) systems**.
The gateway analyzes user input before it reaches the LLM in order to detect **prompt injection attacks and sensitive information leakage**.

The system uses **Microsoft Presidio** for detecting Personally Identifiable Information (PII) and applies security policies to decide whether to **allow, mask, or block** a request.

This project was developed as part of the **Information Security (CEN-451) course assignment**.

---

## System Architecture

User Input → Injection Detection → Presidio Analyzer → Policy Decision → Output

### Pipeline Stages

1. **Injection Detection**

   * Detects prompt injection and jailbreak attempts.
   * Uses a scoring system based on suspicious phrases.

2. **PII Detection (Presidio)**

   * Detects sensitive information such as:

     * Phone numbers
     * Emails
     * Names
     * Custom entities

3. **Policy Decision Engine**

   * Applies security policies:

     * **ALLOW** → Safe input
     * **MASK** → Sensitive information detected
     * **BLOCK** → Prompt injection detected

4. **Output Processing**

   * Masked or blocked responses are returned.

---

## Presidio Customizations

Three custom recognizers were implemented:

1. **API Key Recognizer**

   * Detects API keys using regex patterns.

2. **Internal ID Recognizer**

   * Detects internal organization IDs.

3. **Custom Phone Number Recognizer**

   * Detects phone numbers using custom patterns.

Context-aware scoring is applied using keywords such as **api, token, phone, contact, and id**.

---

## Project Structure

```
llm-security-gateway/

main.py
injection_detector.py
pii_detector.py
policy_engine.py
custom_recognizers.py
evaluation.py
requirements.txt
README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/AnasCodeVerse/llm-security-gateway.git
cd llm-security-gateway
```

Install dependencies:

```
pip install -r requirements.txt
```

Download the spaCy language model:

```
python -m spacy download en_core_web_lg
```

---

## Running the System

Run the security gateway:

```
python main.py
```

The program will prompt for user input and return:

* Security decision
* Processed output
* Latency

Example:

```
Enter prompt: My phone number is 03001234567

Decision: MASK
Output: My phone number is <CUSTOM_PHONE>
Latency: 0.03s
```

---

## Example Security Scenarios

| Input                          | Detection        | Decision |
| ------------------------------ | ---------------- | -------- |
| Hello, how are you?            | None             | Allow    |
| Ignore previous instructions   | Prompt Injection | Block    |
| My phone number is 03001234567 | PII detected     | Mask     |

---

## Technologies Used

* Python
* Microsoft Presidio
* spaCy
* GitHub

---

## Reproducibility

To reproduce the system:

1. Clone the repository
2. Install dependencies
3. Download the spaCy model
4. Run `main.py`

---

## Author

Muhammad Anas
BS Computer Science
Bahria University Islamabad
