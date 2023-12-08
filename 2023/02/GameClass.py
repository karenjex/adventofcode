class Game:
    def __init__(self, input_text):
            self.input_text = input_text

    def calculate_game_id(self):
        # parse input string to get game ID which appears just before the semi colon, after the word "Game"
        game=self.input_text.split(':')[0]
        game_id=int(game.split('Game ')[1])
        return game_id


    def get_handfulls(self):
        # return list of handfulls, each of which is a dictionary containing the number of each colour
 
        def get_colour_count(handfull,colour):
            # for a given handfull, identify the number of the given colour. Return 0 if none exist
            if handfull.find(colour) != -1:      # handfull contains given colour
                num_colour=int(handfull.split(colour)[0].split(',')[-1])
            else:       # handfull contains 0 of this colour
                num_colour=0
            return num_colour

        handfulls=[]
        # parse input string to get the handfulls, which appear just after the semi colon
        handfull_list=self.input_text.split(':')[1].split(';')
        for handfull in handfull_list:
            # print('handfull:',handfull)
            num_blue=get_colour_count(handfull,'blue')
            num_green=get_colour_count(handfull,'green')
            num_red=get_colour_count(handfull,'red')
            handfull_dict={'blue':num_blue,'green':num_green,'red':num_red}
            # print(handfull_dict)
            handfulls.append(handfull_dict)
        return handfulls



