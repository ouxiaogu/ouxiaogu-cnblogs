<!-- pandoc -s blog1.md -o blog1.html -->
## [CSAPP笔记]Binary , Unsigned , Signed 之间的相互装换  ##

Sublime Text 2 下使用Markdown写博客的处女作，试试效果。

### 摘要 
  本文主要讲解 Binary , Unsigned , Signed 三种数据中任意两者之间的转换。下面是文中的一些约定写法。

- 转换名称
    + B2U<sub>w</sub>\(***x***\) : 将位数为w的二进制数 *binary* 转换为无符号数*Unsigned*
    + B2T<sub>w</sub>\(***x***\) : 将位数为w的二进制数 *binary* 转换为补码 *Two's complement*
- 二进制数的表示 \(***x***\)  : 用一个向量表示，___x___ = \( x<sub>1</sub> , x<sub>2</sub> , ... , x<sub>w</sub>)

### 1.  U2B<sub>w</sub>(x)
直接用辗转相除法即可。  

### 2.  S2B<sub>w</sub>(x) 
正数直接装换，然后左边添加`0` ； 负数先将其绝对值装换成二进制数，再对低`w-1`位取反，最高位添加`1`，用公式表示即为：
下面以三位的三进制数来说明有符数的补码表示

- 3 = 011
- 2 = 010
- 1 = 001
- 0 = 000
- -1 = 111
- -2 = 110
- -3 = 101
- -4 = 100

### 3.  B2U<sub>w</sub>(x)

$$B2U_w\left( \overrightarrow{x} \right) \doteq \sum_{i=0}^{w-1} x_i 2^i \label{eq1}$$

### 4.  B2T<sub>w</sub>(x)

$$B2T_w\left( \overrightarrow{x} \right) \doteq -x_{w-1} 2^{w-1} + \sum_{i=0}^{w-2} x_i 2^i \label{eq2}$$

### 5.  T2U<sub>w</sub>(x)

函数  T2U<sub>w</sub>(x)  定义为  T2U<sub>w</sub>(x) =  T2B<sub>w</sub>(B2U<sub>w</sub>(x)) 。这个函数输入的是一个 -2<sup>\(w-1\)</sup> ~ 2<sup>\(w-1\)</sup>-1  之间的数，而输出的无符数也即为该有符数的补码表示。   
对于位模式 $\overrightarrow{x}$ ，对比式 [1]和式[2] ,
计算两者之差，我们就可以得到，$ B2U_w\left( \overrightarrow{x} \right) - B2T_w\left( \overrightarrow{x} \right) = x_{w-1}  \left( 2^{w-1} - \left( -2^{w-1} \right) \right)  =  x_{w-1} 2^w $ ，这样就得到了
$B2U_w\left( \overrightarrow{x} \right) = x_{w-1} 2^w + B2T_w\left( \overrightarrow{x} \right)$
。若令 $\overrightarrow{x} = T2B_w \left( x \right) $ ，则其反函数为
$ x = B2T_w \left( \overrightarrow{x} \right) $ 。
由前面三式以及$T \rightarrow B \rightarrow U$变换的传递性，可得：

$$B2U_w\left( T2B_w \left( x \right) \right) = T2U_w \left( x \right) = x_{w-1} 2^w + x$$
这个关系对于理解“有符数变换得到的无符数也即补码”很有用。
$$T2U_w \left( x \right)=\left\{
        \begin{aligned}
          & x+2^w, & x<0,x_{w-1}=1  \\
          & x, & x \geq 0,x_{w-1}=0 
        \end{aligned}
        \right.$$
下图说明了 $T2U$ 的转换行为：对于非负数（$x \geq 0$）, $T2U$ 保留原值 ；

### 6.  U2T<sub>w</sub>(x)

函数  U2T<sub>w</sub>(x) 定义为  U2T<sub>w</sub>(x) = B2T<sub>w</sub>(U2B<sub>w</sub>(x)) 。这个函数输入的是一个  0 ~ 2<sup>\(w-1\)</sup>-1  之间的数，输出则为一个  -2<sup>w</sup> ~ 2<sup>\(w-1\)</sup>  之间的数。  
上一节我们已经得到，对于负数（$x<0$）,$T2U$ 被装换为一个大于$2^{w-1}$的正数。\
反过来，我们再来推导无符号数 $u$ 和与之对应的有符号数
$U2T_w \left( u \right) $之间的关系。 利用上一节的结论，
$B2T_w\left( \overrightarrow{u} \right) = B2U_w\left( \overrightarrow{u} \right) - u_{w-1} 2^w $
。若令 $\overrightarrow{u} = U2B_w \left( u \right) $ ，则其反函数为
$ u = B2U_w \left( \overrightarrow{x} \right) $ 。由前面三式以及
$T \rightarrow B \rightarrow U$ 变换的传递性，可得：

$$B2T_w\left( U2B_w \left( u \right) \right) = U2T_w \left( u \right) = u - u_{w-1} 2^w$$

在 $u$ 原始的无符号表示法中，最高位$u_{w-1}$决定了 $u$ 是否大于或等于
$2^{w-1}$, 无符数 $u$ 到有符数的装换分段表示为：

$$U2T_w \left( u \right)=\left\{
        \begin{aligned}
          & u, & u<2^{w-1},x_{w-1}=0  \\
          & u-2^w,  & x \leq 0,x_{w-1}=1
        \end{aligned}
        \right.$$

下图说明了 $U2T$ 转换行为：对于小的数（$u<2^{w-1}$）, $U2T$ 保留原值 ；
对于大的数（$u \geq 2^{w-1}$）,$U2T$ 被装换为一个负数。

### 练习

1.如下函数，在32bit系统中，求问foo(2^31-3)的值是：

<code>
1 int foo(int x)
2 {
3     return x&-x;
4 }
</code>

A： 0  B: 1   C:2   D:4

解答：

- (1).运算符号的优先级，减号 '-' 高于异或 '^' 。所以  *2^31-3=2^\(31-3\)=2^28=30*
- (2).32位机器中int整型的位数的为 _w=32_ ，位运算 _x_ 取反,其实为 _0xFFFFFFFF-x_ ,而不是用 _2<sup>32</sup>_ 减去。
- (3).本题中，_x=30=0x1E_ ,依据 *T2U<sub>w</sub>* 可得 *-x=0xFFFFE2*,所以_x&-x=2_,本题选B
- (4)有么有更简单方法。

> y = x & \(-x\)  
> That does a bitwise AND between the variable x and its negation, and assigns the result to the variable y. 
> If your system uses two's complement signed arithmetic , then what that manages to get you is the greatest power of 2 that is a factor of x. 
> So, if x is 24, y gets assigned 8, and if x is 12, y gets assigned 4, and if x is 99, y becomes 1. To understand why it does that, you need to understand binary, and two's complement. Look them up on wikipedia.

- 用 15, 16 ,48 三个数验证结论
    - _x=15=0x0F_  , _-x=-15=2<sup>32</sup>-0x0F=0xFFFFFFF1_ , 所以 _x&-x=0xF1 & 0x0F = 1_ ; 
    - _x=16=0x10_  , _-x=-16=2<sup>32</sup>-0x10=0xFFFFFF0_ , 所以 _x&-x=0xF0 & 0x10 = 16_ 
    - _x=48=0x30_  , _-x=-48=2<sup>32</sup>-0x30=0xFFFFFD0_ , 所以 _x&-x=0xD0 & 0x30 = 16_ 
- 总结起来就是, _x&-x_ 得到的是数x的最高位。 

___reference___

1. CASPP

2. http://answers.yahoo.com/question/index?qid=20111219113642AAs26uY