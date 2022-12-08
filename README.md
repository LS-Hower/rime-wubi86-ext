# rime-wubi86-ext

86 五笔 Unicode 扩展 C、D、E、F 区汉字的 [RIME](https://rime.im/) 词库。正在逐区更新。

如果有错误或者可以改进的地方，请一定要指出。

## 由来

[rime/rime-wubi](https://github.com/rime/rime-wubi) 的 `wubi86.dict.yaml` 只有基本区和扩展 A、B 区的汉字，需要补充。

因为找不到，所以自己来做了。

## 内容

| 文件 | Unicode | 字数 |
| :--- | :------ | :--- |
| wubi86.109.dict.yaml | 9FA6-9FFF<br/>4DB6-4DBF<br/>2A6D7-2A6DF<br/>2B735-2B738 | 90<br/>10<br/>9<br/>4 |
| wubi86.extc.dict.yaml | 2A700-2B734 | 4149 |
| wubi86.extd.dict.yaml | 2B740-2B81D | 222 |
| wubi86.exte.dict.yaml | 2B820-2CEA1 | 5762 |
| wubi86.extf.dict.yaml | 2CEB0-2EBE0 | 7473 |

按照[叶典](http://yedict.com/)的说法，`wubi86.109.dict.yaml` 的四个部分分别叫：基本区补充、扩展 A 补充、扩展 B 补充、扩展 C 补充。

## 使用注意

第一，这些码表有“容错码”，放在每个码表的末尾，用注释 `#容错码` 隔开。容错码同时也总结在了 `summary.txt` 中，可以用来参考。请注意，容错码的正异只是我主观的看法。下面这些情况会产生容错码：

* 86 五笔自己的“容错码”。86 五笔存在一些繁体字根，一些使用繁体字根的字会有两种拆法，如“齒”字，既可以是 `hbj`，也可以是 `hwwb`；
* 一些汉字字形特别、结构难以判断，五笔码不好确定。如“𪭃”字，既是 `nghl`，也是 `nfll`；
* 一些汉字在不同字库中，字形存在分歧，如“鿃”字，本应为⿰目㚒，`hdty`，但 SimSun-ExtB 字体作⿰目夾，`hdww`（要把所有的字都这么处理是很难的，所以这个做得并不完全）；
* 参考了 [rime/rime-wubi](https://github.com/rime/rime-wubi) 的 `wubi86.dict.yaml`。例如“𠕄”字，它作 `mmgg`，所以这里的“𫩦”字既是 `kmgm`，又是 `kmmg`。
* 彩蛋。

第二，这些码表编制时，使用的**字形标准尽量跟随中国大陆（内地）的**。例如，遇到的部件“爭”一律作“争”处理。值得注意的是，**[rime/rime-wubi](https://github.com/rime/rime-wubi) 的 `wubi86.dict.yaml` 似乎并没有特意把字形全部改为中国大陆（内地）标准的**，比如“𨼳”字，作 `bbkf`，这是台湾字形。同时，它对字根的处理也不太一样，比如“𡆢”字，作 `lqi`，而我会认为作 `lnv`。

总之，如果要将这个码表与原有码表混合使用，输入时就要**思考并尝试汉字的各种笔顺、拆分和结构**，这样，才更有可能打出想要的汉字。

## 导入

可以参考 [lotem](https://github.com/lotem) 的[导入码表示例](https://gist.github.com/lotem/5443073)操作。

具体地，要将 `wubi86.109.dict.yaml` 和 `wubi86.extc.dict.yaml` 导入 `wubi86.dict.yaml`，就应该在 `wubi86.dict.yaml` 的 `---` 和 `...` 之间写上：

```
import_tables:
  - wubi86.109
  - wubi86.extc
```

## 感谢

* 软件：[BablePad](https://www.babelstone.co.uk/Software/BabelPad.html)；
* 字库：[天珩全字库](http://cheonhyeong.com/Simplified/download.html)；
* 字库：SimSun-ExtB。
