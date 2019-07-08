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





