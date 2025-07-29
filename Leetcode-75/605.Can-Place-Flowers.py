def main():
    flowerbed = [1,0,0,0,1,0,0]
    number = 2
    print(canPlaceFlowers(flowerbed, number))



def canPlaceFlowers(flowerbed, n):
    l = len(flowerbed)
        
    for i in range(l):
        if flowerbed[i] == 0:
            # Check if left and right positions are planted
            left_ok = (i == 0) or (flowerbed[i-1] == 0)
            right_ok = (i == l - 1) or (flowerbed[i+1] == 0)
            
            if left_ok and right_ok:
                flowerbed[i] = 1  # plant a flower
                n -= 1
    if n <= 0:
        return True
    return False
        
    
if __name__ == "__main__":
    main()

#Runtime 7ms
#Memory 17.98mb