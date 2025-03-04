class UserRepository:
    def __init__(self):
        self.users = {}
    
    def add_user(self, user_id, name):
        self.users[user_id] = name
    
    def get_user(self, user_id):
        return self.users.get(user_id, "User not found")


class UserService:
    def __init__(self, repository):
        self.repository = repository
    
    def register_user(self, user_id, name):
        self.repository.add_user(user_id, name)
    
    def fetch_user(self, user_id):
        return self.repository.get_user(user_id)