<div align="center">

# WebM to GIF 转换
[English](README.md) | [简体中文](README_zh.md)

</div>

## 简介

这是 WebM 到 GIF 转换器的可执行版本，是一个将 WebM 视频文件转换为 GIF 格式的 Python 脚本。

## 系统要求

运行可执行文件无需任何外部依赖。

## 下载

在这里下载可执行文件：[webm2gif.exe](dist/webm2gif.exe)

## 使用方法

1. 在可执行文件所在目录打开命令提示符或终端。

2. 运行以下命令以转换单个 WebM 文件：
   ```bash
   webm2gif.exe -i <输入文件.webm> -o <GIF输出目录> -l <循环次数>
   ```
   - `-i` 或 `--input`：输入的 WebM 文件。
   - `-o` 或 `--output`：GIF 文件的输出目录。
   - `-l` 或 `--loop`: 设置图像循环次数，默认为0(无限循环)

3. 运行以下命令以转换目录中的所有 WebM 文件：
   ```bash
   webm2gif.exe -i <webm输入目录> -o <GIF输出目录>
   ```

## 日志记录

程序会在相同目录下生成一个名为 `webm2gif.log` 的日志文件。其中包含了转换过程的信息、遇到的任何错误以及程序的退出状态。

## 使用示例

转换单个 WebM 文件：
```bash
webm2gif.exe -i input_folder/input.webm -o output_folder
```

转换目录中的所有 WebM 文件：
```bash
webm2gif.exe -i input_folder -o output_folder
```

## 许可证

该项目采用 MIT 许可证进行授权 - 详细信息请查看 [LICENSE](LICENSE) 文件。
