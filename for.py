files = ["joker.mp4","memories.mp4","money heist.mp4"]

for x in files:
    print(x)
print(files)
#only we need for the movie name without the mp4
for x in files:
    print(x[0:-4])
print(files)
#range for numbers ,for iteration
for x in range(5,10):#only print 5 to 10
    print(x)

#the 1st and 2nd means print 5 to 10 and the 3rd one is "which division you want" its divides i  that form
for x in range(5,50,5):
    print(x)