from PIL import Image
import tensorflow as tf
import os
import numpy as np
import pandas as pd
import streamlit as st

class_names = [
        "apple_pie",
        "baby_back_ribs",
        "baklava",
        "beef_carpaccio",
        "beef_tartare",
        "beet_salad",
        "beignets",
        "bibimbap",
        "bread_pudding",
        "breakfast_burrito",
        "bruschetta",
        "caesar_salad",
        "cannoli",
        "caprese_salad",
        "carrot_cake",
        "ceviche",
        "cheesecake",
        "cheese_plate",
        "chicken_curry",
        "chicken_quesadilla",
        "chicken_wings",
        "chocolate_cake",
        "chocolate_mousse",
        "churros",
        "clam_chowder",
        "club_sandwich",
        "crab_cakes",
        "creme_brulee",
        "croque_madame",
        "cup_cakes",
        "deviled_eggs",
        "donuts",
        "dumplings",
        "edamame",
        "eggs_benedict",
        "escargots",
        "falafel",
        "filet_mignon",
        "fish_and_chips",
        "foie_gras",
        "french_fries",
        "french_onion_soup",
        "french_toast",
        "fried_calamari",
        "fried_rice",
        "frozen_yogurt",
        "garlic_bread",
        "gnocchi",
        "greek_salad",
        "grilled_cheese_sandwich",
        "grilled_salmon",
        "guacamole",
        "gyoza",
        "hamburger",
        "hot_and_sour_soup",
        "hot_dog",
        "huevos_rancheros",
        "hummus",
        "ice_cream",
        "lasagna",
        "lobster_bisque",
        "lobster_roll_sandwich",
        "macaroni_and_cheese",
        "macarons",
        "miso_soup",
        "mussels",
        "nachos",
        "omelette",
        "onion_rings",
        "oysters",
        "pad_thai",
        "paella",
        "pancakes",
        "panna_cotta",
        "peking_duck",
        "pho",
        "pizza",
        "pork_chop",
        "poutine",
        "prime_rib",
        "pulled_pork_sandwich",
        "ramen",
        "ravioli",
        "red_velvet_cake",
        "risotto",
        "samosa",
        "sashimi",
        "scallops",
        "seaweed_salad",
        "shrimp_and_grits",
        "spaghetti_bolognese",
        "spaghetti_carbonara",
        "spring_rolls",
        "steak",
        "strawberry_shortcake",
        "sushi",
        "tacos",
        "takoyaki",
        "tiramisu",
        "tuna_tartare",
        "waffles",
    ]

current_path = os.getcwd()

@st.cache(allow_output_mutation=True)
def load_model():
    """
    Loads the model
    """
    model_path = os.path.join(current_path, "statics", 'food_vision.h5')
    model = tf.keras.models.load_model(model_path)
    return model

def preprocess_image(image_path, image_shape):
    image = Image.open(image_path)
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.image.resize(image, [image_shape, image_shape])
    if image.shape[2] == 4:
        image = image[:, :, :3]
    if image.numpy().max() > 1:
        pass
    else:
        image = image * 255
    image = tf.cast(image, tf.float32)
    image = tf.expand_dims(image, 0)
    return image

def predict(image_path, image_shape=224, n=5):
    """
    Predicts image using model
    """
    image = preprocess_image(image_path, image_shape)
    model = load_model()
    preds = model.predict(image)
    sorted_pred = preds.argsort()
    top_preds = list(preds[0][sorted_pred[0][-n:]])
    top_classes = list(np.array(class_names)[sorted_pred[0][-n:]])
    top_preds.reverse(), top_classes.reverse()
    predictions = pd.DataFrame({'Food': top_classes, 'Probability': top_preds})
    predictions["Probability"] = np.round(predictions["Probability"]*100,2)
    return predictions