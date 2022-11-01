from flask import Flask, session, jsonify, request
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder


def preprocess_data(df, encoder):
    df_y = df["exited"]
    df_x = df.drop(["exited"], axis=1)

    cat_features = ["corporation"]
    df_x_cat = df_x[cat_features].values
    df_x_cont = df_x.drop(*[cat_features], axis=1)

    if not encoder:
        encoder = OneHotEncoder(sparse=False, handle_unknown="ignore")
        df_x_cat = encoder.fit_transform(df_x_cat)
    else:
        df_x_cat = encoder.transform(df_x_cat)
    df_x = np.concatenate([df_x_cat, df_x_cont], axis=1)

    return df_x, df_y, encoder