def calculate_fee(course, marks):
    # normalize the course input
    course = course.strip().lower()
    
    if course == "ai":
        fee = 50000
    elif course == "web":
        fee = 40000
    elif course == "data science":
        fee = 45000
    else:
        return None   # invalid course
    
    # applying discount
    if marks > 90:
        print("Discount applied: 5000")
        fee = fee - 5000
        
    return fee


def main():
    print("Student Fee Calculator")
    
    course = input("Enter course (AI/Web/Data Science): ")
    
    try:
        marks = int(input("Enter marks: "))
        
        if marks < 0 or marks > 100:
            print("Invalid marks. Please enter marks between 0 to 100")
            return
            
    except ValueError:
        print("Invalid input. Marks must be a number")
        return
        
    fee = calculate_fee(course, marks)
    
    if fee is None:
        print("Invalid course selection")
    else:
        print("Final Fee:", fee)


main()