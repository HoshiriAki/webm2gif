import os
import imageio
import argparse
import logging
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

# 获取可执行文件所在目录
executable_directory = os.path.dirname(os.path.realpath(sys.executable if getattr(sys, 'frozen', False) else __file__))
log_file_path = os.path.join(executable_directory, "webm2gif.log")

def setup_logging():
    # 设置日志配置
    logging.basicConfig(filename=log_file_path, level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(message)s", filemode='a')
    return log_file_path
def convert_webm_to_gif_single(input_path, output_path, loop):
    try:
        # 处理单个文件的WebM到GIF转换
        logging.info(f"Processing file: {input_path}")

        with imageio.get_reader(input_path) as reader:
            fps = reader.get_meta_data()['fps']
            duration = reader.get_meta_data()['duration']

            with imageio.get_writer(output_path, duration=duration, fps=fps, loop=loop) as writer:
                for frame in reader:
                    writer.append_data(frame)

        logging.info(f"Conversion of {input_path} to {output_path} completed successfully")

    except Exception as e:
        # 处理异常
        logging.error(f"Error converting {input_path}. {str(e)}", exc_info=True)
        print(f"Error converting {input_path}. Check the log file ({log_file_path}) for details.")

def convert_webm_to_gif(input_path, output_folder, loop):
    try:
        # 处理输入路径，支持单个文件或整个文件夹
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        webm_files = []

        if os.path.isfile(input_path) and input_path.lower().endswith('.webm'):
            webm_files = [input_path]
        elif os.path.isdir(input_path):
            webm_files = [os.path.join(input_path, filename) for filename in os.listdir(input_path) if filename.endswith(".webm")]
        else:
            raise ValueError("Invalid input path. Please provide a valid file or directory path.")

        with ThreadPoolExecutor() as executor:
            tasks = []
            for filename in webm_files:
                output_path = os.path.join(output_folder, os.path.splitext(os.path.basename(filename))[0] + ".gif")
                tasks.append(executor.submit(convert_webm_to_gif_single, filename, output_path, loop))

            for _ in tqdm(tasks, desc="Converting", unit="file"):
                pass

    except Exception as e:
        # 处理异常
        logging.error(f"An error occurred. {str(e)}", exc_info=True)
        print(f"An error occurred. Check the log file ({log_file_path}) for details.")

def main():
    # 命令行参数解析
    parser = argparse.ArgumentParser(description="Convert WebM to GIF",
                                     epilog="The program will generate a log file named 'webm2gif.log' in the same directory, containing information about the conversion process, any errors encountered, and the exit status of the program.")
    parser.add_argument("-i", "--input", help="Input directory or single WebM file", required=True)
    parser.add_argument("-o", "--output", help="Output directory for GIF files", required=True)
    # 添加 loop 参数，默认为 0 表示无限循环
    parser.add_argument("-l", "--loop", help="Number of times the GIF will loop (0 for infinite)", type=int, default=0)

    args, _ = parser.parse_known_args()

    # 确保输出目录存在
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    # 设置日志
    setup_logging()

    logging.info(f"Input path: {args.input}")
    logging.info(f"Output path: {args.output}")

    convert_webm_to_gif(args.input, args.output, args.loop)

    logging.info("All tasks completed. Exiting.")

if __name__ == "__main__":
    main()
