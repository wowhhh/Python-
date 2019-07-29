## 编码
- 默认情况下，Python3源码文件以UTF-8编码，所有字符串都是Unicode字符串。
- 编码可以参见习题课视频（基础知识之程序的编码问题）

## 标识符
- 第一个字符：必须是字母表中的字母和下划线，数字不可以打头
- 标识符组成部分：字母、数字和下划线
- 大小写敏感
- Python3中，非ASCII标识符也是允许的
  - Python3选择支持非ASCII码标识符的缘由： https://www.cnblogs.com/program-in-chinese/p/why-python3-chose-to-support-non-ASCII-identifiers.html

## 保留字
- 即关键字
  ```
  #查看关键字的方法
  import keyword #引入关键字的模块
  #打印出系统全部关键字
  print(keyword.kwlist)
  ```
## 注释
### 单行注释
  ```
  # 这是一个注释
  ```
### 多行注释
- '''多行内容 ''' / """多行内容 """

## 行与缩进
- python特色：使用缩进来表示代码块，不使用大括号
- 缩进的空格数可变的，但是同一代码块必须包含相同的缩进空格数

## 多行语句
- 长的语句可以使用反斜杠 \ 来实现多行语句
  ```
  total = item_one + \
  item_two + \
  item_three
  ```
- 在[]，{}或（）中的多行语句，不需要使用反斜杠

## 数字（Number）类型
- 整数、浮点数、布尔类型和复数
  - 整数：int 表示长整型，没有Long
  - 布尔：bool  True
  - 浮点数：float
  - 复数：

## 字符串
- python中单引号和双引号的使用完全相同
- 使用三引号可以指定一个多行字符串
- 转义字符 \
  - 反斜杠可以用来转义
  - 使用 r 可以让反斜杠不发生转义。例如：r"this is a line with \n" \n 是会显示的，而不是显示换行。
- 字符串可以用 + 运算符连接在一起，用 * 表示重复
- python的两种索引方式：从左往右是 0开始 ；从右往左是 -1开始
- python中的字符串不可以改变
- python没有单独的字符类型，一个字符就是长度为1的字符串
- 字符串的截取方法: 变量名[头下标:尾下标:步长 ]
  ```
  str='Runoob'

  print(str)                 # 输出字符串
  print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
  print(str[0])              # 输出字符串第一个字符
  print(str[2:5])            # 输出从第三个开始到第五个的字符
  print(str[2:])             # 输出从第三个开始的后的所有字符
  print(str * 2)             # 输出字符串两次
  print(str + '你好')        # 连接字符串

  print('------------------------------')

  print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
  print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
  ```
  ```
   输出结果：
  Runoob
  Runoo
  R
  noo
  noob
  RunoobRunoob
  Runoob你好
  ------------------------------
  hello
  runoob
  hello\nrunoob
  ```
## 空行
- 分隔两段不同功能的代码， 便于以后的维护工作

## 等待用户输入
```
input("\n\n按下 enter 键后退出")
```
- "\n\n"在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出。

## 同一行显示多条语句
- 意思就是多条语句放一行写，不建议

## 多个语句构成代码组
- 缩进相同的语句构成代码块，称之为代码组

## print 输出
- 注意：print默认输出是换行的，如果要实现不换行，应该在末尾加入end=""
```

x="a"
y="b"
# 换行输出
print( x )
print( y )

print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()
```
```
输出结果：
a
b
---------
a b
```

## 
