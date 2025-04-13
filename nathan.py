import os

def get_android_details():
    details = {}
    
    try:
        details['Android Version'] = os.popen('getprop ro.build.version.release').read().strip()
        details['SDK Version'] = os.popen('getprop ro.build.version.sdk').read().strip()
        details['Device Model'] = os.popen('getprop ro.product.model').read().strip()
        details['Manufacturer'] = os.popen('getprop ro.product.manufacturer').read().strip()
        details['Hardware'] = os.popen('getprop ro.hardware').read().strip()
        details['Bootloader'] = os.popen('getprop ro.bootloader').read().strip()
        details['Radio Version'] = os.popen('getprop gsm.version.baseband').read().strip()
        details['Build ID'] = os.popen('getprop ro.build.id').read().strip()
        details['Build Fingerprint'] = os.popen('getprop ro.build.fingerprint').read().strip()
    except Exception as e:
        details['Error'] = str(e)
    
    return details

if __name__ == "__main__":
    android_details = get_android_details()
    
    # Imprime os detalhes do Android
    for key, value in android_details.items():
        print(f"{key}: {value}")
    
    # Insere os detalhes do Android em um arquivo de log para referência futura
    with open("android_details_log.txt", "a") as log_file:
        for key, value in android_details.items():
            log_file.write(f"{key}: {value}\n")
        log_file.write("\n")
