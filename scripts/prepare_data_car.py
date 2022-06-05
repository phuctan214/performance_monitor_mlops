import pandas as pd
from sklearn.ensemble import RandomForestRegressor


def prepare_data_car(path_data_refer: str, path_data_product: str) -> pd.DataFrame:
    refer_data_car = pd.read_csv(path_data_refer)
    product_data_car = pd.read_csv(path_data_product)

    target = "price"
    numerical_features = ["year", "km_driven", "engine_capacity"]
    categorical_features = ["location", "branch", "model", "origin", "external_color", "internal_color", "num_seats",
                            "fuels", "gearbox", "car_type", "wheel_drive"]

    feature = numerical_features + categorical_features
    model = RandomForestRegressor(random_state=10)
    model.fit(refer_data_car[feature], refer_data_car[target])
    product_data_car["prediction"] = model.predict(product_data_car[feature])

    return product_data_car


if __name__ == '__main__':
    path_refer = "/metrics_app/datasets/data_car/reference.csv"
    path_product = "/metrics_app/datasets/data_car/production.csv"
    product_data_predict = prepare_data_car(path_refer, path_product)
    product_data_predict.to_csv(path_product, index= False)
