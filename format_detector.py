import magic


def format_detector(file_path):
    mime = magic.Magic()
    file_type = mime.from_file(file_path)
    return file_type
