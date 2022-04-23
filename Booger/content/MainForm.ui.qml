/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick 2.15
import QtQuick.Controls 2.15
import Booger 1.0

Rectangle {
    width: Constants.width
    height: 800
    color: "#0d0d0d"
    border.color: "#3a9ff5"


    Image {
        id: image
        x: 549
        y: 317
        width: 353
        height: 262
        source: "../../etc/img/BudgetExecution.png"
        fillMode: Image.PreserveAspectFit
    }
}


