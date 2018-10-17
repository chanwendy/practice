from random import choice
class Random():
    def __init__(self,num=5000):
        self.num=num
        self.x_value=[0]
        self.y_value=[0]
    def fil_work(self):
        while len(self.x_value)<=self.num:
            x_direction=choice([1,-1])
            y_direction=choice([1,-1])
            x_distace=choice([0,1,2,3,4,5])
            y_distance=choice([0,1,2,3,4,5,6])
            x_step=x_direction*x_distace
            y_step=y_direction*y_distance
            if x_step==0 and y_step==0:
                continue
            next_x=self.x_value[-1]+x_step
            next_y=self.y_value[-1]+y_step
            self.x_value.append(next_x)
            self.y_value.append(next_y)