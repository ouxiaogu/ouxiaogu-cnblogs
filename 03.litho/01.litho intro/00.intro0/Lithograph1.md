<!-- pandoc -s Lithograph1.md -o Lithograph1.html -->
##1. 晶圆片 Wafer
晶圆（Wafer）是指硅半导体集成电路制作所用的硅芯片，由于其形状为圆形，故称为晶圆。晶圆是生产集成电路所用的载体，一般意义晶圆多指单晶硅圆片。

以硅晶圆片为例，它的制造经过了一下几个过程：
 二氧化硅 ——> 粗硅 ——> 多晶硅 ——> 单晶硅 ——> 硅晶圆片
如图1,2所示：

1. 二氧化硅 ——> 粗硅
    - 工业上将碳将普通硅砂还原成粗硅。 C + SiO<sub>2</sub> ——> Si + CO<sub>2</sub>, 但粗硅中一般还含有铁、铝、碳、磷、硼、铜等。
2. 粗硅 ——> 多晶硅
    - 粗硅需要进一步提纯，一般用氯化氢（HCl）等到纯度更高的多晶硅。
3. 多晶硅  ——> 单晶硅
    - 单晶硅是将对晶硅经单晶炉拉制而成的。将需提纯的多晶硅和根据需要掺杂的杂质剂放入坩埚中熔化，然后慢慢拉制成单晶硅棒。
    - 单晶(single crystal)是指其内部微粒有规律地排列在一个空间格子内的晶体；多晶硅(polysilicon,Polycrystalline silicon),由很多小的硅晶体醉成的材料，它不同于用于电子和太阳能电池的单晶硅，也不同于用于薄膜设备和太阳能电池的非晶硅。[ref1]:http://en.wikipedia.org/wiki/Single_crystal[ref2]:http://en.wikipedia.org/wiki/Photolithography
    - 单晶根据晶体生长法制作分为 1. 借由柴克劳司基法(Czochralski)，将复晶晶体提炼成对称的、有规律的、成几何型的单晶晶格结构。 2. 浮区法(Floating zone)，可将低纯度硅晶体提炼成对称的、有规律的、成几何型的单晶晶格结构。
    - 柴可夫斯基法[ref3]:http://en.wikipedia.org/wiki/Czochralski_process 
    - 石英(quartz)制作的大坩埚(crucible)盛满多晶硅，再把这个装置放置到一个真空腔(vacuum chamber)中，密闭好之后再注入惰性气体一般为氩(argon)。如图3所示：

    - 柴可夫斯基法[ref4]:http://h2g2.com/approved_entry/A912151 之后，整个过程为 多晶硅熔融melting of polysilicon ——> 引入母晶并开始晶体生成Introduction of the seed crystal and Beginning of the crystal growth ——> 拉伸晶体crystal pulling ——> 由熔融的多晶硅拉制出单晶硅棒Formed crystal with a residue of melted silicon 如图4所示：

4. 单晶硅  ——> 硅晶圆片
    - 首先，将拉制好的单晶硅棒头部和尾部切掉，再用机械对其进行修整，形成直径合适并有一定长度的“单晶硅棒”。
    - 把“单晶硅棒”切成一片一片薄薄的圆片，这些圆片再经过一系列工艺处理后，一片片完美的硅晶圆片就制造出来了。

##2. 集成电路设计
`img5` `img6`

##3. 半导体器件制造
wiki上关于半导体制造的步骤列表如下，ref=http://en.wikipedia.org/wiki/Semiconductor_fabrication

- 芯片处理
    - 湿洗
    - 平版照相术
    - 光刻
    - 离子移植
    - 蚀刻（干法刻蚀Dry etching 、湿法刻蚀Dry etching、等离子蚀刻 Plasma etching） 
    - 热处理
        - 快速热退火
        - 熔炉退火 Furnace anneals
        - 热氧化
    - 化学气相沉积 (CVD) Chemical vapor deposition
    - 物理气相沉积 (PVD)
    - 分子束外延 (MBE)
    - 电化学沉积 (ECD)，见电镀
    - 化学机械平坦化 (CMP)
    - 芯片测试（检验电气特性）
    - 晶背研磨（减小芯片的厚度，使得到的芯片能被嵌入较薄的器件中，像是智能卡或PCMCIA卡。）
- 晶粒制备 Die preparation
    - 芯片组装
    - Die cutting
- 集成电路封装 IC packaging
    - Die attachment
    - IC Bonding
        - Wire bonding
        - Flip chip
        - Tab bonding
    - IC encapsulation
        - Baking
        - Plating
        - Lasermarking
        - Trim and form

##4. 光刻       
半导体制造是一个综合精密的过程，这里只简要介绍一下光刻的基本过程，如图7所示：