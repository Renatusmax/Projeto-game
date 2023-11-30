import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura_tela = 1150
altura_tela = 750
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Herói da RCP")

# Cores
branco = (255, 255, 255)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
preto = (0, 0, 0)

# Fonte para texto
fonte = pygame.font.Font(None, 36)

# Texto
texto = "Ajude o Homem que esta desmaiado"
print(texto)

# Personagem
personagem = pygame.image.load('socorrista.png')  # Substitua 'personagem.png' pela imagem do seu personagem
personagem = pygame.transform.scale(personagem, (100, 100))
x_personagem = largura_tela // 2
y_personagem = altura_tela // 2

# Itens de primeiros socorros
itens = []
for _ in range(5): # Quantidade de personagem
    item = pygame.image.load('homem_desmaiado.png')  # Substitua 'item.png' pela imagem do seu item
    item = pygame.transform.scale(item, (80, 80))
    x_item = random.randint(0, largura_tela - 30)
    y_item = random.randint(0, altura_tela - 30)
    itens.append((item, x_item, y_item))

# Pessoa com parada cardíaca
pessoa = pygame.image.load('socorrista.png')  # Substitua 'pessoa.png' pela imagem da pessoa com parada cardíaca
pessoa = pygame.transform.scale(pessoa, (50, 50))
x_pessoa = random.randint(0, largura_tela - 50)
y_pessoa = random.randint(0, altura_tela - 50)
pessoa_com_parada = False

# Pontuação
pontuacao = 0

# Loop principal do jogo
jogo_ativo = True
while jogo_ativo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo_ativo = False

    # Movimentação do personagem
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a]:
        x_personagem -= 1
    if teclas[pygame.K_d]:
        x_personagem += 1
    if teclas[pygame.K_w]:
        y_personagem -= 1
    if teclas[pygame.K_s]:
        y_personagem += 1

    # Verifica colisões com itens de primeiros socorros
    for item, x, y in itens:
        if x < x_personagem + 50 and x + 30 > x_personagem and y < y_personagem + 50 and y + 30 > y_personagem:
            itens.remove((item, x, y))
            pontuacao += 20

    # Verifica colisões com a pessoa com parada cardíaca
    if not pessoa_com_parada and x_personagem < x_pessoa + 50 and x_personagem + 50 > x_pessoa and y_personagem < y_pessoa + 50 and y_personagem + 50 > y_pessoa:
        pessoa_com_parada = True

    # Atualiza a tela
    tela.fill(branco)
    for item, x, y in itens:
        tela.blit(item, (x, y))
    if pessoa_com_parada:
        tela.blit(pessoa, (x_pessoa, y_pessoa))
        texto_r = fonte.render("Ligue para o SAMU 192! Aperte espaço para continuar", True, vermelho)
        tela.blit(texto_r, (largura_tela // 2 - 150, altura_tela // 2))
    else:
        tela.blit(personagem, (x_personagem, y_personagem))
    texto_pontuacao = fonte.render(f"Ajude o Homem que está desmaiado! >>> Pontuação: {pontuacao}", True, preto)
    tela.blit(texto_pontuacao, (10, 10))

    pygame.display.update()

    # RCP quando a tecla Espaço é pressionada
    if pessoa_com_parada:
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:
            pontuacao += 20
            pessoa_com_parada = False
            x_pessoa = random.randint(0, largura_tela - 50)
            y_pessoa = random.randint(0, altura_tela - 50)

# Encerra o Pygame
pygame.quit()
sys.exit()