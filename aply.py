     from .aply import QtCore, QtWidgets  # type: ignore
     import sys # type:ignore 
     def super_():
     A stub for the super() function.
     This function is used to mimic the behavior of Python 3's super() in a
     project that uses Python 2 style code to prevent errors.
     :return: None
     """
    pass
   def get_response(command: str) -> str:
    """
     Get a response for the given command.

     This function responds to predefined basic commands. It prints the input
     command and the output response for debugging purposes. In a real-world
     application, it could integrate with an NLP API to handle more complex
     commands.

    :param command: A string representing the user's command input.
    :return: A string containing the response to the command.
    """
    # Debugging: Print the input command
    print(f"get_response: Input = {command}")

    # Define a dictionary mapping basic commands to their responses
    # This dictionary is currently in lower case to make it easier to
    # recognize commands, but in a real-world application, the keys should
    # be in the same case as the commands.
    responses = {
        "hola": "Hola, ¿cómo estás?",
        "adiós": "Adiós, que tengas un buen día.",
        "¿cómo estás?": "Estoy bien, gracias. ¿Y tú?",
        "¿tú estás?": "Estoy bien, gracias. ¿Y tu?",
        "hasta luego": "Hasta luego, que tengas un buen día.",
        "adiós": "Adios, que tengas un buen dia.",}



    # Retrieve the corresponding response from the dictionary
    # If the command is not recognized, return a default message
    response = responses.get(command.lower(), "No entiendo lo que dices.")
      # Debugging: Print the output response  print(f"get_response: Output = {response}")
    return response


class JarvisInterface(QtWidgets.QMainWindow):
    def __init__(self):
        """
        Initialize the J.A.R.V.I.S. user interface.

        This class will create a window with a text area to display questions and
        answers and a command input at the bottom.

        :return: None
        """
        super().__init__()
        self.setWindowTitle("J.A.R.V.I.S.")
        self.setGeometry(100, 100, 600, 400)

        # Configure the text area to display questions and answers
        self.text_display = QtWidgets.QTextEdit(self)
        self.text_display.setGeometry(50, 50, 500, 250)
        self.text_display.setReadOnly(True)
        # TODO: Add a vertical scrollbar to the text area

        # Command input
        self.command_input = QtWidgets.QLineEdit(self)
        self.command_input.setGeometry(50, 320, 500, 30)
        self.command_input.setPlaceholderText("Enter your command here...")
        self.command_input.returnPressed.connect(self.process_command)

    def process_command(self) -> None:
        """
        Process user input and display the response.

        This method is called when the user presses the Enter key after
        typing a command in the command input box. It retrieves the user's
        input as a string, clears the input box, appends the user's input
        to the text display, gets the response from the input, and appends
        the response to the text display. The response is a string.

        :return: None
        """
        # Check if the command input field is not None
        if self.command_input is None:
            raise ValueError("Command input field is null")
        
        # Retrieve the user's input from the command input field
        user_input_text: str = self.command_input.text()
        print(f"process_command: User input = {user_input_text}")
        
        # Clear the command input field for new input
        self.command_input.clear()
        print("process_command: Command input cleared")

        # Check if the text display is not None
        if self.text_display is None:
            raise ValueError("Text display field is null")
        
        # Append the user's input to the text display area
        self.text_display.append(f"Usuario: {user_input_text}")
        print(f"process_command: User input appended to text display")

        # Get the response for the user's input using the get_response function
        response_text: str = get_response(user_input_text)
        print(f"process_command: Response = {response_text}")
        
        # Capitalize the response text for better readability
        response_text = response_text.capitalize()
        print("process_command: Response capitalized")

        # Append the response from J.A.R.V.I.S. to the text display area
        self.text_display.append(f"J.A.R.V.I.S.: {response_text}")
        print("process_command: Response appended to text display")



def main():
    """
    Entry point for the program. Creates a QtWidgets.QApplication object
    and JarvisInterface object, shows the interface and starts the
    application event loop.
    """
    app = QtWidgets.QApplication(sys.argv)
    jarvis = JarvisInterface()
    jarvis.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

