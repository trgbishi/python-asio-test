class Global_Var:
    json_data_id = 0

    @classmethod
    def json_data_id_add(cls):
        cls.json_data_id += 1
        return cls.json_data_id