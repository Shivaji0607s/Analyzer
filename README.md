NumPy Data Analyzer

A menu-driven Python application for creating, manipulating, analyzing, and performing statistical operations on NumPy arrays.

This project provides an interactive way to practice and demonstrate fundamental NumPy concepts, including multidimensional arrays, indexing, slicing, mathematical operations, searching, sorting, filtering, array combination, splitting, and statistical analysis.

Features
Array Creation

Create 1D, 2D, and 3D NumPy arrays.

Specify dimensions interactively.

Validate the number of elements before creating an array.

Display the created array immediately.

Indexing and Slicing

Access individual elements from arrays.

Support indexing for 1D, 2D, and 3D arrays.

Support negative indexing.

Slice 1D and 2D arrays using custom ranges.

Validate index and input values.

Mathematical Operations

Perform common mathematical operations between arrays:

Addition

Subtraction

Element-wise multiplication

Division

Dot product

Matrix multiplication

The application also checks for conditions such as incompatible matrix dimensions and division by zero.

Array Combination and Splitting

Combine two 2D arrays using vertical stacking.

Split arrays into multiple parts.

Validate whether an array can be divided equally.

Display each resulting section separately.

Search, Sort, and Filter

Search for specific values within an array.

Display the positions where a value is found.

Sort arrays in ascending order.

Sort arrays in descending order.

Filter and display values greater than a specified number.

Statistical Analysis

Calculate commonly used statistical values:

Sum

Mean

Median

Standard deviation

Variance

Minimum value

Maximum value

Percentiles

Percentile calculations accept values between 0 and 100.

Technologies Used

Python — Core programming language

NumPy — Numerical computing and array operations

Requirements

Before running the project, make sure you have:

Python 3.x

NumPy

Installation
1. Clone the repository

Clone this repository to your local machine using Git.

2. Navigate to the project directory

Open a terminal and move into the project folder.

3. Install NumPy

Install the NumPy dependency using Python's package manager.

4. Run the application

Start the program from the terminal using Python.

The application will display an interactive menu from which you can access the available NumPy operations.

Application Menu

The main menu provides the following options:

Create NumPy Array

Indexing and Slicing

Mathematical Operations

Combine or Split Arrays

Search, Sort and Filter

Statistics and Aggregates

Exit

Project Structure

The project is organized around a main analyzer class responsible for managing the current NumPy array and performing different operations.

The application includes separate functionality for:

Array creation

Data access

Indexing and slicing

Mathematical calculations

Dot products

Matrix multiplication

Array combination

Array splitting

Searching

Sorting

Filtering

Statistical calculations

Application menu management

Error Handling

The application includes input validation to handle common user errors, including:

Invalid menu selections

Non-numeric input

Incorrect numbers of array elements

Invalid array dimensions

Out-of-range indexes

Invalid slicing formats

Division by zero

Incompatible matrix dimensions

Invalid percentile values

Invalid split sizes

This helps prevent the application from terminating unexpectedly during normal interactive use.

Learning Objectives

This project is useful for learning and practicing:

NumPy array creation

Multidimensional arrays

Array shapes and dimensions

NumPy indexing

Array slicing

Element-wise operations

Dot products

Matrix multiplication

Array stacking and splitting

Boolean filtering

Sorting

Searching with NumPy

Descriptive statistics

Python classes and methods

Exception handling

Menu-driven program design

Example Use Cases

The NumPy Data Analyzer can be used as:

A beginner-friendly NumPy practice project

A Python academic project

A demonstration of numerical array operations

A learning tool for multidimensional data manipulation

A starting point for developing a larger data-analysis application

Future Improvements

Possible improvements for future versions include:

Support for floating-point input

Saving and loading arrays from files

CSV import and export

Graphical user interface

Data visualization using Matplotlib

More advanced statistical functions

Array concatenation along different axes

Custom sorting options

Support for larger datasets

Automated test cases

Configuration-based application settings

Contributing

Contributions and suggestions are welcome.

If you would like to improve the project:

Fork the repository.

Create a new branch for your changes.

Make and test your improvements.

Commit your changes.

Submit a pull request.

License

This project can be distributed and modified according to the license included in the repository.

If no license has been added yet, consider adding an appropriate open-source license before publishing the project for public reuse.

Author

Sharma Shivaji

Python & NumPy Project

⭐ If you find this project useful for learning NumPy and Python, consider giving the repository a star.
