row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?(column and row eg:-23) \n")

position_1 = int(position[1]) - 1
position_2 = int(position[0]) - 1
map[position_1][position_2] = "X" 



print(f"{row1}\n{row2}\n{row3}")

