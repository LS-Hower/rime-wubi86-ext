# rime-wubi86-ext

86 五笔 Unicode 扩展 C 至 G 区汉字的 [RIME](https://rime.im/) 词库。正在逐区更新。

如果有错误，或者有可以改进的地方，请指出。

## 由来

[rime/rime-wubi](https://github.com/rime/rime-wubi) 的 `wubi86.dict.yaml` 只有基本区和扩展 A、B 两区的汉字，需要补充。

因为找不到，所以自己来做了。

## 内容

| 文件 | Unicode | 字数 |
| :--- | :------ | :--- |
| wubi86.extext.dict.yaml | 9FA6-9FFF<br/>4DB6-4DBF<br/>2A6D7-2A6DF<br/>2B735-2B739 | 90<br/>10<br/>9<br/>5 |
| wubi86.extc.dict.yaml | 2A700-2B734 | 4149 |
| wubi86.extd.dict.yaml | 2B740-2B81D | 222 |
| wubi86.exte.dict.yaml | 2B820-2CEA1 | 5762 |
| wubi86.extf.dict.yaml | 2CEB0-2EBE0 | 7473 |
| wubi86.extg.dict.yaml | 30000-3134A | 4939 |

按照[叶典](http://yedict.com/)的说法，`wubi86.extext.dict.yaml` 的四个部分分别叫做：基本区补充、扩展 A 补充、扩展 B 补充、扩展 C 补充。

## 使用注意

第一，这些码表有“容错码”，放在每个码表的末尾，用注释 `#容错码` 隔开。容错码同时也总结在了 `summary.txt` 中，可以用来参考。请注意，容错码的正异只是我主观的看法。容错码出现的原因如下：

* 86 五笔自己存在“容错码”。86 五笔有一些繁体字根，一些使用繁体字根的繁体字，会有两种拆法。如“齒”字，既可以是 `hbj`，也可以是 `hwwb`。
* 一些汉字字形比较奇怪，结构难以判断，五笔码不好确定。如“𪭃”字，既是 `nghl`，也是 `nfll`。
* 一些汉字在不同字库中的字形不一样。如“鿃”字，本来应该是⿰目㚒，`hdty`，但 SimSun-ExtB 字体做成了⿰目夾，`hdww`。这两种都收了。所有的字要是都这么处理，就太难了，所以在这一方面做得不完全。主要参考的字库字形是天珩全字库（见最后）。
* 编写的时候参考了 [rime/rime-wubi](https://github.com/rime/rime-wubi) 的 `wubi86.dict.yaml` 这个原本的词库。例如“𠕄”字，它作 `mmgg`，所以这里的“𫩦”字既是 `kmgm`，又是 `kmmg`。
* 我想在码表里面放一点彩蛋。

第二，编写码表的时候，使用的**字形标准是尽量跟随中国大陆（内地）标准的**。例如，遇到的部件“爭”一律作“争”处理。值得注意的是，**[rime/rime-wubi](https://github.com/rime/rime-wubi) 的 `wubi86.dict.yaml` 没有特意把字形全部改为中国大陆（内地）标准的**，比如“𨼳”字，作 `bbkf`，这是台湾字形。同时，它对字根的处理也不太一样，比如“𡆢”字，作 `lqi`，而我会认为作 `lnv`。

总之，在把这个码表和原有码表一起使用的时候，输入时可能要**思考并尝试汉字的各种笔顺、拆分和结构**，这样才更有可能打出想要的汉字。

## 导入

可以参考 [lotem](https://github.com/lotem) 的[导入码表示例](https://gist.github.com/lotem/5443073)进行操作。

具体地，要将 `wubi86.extext.dict.yaml` 和 `wubi86.extc.dict.yaml` 导入 `wubi86.dict.yaml`，就要在 `wubi86.dict.yaml` 的 `---` 和 `...` 之间写上：

```
import_tables:
  - wubi86.extext
  - wubi86.extc
```

以此类推。

## 感谢

* 软件：[BablePad](https://www.babelstone.co.uk/Software/BabelPad.html)；
* 字库：[天珩全字库](http://cheonhyeong.com/Simplified/download.html)；
* 字库：SimSun-ExtB。
