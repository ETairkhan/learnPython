def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_though()
    while pile is not 0:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print ("found a key!")

def look_for_key2(box):
    for item in box:
        if item.is_a_box():
            look_for_key2(item)
        elif item.is_a_key():
            print("Found the key!")