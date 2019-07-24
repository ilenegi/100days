### day 1/100

- Weakness
  - Efficiency not high, CPU-bound task can choose C/C++
  - Code can not be encrypted
  - Many framework, easy to make mistakes when there are many choices
  
- Quote, 'import this' in python

  - > The Zen of Python, by Tim Peters
    >
    > Beautiful is better than ugly.
    > Explicit is better than implicit.
    > Simple is better than complex.
    > Complex is better than complicated.
    > Flat is better than nested.
    > Sparse is better than dense.
    > Readability counts.
    > Special cases aren't special enough to break the rules.
    > Although practicality beats purity.
    > Errors should never pass silently.
    > Unless explicitly silenced.
    > In the face of ambiguity, refuse the temptation to guess.
    > There should be one-- and preferably only one --obvious way to do it.
    > Although that way may not be obvious at first unless you're Dutch.
    > Now is better than never.
    > Although never is often better than *right* now.
    > If the implementation is hard to explain, it's a bad idea.
    > If the implementation is easy to explain, it may be a good idea.
    > Namespaces are one honking great idea -- let's do more of those!

### day 2/100 

- 冯诺依曼结构，计算机五大部件：运算器，控制器，存储器，输入设备，输出设备。两个关键点：
  - 运算器和存储设备分开
  - 二进制方式存储编码
    - 二进制
      - 逻辑右移动，右移几位救在左端补给个0。
      - 算数右移，在左端补k各最高有效位的值。因为考虑到符号。
- 原码，反码，补码 ref([原码, 反码, 补码 详解](https://www.cnblogs.com/zhangziqiu/archive/2011/03/30/ComputerCode.html), [关于2的补码](http://www.ruanyifeng.com/blog/2009/08/twos_complement.html))
  - 最高位是符号位，0为正数，1为负数
  - *正数*反码是其本身。*负数*反码符号位不变，其余各位取反
  - *正数*补码是其本身。*负数*补码是反码后+1
  - 反码的话，+0和-0其实是一样，浪费一个数。补码则用上了这个数做最小值。所以32位int类型，可表示范围是[-2^31, 2^31 - 1]
  - 引入补码的意义还在于让符号位也参与运算，计算机只需要定义加法就好，不需要另外定义减法
- 变量命名
  - 硬性规则
    - 字母，数字，下划线。数字不能开头
    - 大小写敏感
    - 不要跟保留字冲突
  - PEP 8要求
    - 小写字母拼写，多个单词用下划线连接
    - 受保护的实例属性用单个下划线开头
    - 私有的实例属性用两个下划线开头


### day 7/100
- string.rfind 是找最后一次出现的位置

### day 8/100
- 保护变量
    - __开头的变量，是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据。
- 装饰器(day 9/100 有讲一些)
    - ？ 需要后续研究
    
### day 9/100
- __slots __ 可以限定自定义类型对象绑定的属性
    - 也有说实例量级不超过百万不值得使用 ref [slots详解](https://zhuanlan.zhihu.com/p/25930288)
- 和静态方法比较类似，Python还可以在类中定义类方法，类方法的第一个参数约定名为cls，它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象），通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象.

### day 11/100
- 读取文件

操作模式 | 具体含义
:---: | :---:
'r' | 读取 （默认
'w'	|写入（会先截断之前的内容）
'x'	|写入，如果文件已经存在会产生异常
'a'	|追加，将内容写入到已有文件的末尾
'b'	|二进制模式
't'	|文本模式（默认）
'+'	|更新（既可以读又可以写）

- 注意使用`try except`来捕获异常 e.g. 没有文件，编码不对之类。 可以参考[总结：Python中的异常处理](https://segmentfault.com/a/1190000007736783)
    - `with`语句在打开文件后会自动调用`finally`并关闭文件。我们在写 Python 代码时应该尽量避免在遇到这种情况时还使用`try/except/finally`的思维来处理。
    ```python
    # should not
    try:
        f = open(a_file)
        do_something(f)
    finally:
        f.close()
    
    # should 
    with open(a_file) as f:
        do_something(f)
    ```
- json 文件操作
    - `dump` 需要带目标文件操作，`dumps`是将dict转化成str，`load`和`loads`也是类似
    - 可以参考 [`load` vs `loads`, `dump` vs `dumps`](https://riptutorial.com/python/example/1041/-load--vs--loads----dump--vs--dumps-)
    
    
### day11/100
- 正则表达式

符号|解释|示例|说明
:---:|:---:|:---:|:---:
(?=exp)	| 匹配exp前面的位置|\b\w+(?=ing)|可以匹配I'm dancing中的danc
(?<=exp)|匹配exp后面的位置	|(?<=\bdanc)\w+\b|可以匹配I love dancing and reading中的第一个ing

   - 实际开发爬虫应用的时候，有很多人会选择Beautiful Soup或Lxml来进行匹配和信息的提取，前者简单方便但是性能较差，后者既好用性能也好，但是安装稍嫌麻烦，这些内容我们会在后期的爬虫专题中为大家介绍。
   
   
### day12/100
- ？ subprocess， 进程间通信(process 里的queue)
- `t1 = Thread(target=download, args=('Python从入门到住院.pdf',))` 里面的逗号是将括号里的内容变成tuple
- 比较遗憾的一件事情是Python的多线程并不能发挥CPU的多核特性，这一点只要启动几个执行死循环的线程就可以得到证实了。之所以如此，是因为Python的解释器有一个“全局解释器锁”（GIL）的东西，任何线程执行前必须先获得GIL锁，然后每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行，这是一个历史遗留问题，但是即便如此，就如我们之前举的例子，使用多线程在提升执行效率和改善用户体验方面仍然是有积极意义的。


### day13/200
- 网络协议的三要素是：语法、语义和时序.
- 传输图片时，如果用JSON传输，由于JSON是纯文本，不能携带二进制数据，图片的二进制数据要处理成base64编码。读图片的时候`b64encode(f.read()).decode('utf-8')`，发送的时候`self.cclient.send(json_str.encode('utf-8'))`
    - Base64是一种用64个字符表示所有二进制数据的编码方式，通过将二进制数据每6位一组的方式重新组织，刚好可以使用0~9的数字、大小写字母以及“+”和“/”总共64个字符表示从000000到111111的64种状态。