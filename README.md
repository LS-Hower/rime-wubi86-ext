# rime-wubi86-ext

86 五笔扩展区汉字等的 RIME 词库。

## 内容

[rime/rime-wubi](github.com/rime/rime-wubi) 的`wubi86.dict.yaml`收录基本区、扩展 A 区和扩展 B 区的汉字。这儿的是扩展。

1. Unicode 中**扩展 C 区至 G 区的**汉字。

2. **基本区补充**（9FA6-9FFF）、**扩展 A 区补充**（4DB6-4DBF）和**扩展 B 区补充**（2A6D7-2A6DF）**的**汉字，在`wubi86.109.dict.yaml`。共109个汉字。是`wubi86.dict.yaml`没有收全的。

3. **CJK 笔画**（31C0-31E3），在`wubi86.cjk_strokes.dict.yaml`。为避免混淆，笔画后边按 Unicode 标准做了标注。详见[魏安关于 CJK Strokes 的介绍](https://www.babelstone.co.uk/CJK/CJKStroke.html)。

## 注意

看打时，部分汉字难以断定结构等，有的汉字有难以察觉的地区性差异，有的汉字有字体有做错（比如 SimSun-ExtB 把9FC3的“鿃”（⿰目㚒）做成了⿰目夾）。

为方便制作和使用，采取“多开门”方式。如䀹用“hdty”和“hdww”都能打出。

“多开门”的字总结在`summary.txt`中。

## 制作

* 使用了[叶典网的字符集](http://yedict.com/zsts.htm)。汉字显示使用了 SimSun-ExtB 和[天珩全字库](http://cheonhyeong.com/Simplified/download.html)。

* 跟随中国大陆（内地）的字形标准（⿰目㚒是陆标的！）。笔顺等尽量跟随原 86 五笔的标准。