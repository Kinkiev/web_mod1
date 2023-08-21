from abc import ABC, abstractmethod
from rich.table import Table
from rich.console import Console
from rich import box

class UserOutput(ABC):
    
    @abstractmethod
    def render(self):
        pass


class ContactsView(UserOutput):
    def __init__(self, contacts):
        self.contacts = contacts
    
    def render(self):
        # Виведення карток з контактами користувача
        pass


class NotesView(UserOutput):
    def __init__(self, notes):
        self.notes = notes
    
    def render(self):
        # Виведення списку нотаток користувача
        pass


class HelpView(UserOutput):
    def __init__(self, commands):
        self.commands = commands
    
    def render(self): # Виведення сторінки з інформацією про доступні команди
        console = Console()
        table = Table(title=">>> space is the reserved argument separator character <<<", show_header=True, header_style="bold", box=box.ROUNDED)
        table.add_column("Command", style="cyan")
        table.add_column("Description", style="green")
        
        table.add_row("hello", "Greetings and introduction 🚀")
        table.add_row("add [name] [phone] [birthday] [email] [address]", "Add a new contact with details ✅")
        table.add_row("change [name] [phone]", "Change phone number for a contact ✅")
        table.add_row("del [name]", "Deleting contact by name ❌")
        table.add_row("find [name]", "Find contact by name")
        table.add_row("show", "Shows you all contacts in addressbook 📖")
        table.add_row("birthday [name] [date in format dd-mm-yyyy]", "Setting birthday date by name")
        table.add_row("bday [name] [new_birthday]", "Changing birthday date by name")
        table.add_row("period [number of days]", "Shows you a birthdays in a period")
        table.add_row("show-notes", "Shows you a list of notes 📖")
        table.add_row("add-notes [name] [text] [tag]", "Adding notes ✅")
        table.add_row("add-tag [note number] [tag]", "Adding a tag for a note ✅")
        table.add_row("change-tag [note number] [tag]", "Changing a tag in a note")
        table.add_row("add-text [note number] [text]", "Adding a text to a note ✅")
        table.add_row("change-text [note number] [text]", "Changing a text to a note")
        table.add_row("delete-note [note number]", "Deleting a note ❌")
        table.add_row("add-text [note number] [text]", "Adding a text to a note")
        table.add_row("search-n [note number] [text]", "Searching a text in note")
        table.add_row("bye, end, exit", "Exit from the bot-helper")
        table.add_row("help", "shows you this table 💡")
        
        
        console.print(table)
        return ""
