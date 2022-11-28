import os

with open("/model/run.sh", "w") as f:
    f.write("cd /model\n")
    f.write("python setup.py develop\n")
    f.write("python /model/hat/test.py -opt /model/options/test/HAT_SRx4_ImageNet-pretrain.yml\n")

os.system("sh /model/run.sh")
