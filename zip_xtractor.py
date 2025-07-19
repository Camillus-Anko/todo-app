import zipfile

def extractor_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)




if __name__ == "__main__":
    extractor_archive("/home/notion/Desktop/course/Ardit - Python/Files/compressed.zip",
    "/home/notion/Desktop/course/Ardit - Python/Files/Files")