class MON_DATA:
    def __init__(self,ROOM_ID,IP,METRIC,TAGS,COLL_TIME,COLL_VALUE,alarm_lv):
        self.__ROOM_ID = ROOM_ID #private int ROOM_ID;// NUMBER(10) Y N 机房ID
        self.__IP = IP #private String IP;// VARCHAR2(32) Y N 设备IP
        self.__METRIC = METRIC #private String METRIC;// VARCHAR2(64) Y N 采集指标
        self.__TAGS = TAGS #private String TAGS;// VARCHAR2(64) Y N 标签
        self.__COLL_TIME = COLL_TIME #private long COLL_TIME;// DATE Y N 采集时间
        self.__COLL_VALUE = COLL_VALUE #private double COLL_VALUE;// NUMBER(15,2) Y N 指标值
        self.__alarm_lv = alarm_lv #private int alarm_lv;
	
    def __list__(self):
        data_dict = {}
        data_dict['ROOM_ID'] = self.__ROOM_ID
        data_dict['IP'] = str(self.__IP)
        data_dict['METRIC'] = self.__METRIC
        data_dict['TAGS'] = self.__TAGS
        data_dict['COLL_TIME'] = self.__COLL_TIME
        data_dict['COLL_VALUE'] = self.__COLL_VALUE
        data_dict['alarm_lv'] = self.__alarm_lv
        return data_dict