import hashlib

def calculateChecksum(fileName):
    fobj = open(fileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
    fobj.close()

    return hobj.hexdigest()


def main():
    checksum = calculateChecksum("Hello.txt")
    print("Checksum is : ",checksum)

if __name__ == "__main__":
    main()