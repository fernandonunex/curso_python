def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Fernando", "lastname": "Nunez"}

    super_list = [
        {"firstname": "Fernando", "lastname": "Nunez"},
        {"firstname": "Miguel", "lastname": "Nunez"},
        {"firstname": "Pepe", "lastname": "Rodelo"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "Jose", "lastname": "Garcia"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "iteger_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1,4.5,6.43]
    }

    #Dictionary items
    for key, value in super_dict.items():
        print(key,"-",value)
    #List items

    for element in super_list:
        for key, value in element.items():
            print(key,"**",value, end="\n")
        print("")
   
    

if __name__ == '__main__':
    run()
