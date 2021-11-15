# Batch-rename
 批量重命名腾讯问卷文件

`./source/config.json` 文件为配置文件，在这里改配置就行

## 配置参数说明

`./source/config.json` 文件为配置文件，在这里改配置就行

1. `csvPath`：从腾讯问卷导出的 `.csv` 文件位置
2. `needRename`：从腾讯问卷批量导出的文件
3. `renamed`：重命名之后的文件
4. `separator`：分隔符
5. `subname`：新文件名单个部分列表。A 列为 1，L 为 11，M 为 12，一次类推

## 发行版

`./release` 目录下 `renamer.exe` 为发行版，不需要 python 环境，双击运行即可

