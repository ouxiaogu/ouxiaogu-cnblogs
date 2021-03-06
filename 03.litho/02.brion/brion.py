# -*- coding: utf-8 -*
import re
def Html2UBB(content):
    #以下是将html标签转为ubb标签
    pattern = re.compile( '<a href=\"([sS]+?)\"[^>]*>([sS]+?)</a>',re.I)
    content = pattern.sub(r'[url=1]2[/url]',content)
    pattern = re.compile( '<img[^>]+src=\"([^\"]+)\"[^>]*>',re.I)
    content = pattern.sub(r'[img]1[/img]',content)
    pattern = re.compile( '<strong>([sS]+?)</strong>',re.I)
    content = pattern.sub(r'[b]1[/b]',content)
    pattern = re.compile( '<font color=\"([sS]+?)\">([sS]+?)</font>',re.I)
    content = pattern.sub(r'[1]2[/1]',content)
    pattern = re.compile( '<[^>]*?>',re.I)
    content = pattern.sub('',content)
    #以下是将html转义字符转为普通字符
    content = content.replace('&lt;','<')
    content = content.replace('&gt;','>')
    content = content.replace('&rdquo;','”')
    content = content.replace('&ldquo;','“')
    content = content.replace('&quot;','"')
    content = content.replace('&copy;','©')
    content = content.replace('&reg;','®')
    content = content.replace('&nbsp;',' ')
    content = content.replace('&mdash;','—')
    content = content.replace('&ndash;','–')
    content = content.replace('&lsaquo;','‹')
    content = content.replace('&rsaquo;','›')
    content = content.replace('&hellip;','…')
    content = content.replace('&amp;','&')
    return content

content =
"<!DOCTYPE html><html><head><meta charset="utf-8"><style>html { font-size: 100%; overflow-y: scroll; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }

body{
  color:#444;
  font-family:Georgia, Palatino, 'Palatino Linotype', Times, 'Times New Roman',
              "Hiragino Sans GB", "STXihei", "微软雅黑", serif;
  font-size:12px;
  line-height:1.5em;
  background:#fefefe;
  width: 45em;
  margin: 10px auto;
  padding: 1em;
  outline: 1300px solid #FAFAFA;
}

a{ color: #0645ad; text-decoration:none;}
a:visited{ color: #0b0080; }
a:hover{ color: #06e; }
a:active{ color:#faa700; }
a:focus{ outline: thin dotted; }
a:hover, a:active{ outline: 0; }

span.backtick {
  border:1px solid #EAEAEA;
  border-radius:3px;
  background:#F8F8F8;
  padding:0 3px 0 3px;
}

::-moz-selection{background:rgba(255,255,0,0.3);color:#000}
::selection{background:rgba(255,255,0,0.3);color:#000}

a::-moz-selection{background:rgba(255,255,0,0.3);color:#0645ad}
a::selection{background:rgba(255,255,0,0.3);color:#0645ad}

p{
margin:1em 0;
}

img{
max-width:100%;
}

h1,h2,h3,h4,h5,h6{
font-weight:normal;
color:#111;
line-height:1em;
}
h4,h5,h6{ font-weight: bold; }
h1{ font-size:2.5em; }
h2{ font-size:2em; border-bottom:1px solid silver; padding-bottom: 5px; }
h3{ font-size:1.5em; }
h4{ font-size:1.2em; }
h5{ font-size:1em; }
h6{ font-size:0.9em; }

blockquote{
color:#666666;
margin:0;
padding-left: 3em;
border-left: 0.5em #EEE solid;
}
hr { display: block; height: 2px; border: 0; border-top: 1px solid #aaa;border-bottom: 1px solid #eee; margin: 1em 0; padding: 0; }


pre , code, kbd, samp { 
  color: #000; 
  font-family: monospace; 
  font-size: 0.88em; 
  border-radius:3px;
  background-color: #F8F8F8;
  border: 1px solid #CCC; 
}
pre { white-space: pre; white-space: pre-wrap; word-wrap: break-word; padding: 5px 12px;}
pre code { border: 0px !important; padding: 0;}
code { padding: 0 3px 0 3px; }

b, strong { font-weight: bold; }

dfn { font-style: italic; }

ins { background: #ff9; color: #000; text-decoration: none; }

mark { background: #ff0; color: #000; font-style: italic; font-weight: bold; }

sub, sup { font-size: 75%; line-height: 0; position: relative; vertical-align: baseline; }
sup { top: -0.5em; }
sub { bottom: -0.25em; }

ul, ol { margin: 1em 0; padding: 0 0 0 2em; }
li p:last-child { margin:0 }
dd { margin: 0 0 0 2em; }

img { border: 0; -ms-interpolation-mode: bicubic; vertical-align: middle; }

table { border-collapse: collapse; border-spacing: 0; }
td { vertical-align: top; }

@media only screen and (min-width: 480px) {
body{font-size:14px;}
}

@media only screen and (min-width: 768px) {
body{font-size:16px;}
}

@media print {
  * { background: transparent !important; color: black !important; filter:none !important; -ms-filter: none !important; }
  body{font-size:12pt; max-width:100%; outline:none;}
  a, a:visited { text-decoration: underline; }
  hr { height: 1px; border:0; border-bottom:1px solid black; }
  a[href]:after { content: " (" attr(href) ")"; }
  abbr[title]:after { content: " (" attr(title) ")"; }
  .ir a:after, a[href^="javascript:"]:after, a[href^="#"]:after { content: ""; }
  pre, blockquote { border: 1px solid #999; padding-right: 1em; page-break-inside: avoid; }
  tr, img { page-break-inside: avoid; }
  img { max-width: 100% !important; }
  @page :left { margin: 15mm 20mm 15mm 10mm; }
  @page :right { margin: 15mm 10mm 15mm 20mm; }
  p, h2, h3 { orphans: 3; widows: 3; }
  h2, h3 { page-break-after: avoid; }
}
</style><title>brion</title></head><body><p>睿初科技（深圳）有限公司招聘职位列表<br />
职位名称    工作地点    职位类型    发布日期    所属机构  </p>
<p><a href="http://my.yingjiesheng.com/job_321465.html">ASML-Brion2014Campus Recruiting--算法工程师  深圳  全职  9月18日   中国总部</a><br />
<a href="http://my.yingjiesheng.com/job_321462.html">ASML-Brion2014Campus Recruiting--产品工程师  深圳  全职  9月18日   中国总部</a> <br />
<a href="http://my.yingjiesheng.com/job_321460.html">ASML-Brion2014Campus Recruiting--应用软件开发工程师  深圳  全职  9月18日   中国总部</a><br />
<a href="http://my.yingjiesheng.com/job_321457.html">ASML-Brion2014Campus Recruiting--软件测试工程师    深圳  全职  9月18日   中国总部</a>  </p>
<h2 id="_1">睿初科技（深圳）有限公司简介</h2>
<h3 id="asml-brion">ASML-Brion介绍</h3>
<p>随着半导体制造技术进入深亚微米时代，作为半导体制造核心部分的光刻技术迫切需要在物理和光学方面有所突破、创新，以超越制造更小尺寸的限制，从而制造出更快更小的CPU、Flash等集成电路器件。作为创造性提出“计算光刻”概念的领导者，Brion不仅成功地利用“计算光刻”解决了深亚微米和纳米级半导体制造中所面临的各种难题，包括高精度建模、器件设计的检查与修正等，还通过与ASML这样的光刻机设备制造商的技术衔接与创新，极大地扩展了光刻制造的容许度及对应的市场，与ASML一起携手实现半导体制造技术的跨越式发展。</p>
<p>ASML-Brion视创新为企业生命力之本，以尖端技术的研发为企业发展之路。目前Brion的系列产品广泛的涵盖和嵌入在半导体制造工艺的各个节点的重要生产过程，尤其是为ASML制造的世界最先进的EUV光刻机，同步开发了相应的计算光刻产品。</p>
<p>Brion总部位于美国加州的圣克拉拉市，并在中国深圳设有研发中心。为继续提升公司在光刻领域的领导地位，Brion正广募英才，进一步壮大公司的技术和商业团队，为客户提供更先进的设计和制造解决方案。
Brion官方网站：www.brion.com</p>
<h3 id="asml">总部 阿斯麦ASML简介</h3>
<p>总部位于荷兰的ASML公司是全球光刻设备市场的领导者，在全球15个国家设有60个办事处。先进的集成电路芯片制造商均使用ASML光刻设备。许多时尚电子产品，如iPhone、Galaxy、电视及导航仪等，均采用ASML设备生产的芯片。自1984年以来，由于我们不断的技术突破，使电子设备功能更强大、体积更小巧、价格更便宜和使用更节能。</p>
<p>我们每年的人均研发经费名列欧洲第二，从而吸引了大量在物理、电子、机电、软件以及精密技术等领域最富有创造性的人才。我们公司国际化的组织管理、坦诚、开放的工作氛围所创造的技术和设备，成就了智能电子产品的普及，从而促进了全球保健、环境、商业、娱乐及交通等领域的发展。</p>
<p>我们才华横溢的工程师们每天都在技术前沿进行突破性探索。如果您有一腔热情，向往解决复杂的技术难题，敢于挑战数学物理极限，那么ASML适合您。我们的激励机制提供各种发展机会，鼓励持续学习，并提供优厚的待遇。 </p>
<h3 id="asml_1">ASML基本资料及数据</h3>
<p>创立于1984年，在阿姆斯特丹泛欧交易所及纳斯达克上市，股票代码为“ASML”。</p>
<p>全球员工超过7,000人，亚洲员工近1,500人；在15个国家有60多个分支机构。</p>
<p>全球十大集成电路生产商均为ASML的用户。</p>
<p>ASML每年有5亿欧元以上强劲而稳定的研发计划，数倍于竞争对手，从而支持芯片产业的持续进步及创新。</p>
<p>ASML设计、制造光刻设备系统，并拥有自己的服务机构，以确保所有系统保持纳米级精度；29年来，ASML采用独特的价值链商务模式，将600多个供应商组成网络，以速度、技术和灵活性帮助我们在全球市场的竞争中取胜。</p>
<p>了解更多信息，请访问网址: www.asml.com</p>
<blockquote>
<p>电子邮箱：jobs_bc@asml.com<br />
企业网址：http://www.asml.com<br />
联系地址：广东省深圳市南山区高新南5道9号金证科技大楼5楼西侧<br />
邮　　编：518057  </p>
</blockquote></body></html>"

Html2UBB(content)