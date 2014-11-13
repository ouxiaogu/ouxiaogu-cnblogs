<!-- pandoc -s *.md -o *.html -->
# 标题：Atx方式 #
# 标题1
## 标题2
###### 标题6
或者可以在后面添加若干 # ，并且不一定要和前面的个数对应：

# 标题1 #
## 标题2 #
###### 标题6 ##

# 代码段 #
1. 使用 <code>定义
<code>
import os
</code>
2. 使用 ``` 来定义，同样 ``` 在前后都要独占一行。
```
import os
```
3. 使用缩近块，每行要缩近4个空格或1个制表符，中间可以有空行，如：
    import os
   
     os.path

# 行内代码标记 #
可以使用 <code></code> 或 ` 来引用行内的代码。如：
This is <code>test</code> and `test`.
引用
#  #
. 行首使用 > 加上一个空格表示引用段落，内部可以嵌套多个引用
> 这是一个引用，
> 这里木有换行，   
> 
> 在这里换行了。
> > 内部嵌套

# 列表 #
## 无序列表
无序列表使用 * , +, - 后面加空格来表示，且无序列表要和正文用空行隔开。列表可以嵌套，下一级的列表前面应缩近4个空格或1个制表符。

* a
+ b
- c
    + c1
    + c2
如果一行太长写不下，可以是多行，如：

* a         // 输出 . a b c
   b c
+ b
在列表中可以嵌套其它的格式,如代码，quote引用
## 有序列表
使用数字加英文句号加空格表示。如：

1. Item 1
2. Item 2
3. Item 3

# 分隔线
在一行中使用三个或三个以上的 *、- 或 _ 可以添加分隔线，其中可以有空白，但是不能有其他字符。如：
* * * *
------
__ __ __

# HTML片段
首列以 < 开始的将视为HTML片段，如：
<img src="/uploads/tutorials/7/b3120c84d0be11e1a70ff23c91df0780.png">

# 图片
图片的写法和链接差不多，就是在前面多加一个 !  如：
![Test](/uploads/tutorials/7/b3120c84d0be11e1a70ff23c91df0780.png)

# 文本段
文本段可以由多行文本组成，以空行作为一个段落的结束。首字符不能是特殊的段落开始符。除首行外，第二行可以前面有空格。如：

This is a test
paragraph.
This is a test
    paragraph.

# define a ref/urf 参考定义
先如下定义：
This is [an example][id] reference-style link.
然后在文章的任意位置定义：
[id]: http://example.com/  "Optional Title Here"

# 强调
有以下几种强调方式：

- 单星号 = *斜体*
- 单下划线 = _斜体_
- 双星号 = **加粗**
- 双下划线 = __加粗__
- 三星号 = ***粗斜***
- 三下划线 = ___粗斜___
- 双波浪线 = ~~中划线~~
- 尖号 = ^上标文本^
- E = mc<sup>2</sup>
- Water: H<sub>2</sub>O
- 双逗号 = ,,下标文本,,
- 倒单引号 = `代码`

# 换行
一种是在行尾加上两个空格
第一行  // 这里有两个空格
第二行
二是手动添加一个 /br

# par扩展
需要添加一个par的markdown包，点击 [par][ref_par]可以clone。
[ref_par]: https://github.com/limodou/par

## 定义段
首行应顶格，首字符不能是其它段的开始字符，如 *, +, -, # ，最后以 空格+--结束。 第二行开始为缩近段。如：

a --
    This is a definition

## 表格
每行代表一个表格行，字段之间使用 || 分隔，如：
||a||b||c||
||a1||b1||c1||

## Bootstrap 标签页
标签页是par项目做的一个Markdown语法上的扩展，需要在调用相应的解析时传入对应块的处理函数。定义格式为：

[[tabs(id=hello)]]:
    ```
    This is a test
    ```
[[tabs(id=world)]]:
    * this is a list
    * test

## Bootstrap 提醒
生成Bootstrap alert 的展示效果，格式为：
[[alert(class=success)]]:
    Success
[[alert(class=error)]]:
    Error
[[alert(class=info)]]:
    Info
[[alert]]:
    Message
[[alert]]:
    #### Alert Title
    This is alert message
[[alert(class=info,close)]]:
    This is an alert. It'll has a close button.