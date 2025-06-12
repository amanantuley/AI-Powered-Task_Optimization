def anonymize_user():
    from uuid import uuid4
    return f"user_{uuid4().hex[:8]}"