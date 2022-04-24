import math 

boat_area = float(input("Area of boat [m2]: "))
list_paints = []

keepAsking = True
while keepAsking :
    
    # dictonary
    info = {}
    info['name'] = input("Name of paint: ")
    info['paint_cover'] = float(input("Cover of paint [m2/L]: "))
    info['nbr_layer'] = float(input("Number of layers : "))

    vol_one_layer = boat_area/info['paint_cover']
    info['total_vol'] = info['nbr_layer']*vol_one_layer
    
    info['can_vol'] = float(input("Volume of a can [L]: "))
    info['can_price'] = float(input("Price of a can [kr]: "))
    
    info['nbr_cans'] = math.ceil(info['total_vol']/info['can_vol'])
    info['total_price'] = info['can_price']*info['nbr_cans']
    
    info['nbr_layers_of_paint'] = info['nbr_cans']*info['can_vol'] *info['paint_cover'] /boat_area
    
    list_paints.append(info)
    continueStr = input("Add another paint? yes/no: ")
    
    if continueStr.lower() in "yes":
        keepAsking = True
    elif continueStr.lower() in "no":
        keepAsking = False
    else :
        print("Could not read input, will cancel")
        keepAsking = False
        
print('=========== Results =================')        
for i in range(len(list_paints)):
    info = list_paints[i]
    print("For " + info['name'] + "\n")
    print(f" You will need {info['total_vol']:.1f}L to paint {info['nbr_layer']:.0f} layers. Rounded up this is {info['nbr_cans']:.1f} cans á {info['can_price']:.2f}L. It will cost {info['total_price']:.0f}kr. This will cover  {info['nbr_layers_of_paint']:.2f} layers. \n")
    
    
    


