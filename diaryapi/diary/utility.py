import uuid

def generate_key():
    return str(uuid.uuid4()).replace("-","")[:8]
