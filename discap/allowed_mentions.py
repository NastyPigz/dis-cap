

class AM:
    @staticmethod
    def all():
        return {"parse": ["users", "roles", "everyone"], "replied_user": True}
    
    @staticmethod
    def no():
        return {"parse": [], "replied_user": False}
    
    @staticmethod
    def reply(boo:bool=False):
        return {"parse": ["users", "roles", "everyone"], "replied_user": boo}

    @staticmethod
    def custom(*, users:bool=True, roles:bool=True, everyone:bool=True, _users:list=[], _roles:list=[], author:bool=False):
        list_1 = []
        if users:
            list_1.append("users")
        if roles:
            list_1.append("roles")
        if everyone:
            list_1.append("everyone")
        return {"parse": list_1, "users": _users, "roles": _roles, "replied_user": author}
