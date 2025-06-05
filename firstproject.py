import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem)
from ui_mainwindoww import Ui_MainWindow

class Budgetapp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_5.setReadOnly(True)

        self.pushButton.clicked.connect(self.add_item)
        self.pushButton_2.clicked.connect(self.set_budget)
        self.pushButton_3.clicked.connect(self.remove_selected)

        self.tableWidget.itemChanged.connect(self.update_total)


    def add_item(self):
        item_name = self.lineEdit.text().strip()
        price_text = self.lineEdit_2.text().strip()

        if not item_name:
            return

        try:
            price = float(price_text)
            if price < 0:
                return
        except ValueError:
            return

        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        self.tableWidget.setItem(row, 0, QTableWidgetItem(item_name))
        self.tableWidget.setItem(row, 1, QTableWidgetItem(f"{price:.2f}"))

        self.lineEdit.clear()
        self.lineEdit_2.clear()

        self.update_total()

    def set_budget(self):
        text = self.lineEdit_3.text().strip()

        try:
            budget = float(text)
            if budget < 0:
                return

            self.lineEdit_4.setText(f"{budget:.2f}")
            self.lineEdit_3.clear()
        except ValueError:
            return

    def remove_selected(self):
        selected_rows = {item.row() for item in self.tableWidget.selectedItems()}
        for rows in sorted(selected_rows, reverse=True):
            self.tableWidget.removeRow(rows)
        self.update_total()

    def update_total(self):
        total = 0.0
        for row in range(self.tableWidget.rowCount()):
            price_item = self.tableWidget.item(row, 1)
            if price_item:
                try:
                    total += float(price_item.text())
                except ValueError:
                    pass

            self.lineEdit_5.setText(f"{total:.2f}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Budgetapp()
    window.show()
    sys.exit(app.exec_())












