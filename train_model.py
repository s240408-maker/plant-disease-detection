<<<<<<< HEAD
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models

# Dataset path
dataset_path = "dataset/PlantVillage/color"

# Image settings
img_size = (128, 128)
batch_size = 16

# Data preprocessing
datagen = ImageDataGenerator(
rescale=1./255,
validation_split=0.2
)

train_data = datagen.flow_from_directory(
dataset_path,
target_size=img_size,
batch_size=batch_size,
class_mode='categorical',
subset='training'
)

val_data = datagen.flow_from_directory(
dataset_path,
target_size=img_size,
batch_size=batch_size,
class_mode='categorical',
subset='validation'
)

# Simple CNN model
model = models.Sequential([
layers.Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
layers.MaxPooling2D(2,2),

layers.Conv2D(64, (3,3), activation='relu'),
layers.MaxPooling2D(2,2),

layers.Flatten(),
layers.Dense(64, activation='relu'),
layers.Dense(train_data.num_classes, activation='softmax')
])

# Compile
model.compile(
optimizer='adam',
loss='categorical_crossentropy',
metrics=['accuracy']
)

# Train
model.fit(
train_data,
validation_data=val_data,
epochs=25
)

# Save model
model.save("model/plant_model.h5")

=======
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models

# Dataset path
dataset_path = "dataset/PlantVillage/color"

# Image settings
img_size = (128, 128)
batch_size = 16

# Data preprocessing
datagen = ImageDataGenerator(
rescale=1./255,
validation_split=0.2
)

train_data = datagen.flow_from_directory(
dataset_path,
target_size=img_size,
batch_size=batch_size,
class_mode='categorical',
subset='training'
)

val_data = datagen.flow_from_directory(
dataset_path,
target_size=img_size,
batch_size=batch_size,
class_mode='categorical',
subset='validation'
)

# Simple CNN model
model = models.Sequential([
layers.Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
layers.MaxPooling2D(2,2),

layers.Conv2D(64, (3,3), activation='relu'),
layers.MaxPooling2D(2,2),

layers.Flatten(),
layers.Dense(64, activation='relu'),
layers.Dense(train_data.num_classes, activation='softmax')
])

# Compile
model.compile(
optimizer='adam',
loss='categorical_crossentropy',
metrics=['accuracy']
)

# Train
model.fit(
train_data,
validation_data=val_data,
epochs=25
)

# Save model
model.save("model/plant_model.h5")

>>>>>>> d2b87dc07c3ba2ed42c81f24468fc3ebacf1fe77
print("✅ Model Trained & Saved")