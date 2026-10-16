Score_List = [[0, 0] for _ in range(11)]

def main():
    for frame in range(10):
        while True:
            Score_List[frame][0] = int(input(f"Enter the number of pins knocked down in your first roll of frame {frame + 1}: "))
            if 0 <= Score_List[frame][0] <= 10:
                break
        
        while True:
            if Score_List[frame][0] == 10:
                Score_List[frame][1] = 0
                break
            
            Score_List[frame][1] = int(input(f"Enter the number of pins knocked down in your second roll of frame {frame + 1}: "))
            if 0 <= Score_List[frame][1] <= 10 - Score_List[frame][0]:
                break

    if sum(Score_List[9]) == 10:
        while True:
            Score_List[10][0] = int(input("Enter the number of pins knocked down in your first roll of frame 11: "))
            if 0 <= Score_List[10][0] <= 10:
                break
        if Score_List[9][0] == 10:
            while True:
                Score_List[10][1] = int(input("Enter the number of pins knocked down in your second roll of frame 11: "))
                if 0 <= Score_List[10][1] <= 10:
                    break
                
    for frame in range(10):
        if Score_List[frame][0] == 10:
            if frame < 9:
                Score_List[frame].append(Score_List[frame + 1][0])
                if Score_List[frame + 1][0] == 10 and frame < 8:
                    Score_List[frame].append(Score_List[frame + 2][0])
                
                else:
                    Score_List[frame].append(Score_List[frame + 1][1])
            
            else:
                Score_List[frame].append(Score_List[10][0])
                Score_List[frame].append(Score_List[10][1])
        
        elif sum(Score_List[frame]) == 10:
            if frame < 9:
                Score_List[frame].append(Score_List[frame + 1][0])
            
            else:
                Score_List[frame].append(Score_List[10][0])
        
        else:
            Score_List[frame].append(0)

main()
print("Score List:", Score_List)
print("Total Score:", sum(sum(frame) for frame in Score_List[:10]))