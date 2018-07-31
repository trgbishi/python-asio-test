import json
import sys
sys.path.append('C:\\Users\\kdgz\\Desktop\\collector')
from comm.asio.model.global_var_model import Global_Var
'''
* { 
*     "jsonrpc" : 2.0,
*     "method" : "sayHello", 
*     "params" : ["data"], 
*     "id" : 1
* } 
'''
class Json_Data:
    def __init__(self,tmp_list):
        self.__jsonrpc = 2.0
        self.__method = 'sayHello'
        self.__params = tmp_list
        self.__id = Global_Var.json_data_id_add()

    @property
    def params(self):
        return self.__params

    @params.setter
    def params(self,tmp_list):
        self.__params = tmp_list 
        self.__id = Global_Var.json_data_id_add()

        

    def json(self):
        tmp_dict = {}
        tmp_dict['jsonrpc'] = self.__jsonrpc
        tmp_dict['method']  = self.__method
        tmp_dict['params']  = self.__params
        tmp_dict['id']      = self.__id
        return json.dumps(tmp_dict)


