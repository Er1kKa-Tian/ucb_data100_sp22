import os

def main(): 
    for folder_path, _, files in os.walk(os.getcwd()):

        py_test_files = [file for file in files if folder_path.endswith("tests") and file.endswith(".py")]

        for py_test_file in py_test_files:

            file_path = os.path.join(folder_path, py_test_file)
            
            with open(file_path, "r") as file:
                content = file.read()

            new_content = "OK_FORMAT = True\n" + content

            with open(file_path, "w") as file:
                file.write(new_content)

            print(f"Modified {file_path}")



if __name__ == "__main__":
    main()