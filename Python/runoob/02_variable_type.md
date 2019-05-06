# 变量类型

## 变量赋值

Python 中的变量赋值不需要类型声明。

每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。

每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

等号（=）用来给变量赋值。

等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。


## 多个变量赋值

Python允许你同时为多个变量赋值。

a = b = c = 1

## 也可以为多个对象指定多个变量。

a, b, c = 1, 2, "john"


## 标准数据类型

Python有五个标准的数据类型：

Numbers（数字）

String（字符串）

List（列表）

Tuple（元组）

Dictionary（字典）

### 数字

Python支持四种不同的数字类型：

int（有符号整型）

long（长整型[也可以代表八进制和十六进制]），
Python使用 L 来显示长整型

float（浮点型）

complex（复数）

### 字符串

字符串或串(String)是由数字、字母、下划线组成的一串字符

从左到右索引默认0开始的，最大范围是字符串长度少1

从右到左索引默认-1开始的，最大范围是字符串开头

可以使用变量 [头下标:尾下标]，就可以截取相应的字符串，左闭右开

### Python列表

List（列表）用 [ ] 标识，列表中值的切割也可以用到变量 [头下标:尾下标] 

加号 + 是列表连接运算符，星号 * 是重复操作
<pre><code>
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
 
print list               # 输出完整列表
print list[0]            # 输出列表的第一个元素
print list[1:3]          # 输出第二个至第三个元素 
print list[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
print list + tinylist    # 打印组合的列表

</pre></code>

### Python元组

元组用"()"标识，类似于List（列表），但不能二次赋值，相当于只读列表

tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )

tinytuple = (123, 'john')

print tuple[1:3] 


### Python字典

字典用"{ }"标识。字典由索引(key)和它对应的值value组成。

字典当中的元素是通过键来存取的

<pre><code>
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
 
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
 
 
print dict['one']          # 输出键为'one' 的值
print dict[2]              # 输出键为 2 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值

</code></pre>

