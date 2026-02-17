#to_float
def to_float(var):
    try:
        number=float(var)
        return number
    except(ValueError,TypeError):
        return None


#cleaning
def cleaning(var):
    if not isinstance(var,str):
        return None

    cleaned=var.strip()
    cleaned=cleaned.lower()

    return cleaned


#testing

tests=[123,"385","nArgIz",""," HELLO   ","2", "abc"]

float_result=[to_float(x) for x in tests]
cleaning_result=[cleaning (x) for x in tests]

print("Test list: ",tests)
print("Float result: ",float_result)
print("Cleaning result :",cleaning_result)
