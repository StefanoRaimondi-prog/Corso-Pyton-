from abc import ABC, abstractmethod
import random

# Classe base Enemy
class Enemy(ABC):
    def __init__(self, nome, salute, stamina):
        self.nome = nome
        self.salute = salute
        self.stamina = stamina

    @abstractmethod
    def enemyAttaccoLeggero(self):
        pass

    @abstractmethod
    def enemyAttaccoPesante(self):
        pass

    @abstractmethod
    def enemy_ricevi_danno(self, danno):
        pass

    def reset_stamina(self):
        self.stamina = 100

    def attacca(self, giocatore):
        scelta = random.choice(["l", "p"])
        if scelta == "l":
            danno = self.enemyAttaccoLeggero()
        else:
            danno = self.enemyAttaccoPesante()

        if danno:
            giocatore.ricevi_danno(danno)


# Classe EnemyBase
class EnemyBase(Enemy):
    def __init__(self, nome="Goblin", salute=60, stamina=100):
        super().__init__(nome, salute, stamina)

    def enemyAttaccoLeggero(self,player):
        if random.random() > 0.1 and self.stamina >= 10:
            danno = random.randint(30, 50)
            print(f"{self.nome} ti ha colpito! Hai perso {danno} punti vita.")
            self.stamina -= 10
            return danno
        else:
            self.reset_stamina()
            print("Attacco fallito")
            return 0

    def enemyAttaccoPesante(self):
        if random.random() > 0.3 and self.stamina >= 15:
            danno = random.randint(50, 60)
            print(f"{self.nome} ha sferrato un colpo pesante! Hai perso {danno} punti vita.")
            self.stamina -= 15
            return danno
        else:
            self.reset_stamina()
            print("Attacco pesante fallito")
            return 0

    def enemy_ricevi_danno(self, danno):
        if random.random() > 0.1:
            self.salute -= danno
            print(f"Attacco riuscito. Il nemico ha ancora {self.salute} punti vita.")
        else:
            print("Attacco fallito")


# Classe EnemyMedio
class EnemyMedio(Enemy):
    def __init__(self, nome="Soldato", salute=120, stamina=150):
        super().__init__(nome, salute, stamina)

    def enemyAttaccoLeggero(self,player):
        if random.random() > 0.05 and self.stamina >= 10:
            danno = random.randint(50, 80)
            print(f"{self.nome} ti ha colpito! Hai perso {danno} punti vita.")
            self.stamina -= 10
            player.salute -= danno
        else: 
            self.reset_stamina()
            print(f"{self.nome} ti ha mancato")

    def enemyAttaccoPesante(self,player):
        if random.random() > 0.2 and self.stamina >= 15:
            danno = random.randint(90, 110)
            print(f"{self.nome} ha sferrato un colpo pesante! Hai perso {danno} punti vita.")
            self.stamina -= 15
            player.salute -= danno
        else: 
            self.reset_stamina()
            print(f"{self.nome} ti ha mancato")

    def enemy_ricevi_danno(self,danno):
        if random.random() > 0.12:
            self.salute -= danno
            print(f"Attacco riuscito , il nemico ha ancora {self.salute} punti vita")
        else: 
            print(f"{self.nome} ti ha mancato")


# Classe EnemyBoss
class EnemyBoss(Enemy):
    def __init__(self, nome="Mirko Re di Python", salute=300, stamina=200, resistenza=1):
        super().__init__(nome, salute, stamina)
        self.resistenza = resistenza

    def enemyAttaccoLeggero(self,player):
        if random.random() > 0.3 and self.stamina >= 10:
            danno = random.randint(100, 110)
            print(f"{self.nome} ti ha colpito! Hai perso {danno} punti vita.")
            self.stamina -= 10
            player.salute -= danno
        else: 
            self.reset_stamina()
            print(f"{self.nome} ti ha mancato")

    def enemyAttaccoPesante(self,player):
        if random.random() > 0.5 and self.stamina >= 15:
            danno = random.randint(120, 130)
            print(f"{self.nome} ha sferrato un colpo pesante! Hai perso {danno} punti vita.")
            self.stamina -= 15
            player.salute -= danno
        else: 
            self.reset_stamina()
            print(f"{self.nome} ti ha mancato")

    def enemy_ricevi_danno(self, danno):
        danno_effettivo = danno * (1 - self.resistenza)
        if random.random() > 0.2:
            self.salute -= danno_effettivo
            print(f"Attacco riuscito , il nemico ha ancora {self.salute} punti vita")
        else: 
            print(f"{self.nome} ti ha mancato")
            

