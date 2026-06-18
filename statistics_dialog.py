from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QHeaderView,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
)


class StatisticsDialog(QDialog):
    """Окно со статистикой копирования замечаний в буфер обмена."""

    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Статистика копирования")
        self.resize(720, 480)

        layout = QVBoxLayout(self)
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Замечание", "Категория", "Копий"])
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.verticalHeader().setVisible(False)
        self.table.setSortingEnabled(True)
        layout.addWidget(self.table)

        close_button = QPushButton("Закрыть")
        close_button.clicked.connect(self.accept)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(close_button)
        layout.addLayout(button_layout)

        self.refresh(parent)

    def refresh(self, parent):
        stats = parent.get_copy_statistics()
        self.table.setSortingEnabled(False)
        self.table.setRowCount(len(stats))
        for row, entry in enumerate(stats):
            self.table.setItem(row, 0, QTableWidgetItem(entry["text"]))
            self.table.setItem(row, 1, QTableWidgetItem(entry["category"]))
            count_item = QTableWidgetItem()
            count_item.setData(Qt.DisplayRole, entry["copy_count"])
            count_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.table.setItem(row, 2, count_item)
        self.table.setSortingEnabled(True)
        self.table.sortItems(2, Qt.DescendingOrder)
