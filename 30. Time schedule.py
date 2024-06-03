from datetime import datetime, timedelta

start_date = datetime(2024, 4, 11)
class_time = "19:15"
num_lectures = 32
def generate_classes(start_date, class_time, num_lectures):
    current_date = start_date
    lecture_count = 1
    while lecture_count <= num_lectures:
        if current_date.weekday() == 0 or current_date.weekday() == 3:
            print(f"Lecture {lecture_count:2}: {current_date.strftime('%d %b %Y')} {class_time}")
            lecture_count += 1
        current_date += timedelta(days=1)
generate_classes(start_date, class_time, num_lectures)