# http://www.codewars.com/kata/53d16bd82578b1fb5b00128c/

def grader(score):
    if score < 0.6 or score > 1:
        return "F"
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    else:
        return "D"
