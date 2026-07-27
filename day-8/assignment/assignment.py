'''                                              section = a
Q	Answer
1) try
2) except
3) Number-type errors (ValueError)
4) All exceptions
5) All exceptions
6) No exception occurs
7) Always
8) Throw
9) Context manager
10) "r"
11) Reading
12) Truncate and write
13) Append at end
14) str
15) list of lines
16) "w" or "a"
17) Log file reading
18) Handle missing config file
19) Automatically close file
20) Handle missing file


                                                     SECTION = B
                                                    QUESTION = 1
try

Contains the code that may cause an error.

except

Runs if an error occurs.

else

Runs only when no error occurs.

finally

Runs every time, whether there is an error or not.

                                                     (b)
try:
    
except:
    
else:

finally:
                                                      (C)
Real World Use
Config Loader
Log Processor
Banking Software
Student Management System
                                             QUESTION = 2
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")

    print("Eligible")

check_age(15)
                                              QUESTION =3
Mode	Meaning
r=Read
w=Write (overwrite)
a=Append
r+=Read & Write
rb=Read Binary
wb=Write Binary 
                                               QUESTION = 4
CONTEXT MANGER = It automatically closes the file. 
with open("data.txt", "r") as f:
    lines = f.readlines()

print(lines)
                                               QUESTION = 5
try:
    with open("log.txt", "r") as f:
        data = f.read()

except FileNotFoundError:
    print("Log file missing")

except Exception as e:
    print("Error:", e)

else:
    print("Log processed successfully")

finally:
    print("Cleanup completed")

                                              SECTION =C
                                             QUESTION =1
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0

print(safe_divide(10, 0))
print(safe_divide(10, 2))

                                             QUESTION =2
try:
    with open("data.txt", "r") as f:
        print(f.read())

except FileNotFoundError:
    print("File not found")
                                            QUESTION =3
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())
                                             QUESTION =4
data = "Hello, world!"

with open("output.txt", "w") as f:
    f.write(data)

with open("output.txt", "a") as f:
    f.write("\nLine 2")
                                           QUESTION=5
Rahul,85
Priya,90
Amit,78
with open("students.csv", "r") as f:
    for line in f:
        name, marks = line.strip().split(",")
        print(name, marks)
                                             QUESTION =6
with open("scores.txt", "r") as f:
    for line in f:
        try:
            score = int(line.strip())
            print(score)

        except ValueError:
            print("Invalid line:", line.strip())
                                               QUESTION =7
def log_error(error_msg):
    with open("error.log", "a") as f:
        f.write(error_msg + "\n")

try:
    num = 10 / 0

except Exception as e:
    log_error(str(e))
    print("Error Logged")

                                              SECTION = D
                                            QUESTION = 1
def load_config(filename):
    config = {}

    try:
        with open(filename, "r") as f:
            for line in f:
                key, value = line.strip().split("=")
                config[key] = value

    except FileNotFoundError:
        print("Config file not found")

    return config


data = load_config("config.txt")
print(data)
                                          QUESTION = 2

def log_error(msg):
    with open("import_errors.log", "a") as f:
        f.write(msg + "\n")


def import_results(filename):
    students = []

    with open(filename, "r") as f:
        for line in f:
            name, value = line.strip().split(",")

            try:
                marks = int(value)
                students.append({"name": name, "marks": marks})

            except ValueError:
                log_error(f"Invalid marks for {name}: {value}")

    return students


data = import_results("results.csv")

print("Valid Students")

for student in data:
    print(student)

print("Total Valid:", len(data))                                          


































































































































































































































































































































































































































































































































































































































































































'''