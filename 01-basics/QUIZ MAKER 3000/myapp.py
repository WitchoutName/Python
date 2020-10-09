import random
import json
from math import *

alpha = []
alpha[:0] = "abcdefghijklmnopqrstuvwxyz"


class Question:
    def __init__(self, task, answers, right_answer):
        self.task = task
        self.answers = answers
        self. right_answer = right_answer


class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions


class QuizInstance(Quiz):
    correct = 0
    active_question = 0

    def __init__(self, quiz):
        self.name = quiz.name
        self.questions = quiz.questions

    def print_question(self):
        print(f"{self.active_question + 1}) {self.questions[self.active_question].task}")
        for x, answer in enumerate(self.questions[self.active_question].answers):
            print(f"  {alpha[x]}) {answer}")
            count = x
        inp = input()
        if inp in alpha[0:count+1]:
            if self.questions[self.active_question].answers[alpha[0:count+1].index(inp)] == self.questions[self.active_question].right_answer:
                self.correct += 1
            self.active_question += 1
        if self.active_question != len(self.questions):
            self.print_question()
        else:
            self.print_results()

    def print_results(self):
        print("---------------------")
        print(f"Měli jste {self.correct}/{len(self.questions)} správně!")
        print(f"To je {self.percentage()}%")
        inp = input("Zmáčktěte ENTER pro vrácení se\n\n")

    def percentage(self):
        return self.correct / len(self.questions) * 100 if len(self.questions) > 0 else 0


class QuizMaker:
    quizzes = []
    settings_manager = None

    def __init__(self, file_name):
        self.file_name = file_name

    def print_main_menu(self):
        print("QUIZ MAKER 3000")
        print("  a) Udělejte si kvíz")
        print("  b) Upravte si kvíz")
        print("  c) Nastavení")
        inp = input()
        if inp == "a":
            self.print_quizzes()
            self.print_main_menu()
        elif inp == "b":
            self.print_edit_menu()
        elif inp == "c":
            self.print_settings()
            self.print_main_menu()
        else:
            self.print_main_menu()

    def print_quizzes(self):
        print("Dostupné kvízy:")
        count = 0
        for x, quiz in enumerate(self.quizzes):
            print(f"  {alpha[x]}) {quiz.name}")
            count = x
        print(f"\nPočet dostupných kvízů je {len(self.quizzes)}")
        print("\"ESC\" pro vrácení se")
        inp = input()
        if inp in alpha[0:count+1]:
            self.active_quiz = QuizInstance(self.quizzes[alpha.index(inp)])
            if self.settings_manager.settings.shuffle_questions:
                random.shuffle(self.active_quiz.questions)
            if self.settings_manager.settings.shuffle_answers:
                for question in self.active_quiz.questions:
                    random.shuffle(self.active_quiz.questions[self.active_quiz.questions.index(question)].answers)
            if self.settings_manager.settings.only_percentage_of_random_questions_per_quiz:
                new_questions = []
                print(len(self.active_quiz.questions), int(floor((100 - self.settings_manager.settings.the_percentage) * len(self.active_quiz.questions) / 100)))
                for index in range(0, len(self.active_quiz.questions) - int(floor((100 - self.settings_manager.settings.the_percentage) * len(self.active_quiz.questions) / 100))):
                    new_questions.append(self.active_quiz.questions[index])
                self.active_quiz.questions = new_questions
            self.active_quiz.print_question()
        elif inp.upper() == "ESC":
            self.print_main_menu()
        else:
            self.print_quizzes()

    def print_edit_menu(self):
        print("Dostupné akce:")
        print("  a) Vytvořte si nový kvíz")
        print("  b) Upravte si kvíz")
        print("  c) Smažte si kvíz")
        print("\n\"ESC\" pro vrácení se")
        inp = input()
        if inp == "a":
            self.create_new_quiz()
        elif inp == "b":
            self.edit_quiz_list()
        elif inp == "c":
            self.delete_quiz()
        elif inp.upper() == "ESC":
            self.print_main_menu()

    def create_new_quiz(self):
        new_quiz = Quiz("",[])
        new_quiz.name = input("Zadejte jméno nového kvízu: \n")
        inp = "a"
        is_first = True
        while inp != "n":
            if not is_first:
                inp = input(f"Chcete přidat {len(new_quiz.questions)+1}. otázku? (a/n)\n")
            if inp.lower() == "a":
                new_quiz.questions.append(self.create_new_question(len(new_quiz.questions)))
                is_first = False
        self.quizzes.append(new_quiz)
        print(f"Kvíz {new_quiz.name} byl úspěšně vystvořen!")
        self.save_quizzes()
        self.print_main_menu()

    def create_new_question(self, quiz_question_count):
        new_question = Question("", [], "")
        new_question.task = input(f"Zadejte otázku {quiz_question_count+1}. otázky:\n")
        new_question.right_answer = input("Zadejte správnou odpověď na zadanou otázku:\n")
        inp = ""
        is_first = True
        print("Přidejte další možnosti!")
        while inp.lower() != "n":
            if not is_first:
                inp = input("Chcete přidat další možnost? (a/n)\n")
            if inp.lower() == "a" or is_first:
                new_question.answers.append(self.create_new_answer(len(new_question.answers), 2))
                is_first = False
        new_question.answers.insert(random.randrange(0, len(new_question.answers)), new_question.right_answer)
        return new_question

    def create_new_answer(self, question_answer_count, increment):
        inp = input(f"Zadejte {question_answer_count + increment}. možnost: ")
        return inp

    def edit_quiz_list(self):
        print("Kvízy k upravení:")
        count = 0
        for x, quiz in enumerate(self.quizzes):
            print(f"  {alpha[x]}) {quiz.name}")
            count = x
        print(f"\nPočet dostupných kvízů je {len(self.quizzes)}")
        print("\"ESC\" pro vrácení se")
        inp = input()
        if inp in alpha[0:count + 1]:
            self.print_edit_quiz(self.quizzes[alpha.index(inp)])
            self.save_quizzes()
            self.print_edit_quiz(self.quizzes[alpha.index(inp)])
        elif inp.upper() == "ESC":
            self.print_main_menu()
        else:
            self.print_edit_quiz(quiz)

    def print_edit_quiz(self, quiz):
        print("Co chcete upravit?")
        print("  a) Název")
        print("  b) Otázky")
        print("\n\"ESC\" pro vrácení se")
        inp = input()
        if inp == "a":
            self.print_edit_name(quiz)
        elif inp == "b":
            self.print_edit_question_menu(quiz)
        elif inp.upper() == "ESC":
            self.print_main_menu()

    def print_edit_name(self, quiz):
        self.quizzes[self.quizzes.index(quiz)].name = input("Zadejte nový název kvízu: ")
        print(f"Název vkízu byl zněněn na \"{self.quizzes[self.quizzes.index(quiz)].name}\"")


    def print_edit_question_menu(self, quiz):
        print("Dostupné akce:")
        print("  a) Vytvořte si novou otázku")
        print("  b) Upravte si otázku")
        print("  c) Smažte si otázku")
        print("  d) Promíchejte si otázky")
        print("\n\"ESC\" pro vrácení se")
        inp = input()
        if inp == "a":
            self.quizzes[self.quizzes.index(quiz)].questions.append(self.create_new_question(len(quiz.questions)))
            self.save_quizzes()
            self.print_edit_question_menu(quiz)
        elif inp == "b":
            self.print_edit_questions_list(quiz)
        elif inp == "c":
            self.delete_question(quiz)
        elif inp == "d":
            random.shuffle(self.quizzes[self.quizzes.index(quiz)].questions)
            self.save_quizzes()
            self.print_edit_question_menu(quiz)
        elif inp.upper() == "ESC":
            self.print_edit_quiz(quiz)
        else:
            self.print_edit_question_menu(quiz)

    def print_edit_questions_list(self, quiz):
        print("Otázky k upravení:")
        count = 0
        for x, question in enumerate(quiz.questions):
            print(f"  {alpha[x]}) {question.task}")
            count = x
        print("\"ESC\" pro vrácení se")
        inp = input()
        if inp in alpha[0:count + 1]:
            self.print_edit_question(quiz, quiz.questions[alpha.index(inp)])
        elif inp.upper() == "ESC":
            self.print_edit_question_menu(quiz)
        else:
            self.print_edit_questions_list(quiz)

    def print_edit_question(self, quiz, question):
        print("Co chcete upravit?")
        print("  a) Otázka otázky")
        print("  b) Správná odpověď")
        print("  c) Další odpovědi")
        print("\n\"ESC\" pro vrácení se")
        inp = input()
        if inp == "a":
            self.print_edit_question_task(quiz, question)
            self.save_quizzes()
            self.print_edit_question(quiz, question)
        elif inp == "b":
            self.print_edit_question_right_answer(quiz, question)
            self.save_quizzes()
            self.print_edit_question(quiz, question)
        elif inp == "c":
            self.print_edit_answers_menu(quiz, question)
        elif inp.upper() == "ESC":
            self.print_edit_questions_list(quiz)

    def print_edit_question_task(self, quiz, question):
        inp = input("Zadejte novou otázku otázky: ")
        self.quizzes[self.quizzes.index(quiz)].questions[quiz.questions.index(question)].task = inp
        if self.quizzes[self.quizzes.index(quiz)].questions[quiz.questions.index(question)].task == inp:
            print(f"Otázka otázky úspěšně změněna na \"{inp}\"\n")

    def print_edit_question_right_answer(self, quiz, question):
        inp = input("Zadejte novou správnou odpověď otázky: ")
        old_answer = self.quizzes[self.quizzes.index(quiz)].questions[quiz.questions.index(question)].right_answer
        self.quizzes[self.quizzes.index(quiz)].questions[quiz.questions.index(question)].right_answer = inp
        self.quizzes[self.quizzes.index(quiz)].questions[quiz.questions.index(question)].answers[question.answers.index(old_answer)] = inp
        if self.quizzes[self.quizzes.index(quiz)].questions[quiz.questions.index(question)].right_answer == inp:
            print(f"Správná odpověď otázky úspěšně změněna na \"{inp}\"\n")

    def print_edit_answers_menu(self, quiz, question):
        print("Dostupné akce:")
        print("  a) Vytvořte si novou odpověď")
        print("  b) Upravte si odpověď")
        print("  c) Smažte si odpověď")
        print("  d) Promíchejte si odpovědi")
        print("\n\"ESC\" pro vrácení se")
        inp = input()
        if inp == "a":
            self.quizzes[self.quizzes.index(quiz)].questions[quiz.questions.index(question)].answers.append(self.create_new_answer(len(question.answers), 1))
            self.save_quizzes()
            self.print_edit_answers_menu(quiz, question)
        elif inp == "b":
            self.print_edit_answers_list(quiz, question)
        elif inp == "c":
            self.delete_answer(quiz, question)
        elif inp == "d":
            random.shuffle(self.quizzes[self.quizzes.index(quiz)].questions[quiz.questions.index(question)].answers)
            self.save_quizzes()
            self.print_edit_answers_menu(quiz, question)
        elif inp.upper() == "ESC":
            self.print_edit_question(quiz, question)
        else:
            self.print_edit_answers_menu(quiz, question)

    def print_edit_answers_list(self, quiz, question):
        print("Odpovědi k upravení:")
        count = 0
        for x, answer in enumerate(question.answers):
            print(f"  {alpha[x]}) {answer}")
            count = x
        print("\"ESC\" pro vrácení se")
        inp = input()
        if inp in alpha[0:count + 1]:
            self.print_edit_answer_content(quiz, question, question.answers[alpha.index(inp)])
            self.save_quizzes()
            self.print_edit_answers_list(quiz, question)
        elif inp.upper() == "ESC":
            self.print_edit_answers_menu(quiz, question)
        else:
            self.print_edit_answers_list(quiz, question)

    def print_edit_answer_content(self, quiz, question, answer):
        inp = input("Zadejte nový kontent odpovědi: ")
        old_answer = self.quizzes[self.quizzes.index(quiz)].questions[quiz.questions.index(question)].answers[question.answers.index(answer)]
        old_right_answer = self.quizzes[self.quizzes.index(quiz)].questions[quiz.questions.index(question)].right_answer
        if old_answer == old_right_answer:
            self.quizzes[self.quizzes.index(quiz)].questions[quiz.questions.index(question)].right_answer = inp
        self.quizzes[self.quizzes.index(quiz)].questions[quiz.questions.index(question)].answers[question.answers.index(answer)] = inp
        if self.quizzes[self.quizzes.index(quiz)].questions[quiz.questions.index(question)].answers[question.answers.index(inp)] == inp:
            print(f"Nový kontent odpovědi změněn na \"{inp}\"\n")

    def delete_answer(self, quiz, question):
        print("Odovědi ke smazání:")
        count = 0
        for x, answer in enumerate(question.answers):
            print(f"  {alpha[x]}) {answer}")
            count = x
        print("\"ESC\" pro vrácení se")
        inp = input()
        if inp in alpha[0:count + 1]:
            if question.answers[alpha.index(inp)] != question.right_answer:
                self.quizzes[self.quizzes.index(quiz)].questions[quiz.questions.index(question)].answers.remove(question.answers[alpha.index(inp)])
                self.save_quizzes()
            else:
                print("ERROR: Snažíte se smazat správnou odpověď na otázku!\n")
            self.delete_answer(quiz, question)
        elif inp.upper() == "ESC":
            self.print_edit_answers_menu(quiz, question)
        else:
            self.delete_answer(quiz, question)

    def delete_question(self, quiz):
        print("Otázky ke smazání:")
        count = 0
        for x, question in enumerate(quiz.questions):
            print(f"  {alpha[x]}) {question.task}")
            count = x
        print("\"ESC\" pro vrácení se")
        inp = input()
        if inp in alpha[0:count + 1]:
            self.quizzes[self.quizzes.index(quiz)].questions.remove(quiz.questions[alpha.index(inp)])
            self.save_quizzes()
            self.delete_question(quiz)
        elif inp.upper() == "ESC":
            self.print_edit_question_menu(quiz)
        else:
            self.delete_question(quiz)

    def delete_quiz(self):
        print("Kvízy ke smazání:")
        count = 0
        for x, quiz in enumerate(self.quizzes):
            print(f"  {alpha[x]}) {quiz.name}")
            count = x
        print(f"\nPočet dostupných kvízů je {len(self.quizzes)}")
        print("\"ESC\" pro vrácení se")
        inp = input()
        if inp in alpha[0:count + 1]:
            self.quizzes.remove(self.quizzes[alpha.index(inp)])
            self.save_quizzes()
            self.delete_quiz()
        elif inp.upper() == "ESC":
            self.print_edit_menu()
        else:
            self.delete_quiz()

    def print_settings(self):
        self.settings_manager.print_table()
        inp = input("Změnit nastavení? (ano/ne)\n")
        if inp.lower() == "ano":
            self.settings_manager.change_settings()
            self.settings_manager.print_table()
            input("Zmáčkněte \"ENTER\" pro vrácení se...\n\n")
        elif inp.lower() == "ne":
            self.print_main_menu()
        else:
            self.print_settings()

    def load_quizzes(self):
        try:
            with open(self.file_name) as file:
                quizzes = json.load(file)
                for quiz in quizzes:
                    new_quiz = Quiz(**quiz)
                    for question in new_quiz.questions:
                        if type(new_quiz.questions[0]) is not Question:
                            new_quiz.questions.append(Question(**new_quiz.questions[0]))
                            new_quiz.questions.pop(0)
                    self.quizzes.append(new_quiz)
                file.close()
        except FileNotFoundError:
            raise SyntaxError('ERROR: File could not be found')

    def save_quizzes(self):
        try:
            quizzes = []
            for quiz in self.quizzes:
                new_quiz = Quiz("", [])
                new_quiz.name = quiz.name
                for question in quiz.questions:
                    new_quiz.questions.append(question.__dict__)
                quizzes.append(new_quiz.__dict__)
            with open(self.file_name, "w") as file:
                json.dump(quizzes, file)
                file.close()
        except FileNotFoundError:
            raise SyntaxError('ERROR: File could not be found')


class Settings:
    shuffle_questions = False
    shuffle_answers = False
    only_percentage_of_random_questions_per_quiz = False
    the_percentage = 100

    def to_dictionary(self):
        return {"shuffle_questions": self.shuffle_questions,
                "shuffle_answers": self.shuffle_answers,
                "only_percentage_of_random_questions_per_quiz": self.only_percentage_of_random_questions_per_quiz,
                "the_percentage": self.the_percentage
                }


class ImportedSettings(Settings):
    def __init__(self, settings):
        self.shuffle_questions = settings["shuffle_questions"]
        self.shuffle_answers = settings["shuffle_answers"]
        self.only_percentage_of_random_questions_per_quiz = settings["only_percentage_of_random_questions_per_quiz"]
        self.the_percentage = settings["the_percentage"]


class SettingsManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.settings = Settings()

    def print_table(self):
        width = 55

        self.print_line("", "-", width)
        self.print_line("m", ["|", "Nastavení"], width)
        self.print_line("fws", ["|", "="], width)
        self.print_line("l", ["|", f"Promíchat otázky při generování kvízu: {'Ano' if self.settings.shuffle_questions else 'Ne'}"], width)
        self.print_line("fws", ["|", "-"], width)
        self.print_line("l", ["|", f"Promíchat odpovědi při generování kvízu: {'Ano' if self.settings.shuffle_answers else 'Ne'}"], width)
        self.print_line("fws", ["|", "-"], width)
        self.print_line("l", ["|", f"Podat pouze určité procento otázek"], width)
        self.print_line("l", ["|", f"při generování kvízu: {'Ano' if self.settings.only_percentage_of_random_questions_per_quiz else 'Ne'}"], width)
        if self.settings.only_percentage_of_random_questions_per_quiz:
            self.print_line("fws", ["|", "-"], width)
            self.print_line("l", ["|", f"Procento podaných otázek: {self.settings.the_percentage}%"], width)
        self.print_line("fws", ["|", "="], width)
        self.print_line("", "-", width)

    def print_line(self, alignment, strings, width):
        if type(strings) == list:
            strings.append(strings[0])
            width_wf_strings = width - len("".join(strings))
            if alignment.lower() == "l":
                print(f"{strings[0]} {strings[1]}{' '*(width_wf_strings-1)}{strings[0]}")
            elif alignment.lower() == "m":
                if width_wf_strings % 2 == 0:
                    print(f"{strings[0]}{' '*int(width_wf_strings/2)}{strings[1]}{' '*int(width_wf_strings/2)}{strings[0]}")
                else:
                    print(f"{strings[0]}{' '*int(floor(width_wf_strings/2))}{strings[1]}{' '*int(ceil(width_wf_strings/2))}{strings[0]}")
            elif alignment.lower() == "r":
                print(f"{strings[0]}{' '*(width_wf_strings-1)}{strings[1]} {strings[0]}")
            elif alignment.lower() == "fws":
                print(f"{strings[0]}{strings[1]*(width-2)}{strings[0]}")
        elif type(strings) == str:
            print(strings*width)

    def change_settings(self):
        inp = "p"
        while not(inp.lower() == "ano" or inp.lower() == "ne" or inp.lower() == ""):
            inp = input(f"Promíchat otázky při generování kvízu? (ano/ne) \n(Pro ponechání původní hodnoty ({'Ano' if self.settings.shuffle_questions else 'Ne'}) zmáčkněte \"ENTER\")\n")
            if inp.lower() == "ano":
                self.settings.shuffle_questions = True
            elif inp.lower() == "ne":
                self.settings.shuffle_questions = False
        inp = "p"
        while not(inp.lower() == "ano" or inp.lower() == "ne" or inp.lower() == ""):
            inp = input(f"Promíchat odpovědi při generování kvízu? (ano/ne) \n(Pro ponechání původní hodnoty ({'Ano' if self.settings.shuffle_answers else 'Ne'}) zmáčkněte \"ENTER\")\n")
            if inp.lower() == "ano":
                self.settings.shuffle_answers = True
            elif inp.lower() == "ne":
                self.settings.shuffle_answers = False
        inp = "p"
        while not(inp.lower() == "ano" or inp.lower() == "ne" or inp.lower() == ""):
            inp = input(f"Podat pouze určité procento otázek \n při generování kvízu? (ano/ne) \n(Pro ponechání původní hodnoty ({'Ano' if self.settings.only_percentage_of_random_questions_per_quiz else 'Ne'}) zmáčkněte \"ENTER\")\n")
            if inp.lower() == "ano":
                self.settings.only_percentage_of_random_questions_per_quiz = True
            elif inp.lower() == "ne":
                self.settings.only_percentage_of_random_questions_per_quiz = False
        inp = "p"
        exit_loop = False
        if self.settings.only_percentage_of_random_questions_per_quiz:
            while not exit_loop:
                inp = input(f"Procento podaných otázek? (1-100) \n(Pro ponechání původní hodnoty ({'Ano' if self.settings.the_percentage else 'Ne'}) zmáčkněte \"ENTER\")\n")
                if type(int(inp)) != str:
                    if int(inp) >= 1 and int(inp) <= 100:
                        self.settings.the_percentage = int(inp)
                        exit_loop = True
                else:
                    if inp == "":
                        exit_loop = True
        self.save_settings()

    def load_settings(self):
        with open(self.file_name) as file:
            self.settings = ImportedSettings(json.load(file))
            file.close()

    def save_settings(self):
        with open(self.file_name, "w") as file:
            json.dump(self.settings.to_dictionary(), file)
            file.close()


class Program:
    quiz_maker = None

    def __init__(self):
        self.quiz_maker = QuizMaker("quizzes.json")
        self.quiz_maker.settings_manager = SettingsManager("settings.json")
        self.quiz_maker.load_quizzes()
        self.quiz_maker.settings_manager.load_settings()
        self.quiz_maker.print_main_menu()

program = Program()