import math 
import pickle
import json

def print_results_simple(info,res):
    print(info['type'] + ": " + info['name'] + "\n")
    print(f" You will need {res['total_vol']:.1f}L to paint {info['nbr_layer']:.0f} layers. Rounded up to {res['nbr_cans']:.1f} cans á {info['can_price']:.2f}L. It will cost {res['total_price']:.0f}kr. This will cover  {res['nbr_layers_of_paint']:.2f} layers. \n")

def print_results():
    print('=========== Results ===========')     
    print(f"Boat area: {boat_area:.2f}")
    for i in range(len(list_info)):
        info = list_info[i]
        res = list_results[i]
        print_results_simple(info,res)
#        if info["type"] == 'botten' :
#            print("      Primer:" )
#            for primer in info["related"]:
#                print("      "+ primer)
#            print("\n")
            
            
        

loadStr = input("load previous session (yes/no): ")

if loadStr.lower() in "yes":
    
    try:
        with open('paints_input.json') as json_file:
            list_info = json.load(json_file)
            load_session = True
            
    except Exception as error: 
        print('No previous session. Continue with a new') 
        load_session = False
        
    

elif loadStr.lower() in "no":
    load_session = False
else :
    print("Could not read input. NOT IMPLEMENTED")
    

if load_session :
    boat_area = list_info[0]['boat_area']
else :
    boat_area = float(input("Area of boat [m2]: "))
    keepAsking = True
    list_info = []
    
    

keepAsking = True
continueStr = input("Add another paint? yes/no: ")  
if continueStr.lower() in "yes":
    keepAsking = True
elif continueStr.lower() in "no":
    keepAsking = False
else :
    print("Could not read input, will cancel")
    keepAsking = False
    
    
while keepAsking :
    
    # dictonary
    info = {}
    info['boat_area'] = boat_area
    info['name'] = input("Name of paint: ")
    info['type'] = input("Type of paint (primer/botten): ")
    info['paint_cover'] = float(input("Cover of paint [m2/L]: "))
    info['nbr_layer'] = float(input("Number of layers : "))
    info['can_vol'] = float(input("Volume of a can [L]: "))
    info['can_price'] = float(input("Price of a can [kr]: "))
    

    list_info.append(info)
    continueStr = input("Add another paint? yes/no: ")  
    if continueStr.lower() in "yes":
        keepAsking = True
    elif continueStr.lower() in "no":
        keepAsking = False
    else :
        print("Could not read input, will cancel")
        keepAsking = False
        
list_results = []
for i in range(len(list_info)):
        
    # dictonary
    res = {}
    info = list_info[i]
    vol_one_layer = boat_area/info['paint_cover']
    res['total_vol'] = info['nbr_layer']*vol_one_layer
    res['nbr_cans'] = math.ceil(res['total_vol']/info['can_vol'])
    res['total_price'] = info['can_price']*res['nbr_cans']
    
    res['nbr_layers_of_paint'] = res['nbr_cans']*info['can_vol'] *info['paint_cover'] /boat_area
        
    list_results.append(res)
        
print_results()
    
    
# store
with open('paints_input.json', 'w') as outfile:
    json.dump(list_info, outfile)
    
# store
with open('paints_results.json', 'w') as outfile:
    json.dump(list_results, outfile)


