# rime-wubi86-ext

RIME 86五笔 扩展区汉字词库。

因为找不到，所以自己来做了。会做得很慢。

都是单字。

使用了天珩全字库显示汉字。

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
