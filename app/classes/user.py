from flask_login import UserMixin, AnonymousUserMixin

class User(UserMixin):
    def __init__(self, name, id, active=True):
        self.name = name
        self.id = id
        self.active = active

    def is_active(self):
        return self.active


class Anonymous(AnonymousUserMixin):
    name = "Anonymous"


USERS = {
    1: User("admin", 1),
    2: User("user", 2),
    3: User("expired_user", 3, False),
}

USER_NAMES = dict((user.name, user) for user in USERS.values())

