time = int(input("Time in seconds"))
hours = time // 3600
minute = (time % 3600) // 60
second = (time % 3600) % 60
print("{:02d}" "{}" "{:02d}" "{}" "{:02d}".format(hours,":", minute,":", second))