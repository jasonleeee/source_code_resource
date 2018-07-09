from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QPoint, QSettings, QRect, QTimer ,QVariant  ,QPoint
import time


list_data = [1, 2, 3, 5]
list_data_default = [0,0,0,0]
float_value = 321.321123
p = QPoint(1,2)
setting_file = 'isp_default_test.ini'
settings = QSettings(setting_file, QSettings.IniFormat)
settings.setFallbacksEnabled(False)    # File only, no fallback to registry or or.


a = QVariant(123)
b = QVariant(231)

# settings.beginGroup('isp_default_parameter_values')
# settings.setValue('qp', p)
# settings.setValue('status', True)
# settings.setValue('int_value', 321)
# settings.setValue('float_value', float_value)
# settings.setValue('leve1/int_value', 567)
# settings.setValue('list_value', list_data)
# settings.endGroup()
# settings.sync()

time.sleep(1)

settings.beginGroup('isp_default_parameter_values')
set_bool_qp = settings.value('qp', QPoint(1,1))
set_bool = settings.value('status',False)
set_value = settings.value('int_value',1)
set_flaot_value = settings.value('float_value', type(float_value))
set_lv_value = settings.value('leve1/int_value',1, int)
set_list = settings.value('list_value',list_data_default, type(list_data_default[0]))
settings.endGroup()

print ('set_flaot_value')
print (set_flaot_value)
print (type(set_flaot_value))

print (set_bool)
print (type(set_bool))

print ('set_value')
print (set_value)
print (type(set_value))

print ('set_lv_value')
print (set_lv_value)
print (type(set_lv_value))

print (set_list)
print (type(set_list))
print (type(set_list[0]))

print (set_bool_qp)
print (settings.contains('status'))

test_dict = dict()

def dict_gen():
    gen_dict = dict()
    gen_dict['test1'] = {'param': 1}
    gen_dict['test2'] = {
        'linedit':12,
        'factor':{'param':5}

    }
    return gen_dict

test_dict =  dict_gen()

print (test_dict)

if 'param' in test_dict['test2']['factor']:
    print (True)
else:
    print (False)

for key in test_dict.keys():
    print (key)

temp_dict = dict()
temp_dict['temp'] = 1

for item in temp_dict:
    print (type(temp_dict))
    print (type(temp_dict[item]))

for item in test_dict:
    print (test_dict[item])

print ('(===============================)')
def func(test_dict):
    for key in test_dict:
        if type(test_dict[key]) is not type(test_dict):
            pass
            # print (key)
        else:
            func(test_dict[key])
            print (key)

func(test_dict)
print ('(===============================)')


key_list = list()
cnt=0
def list_dictionary(dictionary, settings):
    global key_list
    global cnt

    for key, value in dictionary.items():
        key_list.append(key)
        cnt += 3
        try:
            print (('.'*cnt)+'Key', key)
            if 'param' == key:
                print (key_list)
                setting_key = str()
                for list_item in key_list[:-1]:
                    setting_key += list_item + "/"
                print (setting_key[:-1])
                settings.setValue(setting_key[:-1], value)
            list_dictionary(value, settings)
        except AttributeError:
            print ('Value:' + str(value) + '\n')
        finally:
            cnt -= 3
            key_list.pop(-1)


setting_file = 'test.ini'
settings = QSettings(setting_file, QSettings.IniFormat)
settings.setFallbacksEnabled(False)    # File only, no fallback to registry or or.
settings.beginGroup('isp_default_parameter_values')
list_dictionary(test_dict ,settings)
settings.endGroup()
settings.sync()

