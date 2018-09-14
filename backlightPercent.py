#/usr/bin/python3

import sys
import subprocess

def get_brightness(which):
    p = subprocess.Popen(['cat', f'/sys/class/backlight/intel_backlight/{which}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    out = out.decode('utf-8')
    err = err.decode('utf-8')

    if err != '':
        print(f'ERROR: {err}')
        sys.exit(1)

    return int(out)


if __name__ == '__main__':
    current_brightness = get_brightness('brightness')
    max_brightness = get_brightness('max_brightness')

    percent = int((current_brightness / max_brightness) * 100)

    print(percent)
