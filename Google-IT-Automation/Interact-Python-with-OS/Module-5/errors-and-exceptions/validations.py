def validate_user(username: str, minlen: int):
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True