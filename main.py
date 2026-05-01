import re

class PasswordStrengthMeter:
    def __init__(self, password):
        self.password = password
        self.strength = self.calculate_strength()

    def calculate_strength(self):
        strength = 0

        # 1. Uzunlik
        if len(self.password) >= 8:
            strength += 1

        # 2. Harflar
        if re.search("[a-z]", self.password):
            strength += 1
        if re.search("[A-Z]", self.password):
            strength += 1

        # 3. Raqamlar
        if re.search("[0-9]", self.password):
            strength += 1

        # 4. Simvol
        if re.search("[!@#$%^&*()_+=-{};:'<>,./?]", self.password):
            strength += 1

        return strength

    def get_strength(self):
        if self.strength == 0:
            return "Kam kuchi"
        elif self.strength == 1:
            return "O'rta kuchi"
        elif self.strength == 2:
            return "Yuqori kuchi"
        elif self.strength == 3:
            return "Boshqa darajadagi kuchi"
        elif self.strength == 4:
            return "Yuqori darajadagi kuchi"

# Misol
password = "Aa123!@#"
meter = PasswordStrengthMeter(password)
print(meter.get_strength())
