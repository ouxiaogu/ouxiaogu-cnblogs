<!-- pandoc -s Lithograph2.md -o Lithograph2.html -->
接上一篇介绍IC制造的基本过程，光刻的基本过程。这篇文章继续介绍光刻过程中的一些概念。
目录

1. [IC][IC]Lithograph(0)半导体制造的基本过程 http://www.cnblogs.com/ouxiaogu/p/3407485.html
2. [IC]Lithograph(1)光刻技术分析与展望 http://www.cnblogs.com/ouxiaogu/p/3408374.html
3. [IC]Lithograph(1)光刻技术的精度分析

##1. 光刻投影系统的分辨率

投射到晶圆片上的特征图的精度，取决于投影系统的光波长，以及经过光掩膜板(illuminated mask)衍射光的衍射级次有多少能被会聚透镜(缩图透镜the reduction lens system)捕获。当前最常用的光刻机使用的深紫外光(deep ultraviolet,DUV)，是由波长为248nm和193nm的受激准分子激光器产生的。因此，当前主要的光刻技术也被称为“准分子激光光刻”。

投影系统能够刻印的最小特征尺寸可用瑞利判据给出：
\begin{equation} \label{E1}
    CD = k_1 \cdot\frac{\lambda}{NA}
\end{equation}
$ \,CD $ 为最小特征尺寸(也称为critical dimension)，也常常写成半径的2倍，即$ R = k_1 \cdot\frac{\lambda}{NA}$；
$ \,k_1 $因子，是光刻系统的相关系数，一般为0.4；采用计算光刻技术处理之后，这个系数还能有一定的减小；
$ \,\lambda  $为光的波长；
$ \,NA $,为从晶圆的角度看过去的数值孔径。

通过这个公式，我们以看到分辨率R与光源波长$ \,\lambda  $是成正比的。要提高分辨率$R$，可以减小光波波长$ \,\lambda  $，增大数值孔径$ \,NA $。当掩模版图形尺寸远大于光源波长$ \,\lambda  $,亦即远大于分辨率$R$时,由衍射产生的图形偏差可以忽略不计,在这种情况下光刻胶膜中通过曝光形成的光刻图形与掩模版图形基本相同。然而由于技术发展和资金规模的限制,光刻机所用光源波长的减小，速度远远慢于电路特征尺寸的减小速度。而且随着生产工艺的演进,光刻波长与特征尺寸两者之间的差距越来越小。

另外,由于硅片平整度误差!光刻胶厚度不均匀!调焦误差以及视场弯曲等因素的
存在,最佳成像平面与实际成像平面之间总是存在一定误差"这被称之为离焦,离焦一般会导致畸变的进一步加剧"并且由于光刻胶层有一定的厚度,要保证蚀刻质量也要求其上下表面的成像有一定的一致性"这都要求成像系统要在理想成像平面上下一定范围之内都要有较佳的成像效果,一般将这一范围称之为焦深(DepthofFocus,DoF)"。焦深可以通过下面的公式计算：
\begin{equation} \label{E2}
    D_F = k_2 \cdot\frac{\lambda}{{NA}^2}
\end{equation}
$\,k_2 $,为另一个与相关的系数。
可以看到$D_F$也是与光源波长是成正比的,与数值孔径成反比的。但不同的是，分辨率$R$是越小越好,而焦深$D_F$则是越大越好。因此如果通过减小光源波长以及增大NA的方法提高分辨率则同时也会降低系统的焦深,两者是矛盾的。

现在的光刻，已经很长时间处于“亚波长光刻”时代。以gonm和65nm节点为例,其生产时所采用的ArF光源波长为193nm,特征尺寸还不到光源波长的一半"。由图1，可以看到，在EUVL技术大规模商用之前，光刻技术很长时间都将处于“亚波长光刻”时代，而且特征尺寸与光源波长的之间的间隔一直在扩大。

因此，下一代光刻技术(Next Generation Lithography,NGL)的开发变得十分紧迫，常见的有如下几种,在上一篇文章中也已经有所介绍：

- 极紫外光刻(Extreme Ultraviolet Lithography,EUVL
- 纳米压印光刻(Nanoimprint Lithography,NIL)
- 电子束曝光光刻(Electron-beam Projection Lithography,EPL)

##2. 光学邻近效应

由前面的文章可知，NGL尚未大规模应用之前，光刻很长时间都会处在“亚波长光刻”时代。所生产集成电路的特征尺寸接近曝光系统的理论分辨率极限"在这种情况下,硅片表面成像相对于原始版图出现边角圆化,线端缩短,线宽偏差等严重的不一致。这种掩模图形和硅基表面实际印刷图形之间的图形转移失真现象,一般被称之为光学邻近效应(OPE, Optical Proximity Effects)

##3. 分辨率增强技术

为了减轻以及抵消亚波长光刻工艺产生的日益严重的光学邻近效应,业界提出并
广泛采用了在不改变光刻波长的前提下通过控制光刻系统的其他各项参数(减小$k_1$,增大$k_2$，来实现提高图形转移质量,减小光刻畸变和提高系统焦深的分辨率增强技术(Resolution Enhancement Teehnology,RET)。

- 分辨率增强技术(RET): 
    - 邻近效应校正(Optical Proximity Correcttion,OPC) 
    - 移相掩膜(Phase Shifting Mask,PSM) 
    - 偏轴照明(Off Axis Illumination,OAI) 
    - 次分辨率辅助图形(Sub-Resolution Assist Feature,SRAF)

reference

1. 陈晔. "适用于超深亚微米集成电路制造与验证流程的光学邻近修正方法研究." PhD diss., 浙江大学, 2008.
2. wiki::Computational_lithography http://en.wikipedia.org/wiki/Computational_lithography






