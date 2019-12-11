import init 
from init import *

class Intro(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 4
        self.intro = Label(halign="center", valign="middle", font_size=60, text="Hey, What's up? Welcome to Computer Graphics Test Exam.")
        self.intro.text_size = (self.width*6, None)
        self.add_widget(self.intro)
        self.start = Button(text="Start", font_size=30, size_hint=(.1, .1))
        self.start.bind(on_press=self.start_exam)
        self.add_widget(self.start)
        self.about = Button(text="About", font_size=30, size_hint=(.1, .1))
        self.add_widget(self.about)
        self.exit = Button(text="Exit", font_size=30, size_hint=(.1, .1))
        self.exit.bind(on_press=self.exit_exam)
        self.add_widget(self.exit)
    def start_exam(self, instance):
        mcqs.screen_manager.current = "Choice"
    
    def exit_exam(self, _):
        sys.exit(0)

class Choice(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 5
        self.cate_label = Label(text="Category", font_size=30)
        self.add_widget(self.cate_label)
        self.cate = CategoryExam()
        self.add_widget(self.cate)

        self.rand_label = Label(text="Random", font_size=30)
        self.add_widget(self.rand_label)
        self.random = RandomExam()
        self.add_widget(self.random)

        self.exit = Button(text="Exit", font_size=30)
        self.exit.bind(on_press=self.exit_exam)
        self.add_widget(self.exit)

    def exit_exam(self, _):
        sys.exit(0)

class CategoryExam(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.cols = 4
        self.font_size = 15
        #device
        self.device = Button(halign="center", valign="center", text="Device", \
            text_size=(self.width, None))
        self.device.bind(on_press=self.device_exam)
        self.add_widget(self.device)
        #clipping + color
        self.clipping = Button(halign="center", valign="center", text="Clipping", \
            text_size=(self.width, None))
        self.clipping.bind(on_press=self.clipping_exam)
        self.add_widget(self.clipping)
        #curve
        self.curve = Button(halign="center", valign="center", text="Curve", \
            text_size=(self.width, None))
        self.curve.bind(on_press=self.curve_exam)
        self.add_widget(self.curve)
        #hiddensurface
        self.hdS = Button(halign="center", valign="center", text="Hidden Surface", \
            text_size=(self.width, None))
        self.hdS.bind(on_press=self.hd_exam)
        self.add_widget(self.hdS)
        #manhhoa
        self.manhhoa = Button(halign="center", valign="center", text="Mành hóa", \
            text_size=(self.width, None))
        self.manhhoa.bind(on_press=self.manhhoa_exam)
        self.add_widget(self.manhhoa)
        #transformation
        self.trans = Button(halign="center", valign="center", text="Transfomation", \
            text_size=(self.width, None))
        self.trans.bind(on_press=self.trans_exam)
        self.add_widget(self.trans)
        #opengl
        self.opengl = Button(halign="center", valign="center", text="Opengl", \
            text_size=(self.width, None))
        self.opengl.bind(on_press=self.opengl_exam)
        self.add_widget(self.opengl)
        #lighting
        self.lighting = Button(halign="center", valign="center", text="Lighting", \
            text_size=(self.width, None))
        self.lighting.bind(on_press=self.lighting_exam)
        self.add_widget(self.lighting)

    def device_exam(self, _):
        exam = Exam()
        exam.do_exam("thietbi")
        screen = Screen(name="Exam")
        screen.add_widget(exam)
        mcqs.screen_manager.add_widget(screen)
        mcqs.screen_manager.current = "Exam"
    def clipping_exam(self, _):
        exam = Exam()
        exam.do_exam("clipping")
        screen = Screen(name="Clipping_Exam")
        screen.add_widget(exam)
        mcqs.screen_manager.add_widget(screen)
        mcqs.screen_manager.current =  "Clipping_Exam"
    def curve_exam(self, _):
        exam = Exam()
        exam.do_exam("curve")
        screen = Screen(name="Curve_Exam")
        screen.add_widget(exam)
        mcqs.screen_manager.add_widget(screen)
        mcqs.screen_manager.current =  "Curve_Exam"

    def hd_exam(self, _):
        exam = Exam()
        exam.do_exam("hiddensurface")
        screen = Screen(name="Hd_Exam")
        screen.add_widget(exam)
        mcqs.screen_manager.add_widget(screen)
        mcqs.screen_manager.current =  "Hd_Exam"

    def manhhoa_exam(self, _):
        exam = Exam()
        exam.do_exam("manhhoa")
        screen = Screen(name="Mh_Exam")
        screen.add_widget(exam)
        mcqs.screen_manager.add_widget(screen)
        mcqs.screen_manager.current =  "Mh_Exam"

    def trans_exam(self, _):
        exam = Exam()
        exam.do_exam("transformation")
        screen = Screen(name="Trans_Exam")
        screen.add_widget(exam)
        mcqs.screen_manager.add_widget(screen)
        mcqs.screen_manager.current =  "Trans_Exam"

    def opengl_exam(self, _):
        exam = Exam()
        exam.do_exam("opengl")
        screen = Screen(name="Opengl_Exam")
        screen.add_widget(exam)
        mcqs.screen_manager.add_widget(screen)
        mcqs.screen_manager.current =  "Opengl_Exam"

    def lighting_exam(self, _):
        exam = Exam()
        exam.do_exam("lighting")
        screen = Screen(name="Lighting_Exam")
        screen.add_widget(exam)
        mcqs.screen_manager.add_widget(screen)
        mcqs.screen_manager.current =  "Lighting_Exam"

class RandomExam(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.font_size = 30
        #30
        self.thirty = Button(text="30 Ques")
        self.thirty.bind(on_press=self.test_qa)
        self.add_widget(self.thirty)
        #60
        self.sixty = Button(text="60 Ques")
        self.add_widget(self.sixty)
        #All
        self.whole = Button(text="Whole Ques")
        self.add_widget(self.whole)

    def test_qa(self, _):
        mcqs.screen_manager.current = "Exam"

class QuestionAnswer(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.ans_order = []
        self.ques = Label(halign="left", valign="middle", text_size=(self.width*6, None), font_size=30)
        self.size_hint_y = None
        self.answer = GridLayout(cols=2)
        self.add_widget(self.ques)
        self.add_widget(self.answer)
        self.notice = ""
    def update_ques(self, ques="\nThis is a question"):
        self.ques.text = ques

    def update_answer(self, choice=list(), check=False, correct=list()):
        self.answer.clear_widgets()
        if not check:
            self.ans_order =  list(range(len(choice))) 
            random.shuffle(self.ans_order)
        for tmp in self.ans_order:
            if check and choice[tmp] in correct:
                ans = CheckBox(active=True)
                self.answer.add_widget(ans) 
                ans = Label(text='[color=#00ff00]'+choice[tmp]+'[/color]', markup=True)
            elif check and choice[tmp] not in correct:
                ans = CheckBox(active=False)
                self.answer.add_widget(ans)
                ans = Label(text='[color=#ff0000]'+choice[tmp]+'[/color]', markup=True)
            else:
                ans = CheckBox(active=False, id=str(tmp))
                self.answer.add_widget(ans) 
                ans = Label(text=choice[tmp])
            self.answer.add_widget(ans)
        self.answer.add_widget(Label(text=self.notice))


    def check_ans(self):
        pass

class Exam(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 5
        self.correct = []

    def do_exam(self, name="thietbi"):
        self.name = name
        self.iter = 0
        self.max_iter = 0

        ques, ans, correct, length = get_ques(name, self.iter)
        self.correct = correct
        self.nums = length
        self.ans =  ans

        self.title = Label(text=f"Question {self.iter+1}/{self.nums}")
        self.add_widget(self.title)

        self.ques = QuestionAnswer()
        self.ques.update_ques(ques)
        self.ques.update_answer(self.ans)

        self.add_widget(self.ques)
        self.ques.height =  self.ques.height*3

        self.tmp = Label()
        self.add_widget(self.tmp)

        self.bot = GridLayout(cols=2)
        self.check = Button(text="Check")
        self.check.bind(on_press=self.check_ans)
        self.next = Button(text="Next")
        self.next.bind(on_press=self.next_ques)
        self.pre = Button(text="Previous")
        self.pre.bind(on_press=self.pre_ques)
        self.exit = Button(text="Exit")
        self.exit.bind(on_press=self.exit_exam)
        
        self.bot.add_widget(self.pre)
        self.bot.add_widget(self.next)
        self.bot.add_widget(self.check)
        self.bot.add_widget(self.exit)
        self.bot.height = self.bot.height*0.2
        self.add_widget(self.bot)
        
    def check_ans(self, _):
        self.tmp.text = ""
        #print(self.correct)
        self.ques.update_answer(self.ans, True, self.correct)
    
    def exit_exam(self, _):
        sys.exit(0)
    
    def pre_ques(self, _):
        if self.iter <= 0:
            mcqs.screen_manager.current = "Choice"
        else:
            self.iter -= 1
            self.title.text = f"Question {self.iter+1}/{self.nums}"
            ques, ans, correct, _ = get_ques(self.name, self.iter)
            self.correct = correct
            self.ans = ans
            self.ques.update_ques(ques)
            self.ques.update_answer(ans)
            if self.iter < self.max_iter:
                self.ques.update_answer(self.ans, True, self.correct)

    def next_ques(self, _):
        if self.iter > self.nums-2:
            self.iter = 0
            mcqs.screen_manager.current = "Over"
            self.title.text = f"Question {self.iter+1}/{self.nums}"
            ques, ans, correct, _ = get_ques(self.name, self.iter)
            self.correct = correct
            self.ans = ans
            self.ques.update_ques(ques)
            self.ques.update_answer(ans)
        else:
            self.iter += 1
            if self.max_iter < self.iter:
                self.max_iter = self.iter
            self.title.text = f"Question {self.iter+1}/{self.nums}"
            ques, ans, correct, _ = get_ques(self.name, self.iter)
            self.correct = correct
            # print(self.right)
            self.ans = ans
            self.ques.update_ques(ques)
            self.ques.update_answer(ans)
            if self.iter < self.max_iter:
                self.ques.update_answer(self.ans, True, self.correct)
            #mcqs.screen_manager.current = "Over"

class OverExam(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.add_widget(Label(text="Do you wanna play again?"))
        self.bot =  GridLayout(cols=2, size_hint=(.1, .1))
        self.yes = Button(text="Yes")
        self.yes.bind(on_press=self.play_again)
        self.no = Button(text="No")
        self.no.bind(on_press=self.exit)
        self.bot.add_widget(self.yes)
        self.bot.add_widget(self.no)
        self.add_widget(self.bot)
    def play_again(self, _):
        mcqs.screen_manager.current = "Choice"
    def exit(self, _):
        sys.exit(0)


class MCQApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.screen = Screen(name="Intro")
        self.intro = Intro()
        self.screen.add_widget(self.intro)
        self.screen_manager.add_widget(self.screen)
        
        self.screen = Screen(name="Choice")
        self.choice = Choice()
        self.screen.add_widget(self.choice)
        self.screen_manager.add_widget(self.screen)

        self.over = OverExam()
        self.screen = Screen(name="Over")
        self.screen.add_widget(self.over)
        self.screen_manager.add_widget(self.screen)

        return self.screen_manager
if __name__ == "__main__":
    mcqs = MCQApp()
    mcqs.run()