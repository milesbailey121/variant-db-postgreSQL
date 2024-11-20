import json

def configargs(fpath): 
    """Config loading function which expects JSON config to be formated
        {
            "connection": {
                "type": "database(e.g. mysql or postgreSQL)",
                "config":{
                    "hostname": "hostname",
                    "database": "database",
                    "username": "username",
                    "pwd": "password",
                    "port_id": "port"
                }
            }
        }

    Args:
        fpath (_type_): _description_

    Returns:
        _type_: _description_
    """
    with open(fpath,"r") as config_file:
        connection = json.load(config_file)
    
        db_type = connection.get("connection", {}).get("type")
        db_config = connection.get("connection", {}).get("config", {})
        db_host = db_config.get("hostname")
        db_name = db_config.get("database")
        db_user = db_config.get("username")
        db_password = db_config.get("pwd")
        db_port = db_config.get("port_id")

    return db_type, db_host, db_name, db_user, db_password, db_port