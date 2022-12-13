import openai
import io
import pyttsx3
import time
import datetime
from ai import *


def main():
    # Generate the timestamp and file name
    file_name = getTimeFormatFileName()+".md"

    # Keep track of the previous conversation
    pre_conversation = ""

    # Loop until the user inputs "Goodbye"
    talk = input("请输入内容：")
    while talk != "Goodbye":
        # Call the outputAnswerToFile function and get the response
        answer = generateAnswer(talk, pre_conversation)
        print(answer)
        outToFile(file_name, talk, answer)
        pre_conversation += talk
        # Print the response and ask for the next input
        talk = input("请输入内容：")


# main()
# 在您的mutualtalk.py文件中,您将定义两个AI:小红和李华。您将预先设定小红喜欢围绕主题说话,并在命令行中输入小红和李华讨论的主题。李华每14回合进行一次总结,并向小红提问。其中只有小红的对话通过outToFile保存到markdown文件里。


def main2():
    # Generate the timestamp and file name
    file_name = getTimeFormatFileName()+".md"

    # Keep track of the previous conversation
    pre_conversation = ""

    # Open the input file
    with open('input.md', 'r', encoding='utf-8') as file:
        # Read the lines in the file
        text = file.read()

        # 打开文件并读取内容

        # 替换换行符
        talk = text.replace('\n', '\r')
        # Call the outputAnswerToFile function and get the response
        answer = generateAnswer(talk, pre_conversation)
        print(answer)
        # Write the answer to the file
        outToFile(file_name, talk, answer)
        # Update the previous conversation
        pre_conversation += talk
