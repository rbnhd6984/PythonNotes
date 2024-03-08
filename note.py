from datetime import datetime


class Note:
    def __init__(self, id, title, body, created_at=None, updated_at=None):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = created_at if created_at else datetime.now().strftime('%d.%m.%Y %H:%M')
        self.updated_at = updated_at if updated_at else datetime.now().strftime('%d.%m.%Y %H:%M')

    def update(self, title, body):
        self.title = title
        self.body = body
        self.updated_at = datetime.now().strftime('%d.%m.%Y %H:%M')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
