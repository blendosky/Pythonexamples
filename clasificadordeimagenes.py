import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import math

datos, metadatos = tfds.load('fashion_mnist', as_supervised=True, with_info=True)

print("descarga completa...")

datos_entrena, datos_prueb = datos['train'], datos['test']

nombres_clases = metadatos.features['label'].names


def norm(imagenes, etiquetas):
    imagenes = tf.cast(imagenes, tf.float32)
    imagenes /= 255
    return imagenes, etiquetas


datos_entrena = datos_entrena.map(norm)
datos_prueb = datos_prueb.map(norm)

datos_entrena = datos_entrena.cache()
datos_prueb = datos_prueb.cache()

for imagen, etiqueta in datos_entrena.take(1):
    break
imagen = imagen.numpy().reshape((28,28))

plt.figure()
plt.imshow(imagen, cmap=plt.cm.binary)
plt.colorbar()
plt.grid(False)
plt.show()


plt.figure(figsize=(10,10))
for i, (imagen, etiqueta) in enumerate(datos_entrena.take(25)):
    imagen = imagen.numpy().reshape((28,28))
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(imagen, cmap=plt.cm.binary)
    plt.xlabel(nombres_clases[etiqueta])

plt.show()

#modelo

modelo = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28,1)),
    tf.keras.layers.Dense(50, activation=tf.nn.relu),
    tf.keras.layers.Dense(50,activation=tf.nn.relu),
    tf.keras.layers.Dense(10,activation=tf.nn.softmax)
])

modelo.compile(
    optimizer='adam',
    loss = tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=['accuracy']
)

#lotes

tamano_lote = 32

num_datentrena = metadatos.splits["train"].num_examples
num_datposval = metadatos.splits["test"].num_examples


datos_entrena = datos_entrena.repeat().shuffle(num_datentrena).batch(tamano_lote)
datos_prueb = datos_prueb.batch(tamano_lote)

hist = modelo.fit(datos_entrena, epochs=5, steps_per_epoch= math.ceil(num_datentrena/tamano_lote))

plt.figure()
plt.ylabel("Error")
plt.xlabel("Epoca")
plt.plot(hist.history["loss"])
plt.show()