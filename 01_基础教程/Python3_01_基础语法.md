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
  ```
  '''
  这是
  多行
  注释
  '''
  ```
  ```
  """
  这也是
  多行
  注释
  """
  ```
