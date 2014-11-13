<!-- pandoc -s pi2.md -o pi2.html -->
[Math]Pi(2)

接着前一篇，[\[Math\]Pi(1)][ref1]，下面继续介绍Leonard Euler求`Pi`的第二个公式。
[ref1]:http://www.cnblogs.com/ouxiaogu/p/3398284.html 

其实这个公式也是来源一个古老的问题，[Basel problem][ref2]
[ref2]:http://en.wikipedia.org/wiki/Basel_problem

## 证法1.麦克劳伦级数和零点式
$sin(x)$的 Maclaurin Series为：
\begin{equation}\label{E1} \becuase \sin(x) &= x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots  \end{equation}
再把 $\frac{\sin(x)}{x}$ 表示成零点处的多项式：
\begin{align}\label{E2}
    \therefore \frac{\sin(x)}{x} &= 1 - \frac{x^2}{3!} + \frac{x^4}{5!} - \frac{x^6}{7!} + \cdots \\
                      &=\left(1 - \frac{x}{\pi}\right)\left(1 + \frac{x}{\pi}\right)\left(1 - \frac{x}{2\pi}\right)\left(1 + \frac{x}{2\pi}\right)\left(1 - \frac{x}{3\pi}\right)\left(1 + \frac{x}{3\pi}\right) \cdots \\
                      &= \left(1 - \frac{x^2}{\pi^2}\right)\left(1 - \frac{x^2}{4\pi^2}\right)\left(1 - \frac{x^2}{9\pi^2}\right) \cdots
\end{align}
对比算式(1)和(2)中的$x^2$项的系数有：
$$-\left(\frac{1}{\pi^2} + \frac{1}{4\pi^2} + \frac{1}{9\pi^2} + \cdots \right) =-\frac{1}{\pi^2}\sum_{n=1}^{\infty}\frac{1}{n^2}=-\frac{1}{3!}$$
\begin{equation}\label{E3} \sum_{n=1}^{\infty}\frac{1}{n^2} = \frac{\pi^2}{6}. \end{equation}

## 证法2.傅里叶级数

### 1.Fourier series 
$$ f(x)=\dfrac{a_{0}}{2}+\sum_{n=1}^{\infty }(a_{n}\cos nx+b_{n}\sin x),-\pi \leq x\leq \pi $$ 
其中，
\begin{align*}
a_{n}&=\dfrac{1}{\pi }\int_{-\pi }^{\pi }f(x)\cos nx\;dx\qquad n=0,1,2,3,...,\\
b_{n}=\dfrac{1}{\pi }\int_{-\pi }^{\pi }f(x)\sin nx\;dx\qquad n=1,2,3,... .
\end{align*}

### 2. $f(x)=x^2的傅里叶级数$
当$n=0$，
$$a_{0}=\dfrac{1}{\pi }\int_{-\pi }^{\pi }x^{2}dx=\dfrac{2}{\pi }\int_{0}^{\pi
}x^{2}dx=\dfrac{2\pi ^{2}}{3}.$$
当$n=1,2,3,...$，
\begin{align*}
a_{n}&=\dfrac{1}{\pi }\int_{-\pi }^{\pi }x^{2}\cos nx\;dx=\dfrac{2}{\pi }\int_{0}^{\pi }x^{2}\cos nx\;dx\\
&=\dfrac{2}{\pi }\times&=\dfrac{%2\pi }{n^{2}}(-1)^{n}=(-1)^{n}\dfrac{4}{n^{2}}\\
b_{n}&=\dfrac{1}{\pi }\int_{-\pi }^{\pi }f(x)\sin nx\;dx=0
\end{align*}
$$ \because \int\limits_0^2\pi x^2\cos nx\;dx=\dfrac{2x}{n^{2}}\cos nx+\left( \frac{x^{2}}{n}-\dfrac{2}{n^{3}}\right) \sin nx.$$
因此，
\begin{equation}\label{E3}
  f(x)=\dfrac{\pi ^{2}}{3}+\sum_{n=1}^{\infty }\left( (-1)^{n}\dfrac{4}{n^{2}}\cos nx\right) 
\end{equation}
将$f(\pi )=\pi ^{2}$代入上式
\begin{align}\label{E4}
  f(\pi)&=\dfrac{\pi ^{2}}{3}+\sum_{n=1}^{\infty }\left( (-1)^{n}\dfrac{4}{n^{2}}\cos n\pi\right)\\
        &=\dfrac{\pi ^{2}}{3}+4\sum_{n=1}^{\infty }\left( (-1)^{n}(-1)^{n}\dfrac{1}{n^{2}}\right)\\
        &=\dfrac{\pi ^{2}}{3}+4\sum_{n=1}^{\infty }\dfrac{1}{n^{2}}.
\end{align}
最后，我们就可以得到：
\begin{equation}\label{E5}
    \sum_{n=1}^{\infty }\dfrac{1}{n^{2}}=\dfrac{\pi ^{2}}{4}-\dfrac{\pi ^{2}}{12}=\dfrac{\pi ^{2}}{6}
\end{equation}