import jpype


#    libjvm.so path like;
#   "/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/amd64/server/libjvm.so"

## zemberek jar path
## /home/<user_name>/PycharmProjects/<proje_name>/../zemberek/zemberek-tum-2.0.jar


def zemberek(libjvmpath, zemberekJarpath):
    jpype.startJVM(libjvmpath, "-Djava.class.path=" + zemberekJarpath, "-ea")
    Tr = jpype.JClass("net.zemberek.tr.yapi.TurkiyeTurkcesi")
    tr = Tr()
    Zemberek = jpype.JClass("net.zemberek.erisim.Zemberek")
    zemberek_r = Zemberek(tr)
    return zemberek_r
