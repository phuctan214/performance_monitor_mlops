import yaml
import os


def reformat_json(item_json: dict):
    int_numerical_feature = "year"
    config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.yaml")
    with open(config_file_path, "rb") as config_file:
        config = yaml.safe_load(config_file)

    for cat_feature in config["datasets"]["data_car"]["column_mapping"]["categorical_features"]:
        val = item_json[cat_feature]
        val = int(val)
        item_json[cat_feature] = val

    tmp_val = item_json[int_numerical_feature]
    tmp_val = int(tmp_val)
    item_json[int_numerical_feature] = tmp_val

    return item_json


if __name__ == '__main__':
    item = {
        "year": 2018.0,
        "price": 770.0,
        "location": 0,
        "branch": 0,
        "model": 0,
        "origin": 0,
        "km_driven": 0,
        "external_color": 0,
        "internal_color": 0,
        "num_seats": 0,
        "fuels": 1,
        "engine_capacity": 1.0,
        "gearbox": 0,
        "wheel_drive": 1,
        "car_type": 0,
        "prediction": 998.0033333333334
    }
    print(reformat_json(item))
