"""Figuring out Pytest fixtures, ignore."""
def test_000001_a(uuid_session, uuid_module, uuid_function):
    print("Session UUID: "+uuid_session)
    print("Module UUID: "+uuid_module)
    print("Function UUID: "+uuid_function)

def test_000001_b(uuid_session, uuid_module, uuid_function):
    print("Session UUID: "+uuid_session)
    print("Module UUID: "+uuid_module)
    print("Function UUID: "+uuid_function)

def test_000001_c(uuid_session, uuid_module, uuid_function):
    print(f"Session UUID: {uuid_session}")
    print("Module UUID: "+uuid_module)
    print("Function UUID: "+uuid_function)