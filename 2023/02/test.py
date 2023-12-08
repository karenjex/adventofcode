s = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'

print(s)

game=s.split(':')[0]
game_id=game.split('Game ')[1]

print(game_id)

def get_colour_count(handfull,colour):
    if handfull.find(colour) != -1:      # handfull contains given colour
        num_colour=int(handfull.split(colour)[0].split(',')[-1])
    else:       # handfull contains 0 of this colour
        num_colour=0
    return num_colour

handfulls=[]
handfull_list=s.split(':')[1].split(';')
for handfull in handfull_list:
    print('handfull:',handfull)
    num_blue=get_colour_count(handfull,'blue')
    num_green=get_colour_count(handfull,'green')
    num_red=get_colour_count(handfull,'red')
    handfull_dict={'blue':num_blue,'green':num_green,'red':num_red}
    print(handfull_dict)
    handfulls.append(handfull_dict)

