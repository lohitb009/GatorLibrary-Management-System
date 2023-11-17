import sys

from TestCases import TestCases

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: python Main.py <input_file>")
        sys.exit(1)

    # input file name
    input_file_name = sys.argv[1]

    # set the output-file name
    outputFileName = "input1_output1.txt"

    # set the output-file name
    if input_file_name == "input2.txt":
        outputFileName = "input2_output2.txt"
    elif input_file_name == "input3.txt":
        outputFileName = "input3_output3.txt"
    elif input_file_name == "input4.txt":
        outputFileName = "input4_output4.txt"

    # Create an instance of the Test class
    test_instance = TestCases(outputFileName=outputFileName)

    # Read and execute functions from the input file
    with open(input_file_name, "r") as file:
        lines = file.readlines()

    for line in lines:
        # Split the line to get the function name and arguments
        tokens = line.split('(')
        function_name = tokens[0].strip()
        arguments = tokens[1].replace(')', '').strip()

        # Construct the method call string and execute it
        method_call_string = f'test_instance.{function_name}({arguments})'

        eval(method_call_string)

        if method_call_string == "test_instance.Quit()":
            break