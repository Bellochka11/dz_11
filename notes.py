import pickle

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NoteManager:
    def __init__(self):
        self.notes = []

    def create_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)
        print("Заметка создана!")

    def save_notes(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self.notes, f)
        print("Заметки сохранены!")

    def load_notes(self, filename):
        with open(filename, "rb") as f:
            self.notes = pickle.load(f)

    def list_notes(self):
        if len(self.notes) > 0:
            print("Список заметок:")
            for i, note in enumerate(self.notes):
                print(f"{i+1}. {note.title}")
        else:
            print("У вас пока нет заметок.")

    def edit_note(self, note_index, new_title, new_content):
        if note_index >= 0 and note_index < len(self.notes):
            note = self.notes[note_index]
            note.title = new_title
            note.content = new_content
            print("Заметка отредактирована!")
        else:
            print("Некорректный индекс заметки.")

    def delete_note(self, note_index):
        if note_index >= 0 and note_index < len(self.notes):
            del self.notes[note_index]
            print("Заметка удалена!")
        else:
            print("Некорректный индекс заметки.")

manager = NoteManager()

manager.create_note("Покупки", "Молоко, хлеб, яйца")

manager.save_notes("notes.dat")

manager.load_notes("notes.dat")

manager.list_notes()

manager.edit_note(0, "Покупки на выходные", "Молоко, хлеб, яйца, овощи")

manager.delete_note(0)

manager.list_notes()