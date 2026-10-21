from mapp import Map


def show_mappa(mappa: Map) -> None:
        for row in range(mappa.num_row):
            for column in range(mappa.num_column):
                cell = mappa.mappa[row][column]
                if cell == ".":
                    print(". ", end=" ")
                else:
                    print(cell.name, end=" ")
            print()
