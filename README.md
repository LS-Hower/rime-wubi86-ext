# rime-wubi86-ext

86 五笔 Unicode 扩展区 C 至 H 区汉字 [RIME](https://rime.im/) 词库。

如果有错误或者可以改进的地方，请指出。

## 由来

原版 [rime/rime-wubi](https://github.com/rime/rime-wubi) 的 `wubi86.dict.yaml` 覆盖了基本区和扩展 A、B 区的汉字，但需要补充。

这是那个原版码表有的字：

| 字区   | Unicode 码点      | 字数    |
| :----- | :---------------: | ------: |
| 基本区 |  `4E00` - `9FA5`  | `20902` |
| 扩展 A |  `3400` - `4DB5`  |  `6582` |
| 扩展 B | `20000` - `2A6D6` | `42711` |

因为当时找不到，所以自己来做了。

所以这是这个词库有的字：

| 码表               | 字区        | Unicode 码点      | 字数   |
| :----------------- | :---------- | :---------------: | -----: |
| `wubi86.basiccmpl` | 基本区补充  |  `9FA6` - `9FFF`  |   `90` |
| `wubi86.extacmpl`  | 扩展 A 补充 |  `4DB6` - `4DBF`  |   `10` |
| `wubi86.extbcmpl`  | 扩展 B 补充 | `2A6D7` - `2A6DF` |    `9` |
| `wubi86.extc`      | 扩展 C      | `2A700` - `2B734` | `4149` |
| `wubi86.extccmpl`  | 扩展 C 补充 | `2B735` - `2B739` |    `5` |
| `wubi86.extd`      | 扩展 D      | `2B740` - `2B81D` |  `222` |
| `wubi86.exte`      | 扩展 E      | `2B820` - `2CEA1` | `5762` |
| `wubi86.extf`      | 扩展 F      | `2CEB0` - `2EBE0` | `7473` |
| `wubi86.extg`      | 扩展 G      | `30000` - `3134A` | `4939` |
| `wubi86.exth`      | 扩展 H      | `31350` - `323AF` | `4192` |

`wubi86.basiccmpl` 就是指 `wubi86.basiccmpl.dict.yaml`，以此类推。

## 注意事项

1. 这些码表有“容错码”，即一字多码，同一个字可能可以用两个或多个不同的五笔码。容错码出现的原因如下：

   * 86 五笔自己就有容错码。

     86 五笔有繁体字根，而一些使用繁体字根的繁体字，就会有不止一种拆法。

     如“齒”： `hbj`、 `hwwb`。

   * 扩展区有一大堆字形和结构很难确定的字。

     如“𪭃”： `ngnl`、 `nfll`。

   * 同一个字在不同字体里的字形可能不一样。

     如“鿃”字，本来是⿰目㚒： `hdty`，但 SimSun-ExtB 字体做成了⿰目夾： `hdww`。这两种都收了。

     码表里没有把所有的字都这么处理，因为这样会太费时太费力，意义也不大。

     主要参考的字形是天珩全字库（见最后）的字形。

   * 编写的时候偶尔会参考 [`rime/rime-wubi`](https://github.com/rime/rime-wubi) 的 `wubi86.dict.yaml` 这个“原本的词库”。

     比如它的“𠕄”（↷凹）： `mmgg`，所以“𫩦”（⿰口↷凹）： `kmgm`、 `kmmg`。

   * 我想在码表里面放一点彩蛋。

2. 编写码表的时候，使用的 **字形标准尽量跟随中国大陆（内地）的标准**。

   比如遇到的部件“爭”都当作“争”处理了。

   注意： 上文提到的那个“原本的词库” `wubi86.dict.yaml` 没有特意把字形全部改为中国大陆（内地）标准的，比如它的“𨼳”： `bbkf`，这是台湾字形。

   字根的处理也不太一样，比如它的“𡆢”： `lqi`，而我会认为“𡆢”： `lnv`。

总之，这个码表和“原本的词库”一起使用，输入生僻字时可能要 **思考并尝试各种笔顺、拆分和结构**，这样才更容易打出想要的字。

## 导入

请参考 [lotem](https://github.com/lotem) 的[导入码表示例](https://gist.github.com/lotem/5443073)进行操作。

附上在 Windows 上通常的使用方法：

1. **找到你的 `wubi86` 输入方案正在使用的“主码表”文件。** 打开小狼毫的“用户文件夹”，如果你写过 `wubi86.custom.yaml`，那么在它的 `patch:` 下可能会有 `translator/dictionary:` 项，看它设置成了什么。如果没有，就打开 `wubi86.schema.yaml`，找到 `translator:` 下的 `dictionary:`，看它设置成了什么。例如我的设置成了 `wubi86.custom`，那么我的“主码表”文件就是 `wubi86.custom.dict.yaml`。

2. **导入码表。** 下载这 10 个以 `.dict.yaml` 结尾的码表文件，把它们放进小狼毫的“用户文件夹”。然后在你的“主码表”文件里，在 `---` 与 `...` 两行中间写上：

```
import_tables:
  - wubi86.basiccmpl
  - wubi86.extacmpl
  - wubi86.extbcmpl
  - wubi86.extc
  - wubi86.extccmpl
  - wubi86.extd
  - wubi86.exte
  - wubi86.extf
  - wubi86.extg
  - wubi86.exth
```

3. **重新部署小狼毫。**

注意：如果打不出扩展区字符，可能是因为没有把五笔 86 的从“常用”模式调到“增广”模式。

## 其他一些大字集五笔码表

* [`lxgw/wubi86-super`](https://github.com/lxgw/wubi86-super)
* [`CNMan/UnicodeCJK-WuBi`](https://github.com/CNMan/UnicodeCJK-WuBi)

## 感谢

* 文本编辑器：[BabelPad](https://www.babelstone.co.uk/Software/BabelPad.html)
* 网站：[叶典（字海网）](http://yedict.com/)
* 网站：[字统网](https://zi.tools/)
* 字体：[天珩全字库](http://cheonhyeong.com/Simplified/download.html)
* 字体：SimSun-ExtB
