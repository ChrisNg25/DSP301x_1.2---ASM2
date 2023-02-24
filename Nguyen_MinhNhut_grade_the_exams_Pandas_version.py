import pandas as pd 
import numpy as np


def open_read_file():
  filename = input('Nhập tên file: ')
  try:
    with open(filename,'r') as f:
      return f.read()
  except:
    print ("File không tồn tại")
    return 'Vui lòng thử lại sau'

# Điểm của từng học sinh 
class_test = open_read_file() # class_test là bài kiểm tra của từng lớp
# in từng dòng đáp án của học sinh 
student_test = class_test.split('\n')
# tạo list_student với mỗi học sinh là một phần tử của list 
list_student = []
for line in student_test:
  if line: # loại bỏ các dòng rỗng nếu có 
     list_student.append(line)
# Xác định số lượng bài nộp của sinh viên
print('Số lượng bài nộp của sinh viên: ', len(list_student))
#print(list_student)

# tạo list student, dữ liệu dạng student = [[MSV1, ĐA1, ĐA2,...],[MSV2, ĐA1, ĐA2,...],[....] ......]
student = []
for lne in range(len(list_student)):
  a = list_student[lne].split(',')
  student.append(a)

# Kiểm tra tính hợp lệ trong bài thi của từng sinh viên 
valid_test = 0  # valid_test: Đếm số bài hợp lệ
invalid_test = 0 # invalid_test: Đếm số bài không hợp lệ 
valid_student = [] #tạo valid_student,  trả về dữ liệu valid_student = [[MSV1, ĐA1, ĐA2,...],[MSV2, ĐA1, ĐA2,...],[....] ......]
for b in range(len(student)):
  if len(student[b])== 26 and student[b][0][0] =='N' and len(student[b][0]) == 9:
    valid_student.append(student[b])
    valid_test += 1 
  else:
    invalid_test += 1 
print('Số bài thi hợp lệ là: ', valid_test)
print('Số bài thi không hợp lệ là: ', invalid_test)
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer =[]
for c in answer_key.split(','):
  answer.append(c)
# Tính điểm các bài thi hợp lệ và trả về 1 dict với keys là mã sinh viên và values là điểm số của sinh viên
for c in range(len(valid_student)):
  score = 0 # điểm số 
  for d in range(len(answer)):
    if valid_student[c][d+1] == "":
      score += 0
    elif valid_student[c][d+1] == answer[d]:
      score += 4
    else:
      score += -1
  valid_student[c].append(score)

# Chuyển list valid_student về DataFrame 
student_df = pd.DataFrame(valid_student)
print('Điểm số lớn nhất là: ',np.max(student_df[26])) 
print('Điểm số nhỏ nhất là: ',np.min(student_df[26]))
print('Miền giá trị của điểm: ', np.max(student_df[26]) - np.min(student_df[26]))
print('Điểm trung bình là: ', round(sum(student_df[26])/len(student_df[26]),3))
# Sắp xếp các giá trị của cột column_name theo thứ tự tăng dần
sorted_column = student_df[26].sort_values()
# Tìm điểm trung vị
n = len(sorted_column)
if n % 2 == 0:
    median = (sorted_column.iloc[n//2] + sorted_column.iloc[n//2 + 1]) / 2
else:
    median = sorted_column.iloc[n//2]

print("Điểm trung vị là:", median)
dict_skip = {}
dict_wrong = {}
for e in range(len(answer)): # e chạy từ 0 đến 24
  count_skip = 0
  count_wrong = 0
  for f in range(len(valid_student)):
    if valid_student [f][e+1] == '':
      count_skip += 1 
    elif valid_student [f][e+1] != answer[e]:
      count_wrong += 1
  dict_skip.update({e +1 : count_skip})
  dict_wrong.update({e + 1 : count_wrong})
dict_wrong

# tạo hàm get_question để tìm ra câu hỏi bị bỏ qua và sai nhiều nhất 
def get_question (my_dict, value):
  key = []
  for k,v in my_dict.items():
    if v == value:
      key.append(k)
  return key

# Câu bị bỏ qua nhiều nhất 
most_skip = get_question(dict_skip, max(dict_skip.values()))
print ('Câu sinh viên bỏ qua nhiều nhất: ',most_skip, '-', max(dict_skip.values()), '-',round(max(dict_skip.values())/len(valid_student),3))

# Câu sai nhiều nhất 
most_wrong = get_question(dict_wrong, max(dict_wrong.values()))
print ('Câu sinh viên sai nhiều nhất: ',most_wrong, '-', max(dict_wrong.values()), '-',round(max(dict_wrong.values())/len(valid_student),3))
filename_output = input(" Nhập tên file cần xuất: ")
with open(filename_output,'w') as file:
    file.write(' Kết quả bài thi\n')
    for line in range(len(student_df)):
        file.write(str(student_df[0][line]))
        file.write(',')
        file.write(str(student_df[26][line]) )
        file.write('\n')

