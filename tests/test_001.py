def test_ping():
    print("Pong")
    return "Pong"

def test_uuid():
    import uuid
    run_uuid = uuid.uuid4()
    print(run_uuid)
    return run_uuid
