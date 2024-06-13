from PyQt6.QtWidgets import QFileDialog

# Simple helper function for opening a file select dialog
def selectFile():
    # TODO: Update window text to be more descriptive
    # TODO: Update starting directory
    fileSelector = QFileDialog()
    fileSelector.setFileMode(QFileDialog.FileMode.ExistingFile)
    fileSelector.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
    fileSelector.setNameFilter("Text files (*.txt)")

    if fileSelector.exec():
        fileName = fileSelector.selectedFiles()
        return fileName[0]

    # widget = QWidget()
    # fileName = QFileDialog.getOpenFileName(widget, 'Open file', '~', 'Image files (*.jpg *.gif)')
