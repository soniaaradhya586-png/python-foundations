def main():
    height = get_height()
    for i in range(height):
        print(" " * (height - i - 1) + "#" * (i + 1)) 

def get_height():
    while True:
            height = int(input("Height: "))
            if height > 0 and height < 9:
                return height
                pass
    
        
main()