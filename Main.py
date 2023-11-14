from TestCases import TestCases

if __name__ == '__main__':

    # Create an instance of the Test class
    test_instance = TestCases(outputFileName="output1.txt")

    # Read and execute functions from the input file
    with open("input1.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        # Split the line to get the function name and arguments
        tokens = line.split('(')
        function_name = tokens[0].strip()
        arguments = tokens[1].replace(')', '').strip()

        # Construct the method call string and execute it
        method_call_string = f'test_instance.{function_name}({arguments})'
        eval(method_call_string)
