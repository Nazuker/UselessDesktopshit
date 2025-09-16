from PyQt6 import QtWidgets
from PyQt6.QtXml import QDomDocument

def create_simple_ui():
    doc = QDomDocument()
    
    # Создаем базовую структуру UI файла
    ui = doc.createElement("ui")
    ui.setAttribute("version", "4.0")
    doc.appendChild(ui)
    
    class_ = doc.createElement("class")
    class_.appendChild(doc.createTextNode("Dialog"))
    ui.appendChild(class_)
    
    widget = doc.createElement("widget")
    widget.setAttribute("class", "QDialog")
    widget.setAttribute("name", "Dialog")
    ui.appendChild(widget)
    
    # Сохраняем в файл
    with open("dialog.ui", "w", encoding="utf-8") as f:
        f.write(doc.toString())
    
    print("Файл dialog.ui создан!")

create_simple_ui() 