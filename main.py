from note_app import NoteApp


def main():
    app = NoteApp('notes.json')

    while True:
        print("\n1. Создать заметку")
        print("2. Обновить заметку")
        print("3. Удалить заметку")
        print("4. Показать заметку")
        print("5. Показать все заметки")
        print("6. Выход")

        choice = input("\nВыберите действие: ")

        if choice == '1':
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            app.create_note(title, body)
        elif choice == '2':
            id = input("Введите ID заметки: ")
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            app.update_note(id, title, body)
        elif choice == '3':
            id = input("Введите ID заметки: ")
            app.delete_note(id)
        elif choice == '4':
            id = input("Введите ID заметки: ")
            note = app.get_note(id)
            if note:
                print(
                    f"ID: {note.id}\nЗаголовок: {note.title}\nТекст: {note.body}\nДата создания: {note.created_at}\nДата обновления: {note.updated_at}")
            else:
                print("Заметка не найдена.")
        elif choice == '5':
            notes = app.get_all_notes()
            for note in notes:
                print(
                    f"\nID: {note.id}\nЗаголовок: {note.title}\nТекст: {note.body}\nДата создания: {note.created_at}\nДата обновления: {note.updated_at}")
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте еще раз.")


if __name__ == "__main__":
    main()
