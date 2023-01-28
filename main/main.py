### MODULOS IMPORTADOS ###

#### Tkinter ####

from tkinter import *
from tkinter import ttk

#### Pillow ####

from PIL import Image, ImageTk

#### IMPORTANDO BIBLIOTECA DADOS.PY ####

from dados import * 

### CORES ###

co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#ef5350"  # vermelha

### JANELA  PRINCIPAL ###

janela = Tk()
janela.title('Pokedex')
janela.geometry('550x510')
janela.configure(bg = co1)

ttk.Separator(janela, orient = HORIZONTAL). grid(row = 0, columnspan = 1, ipadx = 272)

style = ttk.Style(janela)
style.theme_use("clam")


### FRAME ###

frame_pokemon = Frame(janela, width = 550, height = 290, relief = 'flat')
frame_pokemon.grid(row = 1, column = 0)


def trocar_pokemon(i):
    global imagem_pokemon, pok_imagem
    
    #### ALTERANDO FRAME #####
    
    frame_pokemon['bg'] = pokemon[i]['Tipo'][3]
    
    #### TIPO DE POKEMON ####
    pokemon_nome['text'] = i
    pokemon_nome['bg'] = pokemon[i]['Tipo'][3]
    
    pokemon_tipo['text'] = pokemon[i]['Tipo'][1]
    pokemon_tipo['bg'] = pokemon[i]['Tipo'][3]
    
    pokemon_id['text'] = pokemon[i]['Tipo'][0]
    pokemon_id['bg'] = pokemon[i]['Tipo'][3]
    
    imagem_pokemon = pokemon[i]['Tipo'][2]
    
    ### IMAGEM POKEMON ####

    imagem_pokemon = Image.open(imagem_pokemon)
    imagem_pokemon = imagem_pokemon.resize((238,238))
    imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

    pok_imagem = Label(frame_pokemon, image = imagem_pokemon, relief = 'flat', bg =pokemon[i]['Tipo'][3], fg = co1)
    pok_imagem.place(x = 60, y = 50)

    pokemon_tipo.lift()
    

    #### TROCA DE STATYUS ####
    pokemon_hp ['text'] = pokemon[i]['Status'][0]
    pokemon_ataque['text'] = pokemon[i]['Status'][1]
    pokemon_defesa['text'] = pokemon[i]['Status'][2]
    pokemon_velocidade['text'] = pokemon[i]['Status'][3]
    pokemon_total['text'] = pokemon[i]['Status'][4]

    #### TROCA HABILIDADES ####
    
    pokemon_habilidade_1['text'] = pokemon[i]['Habilidades'][0]
    pokemon_habilidade_2['text'] = pokemon[i]['Habilidades'][1]

### NOME ###

pokemon_nome = Label(frame_pokemon, text = '', relief = 'flat', anchor = CENTER, font = ('Fixedsys 20'), fg = co1)
pokemon_nome.place(x = 12, y = 15)


### CATEGORIA ###

pokemon_tipo = Label(frame_pokemon, text = '', relief = 'flat', anchor = CENTER, font = ('Ivy 10 bold'), bg = co1, fg = co1)
pokemon_tipo.place(x = 12, y = 50)

### ID POKEMON ###

pokemon_id = Label(frame_pokemon, text = '', relief = 'flat', anchor = CENTER, font = ('Ivy 10 bold'), bg = co1, fg = co1)
pokemon_id.place(x = 12, y = 70)




### STATUS ###
pokemon_status = Label(janela, text = 'Status', relief = 'flat', anchor = CENTER, font = ('Verdana 20'), bg = co1, fg = co0)
pokemon_status.place(x = 15, y = 310)

### HP ###
pokemon_hp = Label(janela, text = 'HP: 100', relief = 'flat', anchor = CENTER, font = ('Verdana 10'), bg = co1, fg = co4)
pokemon_hp.place(x = 15, y = 360)

### ATAQUE ###
pokemon_ataque = Label(janela, text = 'Ataque: 600', relief = 'flat', anchor = CENTER, font = ('Verdana 10'), bg = co1, fg = co4)
pokemon_ataque.place(x = 15, y = 380)

### DEFESA ###
pokemon_defesa = Label(janela, text = 'Defesa: 500', relief = 'flat', anchor = CENTER, font = ('Verdana 10'), bg = co1, fg = co4)
pokemon_defesa.place(x = 15, y = 400)

### VELOCIDADE ###
pokemon_velocidade = Label(janela, text = 'Velocidade: 300', relief = 'flat', anchor = CENTER, font = ('Verdana 10'), bg = co1, fg = co4)
pokemon_velocidade.place(x = 15, y = 420)

### TOTAL ###
pokemon_total = Label(janela, text = 'Total: 1.700', relief = 'flat', anchor = CENTER, font = ('Verdana 10'), bg = co1, fg = co4)
pokemon_total.place(x = 15, y = 440)

### ------------------------------> HABILIDADES < ------------------------ ###

### HABILIDADES ###
pokemon_habilidades = Label(janela, text = 'Habilidades', relief = 'flat', anchor = CENTER, font = ('Verdana 20'), bg = co1, fg = co0)
pokemon_habilidades.place(x = 180, y = 310)

### HABILIDADE 1 ###
pokemon_habilidade_1 = Label(janela, text = 'Choque do Trovão - Dano: 200', relief = 'flat', anchor = CENTER, font = ('Verdana 10'), bg = co1, fg = co4)
pokemon_habilidade_1.place(x = 180, y = 360)

### HABILIDADE 2 ###
pokemon_habilidade_2 = Label(janela, text = 'Cabeçada - Dano: 100', relief = 'flat', anchor = CENTER, font = ('Verdana 10'), bg = co1, fg = co4)
pokemon_habilidade_2.place(x = 180, y = 380)


#### ---------------------- > CRIAÇÃO DO MENU DA POKEDEX <-------------------------------- ####

#### BOTÃO PIKACHU ####

imagem_cabeca_pokemon_1 = Image.open('images/cabeca-pikachu.png')
imagem_cabeca_pokemon_1 = imagem_cabeca_pokemon_1.resize((40,40))
imagem_cabeca_pokemon_1 = ImageTk.PhotoImage(imagem_cabeca_pokemon_1)

botao_img_poke1 = Button(janela,command = lambda:trocar_pokemon('Pikachu'), image = imagem_cabeca_pokemon_1, text= 'Pikachu', width= 150, relief='raised', overrelief = RIDGE, compound = LEFT, anchor = NW, padx = 5, font=('Verdana 12'), bg = co1, fg = co0)
botao_img_poke1.place(x = 375, y = 10)

### BOTÃO BULBASAURO ####

imagem_cabeca_pokemon_2 = Image.open('images/cabeca-bulbasaur.png')
imagem_cabeca_pokemon_2 = imagem_cabeca_pokemon_2.resize((40,40))
imagem_cabeca_pokemon_2 = ImageTk.PhotoImage(imagem_cabeca_pokemon_2)

botao_img_poke2 = Button(janela,command = lambda:trocar_pokemon('Bulbasauro'), image = imagem_cabeca_pokemon_2, text= 'Bulbasauro', width= 150, relief='raised', overrelief = RIDGE, compound = LEFT, anchor = NW, padx = 5, font=('Verdana 12'), bg = co1, fg = co0)
botao_img_poke2.place(x = 375, y = 60)

### BOTÃO CHARMANDER ####
 
imagem_cabeca_pokemon_3 = Image.open('images/cabeca-charmander.png')
imagem_cabeca_pokemon_3 = imagem_cabeca_pokemon_3.resize((40,40))
imagem_cabeca_pokemon_3 = ImageTk.PhotoImage(imagem_cabeca_pokemon_3)

botao_img_poke3 = Button(janela,command = lambda:trocar_pokemon('Charmander'), image = imagem_cabeca_pokemon_3, text= 'Charmander', width= 150, relief='raised', overrelief = RIDGE, compound = LEFT, anchor = NW, padx = 5, font=('Verdana 12'), bg = co1, fg = co0)
botao_img_poke3.place(x = 375, y = 110)

#### BOTÃO GAYARADOS ####

imagem_cabeca_pokemon_4 = Image.open('images/cabeca-gyarados.png')
imagem_cabeca_pokemon_4 = imagem_cabeca_pokemon_4.resize((40,40))
imagem_cabeca_pokemon_4 = ImageTk.PhotoImage(imagem_cabeca_pokemon_4)

botao_img_poke4 = Button(janela,command = lambda:trocar_pokemon('Gyarados'), image = imagem_cabeca_pokemon_4, text= 'Gayarados', width= 150, relief='raised', overrelief = RIDGE, compound = LEFT, anchor = NW, padx = 5, font=('Verdana 12'), bg = co1, fg = co0)
botao_img_poke4.place(x = 375, y = 160)

#### BOTÃO GENGAR ####

imagem_cabeca_pokemon_5 = Image.open('images/cabeca-gengar.png')
imagem_cabeca_pokemon_5 = imagem_cabeca_pokemon_5.resize((40,40))
imagem_cabeca_pokemon_5 = ImageTk.PhotoImage(imagem_cabeca_pokemon_5)

botao_img_poke5 = Button(janela,command = lambda:trocar_pokemon('Gengar'), image = imagem_cabeca_pokemon_5, text= 'Gengar', width= 150, relief='raised', overrelief = RIDGE, compound = LEFT, anchor = NW, padx = 5, font=('Verdana 12'), bg = co1, fg = co0)
botao_img_poke5.place(x = 375, y = 210)

#### BOTÃO DRAGONITE ####

imagem_cabeca_pokemon_6 = Image.open('images/cabeca-dragonite.png')
imagem_cabeca_pokemon_6 = imagem_cabeca_pokemon_6.resize((40,40))
imagem_cabeca_pokemon_6 = ImageTk.PhotoImage(imagem_cabeca_pokemon_6)

botao_img_poke6 = Button(janela,command = lambda:trocar_pokemon('Dragonite'), image = imagem_cabeca_pokemon_6, text= 'Dragonite', width= 150, relief='raised', overrelief = RIDGE, compound = LEFT, anchor = NW, padx = 5, font=('Verdana 12'), bg = co1, fg = co0)
botao_img_poke6.place(x = 375, y = 260)

#### PRIMEIRO POKEMON NO DISPLAY ALEATÓRIO ####

import random

lista_pokemon = ['Dragonite', 'Gengar', 'Gyarados', 'Charmander', 'Bulbasauro', 'Pikachu']
pokemon_escolhido = random.sample(lista_pokemon, 1)
trocar_pokemon(pokemon_escolhido[0])


janela.mainloop()