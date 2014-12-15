from . import festival
import six
import subprocess

def textToWav(text):
    if not isinstance(text, six.text_type):
        text = text.decode('utf-8')
    wav_file = festival._textToWav(text)
    cmd = "lame --quiet -V 9 %s -" % wav_file
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

def sayText(text):
    if not isinstance(text, six.text_type):
        text = text.decode('utf-8')
    festival._sayText(text)

