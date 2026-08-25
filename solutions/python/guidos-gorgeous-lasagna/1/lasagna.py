EXPECTED_BAKE_TIME= 40

def preparation_time_in_minutes(number_of_layers):
    """This function returns the time used in layering"""
    return number_of_layers * 2

def bake_time_remaining(actual_minutes):
    """This function is for calculating the remaining time"""
    return EXPECTED_BAKE_TIME-actual_minutes

def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """This function is used to check the total prepping+elapased bake time """
    return (number_of_layers*2)+elapsed_bake_time

preparation_time_in_minutes(3)
bake_time_remaining(30)
elapsed_time_in_minutes(2,20)