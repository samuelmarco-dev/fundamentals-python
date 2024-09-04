class ConversorTemperatura:
    def __init__(self, temperatura):
        self.temperatura = temperatura

    def celsius_to_fahrenheit(self):
        return (self.temperatura * 9/5) + 32

    def fahrenheit_to_celsius(self):
        return (self.temperatura - 32) * 5/9

    def celsius_to_kelvin(self):
        return self.temperatura + 273.15

    def kelvin_to_celsius(self):
        return self.temperatura - 273.15

    def fahrenheit_to_kelvin(self):
        return (self.temperatura - 32) * 5/9 + 273.15

    def kelvin_to_fahrenheit(self):
        return self.celsius_to_kelvin - 459.67

# Exemplo de uso
temperatura = float(input('Digite a temperatura em graus Celsius: '))
conversor = ConversorTemperatura(temperatura)
print(f'{temperatura}°C é igual a {conversor.celsius_to_fahrenheit()}F')
print(f'{temperatura}°C é igual a {conversor.celsius_to_kelvin()}K')
