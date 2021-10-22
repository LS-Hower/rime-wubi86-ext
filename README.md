# rime-wubi86-ext

RIME 86五笔 扩展区汉字等的词库。

因为找不到，所以自己来做了。

都是单字。

汉字显示使用了 SimSun-ExtB 和天珩全字库。

## 使用方法（Windows）

将`wubi86.extc.dict.yaml`等文件放在`Rime`目录下。

找到`wubi86.custom.yaml`或`wubi86.schema.yaml`中设定的词典（`translator/dictionary`）（默认是`wubi86.dict.yaml`），在`...`上方添加：

```
import_tables:
  - wubi86.extc.dict.yaml
  - wubi86.extd.dict.yaml
  ...
```

保存部署即可。
