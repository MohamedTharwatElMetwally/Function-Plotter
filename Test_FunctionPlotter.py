
import pytest
import PySide2
from PySide2 import QtCore
import FunctionPlotter

validation = FunctionPlotter.ValidationCriteria()


# ======================================== Perform Automated Tests On Methods using pytest ========================================


# Testcases for Equation Validation

def test_equation_1():
    assert validation.validate_equation('') == 'empty'

def test_equation_2():
    assert validation.validate_equation('x++') == 'invalid syntax'

def test_equation_3():
    assert validation.validate_equation('5 * x^2 / 20 ?') == 'invalid syntax'

def test_equation_4():
    assert validation.validate_equation('5 * x^2 / 20 ') not in ['invalid syntax', 'empty']

def test_equation_5():
    assert validation.validate_equation('5 * x ^ 2/ 2 0      ') == '5*x^2/20'


# Testcases for Xmin & Xmax Validations

def test_number_1():
    assert validation.validate_number('') == 'empty'

def test_number_2():
    assert validation.validate_number('-100++') == 'invalid syntax'

def test_number_3():
    assert validation.validate_number('1000') == 1000

def test_number_4():
    assert validation.validate_number('-26.5') == -27

def test_number_5():
    assert validation.validate_number('255.9999') == 255


# Testcases for Xmin & Xmax Range Validation

def test_range_1():
    assert validation.validate_range(Xmax=-100, Xmin=100) == False

def test_range_2():
    assert validation.validate_range(Xmax=100, Xmin=-100) == True

def test_range_3():
    assert validation.validate_range(Xmax=500, Xmin=500) == True


# Testcases to Validate Equation Output

def test_equation_output_1():
    assert FunctionPlotter.Calculate_Y(equation='x^2 * x^3 / 100', x=10) == 1000

def test_equation_output_2():
    assert FunctionPlotter.Calculate_Y(equation='x^2', x=-10) == 100



# ======================================== Perform Automated Tests On GUI Application using pytest-qt ========================================


# Test Some of App Features

@pytest.fixture
def app(qtbot):

    # Fixture to create and return the application instance
    test_app = FunctionPlotter.MainWindow()
    qtbot.addWidget(test_app)
    return test_app


def test_app_main_components(app):

    assert app.findChild(PySide2.QtWidgets.QPushButton, 'Plot Button') is not None
    assert app.findChild(PySide2.QtWidgets.QPushButton, 'Exit Button') is not None

    assert app.findChild(PySide2.QtWidgets.QLabel, 'Equation Label') is not None
    assert app.findChild(PySide2.QtWidgets.QLabel, 'Xmin Label') is not None
    assert app.findChild(PySide2.QtWidgets.QLabel, 'Xmax Label') is not None

    assert app.findChild(PySide2.QtWidgets.QLineEdit, 'Equation Line Edit') is not None
    assert app.findChild(PySide2.QtWidgets.QLineEdit, 'Xmin Line Edit') is not None
    assert app.findChild(PySide2.QtWidgets.QLineEdit, 'Xmax Line Edit') is not None


# Testcases for Different Correct Scenarios

def test_correct_scenario_1(app, qtbot):

    previous_value = app.update_times

    app.equation.setText('x^2')
    app.Xmin.setText('-100')
    app.Xmax.setText('100')
    qtbot.mouseClick(app.plot_button, QtCore.Qt.LeftButton)

    assert app.update_times == previous_value + 1     # Update Graph Successfully  

def test_correct_scenario_2(app, qtbot):

    previous_value = app.update_times

    app.equation.setText('5*x^2+2^x')
    app.Xmin.setText('-99.1')
    app.Xmax.setText('100')
    qtbot.mouseClick(app.plot_button, QtCore.Qt.LeftButton)

    assert app.update_times == previous_value + 1     # Update Graph Successfully  


# Testcases for Different Error Scenarios
 
def test_range_error(app, qtbot):   # Range Error

    previous_value = app.update_times

    app.equation.setText('x^2')
    app.Xmin.setText('100')
    app.Xmax.setText('-100')
    qtbot.mouseClick(app.plot_button, QtCore.Qt.LeftButton)

    assert app.update_times == previous_value     # No Updates


def test_empty_equation(app, qtbot):   # Empty Equation

    previous_value = app.update_times

    app.equation.setText('')
    app.Xmin.setText('-100')
    app.Xmax.setText('100')
    qtbot.mouseClick(app.plot_button, QtCore.Qt.LeftButton)

    assert app.update_times == previous_value     # No Updates


def test_invalid_equation(app, qtbot):   # Invalid Equation

    previous_value = app.update_times

    app.equation.setText('x+?/5')
    app.Xmin.setText('-100')
    app.Xmax.setText('100')
    qtbot.mouseClick(app.plot_button, QtCore.Qt.LeftButton)

    assert app.update_times == previous_value     # No Updates


def test_empty_number(app, qtbot):   # Empty Number

    previous_value = app.update_times

    app.equation.setText('X^3')
    app.Xmin.setText('')
    app.Xmax.setText('100')
    qtbot.mouseClick(app.plot_button, QtCore.Qt.LeftButton)

    assert app.update_times == previous_value     # No Updates


def test_invalid_number(app, qtbot):   # Invalid Number

    previous_value = app.update_times

    app.equation.setText('X^3')
    app.Xmin.setText('-100')
    app.Xmax.setText('100??')
    qtbot.mouseClick(app.plot_button, QtCore.Qt.LeftButton)

    assert app.update_times == previous_value     # No Updates


