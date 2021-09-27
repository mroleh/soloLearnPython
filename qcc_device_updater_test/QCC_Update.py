import subprocess
import os
import glob

path = os.getcwd()
print('Get current working directory :      ', path)
qcc_folder_path = os.getcwd() + '\\QCC_cardo_pscli_ver_0.7'


def read_ps_key(ps_key_number):
    output = subprocess.getoutput("cardo_pscli usb read " + ps_key_number)

    output_line = output.split("\n")

    output_line_value = output_line[2].split("0x")
    output_line_value.remove(output_line_value[0])

    ps_key_value = ""
    for i in output_line_value:
        temp_value = "0x" + i
        ps_key_value += temp_value

    print(ps_key_value)
    return ps_key_value


def write_ps_key(ps_key_number, ps_key_value):
    set_ps_key18 = subprocess.getoutput("cardo_pscli usb write " + ps_key_number + " " + ps_key_value)
    print(set_ps_key18)


def read_mib():
    print('Get current working directory :      ', qcc_folder_path)

    os.chdir(qcc_folder_path)  # This will change the present working directory
    os.system("Read_MIB.bat")  # Some application invocation I need to do.


def write_mib():
    print('Get current working directory :      ', qcc_folder_path)

    os.chdir(qcc_folder_path)  # This will change the present working directory
    os.system("Write_MIB.bat")  # Some application invocation I need to do.


def find_file():
    os.chdir(path)
    for file in glob.glob('*.xuv'):
        print("Burning this file:   " + file)
        return file


def flash_device_nvs_app():
    var = subprocess.getoutput(
        "nvscmd burn \"" + path + "\\" + find_file() + "\" -usbdbg 100 -deviceid 4 0")

    print(var)
