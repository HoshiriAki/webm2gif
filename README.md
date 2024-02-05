<div align="center">

# WebM to GIF Converter
[English](README.md) | [简体中文](README_zh.md)

</div>


## Introduction

This is an executable version of the WebM to GIF Converter, a Python script that converts WebM video files to GIF format.

## Requirements

No external dependencies are required to run the executable. 

## Download

Download the executable file here: [webm2gif.exe](webm2gif.exe)

## Usage

1. Open a command prompt in the directory where the executable is located.

2. Run the following command to convert a single WebM file:
   ```bash
   webm2gif.exe -i <input_webm_file.webm> -o <output_gif_folder>
   ```
   - `-i` or `--input`: Input WebM file.
   - `-o` or `--output`: Output directory for GIF files.

3. Run the following command to convert all WebM files in a directory:
   ```bash
   webm2gif.exe -i <input_webm_folder> -o <output_gif_folder>
   ```

## Logging

The program generates a log file named `webm2gif.log` in the same directory. It includes information about the conversion process, any errors encountered, and the program's exit status.

## Examples

Convert a single WebM file:
```bash
webm2gif.exe -i input_folder/input.webm -o output_folder
```

Convert all WebM files in a directory:
```bash
webm2gif.exe -i input_folder -o output_folder
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
