class Equipo:
    def assign_attributes(self,attributes):
        self.name=attributes[4]
        self.tecnica=attributes[0]
        self.rend_local=attributes[1]
        self.rend_visit=attributes[2]
        self.tactica=attributes[3]


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
print a.tecnica
print c.name
print d.rend_visit


