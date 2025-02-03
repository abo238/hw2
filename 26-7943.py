students_database = {}

with open('26-159.txt', 'r') as file:
    number = int(file.readline())
    for line in file:
        student_id, task_id = map(int, line.split())
        if student_id not in students_database:
            students_database[student_id] = set()
        students_database[student_id].add(task_id)

max_in_row = 0
max_student_id = None

for student_id, tasks in sorted(students_database.items()):
    sorted_tasks = sorted(tasks)
    local_max_in_row = 1
    in_row = 1

    for i in range(1, len(sorted_tasks)):
        if sorted_tasks[i] == sorted_tasks[i - 1] + 1:
            in_row += 1
        else:
            local_max_in_row = max(local_max_in_row, in_row)
            in_row = 1

    local_max_in_row = max(local_max_in_row, in_row)

    if local_max_in_row > max_in_row or (local_max_in_row == max_in_row and student_id < max_student_id):
        max_in_row = local_max_in_row
        max_student_id = student_id

print(max_student_id, max_in_row)
