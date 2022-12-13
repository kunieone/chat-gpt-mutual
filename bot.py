from ai import *
from mutual import *


def bot_main():
    bot = AnsweringBot("AI", preset="")
    while True:
        input("等待中...")
        text = ""
        with open('input.md', 'r', encoding='utf-8') as file:
            # Read the lines in the file
            text = file.read()

            # 打开文件并读取内容

            # 替换换行符
        talk = text.replace('\n', '\r')
        # Wait for user input

        answer = bot.answer(talk)
        with io.open("output.md", "a", encoding="utf-8") as f:
            f.write(answer + "\n"+("#" * 30)+"\n")


bot_main()
