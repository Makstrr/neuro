import keras

model = keras.models.load_model('model1')


def pred(x):
    pred = model.predict(x)
    return(pred[-1])