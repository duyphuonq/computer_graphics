import json
import os 


def get_ques(name="thietbi", index=0):
    name = "data/"+name+".json"
    with open(name, 'r', encoding='utf-8') as f:
        ques_opt = json.load(f)
    ques = list(ques_opt.keys())[index]
    length = len(list(ques_opt.keys()))
    answer = ques_opt[ques][:-1]
    correct = list(ques_opt[ques][-1])
    return ques, answer, correct, length

if __name__ == "__main__":    
    ques, answer, right, length = get_ques("thietbi", 2)
    print(ques)
    print(answer)
    print(right)
    print(length)