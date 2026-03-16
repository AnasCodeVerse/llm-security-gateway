from presidio_analyzer import Pattern, PatternRecognizer


def get_custom_recognizers():

    recognizers = []

    # 1️⃣ Custom Recognizer — API Key
    api_pattern = Pattern(
        name="api_key_pattern",
        regex=r"sk-[a-zA-Z0-9]{16,}",
        score=0.9,
    )

    api_recognizer = PatternRecognizer(
        supported_entity="API_KEY",
        patterns=[api_pattern],
        context=["api", "key", "token"]  # context-aware scoring
    )

    recognizers.append(api_recognizer)


    # 2️⃣ Custom Recognizer — Internal ID
    id_pattern = Pattern(
        name="internal_id_pattern",
        regex=r"ID-\d{4,}",
        score=0.8,
    )

    id_recognizer = PatternRecognizer(
        supported_entity="INTERNAL_ID",
        patterns=[id_pattern],
        context=["employee", "internal", "id"]
    )

    recognizers.append(id_recognizer)


    # 3️⃣ Composite Example — Phone + Name context
    phone_pattern = Pattern(
        name="custom_phone_pattern",
        regex=r"03\d{9}",
        score=0.85,
    )

    phone_recognizer = PatternRecognizer(
        supported_entity="CUSTOM_PHONE",
        patterns=[phone_pattern],
        context=["phone", "contact", "number"]
    )

    recognizers.append(phone_recognizer)

    return recognizers