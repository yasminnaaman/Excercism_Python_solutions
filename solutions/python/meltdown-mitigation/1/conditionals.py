"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    product_of_temp_and_neutrons_emitted= temperature * neutrons_emitted
    if temperature < 800 and neutrons_emitted > 500 and product_of_temp_and_neutrons_emitted < 500000:
        return True
    return False
def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power= voltage * current
    percentage_value=(generated_power/theoretical_max_power) * 100 
    if percentage_value >= 80.0 :
        return "green"
    elif percentage_value >= 60.0 :
        return "orange"
    elif percentage_value >= 30.0:
        return "red"
    else :
        return "black"

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    product = temperature * neutrons_produced_per_second

    if product < 0.90 * threshold:
        return "LOW"
    elif product <= 1.10 * threshold:
        return "NORMAL"
    else:
        return "DANGER"

    
