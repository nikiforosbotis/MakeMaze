import sys
import random
sys.setrecursionlimit(10000) #δεν έχει κάποια ιδιαίτερη σημασία ο αριθμός, το προσέθεσα αυτό επειδή αλλιώς έβγαζε σαν λάθος όταν ο αριθμός n ήταν αρκετά μεγάλος
n = sys.argv[1]
x = sys.argv[2]
y = sys.argv[3]
input_seed = sys.argv[4]
output_file = sys.argv[5]
n = int(n)
x = int(x)
y = int(y)
visited = []
random.seed(input_seed)

def DFS(x,y):
    if((x,y)) not in visited: #αν το σημείο (x,y) δεν ανήκει στη λίστα visited, τότε προσέθεσέ το σε αυτή
        visited.append((x,y))
    t1 = ((x + 1), y)  #τα t1, t2, t3, t4 είναι tuples με τα οποία εκφράζονται οι πιθανοί γείτονες ώστε να διευκολύνουν την δημιουργία της neighbouring_list
    t2 = (x, (y + 1))
    t3 = ((x - 1), y)
    t4 = (x, (y - 1))
    if((x == 0) and (y == 0)): #όλος αυτος ο βρόχος με τα if και elif δημιουργει τη λίστα γειτνίασης ανάλογα με τη θέση του κόμβου (x,y)
        neighbouring_list = [t1, t2]
    elif (x == (n - 1) and y == 0):
        neighbouring_list = [t3, t2]
    elif (y == 0):
        neighbouring_list = [t1, t3, t2]
    elif (y == (n - 1) and x == 0):
        neighbouring_list = [t4, t1]
    elif (x == 0):
        neighbouring_list = [t2, t4, t1]
    elif (x == (n - 1) and y == (n - 1)):
        neighbouring_list = [t4, t3]
    elif (x == (n - 1)):
        neighbouring_list = [t3, t2, t4]
    elif (y == (n - 1)):
        neighbouring_list = [t4, t3, t1]
    else:
        neighbouring_list = [t3, t1, t2, t4]

    random_neighbours = random.sample(neighbouring_list, len(neighbouring_list)) #η random_neighbours είναι η λίστα neighbouring_list ανακατεμένη

    i = 0

    while((random_neighbours[i] in visited) and (i < (len(random_neighbours) - 1 ))): #όσο ο γείτονας που εξετάζεται υπάρχει στη λίστα visited (δηλαδή έχουμε περάσει απο κει) και δεν ξεπερνάμε τα όρια της λίστας, τότε προχώρα στον επόμενο γείτονα
        i = i + 1
        
    x, y = random_neighbours[i]
    
    if(len(visited) < (n * n)): #η αναδρομική κλήση της DFS
        DFS(x,y)


DFS(x,y) #η πρώτη κλήση της DFS με τα (x,y) που έχει δώσει ο χρήστης
print(visited)

with open(output_file, 'w') as f: #σε αυτό το βρόχο ουσιαστικά γράφεται η λίστα visited στο αρχείο που έχει υποδείξει ο χρήστης και με τη μορφή που χρειάζεται ώστε να σχηματιστεί τελικά ο λαβύρινθος
    i = 0
    total = 1
    while(total < (len(visited))):
        while(i < 2):
            if(i == 0):
                f.write(str(visited[total - 1]))
            if(i == 1):
                f.write(', ')
                f.write(str(visited[total]))
            i = i + 1
        total = total + 1    
        i = 0
        f.write('\n')
f.close()
        
