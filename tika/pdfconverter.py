import os
from subprocess import PIPE
from subprocess import run
from zemberek_python.settings import tikaURL
from urllib.request import urlopen
import ssl
import io

ssl._create_default_https_context = ssl._create_unverified_context


class PDFParser:
    def __init__(self, file):
        self.localpath = os.path.dirname(os.path.realpath(__file__)) + '/'  # local path
        self.tikapath = self.localpath + 'tika-app-1.18.jar'  # path to Apache Tika jar file
        self.file = file

    def parse(self):
        if os.path.exists(self.tikapath) == True:
            return self.tika(self.file)
        else:
            print("Downloading tika-app-1.18.jar..")
            with urlopen(tikaURL) as Response:
                Length = Response.getheader('content-length')
                BlockSize = 1000000  # default value

                if Length:
                    Length = int(Length)
                    BlockSize = max(4096, Length // 20)

                print("Blocksize: ", Length, BlockSize)

                BufferAll = io.BytesIO()
                Size = 0
                while True:
                    BufferNow = Response.read(BlockSize)
                    if not BufferNow:
                        break
                    BufferAll.write(BufferNow)
                    Size += len(BufferNow)
                    if Length:
                        Percent = int((Size / Length) * 100)
                        print(f"Download: {Percent}% {tikaURL}")

                print("Buffer All len:", len(BufferAll.getvalue()))
                with open(self.tikapath, 'wb') as f:
                    f.write(BufferAll.getvalue())

            return self.tika(self.file)

    def tika(self, file):
        command = ['java', '-jar', self.tikapath, '-t', file]  # command line for Apache Tika parser
        result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)  # run command
        content = result.stdout  # get command line output as file content
        return content
