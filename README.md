# rime-wubi86-ext

(更新中) 86 五笔扩展 C、D 区汉字的 [RIME](https://rime.im/) 词库。

以后会逐区地加上更多汉字。

如果有错误或可以改进的地方，请务必指出。

## 由来

[rime/rime-wubi](https://github.com/rime/rime-wubi) 的 `wubi86.dict.yaml` 只有基本区和扩展 A、B 区的汉字，仍需补充。

因为找不到补充的，所以自己来做了。

## 特点

尽量跟随中国大陆（内地）的字形标准。例如，遇到部件“爭”时一律作“争”处理。

有容错码。置于每个码表的后部，用一行注释 `#容错码` 隔开。同时总结在 `summary.txt` 中，用于参考。

* 86 五笔自己存在一些繁体字根，如“齒”字既可以是 `hbj`，也可以是 `hwwb`；
* 一些汉字字形清奇、结构难以判断，设置容错码。如“𪭃”字，既是 `nghl`，也是 `nfll`。
* 一些汉字不同字库字形有分歧，如“鿃”字，本应为⿰目㚒，`hdty`，但 SimSun-ExtB 字体作⿰目夾，`hdww`。

请注意，容错码的正异只是主观判断。

## 内容

| 文件 | Unicode | 字数 |
| :--- | :------ | :--- |
| wubi86.109.dict.yaml | 9FA6-9FFF<br/>4DB6-4DBF<br/>2A6D7-2A6DF<br/>2B735-2B738 | 90<br/>10<br/>9<br/>4 |
| wubi86.extc.dict.yaml | 2A700-2B734 | 4149 |
| wubi86.extd.dict.yaml | 2B740-2B81D | 222 |

按[叶典](http://yedict.com/)的说法，`wubi86.109.dict.yaml`的四部分叫做基本区补充、扩展 A 补充、扩展 B 补充、扩展 C 补充。

## 导入

可以参考 [lotem](https://github.com/lotem) 的[导入码表示例](https://gist.github.com/lotem/5443073)。

具体地，比如要将`wubi86.109.dict.yaml`和`wubi86.extc.dict.yaml`导入`wubi86.custom.dict.yaml`，就要在`wubi86.custom.dict.yaml`的`---`和`...`之间写上：
```
import_tables:
  - wubi86.109
  - wubi86.extc
```

## 感谢

* 软件：[BablePad](https://www.babelstone.co.uk/Software/BabelPad.html)；
* 字库：[天珩全字库](http://cheonhyeong.com/Simplified/download.html)；
* 字库：SimSun-ExtB。
