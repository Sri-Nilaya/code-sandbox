#import required modules from other files
class CalculatorCLI:

    def operation_selection(self):
        #Get user input of which operation they want to perform by displaying the options
        try:
            operation = int(input("Enter the option you want to choose:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division"))
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except EOFError:
            print("No input received.")
        except Exception as e:
            print(f"An Error occurred: {e}")
        
        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: ")) #write code to catch exceptions when division is selected numerator is greater than denom
        
        #Dictionary to map user input to respective operation
        math_operations = {
            "1": addition(num1,num2) 
        }



        

