# Function Plotter
## Master Micro Internship Task

## Built with
<ul>
  <li><a href="https://www.python.org/">Python</a></li>
  <li><a href="https://pypi.org/project/PySide2/">PySide2</a></li>
  <li><a href="https://matplotlib.org/">Matplotlib</a></li>
  <li><a href="https://docs.pytest.org/en/7.4.x/">pytest</a></li>
  <li><a href="https://pypi.org/project/pytest-qt/">pytest-qt</a></li>
</ul>

## Installation
1. **Clone the repository**
   > $ git clone https://github.com/MohamedTharwatElMetwally/Function-Plotter
2. **Move to repository directory**
   > $ chdir Function-Plotter
3. **Install dependencies**
   > $ pip install matplotlib

   > $ pip --default-timeout=1000 install PySide2

   > $ pip install pytest

   > $ pip install pytest-qt

## Running
1. Open Cmder or any other Terminal
2. For running the Function Plotter, Run this command:
   > $ python FunctionPlotter.py
3. For running the testcases file, Run this command:
   > $ pytest Test_FunctionPlotter.py

# Snapshots
## Sample Run of Function Plotter
<img src="https://github.com/MohamedTharwatElMetwally/Function-Plotter/blob/master/screens/sample1.png">
<br>
<img src="https://github.com/MohamedTharwatElMetwally/Function-Plotter/blob/master/screens/sample2.png">
<br>
<img src="https://github.com/MohamedTharwatElMetwally/Function-Plotter/blob/master/screens/sample3.png">
<br>
<img src="https://github.com/MohamedTharwatElMetwally/Function-Plotter/blob/master/screens/sample4.png">
<br>
<img src="https://github.com/MohamedTharwatElMetwally/Function-Plotter/blob/master/screens/sample5.png">

## Validation for Different Error Scenarios

### Validation of Input Equation
<img src="https://github.com/MohamedTharwatElMetwally/Function-Plotter/blob/master/screens/empty_equation.png">
<br>
<img src="https://github.com/MohamedTharwatElMetwally/Function-Plotter/blob/master/screens/invalid_equation.png">

-------------------------
### Validation of Xmin
<img src="https://github.com/MohamedTharwatElMetwally/Function-Plotter/blob/master/screens/empty_Xmin.png">
<br>
<img src="https://github.com/MohamedTharwatElMetwally/Function-Plotter/blob/master/screens/invalid_Xmin.png">

-----------------------------------
### Validation of Xmax
<img src="https://github.com/MohamedTharwatElMetwally/Function-Plotter/blob/master/screens/empty_Xmax.png">
<br>
<img src="https://github.com/MohamedTharwatElMetwally/Function-Plotter/blob/master/screens/invalid_Xmax.png">

------------------------------------
### Validation of Invalid Range for X
<img src="https://github.com/MohamedTharwatElMetwally/Function-Plotter/blob/master/screens/range_error.png">

## Snapshot for Running Tests using pytest
<img src="https://github.com/MohamedTharwatElMetwally/Function-Plotter/blob/master/screens/run_pytest.png">
