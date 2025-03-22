from calculator.core.operations import Calculator
class CalculatorCLI:
    def perform_calculation(self, num1, num2, selected_operation):
                            calculation = Calculator(num1,num2)
                            math_operations(selected_operation)

                            #Dictionary to map user input to respective operation
                            math_operations = {
                                    "1": calculation.addition(),
                                    "2": calculation.subtraction(),
                                    "3": calculation.multiplication(),
                                    "4": calculation.division()     
                                } 


    def  get_valid_inputs(self,selected_operation):
                            
                            try:
                                num1 = float(input("Enter number 1: "))
                            except ValueError:
                                  print("Invalid input. Please enter a valid number.")
                            except EOFError:
                                  print("No input received.")
                            except Exception as e:
                                  print(f"An Error occurred: {e}")

                            try:
                                num2 = float(input("Enter number 2: "))
                            except ValueError:
                                  print("Invalid input. Please enter a valid number.")
                            except EOFError:
                                  print("No input received.")
                            except Exception as e:
                                  print(f"An Error occurred: {e}")
                            self.perform_calculation(num1,num2,selected_operation)                            
                            
    def operation_selection(self):

        while(True):
                #Get user input of which operation they want to perform by displaying the options
                try:
                    selected_operation = int(input("Enter the option you want to choose:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division \n5. Exit"))
                
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                except EOFError:
                    print("No input received.")
                except Exception as e:
                    print(f"An Error occurred: {e}")
                
                if selected_operation >0 and selected_operation <= 4:
                    self.get_valid_inputs(selected_operation)
                elif selected_operation == 5:
                     break
                else:
                     print("Enter a number between 1 to 5 to chose the option. To exit press 5")




                    



                    
                    