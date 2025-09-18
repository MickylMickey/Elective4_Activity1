#User Profile
name = "Jon Mickyl Sumagang"
age = 22
height = 1.72
address = "Bayambang Pangasinan"
student_Status = True

print("=== USER-PROFILE ===")
print("Name: " + name)
print("Age: " + str(age))
print("Height: " + str(height))
print("Address: " + address)
print("Student Status: " + str(student_Status))


#Simple Calculator
print("\n\n=== SIMPLE CALCULATOR ===")
num1 = float(input("Enter Your First Number: "))
num2 = float(input("Enter Your Second Number: "))
sum = num1 + num2

print("\nResults for " + str(num1) + " and " + str(num2))
print("Addition: " + str(sum))
print(f"Subtractio: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} x {num2} = {num1 * num2}")
print(f"Division: {num1} ÷ {num2} = {num1 / num2}")
print(f"Modulus: {num1} % {num2} = {num1 % num2}")
print(f"Exponentiation: {num1} ^ {num2} = {num1 ** num2}")
print(f"Floor Division: {num1} // {num2} = {num1 // num2}")


#String Operations
print("\n\n=== STRING OPERATIONS ===")
user_name = "Alice Johnson"
user_age = 28
user_height = 1.75
user_address = "New York"

print(f"Concatenated greeting: Hello, {user_name} from {user_address}")
print("----------------------------------------------------------------")
print("Name in uppercase: " , user_name.upper())
print("Name in lowercase: " , user_name.lower())
print(f"Name lenght: {len(user_name)} characters")


#DataType Information
print("\n\n=== DATA TYPE INFORMATION ===")
print(f"Type of user_name {type(user_name)}")
print(f"Type of user_age {type(user_age)}")
print(f"Type of user_height {type(user_height)}")
print(f"Type of is_Student {type(student_Status)}")
print(f"Type of addition result {type(sum)}")


#Comparison Operations
print("\n\n=== COMPARISON OPERATIONS ===")
print(f"Is {num1} equal to {num2} = {num1 == num2}")
print(f"Is {num1} greater than {num2} = {num1 > num2}")
print(f"Is {num1} less than or equal to {num2} = {num1 <= num2}")