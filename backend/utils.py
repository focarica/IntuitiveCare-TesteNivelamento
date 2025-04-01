import zipfile

def zipFiles(files: list, folderToZip: str) -> None:
    with zipfile.ZipFile(folderToZip, 'w') as zipf:
        for file in files:
            zipf.write(file, arcname=file.split('/')[-1]) 
    
    
def unzipFiles(zippedFolder: str, dest: str) -> None: 
    with zipfile.ZipFile(zippedFolder, 'r') as zipf:
        zipf.extractall(dest)
        