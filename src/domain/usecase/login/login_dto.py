def mapper(data: dict):
    return {
        "id": data['id'],
        "name": data['name'],
        "username": data['username'],
        "created_at": data['created_at'],
        "updated_at": data['updated_at']
    }
