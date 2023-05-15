# rime-wubi86-ext

86 五笔 Unicode 扩展区 C 至 H 区汉字 [RIME](https://rime.im/) 词库。

如果有错误或者可以改进的地方，请指出。

## 由来

[rime/rime-wubi](https://github.com/rime/rime-wubi) 的 `wubi86.dict.yaml` 只有基本区和扩展 A、B 区的汉字，需要补充。

因为当时找不到，所以自己来做了。

## 内容

| 文件 | Unicode 码点 | 字数 |
| :--- | :------ | :--- |
| wubi86.extext.dict.yaml | 9FA6-9FFF<br/>4DB6-4DBF<br/>2A6D7-2A6DF<br/>2B735-2B739 | 90<br/>10<br/>9<br/>5 |
| wubi86.extc.dict.yaml | 2A700-2B734 | 4149 |
| wubi86.extd.dict.yaml | 2B740-2B81D | 222 |
| wubi86.exte.dict.yaml | 2B820-2CEA1 | 5762 |
| wubi86.extf.dict.yaml | 2CEB0-2EBE0 | 7473 |
| wubi86.extg.dict.yaml | 30000-3134A | 4939 |
| wubi86.exth.dict.yaml | 31350-323AF | 4192 |

用[叶典](http://yedict.com/)的话说：

`wubi86.extext.dict.yaml` 的四部分分别是基本区补充、扩展 A 补充、扩展 B 补充、扩展 C 补充。

## 注意事项

1. 这些码表有“容错码”，放在每个码表的末尾，用注释 `#容错码` 隔开。

   容错码同时也总结在了 `multicode.txt` 中，可以参考。

   请注意，容错码的正异只是我主观的看法。容错码出现的原因如下：

   * 86 五笔自己就有“容错码”。

     86 五笔有繁体字根，而一些使用繁体字根的繁体字，就会有不止一种拆法。

     如“齒”： `hbj`、 `hwwb`。

   * 扩展区汉字总有一大堆字形和结构很难确定的字。

     如“𪭃”： `ngnl`、 `nfll`。

   * 同一个字在不同字体里的字形可能不一样。

     如“鿃”字，本来是⿰目㚒： `hdty`，但 SimSun-ExtB 字体做成了⿰目夾： `hdww`。这两种都收了。

     码表里没有把所有的字都这么处理，因为这样会太费时太费力，意义也不大。

     主要参考的字形是天珩全字库（见最后）的字形。

   * 编写的时候参考了 [rime/rime-wubi](https://github.com/rime/rime-wubi) 的 `wubi86.dict.yaml` 这个“原本的词库”。

     比如它的“𠕄”： `mmgg`，所以“𫩦”： `kmgm`、 `kmmg`。

   * 我想在码表里面放一点彩蛋。

2. 编写码表的时候，使用的 **字形标准是尽量跟随中国大陆（内地）标准的**。

   比如遇到的部件“爭”都当作“争”处理了。

   注意： **上文提到的“原本的词库” `wubi86.dict.yaml` 没有特意把字形全部改为中国大陆（内地）标准的**，比如它的“𨼳”： `bbkf`，这是台湾字形。

   字根的处理也不太一样，比如它的“𡆢”： `lqi`，而我会认为“𡆢”： `lnv`。

总之，这个码表应该和“原本的词库”一起使用，但在输入生僻字时可能要 **思考并尝试各种笔顺、拆分和结构**，这样才更容易打出想要的字。

## 导入

可以参考 [lotem](https://github.com/lotem) 的[导入码表示例](https://gist.github.com/lotem/5443073)来操作。

在 Windows 上的具体做法是：
1. 找到你的五笔方案正在使用的主词典；
2. 下载文件，将 7 个码表文件放在这个“主词典”所在的文件夹；
3. 在这个“主词典”中，在 `---` 和 `...` 中间添上：

```
import_tables:
  - wubi86.extc
  - wubi86.extd
  - wubi86.exte
  - wubi86.extf
  - wubi86.extg
  - wubi86.exth
  - wubi86.extext
```

4. 重新部署。

## 感谢

* 文本编辑器：[BabelPad](https://www.babelstone.co.uk/Software/BabelPad.html)
* 网站：[叶典（字海网）](http://yedict.com/)
* 网站：[字统网](https://zi.tools/)
* 字体：[天珩全字库](http://cheonhyeong.com/Simplified/download.html)
* 字体：SimSun-ExtB
