def read_file_to_string(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"The file '{path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
