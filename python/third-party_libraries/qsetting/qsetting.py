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
    gen_dict['test3'] = {
    'linedit':12
    }
    gen_dict['test4'] = {
        'linedit':12,
        'factors':{'factors':{'param':10}}
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

param_dict_key_list = []
save_dict = {}
def param_dict_to_settings_dict(param_dict, settings_dict={}, key_list=[]):
    if isinstance(param_dict, dict):
        for key, value in param_dict.items():
            key_list.append(key)
            if 'param' == key:
                setting_key = str()
                value = 10
                for list_item in key_list[:-1]:
                    setting_key += list_item + "/"
                settings_dict[setting_key[:-1]] = {'param': value}
            else:
                param_dict_to_settings_dict(value, settings_dict, key_list)
            key_list.pop(-1)
    return settings_dict

def list_gen_dict(param_dict, key_list):
    if len(key_list) == 0:
        param_dict = {'param': 0}
        return param_dict
    else:
        key = key_list[0]
        temp_dict = dict()
        if key in param_dict:
            param_dict[key] = list_gen_dict(temp_dict, key_list[1:])
        else:
            param_dict[key] = list_gen_dict(temp_dict, key_list[1:])
    return param_dict

def settings_dict_to_param_dict(settings_dict, param_dict={}, key_list=[]):
    for key, value in settings_dict.items():
        key_list = key.split('/')
        print ('key_list', key_list)
        temp_dict = param_dict
        for itm in list(reversed(key_list)):
            loop_dict = {}
            loop_dict[itm] = temp_dict
            temp_dict = loop_dict
        for key, value in loop_dict.items():
            param_dict[key] = value
    return param_dict

def param_dict_copy(dest_dict, src_dict, key=''):
    if isinstance(src_dict, dict):
        for key in src_dict:
            try:
                if 'param' == key:
                    dest_dict[key] = src_dict[key]
                else:
                    param_dict_copy(dest_dict[key], src_dict[key], key)
            except AttributeError:
                return False
            except KeyError:
                return False
        return True


 
def deepSearch(dict1, dict2):
    if isinstance(dict2, dict):
        for key in dict2.keys():
            if key not in dict1.keys():
                dict1[key] = dict2[key]
            else:
                if 'param' == key and isinstance(dict2[key], int):
                    dict1[key] = dict2[key]
                deepSearch(dict1[key], dict2[key])



setting_file = 'test.ini'
settings = QSettings(setting_file, QSettings.IniFormat)
settings.setFallbacksEnabled(False)    # File only, no fallback to registry or or.
settings.beginGroup('isp_default_parameter_values')
# list_dictionary(test_dict ,settings)
save_dict = param_dict_to_settings_dict(test_dict)
settings.endGroup()
settings.sync()

print ('test_dict', test_dict)
print ('save_dict', save_dict)
temp_param_dict = settings_dict_to_param_dict(save_dict)
print ('temp_param_dict', temp_param_dict)
rst = param_dict_copy(test_dict, temp_param_dict)
print ('test_dict', test_dict)
test_dict['test1']['hello'] = 120
print ('test_dict', test_dict)
print (rst)
param_dict = dict()
key_list = ['1231', 'adb', '23e1']
list_gen_dict(param_dict, key_list)
print (param_dict)
param_dict_new = dict()
key_list = ['1231', 'adb', 'lishijie']
list_gen_dict(param_dict_new, key_list)
print (param_dict)
merge_dict = {'1231': {'adb': {'lishijie': {'param': 0}}}}
param_dict = {'1231': {'new': {'lishijie': {'param': 1}}}}
print (param_dict)
print (merge_dict)
deepSearch(merge_dict, param_dict)
print (merge_dict)

