def main():
    fileName = input("File name: ")
    print(processMediaType(fileName))

def processMediaType(fileName):
    extension = processFileName(fileName)

    match extension:
        case "gif" | "jpeg" | "png":
            return "image/" + extension
        case "pdf" | "zip":
            return "application/" + extension
        case "txt":
            return "text/plain"
        case _:
            return "application/octet-stream"

def processFileName(fileName):
    extension = fileName.strip().split(".")[-1].lower()
    if extension == "jpg":
        return "jpeg"
    else:
        return extension

main()