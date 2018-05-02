tempInput = float(input("Please enter a temperature: "))
convInput = input("Is this temperature in fahrenheit or celsius? ")

if convInput == "fahrenheit":
    print(f"{tempInput} degrees Fahrenheit is {(tempInput - 32) * .5556} degrees Celsius")
elif convInput == "celsius":
    print(f"{tempInput} degrees Celsius is {(tempInput * 1.8) + 32} degrees Fahrenheit")
else:
    print("Please enter a valid temperature")
