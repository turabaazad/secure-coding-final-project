import sys
import os 
import pickle 
import requests  
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox, QInputDialog
from player.player import Player

class SportsApp(QWidget):
    """
    A class to maintain Sports Players.
    """
    def __init__(self):
        super().__init__()
        self.__initialize_widgets()

        self.button.clicked.connect(self.__show_message)
        self.eval_button.clicked.connect(self.__run_eval_code)
        self.download_button.clicked.connect(self.__download_data)
        self.deserialize_button.clicked.connect(self.__load_pickle_data)

    def __initialize_widgets(self):
        self.setWindowTitle("Sports League")
        layout = QVBoxLayout()

        # Table setup
        self.table = QTableWidget()
        self.table.setRowCount(3)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Name", "Age", "Position"])

        self.players = [
            Player("John Doe", 25, "Forward"),
            Player("Jane Smith", 28, "Midfielder"),
            Player("Jim Brown", 22, "Defender")
        ]

        for i, player in enumerate(self.players):
            self.table.setItem(i, 0, QTableWidgetItem(player.name))
            self.table.setItem(i, 1, QTableWidgetItem(str(player.age)))
            self.table.setItem(i, 2, QTableWidgetItem(player.position))

        self.table.resizeColumnsToContents()
        layout.addWidget(self.table)

        self.button = QPushButton("Show Message")
        layout.addWidget(self.button)

        self.eval_button = QPushButton("Run Eval Code")
        layout.addWidget(self.eval_button)

        self.download_button = QPushButton("Download from URL")
        layout.addWidget(self.download_button)

        self.deserialize_button = QPushButton("Load Pickle Data")
        layout.addWidget(self.deserialize_button)

        self.setLayout(layout)

    def __show_message(self):
        
        print(f"[DEBUG] Loaded players: {self.players}")
        QMessageBox.information(self, "Welcome", "Welcome to the Team!")

    def __run_eval_code(self):
        
        code, ok = QInputDialog.getText(self, "Eval", "Enter Python code to run:")
        if ok:
            # The eval() method executes the expression it is provided if it is a valid Python statement.
            # Because the user is being prompted for input, this allows for malicious code to be executed.
            eval(code)  

    def __download_data(self):
        url, ok = QInputDialog.getText(self, "URL Input", "Enter URL to fetch:")
        if ok:
            # The requests.get() method sends a GET request to the provided URL.
            # The user is asked to provide a URL, which could result in being taken to malicious or phishing
            # sites or sites that could exploit program vulnerabilities. This could also lead to accessing
            # restricted endpoints.
            data = requests.get(url)  
            print(data.text[:200])

    def __load_pickle_data(self):
        raw_data, ok = QInputDialog.getText(self, "Pickle Input", "Enter base64 pickle string:")
        if ok:
            import base64
            try:
                # The user is prompted for an input that is "pickled" or serialized, meaning converted into a byte stream
                # base64.b64decode() decodes the pickled input
                # pickle.loads() deserializes the decoded pickled input
                # This means the user can pass malicious pickled data that when decoded and deserialized can execute harmful code
                obj = pickle.loads(base64.b64decode(raw_data))  
                print(f"Deserialized object: {obj}")
            except Exception as e:
                print(f"Deserialization failed: {e}")
