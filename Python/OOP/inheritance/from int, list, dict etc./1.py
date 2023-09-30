class CustomList(list):
    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        # Customize the string representation
        return f"CustomList({super().__str__()})"


# Create an instance of the custom list
custom_list = CustomList([1, 2, 3, 4, 5])

# Print the custom list
print(custom_list)  # CustomList([1, 2, 3, 4, 5])
