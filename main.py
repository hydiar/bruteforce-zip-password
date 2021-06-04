import zipfile


def extract(file, passAttempt):
    try:
        file.extractall(pwd=passAttempt)
        return passAttempt
    except:
        return


if __name__ == '__main__':
    zipFilePath = 'test.zip'
    dictFilePath = 'dictionary.txt'
    try:
        zipFile = zipfile.ZipFile(zipFilePath)
    except:
        print("Filepath \'" + zipFilePath + "\' not found")
        exit()
    try:
        pwdDict = open(dictFilePath)
    except:
        print("Filepath \'" + dictFilePath + "\' not found")
        exit()
    for line in pwdDict.readlines():
        pwd = line.strip('\n')
        if attempt := extract(zipFile, pwd):
            print("Password found: " + pwd)
            break
