file = input("File name: ").lower().strip().split(".")

if file[1].find("jpg") == 0 or file[1].find("jpeg") == 0:
    print("image/jpeg")
elif file[1].find("gif") == 0:
    print("image/gif")
elif file[1].find("png") == 0:
    print("image/png")
elif file[1].find("pdf") == 0:
    print("application/pdf")
elif file[1].find("txt") == 0:
    print("txt/plain")
elif file[1].find("zip") == 0:
    print("application/zip")
else:
    print("application/octet-stream")

