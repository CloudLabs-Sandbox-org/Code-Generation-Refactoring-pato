class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero.")
        return a / b

if __name__ == "__main__":
    calc = Calculator()
    print("Calculadora básica en Python")
    while True:
        try:
            op = input("Operación (+, -, *, /) o 'salir': ")
            if op == "salir":
                break
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            if op == "+":
                print("Resultado:", calc.add(a, b))
            elif op == "-":
                print("Resultado:", calc.subtract(a, b))
            elif op == "*":
                print("Resultado:", calc.multiply(a, b))
            elif op == "/":
                print("Resultado:", calc.divide(a, b))
            else:
                print("Operación no válida.")
        except Exception as e:
            print("Error:", e)