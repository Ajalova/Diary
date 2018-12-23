import sys
import math
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from random import shuffle, choice
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    
    def __init__(self):
        self.k={'01.01': 'Петрикор', '02.01': 'Эглет', '03.01': 'Лунула', '04.01': 'Натиформа', '05.01': 'Мондегрин', '06.01': 'Фосфены', '07.01': 'Колливубл', '08.01': 'Пунт', '09.01': 'Феррул', '10.01': 'Лемниската', '11.01': 'Дисания', '12.01': 'Парестезия', '13.01': 'Интерробанг', '14.01': 'Дефенестрация', '15.01': 'Фильтрум', '16.01': 'Флоэмы', '17.01': 'Обелус', '18.01': 'Фриссон', '19.01': 'Колумелла', '20.01': 'Мисофония', '21.01': 'Нёрдл', '22.01': 'Депривация', '23.01': 'Цугцванг', '24.01': 'Палинфразия', '25.01': 'Экивоки', '26.01': 'Фрустрация ', '27.01': 'Ляссе', '28.01': 'Визави', '29.01': 'Эрроризм', '30.01': 'Блоттер', '31.01': 'Хюгге'}
        self.v={'Петрикор': '— запах земли после дождя.', 'Эглет': '— металлический или пластиковый наконечник шнурка, облегчающий вдевание шнурков.', 'Лунула': '— полумесяц у основания ногтя.', 'Натиформа':
         '— природные образования, обычно деревья, скалы, камни, которые напоминают женские формы.', 'Мондегрин': '— непонятные слова в песнях.', 'Фосфены': '— пятна света, которые вы видите,когда закрываете глаза и давите пальцами на глазные яблоки.',
         'Колливубл': '— урчание в животе от голода.', 'Пунт': '— нижняя часть бутылки вина.', 'Феррул': '— металлическая часть на конце карандаша с ластиком.', 'Лемниската': '— знак бесконечности.'
         , 'Дисания': '— это состояние, при котором тяжело с утра встать с постели.', 'Парестезия': ' — чувство покалывания, онемения и мурашек в конечностях.', 'Интерробанг':
         '— когда вы используете вопросительный и восклицательный знаки одновременно.', 'Дефенестрация': ' — акт выбрасывания кого-либо из окна.', 'Фильтрум': '— вертикальное углубление между перегородкой носа и верхней губой.', 'Флоэмы': '— длинные волокна на кожуре от банана.', 'Обелус': '— знак деления.', 'Фриссон': ' — озноб во время прослушивания музыки, которая вам нравится.', 'Колумелла': '— пространство между ноздрями.', 'Мисофония': '— неконтролируемая ярость в отношении человека, который громко ест или даже дышит во время трапезы с вами.', 'Нёрдл': '— очень маленький кусочек зубной пасты, который не хочет отделиться от тюбика.', 'Депривация': '— ощущение недостаточности удовлетворения своих потребностей.', 'Цугцванг': '— вынужденный ход в шахматной партии, ухудшающий положение игрока, сделавшего его. В широком смысле, ситуация, при которой любые действия только ухудшают положение дел.', 'Палинфразия': '— патологически частое повторение определенных слов или фраз в речи.', 'Экивоки': '— двусмысленные намеки, увертки.', 'Фрустрация': ' — период полного разочарования в жизни.', 'Ляссе': '— узкая лента в книге, используемая в качестве закладки.', 'Визави': '— тот, кто находится напротив, лицом к лицу с кем-нибудь.',
         'Эрроризм': '— коллекционирование монет с ошибками или браком.', 'Блоттер': '— бумажная полоска-тестер для знакомства с парфюмерией в магазине.', 'Хюгге': '— наслаждение простыми радостями жизни, домашним уютом.'}
        super().__init__()
        uic.loadUi('666.ui',self)
        self.knpk.clicked.connect(self.hello)
        #кнопка поиска слова
        self.clndr.clicked.connect(self.showDate8)
        #выбор даты в календаре
        self.dal.clicked.connect(self.daaa)
        #следующее слово в тесте
    def daaa(self):
        self.flag=False
        self.l33.setText('')
        self.slovo=choice(list((self.v).keys()) )
        self.l2.setText("Что такое, {}?".format(self.slovo))
        #вбор и вывод тезиса
        self.a=choice(list((self.v).values()) )
        self.b=choice(list((self.v).values()) )
        self.c=choice(list((self.v).values()) )
        #выбор неверных вариантов овета 
        self.abc=[ self.c , self.b , self.a ,self.v[self.slovo]]
        shuffle(self.abc)
        self.s1=(self.abc[0])
        self.rb1.setText(self.s1)
        self.s2=self.abc[1]
        self.rb2.setText(self.s2)
        self.s3=self.abc[2]
        self.rb3.setText(self.s3)
        self.s4=self.abc[3]
        self.rb4.setText(self.s4)
        #случайное распределение вариантов ответа по радио-кнопкам
        self.rb1.clicked.connect(self.a1)
        self.rb2.clicked.connect(self.a2)
        self.rb3.clicked.connect(self.a3)
        self.rb4.clicked.connect(self.a4)
        self.otv.clicked.connect(self.answer)
        
    def a1(self):
        if self.s1==self.v[self.slovo]:
            self.flag=True
        #если ответ правильный поднять влажок    
        else:
            self.lose='1'
        #если же нет, то запсаться в луз
    def a2(self):
        if self.s2==self.v[self.slovo]:
            self.flag=True
        else:
            self.lose='2'
    def a3(self):
        if self.s3==self.v[self.slovo]:
            self.flag=True
        else:
            self.lose='3'        
    def a4(self):
        if self.s4==self.v[self.slovo]:
            self.flag=True
        else:
            self.lose='4'
    def answer(self):
        #строка проверки
        if self.flag==True:
            self.l33.setText('Moлодец!!!')
        else:
           self.l33.setText('попробуй ещё раз')
    #def ansver_choices(self, h, f):
        
       # return (self.abc[f])
    def showDate8(self):
        self.dat=str(self.clndr.selectedDate())
        #получаем дату в формате"PyQt5.QtCore.QDate(ГОД, МЕСЯЦ, ДЕНЬ)"
        #преобразование этой херни в дату из юленого словаря формата"ДЕНЬ.МЕСЯЦ"
        self.a=list(self.dat)
        self.b=[]
        for i in range(0,len(self.a)-1):
            if (i-24)>0 and self.a[i]!=' ' and self.a[i]!=')':
                self.b.append(self.a[i])
        if len(self.b)==4:
            if self.b[2]==',':
                self.b.insert(3,'0')
            else:
                self.b.insert(0,'0')
        if len(self.b)==3:
            self.b.insert(2,'0')
            self.b.insert(0,'0')
        del self.b[2]
        self.b.insert(2,'.')
        self.b=''.join(self.b)
        self.b=self.b.split('.')
        self.b.reverse()
        self.b='.'.join(self.b)
        #после этого пса с рогами вывод значения слова через два словаря
        self.ll.setText(self.k[self.b]+self.v[self.k[self.b]])
        
    def hello(self):
        self.name = self.input2.text()
        if self.name in self.v:
            self.l3.setText(self.name+self.v[self.name])
        else:
            self.l3.setText('Я ХЗ. ЗАГУГЛИ.')

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
