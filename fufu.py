def semantic_value(x):
    if x==0 or x<=2:
        return 'Muy bajo'
    elif x==3 or x<=5:
        return 'Bajo'
    elif x==6 or x<=7:
        return 'Intermedio'
    elif x==8 or x<=9:
        return 'Alto'
    elif x==10:
        return 'Muy alto'
def inference_rules(x,y):
    #x muy bajo contra otros valores de y
    if x=='Muy bajo' and y=='Muy bajo'
        return 'Muy bajo'
    elif x=='Muy bajo' and y=='Bajo'
        return 'Bajo'
    elif x=='Muy bajo' and y=='Intermedio'
        return 'Bajo'
    elif x=='Muy bajo' and y=='Alto'
        return 'Intermedio'
    elif x=='Muy bajo' and y=='Muy alto'
        return 'Intermedio'
    #x bajo contra otros valores de y
    elif x=='Bajo' and y=='Muy bajo'
        return 'Bajo'
    elif x=='Bajo' and y=='Bajo'
        return 'Bajo'
    elif x=='Bajo' and y=='Intermedio'
        return 'Bajo'
    elif x=='Bajo' and y=='Alto'
        return 'Intermedio'
    elif x=='Bajo' and y=='Muy alto'
        return 'Intermedio'
    #x intermedio contra otros valores de y
    elif x=='Intermedio' and y=='Muy bajo'
        return 'Bajo'
    elif x=='Intermedio' and y=='Bajo'
        return 'Bajo'
    elif x=='Intermedio' and y=='Intermedio'
        return 'Intermedio'
    elif x=='Intermedio' and y=='Alto'
        return 'Alto'
    elif x=='Intermedio' and y=='Muy alto'
        return 'Alto'
    #x alto contra otros valores de y
    elif x=='Alto' and y=='Muy bajo'
        return 'Intermedio'
    elif x=='Alto' and y=='Bajo'
        return 'Intermedio'
    elif x=='Alto' and y=='Intermedio'
        return 'Alto'
    elif x=='Alto' and y=='Alto'
        return 'Alto'
    elif x=='Alto' and y=='Muy alto'
        return 'Muy alto'
    #x Muy alto contra otros valores de y
    elif x=='Muy alto' and y=='Muy bajo'
        return 'Alto'
    elif x=='Muy alto' and y=='Bajo'
        return 'Alto'
    elif x=='Muy alto' and y=='Intermedio'
        return 'Alto'
    elif x=='Muy alto' and y=='Alto'
        return 'Muy alto'
    elif x=='Muy alto' and y=='Muy alto'
        return 'Muy alto'
class Equipo:
    def assign_attributes(self,attributes):
        self.name=attributes[4]
        self.tecnica=attributes[0]
        self.rend_local=attributes[1]
        self.rend_visit=attributes[2]
        self.tactica=attributes[3]
        #semantic values
        self.tecnica_s=semantic_value(attributes[0])
        self.rend_local_s=semantic_value(attributes[1])
        self.rend_visit_s=semantic_value(attributes[2])
        self.tactica_s=semantic_value(attributes[3])

    def local_performance(self):
        internal_ability=self.tecnica+self.tactica
        rend_local=self.rend_local


a=Equipo()
b=Equipo()
c=Equipo()
d=Equipo()
e=Equipo()
a.assign_attributes([8,2,6,8,'Ferchos FC'])
b.assign_attributes([7,5,5,9,'Deportivo Edwins'])
c.assign_attributes([7,8,3,7,'Atletico Polainas'])
d.assign_attributes([2,6,4,8,'Club Jotos'])
e.assign_attributes([2,3,4,2,'Colegio Robertas'])
print a.tecnica_s




