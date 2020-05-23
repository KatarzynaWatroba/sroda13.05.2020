number_of_bricks = int(input("ile masz klockow: "))
current_layer = 1
#next_layer = current_layer + 1
number_of_builded_layers = 0 

while number_of_bricks >= current_layer:
    print("buduje warstwe")
    number_of_bricks = number_of_bricks - current_layer
    number_of_builded_layers = number_of_builded_layers + 1
    #++number_of_builded_layers - to samo co wyzej
    current_layer =  current_layer + 1
print("tyle jest warstw: ", number_of_builded_layers)
