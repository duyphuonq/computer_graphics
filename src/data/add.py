import json
import os 
import string

choice = {"1": "thietbi", "2":"manhhoa", "3":"clipping", "4":"transformation", \
    "5":"hiddensurface", "6":"curve", "7":"lighting", "8":"opengl"}

thietbi = 0
manhhoa = 0
clipping = 0
transformation = 0
hiddensurface = 0
curve = 0
lighting = 0
opengl = 0

for tmp in os.listdir():
    if tmp != "add.py":
        with open(tmp, 'r', encoding='utf-8') as f:
            tmp2 = json.load(f)
        if tmp[:-5] == "thietbi": thietbi = len(tmp2.keys())
        elif tmp[:-5] == "manhhoa": manhhoa = len(tmp2.keys())
        elif tmp[:-5] == "clipping": clipping = len(tmp2.keys())
        elif tmp[:-5] == "transformation": transformation = len(tmp2.keys())
        elif tmp[:-5] == "hiddensurface": hiddensurface = len(tmp2.keys())
        elif tmp[:-5] == "curve": curve = len(tmp2.keys())
        elif tmp[:-5] == "lighting": lighting = len(tmp2.keys())
        elif tmp[:-5] == "opengl": opengl = len(tmp2.keys())

option = input(f"Bạn đang nhập câu hỏi cho loại nào? \n1.Thiết bị({thietbi}/41)\t2.Mành hóa({manhhoa}/31)\n3.Clipping({clipping}/21) \
\t4.Transformation({transformation}/34)\n5.Hidden Suface({hiddensurface}/14)\t6.Curve({curve}/14)\n7.Lighting({lighting}/11)\t8.openGL({opengl}/110)\nLựa chọn: ")

while option not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
    option = input("Bạn chỉ có thể chọn từ 1 đến 8, mời bạn nhập lại: ")        #validate choice 

#Open file, using utf8 
option = choice[option] + ".json"
if option in os.listdir():
    with open(option, 'r', encoding='utf-8') as f:
        ques_opt = json.load(f) 
else: ques_opt = {}
print(f"Bạn đang nhập câu hỏi cho {option}")
#Add to dict
def add_quest(ques, opt):
    ques_opt[ques] = opt

label = ['1', '2', '3', '4', '5', '6']
opt = []        #options 
while True:
    print("#----------------------#")
    ques = input(f"Nhập câu hỏi thứ {len(ques_opt.keys()) + 1}: ")
    ques = ques.translate(str.maketrans('', '', string.punctuation))        #remove string punctuation 
    if ques != '':
        if ques in ques_opt.keys():     #alreađy has this question 
            ans = ques_opt[ques]
            print("+------------------+")
            tmp = input(f"Câu này đã được nhập vào, đáp án cũ là {ans[-1]}, bạn có muốn nhập lại không?(y or n)")
            if tmp.startswith('n'):
                continue
        print("----------------------------------")
        print("Chú ý: Nhập đáp án đúng trước tiên")
        print("----------------------------------")
        multi_opt = input("Có bao nhiêu đáp án đúng? :")
        while not multi_opt.isdigit() :     #validate right options 
            multi_opt = input("Hãy nhập một con số hợp lệ: ")
        multi_opt = int(multi_opt)
        print("Số đáp án đúng: ", multi_opt)
        print("----------------------------------")
        for l in label:
            tmp = input(f"Nhập lựa chọn {l}: ").strip()
            if tmp == '':
                break 
            opt.append(tmp)     #append options 
        while multi_opt > len(opt):     #validate multi_right_options 
            multi_opt = input("Số đáp án đúng không hợp lệ, mời nhập lại: ")
            while not multi_opt.isdigit() :
                multi_opt = input("Hãy nhập một con số hợp lệ: ")
            multi_opt = int(multi_opt)
        opt.append(opt[:multi_opt])     #append right options 
        add_quest(ques, opt)    #add to dict 
        opt = []    #clear options for new loop 
    else: break
    #Write to file, using utf8 
    with open(option, 'w', encoding='utf-8') as f:
        json.dump(ques_opt, f, indent=4, ensure_ascii=False)
    
print("Thank u :*")