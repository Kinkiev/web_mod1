from abc import ABC, abstractmethod
from rich.table import Table
from rich.console import Console
from rich import box

class UserOutput(ABC):
    
    @abstractmethod
    def print_message(self, message: str):
        pass
    
    @abstractmethod
    def print_table(self):
        pass

class ConsoleUserOutput(UserOutput):
    def __init__(self):
        self.console = Console()

    def print_message(self, message: str):
        self.console.print(message)

    def print_table(self, table):
        self.console.print(table)
        

class HelpView:
    def __init__(self, user_output: UserOutput):
        self.user_output = user_output
        
    def show_help(self, help_text):
        self.user_output.print_message(help_text)
        
    def show_command_list(self, command_list):
        table = Table(title="COMMAND HELP", style="red", show_header=True, header_style="bold", box=box.ROUNDED)
        table.add_column("Command", style="cyan")
        table.add_column("Description", style="green")
        
        for cmd, desc in command_list:
            table.add_row(cmd, desc)
        
        self.user_output.print_table(table)
    


# class ContactsView(UserOutput):
#     def __init__(self, contacts):
#         self.contacts = contacts
    
#     def render(self):
#         # Виведення карток з контактами користувача
#         pass


# class NotesView(UserOutput):
#     def __init__(self, notes):
#         self.notes = notes
    
#     def render(self):
#         # Виведення списку нотаток користувача
#         pass