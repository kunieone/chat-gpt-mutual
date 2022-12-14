"""  这是我的main.py文件,现在我要写另一个python文件
 mutualtalk.py,来完成两个AI的互相对话,两个AI分
 别叫小红和李华,小红和李华并不是仅仅调用Ai对话生成
 的函数,小红比较喜欢围绕主题说话,这个Ai将会预设被
 灌输一些“我接下来的话将会围绕着某某某主题”这样的
 思想,来防止和李华这个Ai对话的时候跑题。在一开始
 我会在命令行输入这两个AI讨论的主题,之后AI会互相
 调用我前面的一些函数,来完成互相交流。并且双方会把
 交流的内容按照上面的方式保存在markdown文件里。在
 两个AI交流的过程中,将会由李华这个AI在每14回合进
 行一个总结,之后向小红进行如下的提问：“小红,你对这
 件事情的客观理解和我的出入大吗,你认为如果极端来讲
 你会怎么做”诸如此类的话语,同时也输出到markdown文
 件里（和前面的一样）他们之间的对话会一直进行。并且
 为了防止AI说出“I am a large language model 
 trained by OpenAI to assist with answering
 questions and providing information. ”这样
 逃避问题的话,某一方如果发现对方说出了和如上差不多的
 话的时候,请立刻让一方做出纠正：“请重新对某某某主题”
  进行讨论。小红和李华都会说话，请只以小红的视角把对
  话内容按照前面函数的格式来输出，而不要都调用，因为
  否则会重复。"""
