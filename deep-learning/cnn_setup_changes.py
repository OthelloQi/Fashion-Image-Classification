model = Sequential()

model.add(Conv2D(64, kernel_size=(3,3), padding = 'same', activation = 'relu', input_shape=input_shape))
mode