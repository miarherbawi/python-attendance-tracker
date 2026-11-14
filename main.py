
print ('Attendance Risk Taker')
report = []
while True:   
    course = input("Enter course name : ")
    total_hours = int(input("Enter total semester hours : "))

    missed_hours=int(input("Enter missed hours so far : "))
    absence_rate = (missed_hours / total_hours)*100
    max_allowed = total_hours*0.20
    remaining = max_allowed - missed_hours
    print(f"Course = {course} | Absence Rate:{absence_rate : .2f}%")

    if missed_hours>max_allowed:
      print("Status: DANGER - Exceeded the 20% absence limit !")
      status = "DANGER"
    elif absence_rate>=20.0:
      print(f"Status: WARNING - Only {remaining:.2f} hours left before failing.")
      status = "WARNING"
    else :
        print(f"Status : SAFE - you still have {remaining:.2f} hours left.")
        status = "SAFE"
        
    report.append(f"{course}: {absence_rate:.1f}% - {status}")
    again = input("\nCheck another course? (yes/no): ").strip().lower()
    if again != "yes" and again != "y":
        print("\n Final Attendance Summary ")
        for item in report:
            print(f"- {item}")
        break
