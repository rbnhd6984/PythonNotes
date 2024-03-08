import json
from datetime import datetime

from note import Note


class NoteApp:
    def __init__(self, filename):
        self.filename = filename
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.filename, 'r') as f:
                notes_dict = json.load(f)
                return {id: Note(id, note_dict['title'], note_dict['body'], note_dict['created_at'],
                                 note_dict['updated_at']) for id, note_dict in notes_dict.items()}
        except FileNotFoundError:
            return {}

    def save_notes(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump({id: note.to_dict() for id, note in self.notes.items()}, f, ensure_ascii=False)

    def create_note(self, title, body):
        id = str(len(self.notes) + 1)
        now = datetime.now().strftime('%d.%m.%Y %H:%M')
        self.notes[id] = Note(id, title, body, now, now)
        self.save_notes()

    def update_note(self, id, title, body):
        if id in self.notes:
            self.notes[id].update(title, body)
            self.save_notes()

    def delete_note(self, id):
        if id in self.notes:
            del self.notes[id]
            self.save_notes()

    def get_note(self, id):
        return self.notes.get(id, None)

    def get_all_notes(self):
        return list(self.notes.values())
