import os
from config import *

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path, file_path))
        
        if os.path.commonpath([abs_path, target_dir]) != abs_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory' 
        if not os.path.isfile(target_dir):
            return f'Error: File not found or is not a regular file: {file_path}'
        
        with open(target_dir, "r") as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        
        return content
    except Exception as e:
        return f"Error: {e}"







        if not os.path.isdir(target_dir):
            return f'Error: {directory} is not a directory'
        
        files_info: list[str] = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
