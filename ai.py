# 在您的mutualtalk.py文件中,您将定义两个AI:小红和李华。您将预先设定小红喜欢围绕主题说话,并在命令行中输入小红和李华讨论的主题。李华每14回合进行一次总结,并向小红提问。其中只有小红的对话通过outToFile保存到markdown文件里。以下是可以调用的代码:
import datetime
import time
import pyttsx3
import io
import openai
API_KEY = "YOUR_API_KEY_HERE"


def reviser(text):
    return generateAnswer("简述:"+text, "")


def retort(talk):
    return generateAnswer("反驳一下这个观点，并且精简，要有信服力"+talk, "")


def deRepeat(talk):
    return generateAnswer("对接下来的话去重："+talk)


def generateAnswer(talk, previous_conversation=""):
    # Set your OpenAI API key
    openai.api_key = API_KEY

    # Generate text using GPT-3
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=talk + "\n" + previous_conversation,
        max_tokens=512,
        temperature=0,
    )
    # Return the generated text
    return response["choices"][0]["text"].strip()


def textToAudio(answer):
    engine = pyttsx3.init()
    engine.say(answer)
    engine.runAndWait()


def outToFile(file_name, talk, answer, QName="Q", AName="A"):
    with io.open(file_name, "a", encoding="utf-8") as file:
        file.write("## "+QName+": " + talk + "\n")
        file.write(AName+": " + answer + "\n")


def getTimeFormatFileName():
    # Generate the timestamp and file name
    timestamp = time.time()
    date = datetime.datetime.fromtimestamp(timestamp)
    file_name = date.strftime("%m-%d-%H:%M:%S")
    return file_name
