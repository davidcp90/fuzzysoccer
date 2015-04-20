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
#Este metodo calculo el valor de pertenencia, en este caso el rendimiento
#ponderado entre 2 valores
    #x muy bajo contra otros valores de y
    if x=='Muy bajo' and y=='Muy bajo':
        return 'Muy bajo'
    elif x=='Muy bajo' and y=='Bajo':
        return 'Bajo'
    elif x=='Muy bajo' and y=='Intermedio':
        return 'Bajo'
    elif x=='Muy bajo' and y=='Alto':
        return 'Intermedio'
    elif x=='Muy bajo' and y=='Muy alto':
        return 'Intermedio'
    #x bajo contra otros valores de y
    elif x=='Bajo' and y=='Muy bajo':
        return 'Bajo'
    elif x=='Bajo' and y=='Bajo':
        return 'Bajo'
    elif x=='Bajo' and y=='Intermedio':
        return 'Bajo'
    elif x=='Bajo' and y=='Alto':
        return 'Intermedio'
    elif x=='Bajo' and y=='Muy alto':
        return 'Intermedio'
    #x intermedio contra otros valores de y
    elif x=='Intermedio' and y=='Muy bajo':
        return 'Bajo'
    elif x=='Intermedio' and y=='Bajo':
        return 'Bajo'
    elif x=='Intermedio' and y=='Intermedio':
        return 'Intermedio'
    elif x=='Intermedio' and y=='Alto':
        return 'Alto'
    elif x=='Intermedio' and y=='Muy alto':
        return 'Alto'
    #x alto contra otros valores de y
    elif x=='Alto' and y=='Muy bajo':
        return 'Intermedio'
    elif x=='Alto' and y=='Bajo':
        return 'Intermedio'
    elif x=='Alto' and y=='Intermedio':
        return 'Alto'
    elif x=='Alto' and y=='Alto':
        return 'Alto'
    elif x=='Alto' and y=='Muy alto':
        return 'Muy alto'
    #x Muy alto contra otros valores de y
    elif x=='Muy alto' and y=='Muy bajo':
        return 'Alto'
    elif x=='Muy alto' and y=='Bajo':
        return 'Alto'
    elif x=='Muy alto' and y=='Intermedio':
        return 'Alto'
    elif x=='Muy alto' and y=='Alto':
        return 'Muy alto'
    elif x=='Muy alto' and y=='Muy alto':
        return 'Muy alto'
def get_score_local(s):
    if s=='Muy bajo':
        return 0
    elif s=='Bajo':
        return 0
    elif s=='Intermedio'
        return 1
    elif s=='Alto':
        return 3
    elif s=='Muy alto':
        return 3
def get_score_visitor(s):
    if s==3:
        return 0
    elif s==1:
        return 1
    elif s==0
        return 3
def copa_ciber_dosmilquince(equipos):
    #array 1 con todos los equipos
    locales=equipos
    #array 2 con equipos como visitantes
    visitantes=equipos
    participantes=[]
    resultados=[]
    for l in locales:
        power_l=l.local_performance()
        for v in visitantes:
            if l.name==v.name:
                print 'n/a'
            else:
                print '************************************'
                print l.name+' vs '+v.name
                power_v=v.visitor_performance()
                #comparo el rendimiento en el partido
                match=inference_rules(power_l,power_v)
                #saco los puntajes para cada uno
                local_score=get_score_local(match)
                visitor_score=get_score_visitor(local_score)
                #muestro quien gana
                if local_score > visitor_score:
                    print l.name+' - Gana'
                    print v.name+' - Pierde'
                elif local_score == visitor_score:
                    print l.name+' - Empata con - '+v.name
                elif local_score < visitor_score:
                    print l.name+' - Gana'
                    print v.name+' - Pierde'
                #sumo el puntaje a el puntaje de cada equipo
                l.score=l.score+local_score
                v.score=v.score+visitor_score
                print '************************************'
        resultados=resultados.update({l.name:l.score})


    tabla_posiciones=sorted(resultados.items(), reverse=True)
    print 'La tabla de posiciones es'
    print tabla_posiciones
class Equipo:
    def assign_attributes(self,attributes):
        self.name=attributes[4]
        #describe la capacidad tecnica del equipo
        self.tecnica_s=semantic_value(attributes[0])
        #describe el promedio de su rendimiento como local
        self.rend_local_s=semantic_value(attributes[1])
         #describe el promedio de su rendimiento como visitante
        self.rend_visit_s=semantic_value(attributes[2])
        #describe la capacidad tactica del equipo
        self.tactica_s=semantic_value(attributes[3])
        #puntaje de torneo inicializado en cero
        self.score=0
    def local_performance(self):
        internal_ability=inference_rules(self.tecnica_s,self.tactica_s)
        rend_local=self.rend_local_s
        local_p=inference_rules(internal_ability,rend_local)
        return local_p
    def visitor_performance(self):
        internal_ability=inference_rules(self.tecnica_s,self.tactica_s)
        rend_local=self.rend_local_s
        visit_p=inference_rules(internal_ability,rend_local)
        return visit_p


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
copa_ciber_dosmilquince([a,b,c,d,e])




