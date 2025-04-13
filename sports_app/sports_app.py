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
            # We should avoid using the eval function, as it can lead to injection attacks.
            eval(code)  

    def __download_data(self):
        url, ok = QInputDialog.getText(self, "URL Input", "Enter URL to fetch:")
        if ok:
            # 1. if we could set the timeout setting for the request, it would be more secure to aviod DoS attack
            # 2. use try catch block to catch the error would be more friendly to avoid program crashing unexpectedly
            data = requests.get(url)  
            print(data.text[:200])

    def __load_pickle_data(self):
        raw_data, ok = QInputDialog.getText(self, "Pickle Input", "Enter base64 pickle string:")
        if ok:
            import base64
            try:
                obj = pickle.loads(base64.b64decode(raw_data))  
                print(f"Deserialized object: {obj}")
            except Exception as e:
                print(f"Deserialization failed: {e}")
