# rime-wubi86-ext

86 五笔扩展区汉字等的 RIME 词库。

## 内容

* Unicode 扩展 C 区至 G 区的汉字。

* 基本区补充（9FA6-9FFF）、扩展 A 区补充（4DB6-4DBF）和扩展 B 区补充（2A6D7-2A6DF）。

[rime/rime-wubi](github.com/rime/rime-wubi) 的`wubi86.dict.yaml`有收录基本区、扩展 A 区和扩展 B 区的汉字，但三个“补充”处的没有收全。

* CJK 笔画（31C0-31E3）。

## 使用方法（Windows）

以`wubi86.cjk_strokes.dict.yaml`和`wubi86.extd.dict.yaml`为例。

1. 将这两个文件放在`Rime`目录下；

2. 找到`wubi86.custom.yaml`或`wubi86.schema.yaml`中设定的词典（默认是`wubi86.dict.yaml`）；

3. 在里面的`...`上方添加

```
import_tables:
  - wubi86.cjk_strokes.dict.yaml
  - wubi86.extd.dict.yaml
```
；

4. 保存部署。

## 制作

* 汉字显示使用了 SimSun-ExtB 和天珩全字库。

* 跟随中国大陆（内地）的字形标准。笔顺等细节尽量跟随 86 五笔的标准。

* 很可能出现错误。

* 学业为重，由于课业因素，2024 年之前不太可能完成。
