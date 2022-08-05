from model.players import Players
import copy

class SimpleAI(Players):
    
    def choose_move(self, possible_moves: dict):
        copy_possible_moves = copy.deepcopy(possible_moves)
        most_moves = 0
        point = (0, 0)

        while len(copy_possible_moves):
            item = copy_possible_moves.popitem()

            target_cell = item[0]
            possible_moves_of_point = item[1]
            temp = 1

            for el in possible_moves_of_point:
                direction = el[0]
                final_point = el[1]
                curr_cell = final_point

                while curr_cell != final_point:
                    curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])
                    temp += 1
            
            if temp > most_moves:
                most_moves = temp
                point = target_cell
        
        return point