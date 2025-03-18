class Calculator:
    def divide(self, a, b):
        """Divides two numbers with exception handling."""
        try:
            result = a / b
            print(f"Result: {result}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            print("End!")

calc = Calculator()
calc.divide(10, 2)
calc.divide(5, 0) 