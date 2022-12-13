from ai import *
from termcolor import colored


def randomConversation(talk):
    return retort(talk)


# class MutualTalk:
#     def __init__(self, topic):
#         self.topic = topic
#         self.xiaohong_conversation = "你现在是小红,我是李华,你接下来将会喜欢阐述自己的态度,并且喜欢反驳观点。\n"
#         self.lihua_conversation = "我现在是小红,我在对你说话,你是李华,你现在是一个好奇的AI,并且喜欢反驳观点。接下来你会问题并且摆明自己的态度。\n"
#         self.file_name = getTimeFormatFileName()

#     def start(self):
#         # 小红开场
#         talk = "今天我们聊聊" + self.topic + ",你有什么想法吗？"
#         answer = generateAnswer(talk, self.xiaohong_conversation)

#         outToFile(self.file_name, talk, answer, "小红", "李华")
#         # textToAudio(answer)
#         self.xiaohong_conversation += talk+self.xiaohong_conversation

#         # 每14回合李华总结
#         i = 1
#         while(1):
#             print("开始第" + str(i) + "段辩论...")
#             print("xiaohong_conversation:\n")
#             print(self.xiaohong_conversation)
#             print("lihua_conversation:\n")
#             print(self.lihua_conversation)

#             if i % 14 == 0:
#                 i = 1
#                 talk = "最近我们谈论的" + self.topic + ",你有什么收获吗？"
#                 answer = generateAnswer(talk, self.lihua_conversation)

#             if i % 3 == 0:
#                 talk = ",但是" + \
#                     randomConversation(talk)+"你有什么见解,所以你来提问一下吧,稍微不相关的也可以"

#             # 现在是李华听了小红的话,李华做出回答。
#             answer = generateAnswer(talk, self.lihua_conversation)
#             # 现在是小红听了的李华的话,做出回答。
#             talk = generateAnswer(answer, self.xiaohong_conversation)

#             # 提问人李华记录日志
#             outToFile(self.file_name, talk, answer, "小红", "李华")
#             # textToAudio(answer)
#             self.lihua_conversation += (answer + "\n")
#             self.xiaohong_conversation += (talk + "\n")

#             i += 1


class AskingBot:
    def __init__(self, name, topic, preset="你现在只能使用中文来回答和提问。你现在是一个喜欢提问与讨论的AI,你有20%的概率对我给你的主题提问，一次只提问一个问题。接下来请结合主题讨论或者提问："):
        self.name = name
        self.topic = topic
        self.previous_conversation = preset
        self.preset = preset+"你接下来讨论的主题："+topic

    def clear_preset(self):
        self.previous_conversation = ""

    def addFeature(self, teach_word):
        self.answer(teach_word)

    def answer(self, input):
        asw = generateAnswer(input, self.previous_conversation)
        self.previous_conversation += "\n"+input
        return asw


class AnsweringBot:
    def __init__(self, name, topic="", preset="你现在只能使用中文来回答和提问。你现在是一个喜欢回答问题的AI,你很能言善辩，接下来如果你被问到了一连串问题，你会依次回答。接下来请你认真分析："):
        self.name = name
        self.topic = topic
        self.previous_conversation = preset

    def clear_preset(self):
        self.previous_conversation = ""

    def addFeature(self, teach_word):
        self.answer(teach_word)

    def answer(self, input):
        asw = generateAnswer(input, self.previous_conversation)
        self.previous_conversation += "\n"+input
        return asw


class DebateTalk:
    def __init__(self, topic, limit=20):
        self.topic = topic
        self.limit = limit
        # self.questions = generateAnswer(
        #     "请对该主题:「"+topic+"」做出发散思维的想象,把它变成关于这个主题的5个问题", "")
        self.xiaohong = AskingBot("小红", topic)
        self.lihua = AnsweringBot("李华", topic)
        self.file_name = getTimeFormatFileName()+topic + ".md"

    def start(self):
        # 开场白
        xiaohongs_talk = self.topic
        print("开场白:"+colored(xiaohongs_talk, color="red"))
        i = 1
        while(1):
            if i == self.limit:
                print("结束")
                # 总结
                lihuas_answer = self.lihua.answer("好了，请把刚才说的所有的理论与观点做出总结吧")
                outToFile(self.file_name, xiaohongs_talk, lihuas_answer,
                          self.xiaohong.name, self.lihua.name)
                break

            print("开始第" + str(i) + "场辩论")

            # if i % 7 == 0:
            #     xiaohongs_talk = reviser(self.topic+lihuas_answer)

            if i % 8 == 0:
                print("-重制")
                self.lihua.previous_conversation = ""
                self.xiaohong.previous_conversation = ""

            lihuas_answer = ""
            while lihuas_answer.strip() == "":
                lihuas_answer = self.lihua.answer(xiaohongs_talk)
            print(colored("李华："+lihuas_answer, color="blue"))

            # if i % 5 == 0:
            #     print("lihua做出反驳")
            #     lihuas_answer = "但是" + \
            #         retort(xiaohongs_talk)

            outToFile(self.file_name, xiaohongs_talk, lihuas_answer,
                      self.xiaohong.name, self.lihua.name)
            xiaohongs_talk = ""
            while xiaohongs_talk.strip() == "":
                xiaohongs_talk = self.xiaohong.answer(lihuas_answer)
            print(colored("小红："+xiaohongs_talk, color="red"))

            i += 1


meta1 = "请只提问一个问题：接下来请随机生成一个天文、地理、政治、物理、化学、马克思主义哲学原理、哲学等方面其中前沿的有争议的具体的问题，采用精简的中文来提问，但是不能太笼统。"
meta2 = "请随机生成一道数据结构考研题类似的题，有一定难度的更好"
meta3 = "来一点难以听懂的笑话"


def main_talk():
    while True:
        question = generateAnswer(
            meta3)
        print(colored("问题:"+question, color="yellow"))
        t = DebateTalk(question, 300)
        t.start()


main_talk()
