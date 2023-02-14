import arcade


class Board(arcade.Window):
    def __init__(self, width=780, height=680, title="P4"):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)
        

    def setup(self):
        arcade.start_render()
        for i in range(7):
            for j in range(6):
                arcade.draw_circle_filled(60+110*i, 60+110*j,50,arcade.color.BLACK_LEATHER_JACKET)
        arcade.finish_render()

    def draw(self,matrix):
        arcade.start_render()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i,j] == 1:
                    arcade.draw_circle_filled(60+110*i, 60+110*j,50,arcade.color.RED)
                if matrix[i,j] == -1:
                    arcade.draw_circle_filled(60+110*i, 60+110*j,50,arcade.color.BLUE)
                else:
                    arcade.draw_circle_filled(60+110*i, 60+110*j,50,arcade.color.BLACK_LEATHER_JACKET)
        arcade.finish_render()

def main():
    """ Main function """
    game = Board()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()