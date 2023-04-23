
coords_dirt = [[(0,39),(200,37)],
[(87,111),(116,103)],
[(91,103),(114,93)],
[(114,97),(165,95)],
[(135,110),(138,97)],
[(95,119),(116,111)],
[(115,117),(122,114)],
[(119,155),(122,117)],
[(107,120),(110,119)],
[(6,125),(14,123)],
[(65,70),(68,61)],
[(93,36),(112,28)],
[(94,28),(111,25)],
[(96,25),(109,24)],
[(99,24),(105,23)],]








def get_back_coords():
    global new_list, sorted_list
    new_list = []
    for i in coords_dirt:
        for x in range(round(i[1][0] - i[0][0])):
            for y in range(round(i[0][1] - i[1][1])):
                new_list.append([round(x + i[0][0]), round(i[0][1] - y)])

    set_of_sets = set([frozenset(sublist) for sublist in new_list])
    sorted_list = [list(subset) for subset in set_of_sets]

    return new_list

get_back_coords()
print('elemek:', len(new_list))
print('el_rep',len(sorted_list))
print(new_list)
