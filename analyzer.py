import numpy as np


def wait_for_user():
    input("\nPress Enter to continue...")


class NumPyAnalyzer:
    def __init__(self):
        self.data = None

    def build_array(self):
        print("\n--- Create Array ---")
        print("1. One Dimensional")
        print("2. Two Dimensional")
        print("3. Three Dimensional")

        try:
            option = int(input("Choose array type: "))
        except ValueError:
            print("Please enter a valid number.")
            return

        if option == 1:
            raw = input("Enter values separated by spaces: ")
            values = [int(item) for item in raw.split()]
            self.data = np.array(values)

        elif option == 2:
            try:
                rows = int(input("Rows: "))
                cols = int(input("Columns: "))
                total = rows * cols
                raw = input(f"Enter {total} values separated by spaces: ")
                values = [int(item) for item in raw.split()]

                if len(values) != total:
                    print("The number of values does not match the requested size.")
                    return

                self.data = np.array(values).reshape(rows, cols)

            except ValueError:
                print("Invalid numeric input.")
                return

        elif option == 3:
            try:
                layers = int(input("Layers: "))
                rows = int(input("Rows: "))
                cols = int(input("Columns: "))
                total = layers * rows * cols

                raw = input(f"Enter {total} values separated by spaces: ")
                values = [int(item) for item in raw.split()]

                if len(values) != total:
                    print("The number of values does not match the requested size.")
                    return

                self.data = np.array(values).reshape(layers, rows, cols)

            except ValueError:
                print("Invalid numeric input.")
                return

        else:
            print("Invalid selection.")
            return

        print("\nArray created:")
        print(self.data)

    def access_data(self):
        if self.data is None:
            print("Create an array before using this option.")
            return

        while True:
            print("\n--- Indexing & Slicing ---")
            print("1. Access an element")
            print("2. Slice the array")
            print("3. Return to main menu")

            try:
                option = int(input("Choose an option: "))
            except ValueError:
                print("Invalid input.")
                continue

            if option == 1:
                self._index_element()

            elif option == 2:
                self._slice_data()

            elif option == 3:
                return

            else:
                print("Invalid option.")

            wait_for_user()

    def _index_element(self):
        try:
            if self.data.ndim == 1:
                position = int(input("Enter index: "))

                if -self.data.shape[0] <= position < self.data.shape[0]:
                    print("Value:", self.data[position])
                else:
                    print("Index is outside the array.")

            elif self.data.ndim == 2:
                row = int(input("Enter row index: "))
                col = int(input("Enter column index: "))

                valid = (
                    -self.data.shape[0] <= row < self.data.shape[0]
                    and -self.data.shape[1] <= col < self.data.shape[1]
                )

                if valid:
                    print("Value:", self.data[row, col])
                else:
                    print("Index is outside the array.")

            else:
                layer = int(input("Enter layer index: "))
                row = int(input("Enter row index: "))
                col = int(input("Enter column index: "))

                valid = (
                    -self.data.shape[0] <= layer < self.data.shape[0]
                    and -self.data.shape[1] <= row < self.data.shape[1]
                    and -self.data.shape[2] <= col < self.data.shape[2]
                )

                if valid:
                    print("Value:", self.data[layer, row, col])
                else:
                    print("Index is outside the array.")

        except ValueError:
            print("Index must be an integer.")

    def _slice_data(self):
        try:
            if self.data.ndim == 1:
                start = int(input("Start index: "))
                stop = int(input("End index: "))
                print("\nResult:")
                print(self.data[start:stop])

            elif self.data.ndim == 2:
                row_text = input("Row range (start:end): ")
                col_text = input("Column range (start:end): ")

                row_start, row_end = map(int, row_text.split(":"))
                col_start, col_end = map(int, col_text.split(":"))

                print("\nResult:")
                print(self.data[row_start:row_end, col_start:col_end])

            else:
                print("\n3D arrays:")
                print(self.data)

        except ValueError:
            print("Enter ranges in the correct format.")

    def math_menu(self):
        if self.data is None:
            print("Create an array before using this option.")
            return

        print("\n--- Mathematical Operations ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Element-wise Multiplication")
        print("4. Division")
        print("5. Dot Product")
        print("6. Matrix Multiplication")

        try:
            option = int(input("Choose an operation: "))
        except ValueError:
            print("Invalid input.")
            return

        if option in (1, 2, 3, 4):
            self._element_operations(option)

        elif option == 5:
            self._dot_product()

        elif option == 6:
            self._matrix_product()

        else:
            print("Invalid option.")

    def _element_operations(self, option):
        try:
            raw = input(
                f"Enter {self.data.size} values for the second array: "
            )
            values = [int(item) for item in raw.split()]

            if len(values) != self.data.size:
                print("Incorrect number of values.")
                return

            other = np.array(values).reshape(self.data.shape)

            print("\nCurrent array:")
            print(self.data)
            print("\nSecond array:")
            print(other)

            if option == 1:
                answer = self.data + other
                title = "Addition"

            elif option == 2:
                answer = self.data - other
                title = "Subtraction"

            elif option == 3:
                answer = self.data * other
                title = "Multiplication"

            else:
                if np.any(other == 0):
                    print("Division by zero is not allowed.")
                    return
                answer = self.data / other
                title = "Division"

            print(f"\n{title} result:")
            print(answer)

        except ValueError:
            print("Please enter integer values only.")

    def _dot_product(self):
        if self.data.ndim != 1:
            print("Dot product can only be used with a 1D array.")
            return

        try:
            raw = input(f"Enter {self.data.size} values: ")
            values = [int(item) for item in raw.split()]

            if len(values) != self.data.size:
                print("Incorrect number of values.")
                return

            other = np.array(values)

            print("\nFirst array:")
            print(self.data)
            print("Second array:")
            print(other)
            print("Dot product:", np.dot(self.data, other))

        except ValueError:
            print("Please enter integer values only.")

    def _matrix_product(self):
        if self.data.ndim != 2:
            print("Matrix multiplication requires a 2D array.")
            return

        try:
            rows = int(input("Rows in second matrix: "))
            cols = int(input("Columns in second matrix: "))

            if self.data.shape[1] != rows:
                print("The matrix dimensions are not compatible.")
                return

            raw = input(f"Enter {rows * cols} values: ")
            values = [int(item) for item in raw.split()]

            if len(values) != rows * cols:
                print("Incorrect number of values.")
                return

            other = np.array(values).reshape(rows, cols)
            answer = np.matmul(self.data, other)

            print("\nFirst matrix:")
            print(self.data)
            print("\nSecond matrix:")
            print(other)
            print("\nProduct:")
            print(answer)

        except ValueError:
            print("Please enter valid numeric values.")

    def join_or_split(self):
        if self.data is None:
            print("Create an array before using this option.")
            return

        print("\n--- Combine / Split ---")
        print("1. Combine two arrays")
        print("2. Split the current array")

        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input.")
            return

        if option == 1:
            self._combine_arrays()

        elif option == 2:
            self._split_array()

        else:
            print("Invalid option.")

    def _combine_arrays(self):
        if self.data.ndim != 2:
            print("Combining is available for 2D arrays only.")
            return

        try:
            raw = input(f"Enter {self.data.size} values: ")
            values = [int(item) for item in raw.split()]

            if len(values) != self.data.size:
                print("Incorrect number of values.")
                return

            other = np.array(values).reshape(self.data.shape)
            combined = np.vstack((self.data, other))

            print("\nCurrent array:")
            print(self.data)
            print("\nSecond array:")
            print(other)
            print("\nCombined result:")
            print(combined)

        except ValueError:
            print("Please enter integer values only.")

    def _split_array(self):
        try:
            parts = int(input("How many parts should be created? "))

            if parts <= 0:
                print("Number of parts must be greater than zero.")
                return

            if self.data.size % parts != 0:
                print("The array cannot be divided equally into that many parts.")
                return

            pieces = np.array_split(self.data, parts)

            print("\nSplit result:")
            for number, piece in enumerate(pieces, start=1):
                print(f"\nPart {number}:")
                print(piece)

        except ValueError:
            print("Please enter a valid number.")

    def find_sort_filter(self):
        if self.data is None:
            print("Create an array before using this option.")
            return

        print("\n--- Search / Sort / Filter ---")
        print("1. Search for a value")
        print("2. Sort the array")
        print("3. Show values greater than a number")

        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input.")
            return

        if option == 1:
            self._search_value()

        elif option == 2:
            self._sort_values()

        elif option == 3:
            self._filter_values()

        else:
            print("Invalid option.")

    def _search_value(self):
        try:
            target = int(input("Value to search: "))
            locations = np.where(self.data == target)

            if locations[0].size:
                print("Value found.")
                print("Position:", locations)
            else:
                print("Value not found.")

        except ValueError:
            print("Please enter an integer.")

    def _sort_values(self):
        print("\nCurrent array:")
        print(self.data)

        direction = input("Sort order (asc/desc): ").strip().lower()

        if direction == "asc":
            sorted_data = np.sort(self.data, axis=-1)

        elif direction == "desc":
            sorted_data = np.sort(self.data, axis=-1)

            if self.data.ndim == 1:
                sorted_data = sorted_data[::-1]
            elif self.data.ndim == 2:
                sorted_data = sorted_data[:, ::-1]
            else:
                sorted_data = sorted_data[:, :, ::-1]

        else:
            print("Enter either 'asc' or 'desc'.")
            return

        print("\nSorted array:")
        print(sorted_data)

    def _filter_values(self):
        try:
            limit = int(input("Show values greater than: "))
            selected = self.data[self.data > limit]

            print(f"\nValues greater than {limit}:")
            print(selected)

        except ValueError:
            print("Please enter an integer.")

    def statistics_menu(self):
        if self.data is None:
            print("Create an array before using this option.")
            return

        print("\n--- Statistics ---")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum")
        print("7. Maximum")
        print("8. Percentile")

        try:
            option = int(input("Choose an operation: "))
        except ValueError:
            print("Invalid input.")
            return

        print("\nArray:")
        print(self.data)

        if option == 1:
            print("Sum:", np.sum(self.data))

        elif option == 2:
            print("Mean:", np.mean(self.data))

        elif option == 3:
            print("Median:", np.median(self.data))

        elif option == 4:
            print("Standard Deviation:", np.std(self.data))

        elif option == 5:
            print("Variance:", np.var(self.data))

        elif option == 6:
            print("Minimum:", np.min(self.data))

        elif option == 7:
            print("Maximum:", np.max(self.data))

        elif option == 8:
            try:
                percentage = float(input("Enter percentile from 0 to 100: "))

                if 0 <= percentage <= 100:
                    value = np.percentile(self.data, percentage)
                    print(f"{percentage}th Percentile:", value)
                else:
                    print("Percentile must be between 0 and 100.")

            except ValueError:
                print("Enter a valid percentile.")

        else:
            print("Invalid option.")


def run_program():
    app = NumPyAnalyzer()

    print("=" * 44)
    print("          NUMPY DATA ANALYZER")
    print("=" * 44)

    while True:
        print("\nMain Menu")
        print("1. Create NumPy Array")
        print("2. Indexing and Slicing")
        print("3. Mathematical Operations")
        print("4. Combine or Split Arrays")
        print("5. Search, Sort and Filter")
        print("6. Statistics and Aggregates")
        print("7. Exit")

        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number from the menu.")
            wait_for_user()
            continue

        if option == 1:
            app.build_array()
            wait_for_user()

        elif option == 2:
            app.access_data()
            wait_for_user()

        elif option == 3:
            app.math_menu()
            wait_for_user()

        elif option == 4:
            app.join_or_split()
            wait_for_user()

        elif option == 5:
            app.find_sort_filter()
            wait_for_user()

        elif option == 6:
            app.statistics_menu()
            wait_for_user()

        elif option == 7:
            print("\n" + "=" * 44)
            print("       Thanks for using the analyzer!")
            print("                 Goodbye")
            print("=" * 44)
            break

        else:
            print("Invalid choice. Please try again.")
            wait_for_user()


if __name__ == "__main__":
    run_program()
