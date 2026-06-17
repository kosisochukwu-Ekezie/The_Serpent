class body:
    def __init__(self,x,y,next):
        self.x = x
        self.y = y
        self.next = next 

class snake:
    def __init__(self,head,tail):
        self.head = head
        self.tail = tail
        self.grow_pending = False
        self.direction = (0, 0)
        self.last_direction = (0, 0)

    def add_head(self,new):
        new.next = self.head
        self.head = new

    def remove_tail(self):
        if self.head == self.tail:
            return
        
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        temp.next = None 
        self.tail = temp
    def grow(self):
        self.grow_pending = True 
           
    def move(self, xchange, ychange):
        if (xchange, ychange) == (-self.last_direction[0], -self.last_direction[1]):
            xchange, ychange = self.last_direction
        self.last_direction = (xchange, ychange)

        n = body(self.head.x + xchange, self.head.y + ychange, None)
        self.add_head(n)

        if not self.grow_pending:
            self.remove_tail()
        else:
            self.grow_pending = False


    
    def check_selfcollision(self):
        temp = self.head.next
        while temp:
            if temp.x == self.head.x and temp.y == self.head.y:
                return True
            temp = temp.next
        return False
    def check_wallcollision(self, width, height):
        return (
            self.head.x < 0 or self.head.x + 35 > width or
            self.head.y < 70 or self.head.y + 35 > height
        )