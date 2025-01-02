from calendar import c
import re
from oocana import Context

def read_markdown_file(file_path):
  try:
      with open(file_path, 'r', encoding='utf-8') as file:
          return file.read()
  except FileNotFoundError:
      print(f"Error: 文件 {file_path} 未找到。")
      return None
  except Exception as e:
      print(f"Error: 读取文件时发生错误 - {e}")
      return None


def main(params: dict, context: Context):
  csv_file_3d = params.get("csv_file_3d")
  markdown_file = params.get("markdown")
  if csv_file_3d is None or markdown_file is None:
    raise ValueError("3d_csv_filr parameter is required")
  return { 
    "csv_file_3d": csv_file_3d,
    "image": "https://oomol-flows.oss-cn-hangzhou.aliyuncs.com/colin-watts-2fWZ9jsoIe0-unsplash.jpg",
    "video": "https://oomol-flows.oss-cn-hangzhou.aliyuncs.com/204565-924698132_small.mp4",
    "audio": "https://oomol-flows.oss-cn-hangzhou.aliyuncs.com/celebrated.mp3",
    "markdown": read_markdown_file(markdown_file),
  }
