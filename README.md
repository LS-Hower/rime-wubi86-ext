# rime-wubi86-ext

(更新中) 86 五笔扩展 C、D 区汉字的 [RIME](https://rime.im/) 词库。以后会逐区地加上 E、F、G、H、I 区，甚至更靠后的汉字。

如果有错误或可以改进的地方，请务必指出。我很高兴能够改正错误。

## 由来

[rime/rime-wubi](https://github.com/rime/rime-wubi) 的 `wubi86.dict.yaml` 已经有了基本区、扩展 A、B 区汉字，仍需补充。

这轮子由此而生（真的吗？）

## 特点

字形标准：尽量跟随中国大陆（内地）的字形标准。

容错码：置于每个码表的后边，用一行注释 `#容错码` 隔开。同时总结在 `summary.txt` 中。

* 有 86 自己的容错码，例如字里的“飠”，既可以是 `wp`，也可以是 `wyvc`；
* 对于一些字形清奇、结构清奇，或不同字库字形有分歧的字，也设置容错码。如“𪭃”字，既是 `nghl`，也是 `nfll`。

## wubi86.109.dict.yaml 里的字，是哪里的？

* 9FA6-9FFF，共 90 个，在基本区的后面；
* 4DB6-4DBF，共 10 个，在扩展 A 区的后面；
* 2A6D7-2A6DF，共 9 个，在扩展 B 区的后面。

可以说是“基本区补充”“扩展A补充”和“扩展B补充”。也都是 [rime/rime-wubi](https://github.com/rime/rime-wubi) 的 `wubi86.dict.yaml` 没有的字。

## 安装与使用的方法

网上有现成的，这轮子我就不想造啦。

## 十分感谢！

* 软件：[BablePad](https://www.babelstone.co.uk/Software/BabelPad.html)；
* 字体：[天珩全字库](http://cheonhyeong.com/Simplified/download.html)；
* 字体：SimSun-ExtB。
* 还有你！
