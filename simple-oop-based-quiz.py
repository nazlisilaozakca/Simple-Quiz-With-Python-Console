# Questions classı

class Question:
    def __init__(self,text,choices,answer): #constructor metod tanımlaması
        self.text = text
        self.choices = choices
        self.answer = answer
    
    #cevapları kontrol edelim.
    def check(self, answer):
        return self.answer == answer #true ya da false değer döndürür


#Q  Quiz classı

class Quiz:
    def __init__(self, questionList):
        self.questionList = questionList
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self): # soruyu indexe göre alma
        return self.questionList[self.questionIndex]
    
    def displayQuestion(self): #soruları  görüntüleme
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1 }: {question.text}")

        for q in question.choices: #cevapları görüntüleme
            print("- "+q)

        answers = input("cevap : ") # kullanıcıdan cevabı alma
        self.guess(answers)
        self.loadQuestion()


    def guess(self, answers):
        question = self.getQuestion()
        if question.check(answers):
            self.score +=1
        self.questionIndex +=1
        

    def loadQuestion(self):
        if len(self.questionList) == self.questionIndex:
            self.showScore()
        else: 
            self.displayProgress()
            self.displayQuestion()
            

    def showScore(self):
        print("score: ",self.score)
    
    def displayProgress(self):
        total_question = len(self.questionList)
        question_nmber = self.questionIndex +1

        if question_nmber > total_question:
            print("Quiz sonlandı")
        else:
            print(f"{total_question} adet sorudan {question_nmber}. gösterilmektedir.")
question1=Question("Titanik 15 Nisan'da Southampton'dan ilk yolculuğunda Atlantik Okyanusu'nda hangi yıl battı?",['1912','1913','1914'],'1912')
question2=Question("1958'de yapılan ve piyasaya sürülen ilk Carry On filminin adı nedir?",['Güneşi görelim','Kelebekler','Çavuş Taşıyın'],'Çavuş Taşıyın')
question3=Question("Güney Kore'deki en büyük teknoloji şirketinin adı nedir?",['Nokia','Huawei','Samsung'],'Samsung')
question4=Question("Portekiz'in başkenti nedir?",['Lizbon','Amsterdam','Bükreş'],'Lizbon')
question5=Question("İnsan vücudu her gün kaç nefes alır?",['15,000','20,000','25,000'],'20,000')

questionList=[question1,question2,question3,question4,question5]
#quizden bir onje üretiyoruz
quiz=Quiz(questionList)
#question listin içinden bir indexe ulaşmaya çalışıyoruz

quiz.loadQuestion()