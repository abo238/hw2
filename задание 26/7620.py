file = open("26-154.txt").read()
filelines = file.split('\n')
N = int(filelines[0])  
A = filelines[1:-1] if filelines[-1] == "" else filelines[1:]  

passed = []  
failed = []  

for line in A:
    str_list = list(map(int, line.split()))
    ID, marks = str_list[0], str_list[1:]  
    if 2 in marks:
        k2 = marks.count(2)
        failed.append((ID, k2))
    else:
        avg = sum(marks) / 4
        passed.append((ID, avg))

passed.sort(key=lambda item: (-item[1], item[0]))

failed.sort(key=lambda item: (item[1], item[0]))

top_25_percent = len(passed) // 4
last_id = passed[top_25_percent - 1][0] 

two_twos = next((student[0] for student in failed if student[1] > 2), None)

print(two_twos)
