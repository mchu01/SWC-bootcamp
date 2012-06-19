def read_animals(filename):
    """
    Reads animal count filename
    Columns are date, time, animal name, number
    """
    f=open(filename,'r')
    date=[]
    time=[]
    animal=[]
    number=[]
    
    # iterate over the file one line at a time
    for line in f:
        d,t,a,n=line.split()
        date.append(d)
        time.append(t)    
        animal.append(a)
        number.append(int(n))
    return date, time, animal, number

def mean(l):
    sum = 0
    for x in l:
        sum=sum+x
        
    return sum/float(len(l))
    
def get_animal(date,animal,number,animal_name):
    """
    Return the number of sighting for the given animal
    """
    new_date=[]
    new_time=[]
    new_number=[]
    # for i in range(len(animal))
    
    for d,t,a,n in zip(date,time,animal,number):
        if a == animal_name:
	     new_date.append(d)
	     new_time.append(t)
	     new_number.append(n)
    return new_date, new_time, new_number
    
def main(filename, animal):
    date,time,animals, counts=read_animals(filename)
    