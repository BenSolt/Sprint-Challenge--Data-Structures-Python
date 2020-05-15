class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.currrent = None


    def append(self, item):
        if len() == 0:
            self.storage.add_to_tail(item)
            self.current = self.storage.add_to_tail
        #else if length of storage is full
        elif len(self.storage) == self.capacity:
            #if current is equal to end
            if self.current == self.storage.tail:
                #remove end
                self.storage.remove_from_tail()
                #add end
                self.storage.add_to_tail(item)

    def get(self):
#############################################  
        list_buffer = []

        start = self.storage.head
        while True:
            list_buffer .append(start.value)
            if start.next == None:
            #end program
                break
            start = start.next

            print(list_buffer)
            return list_buffer