

extension_mime_map = {
    "csv": "text/csv"
}


def mime_type_for_file(path: str):
    last_dot = path.rfind('.') - len(path) + 1
    extension = path[last_dot:]
