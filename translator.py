import os
os.environ["KERAS_BACKEND"] = "tensorflow"
import tensorflow as tf
import openvino as ov

def main():
    print('Starting translation...')
    loaded = tf.keras.models.load_model('squeezenet.keras')
    loaded.load_weights('squeezenet.weights.h5')
    loaded.summary()
    loaded.export('squeeze_base')
    print('translated')
    ov.convert_model('squeeze_base')
    pass

if __name__ == "__main__":
    main()
