from pygame import *

init()
font.init()

# font, text, width
def mul_lines(f, t, wid, f_color=(0,0,0), align="left"):
	lines = []
	while f.size(t)[0] > wid:
		pos = len(t)
		while f.size(t[0:pos])[0] > wid:
			pos = t.rfind(' ', 0, pos)
			if pos == -1:
				continue
		lines.append(t[0:pos])
		t = t[pos+1:]
	lines.append(t)

	totHeight = f.size(lines[0])[1] * len(lines)
	surf = Surface((wid, totHeight), SRCALPHA)
	surf.fill((0,0,0,0))
	for p in range(len(lines)):
		lineFont = f.render(lines[p], True, f_color)
		lineFontRect = lineFont.get_rect()
		if align == "left": lineFontRect.topleft = 0, p * lineFont.get_height()
		elif align == "center": lineFontRect.midtop = wid/2, p * lineFont.get_height()
		surf.blit(lineFont, lineFontRect)
	return surf

def get_image(sheet, pos):
	img = Surface((pos[2],pos[3]), SRCALPHA)
	img.fill((255,255,255,0))
	img.blit(sheet, img.get_rect(), pos)
	return img

def scale(pics, scale):
	for i in range(len(pics)):
		r = pics[i].get_rect()
		pics[i] = transform.scale(pics[i], (int(r.width*scale), int(r.height*scale)))

# Menu background and buttons images
menu = image.load("images/menu/menu.png")
playB = image.load("images/menu/play.png")
helpB = image.load("images/menu/help.png")
creditsB = image.load("images/menu/credits.png")
backB = image.load("images/menu/back.png")
helpS = image.load("images/menu/helpS.png")
creditsS = image.load("images/menu/creditsS.png")

# Button rects
playR = Rect(389, 349, 502, 58)
helpR = Rect(389, 416, 502, 58)
creditsR = Rect(389, 483, 502, 58)
backR = Rect(650, 483, 502, 58)

fonts = []
fonts.append(font.Font("fonts/sao.ttf", 60))
fonts.append(font.Font("fonts/sao.ttf", 46))
fonts.append(font.Font("fonts/sao.ttf", 36))
fonts.append(font.Font("fonts/sao.ttf", 20))

textbox = image.load("images/textbox.png")

playerSheet = image.load('images/character_alpha.png')
playerImages = []
playerImages.append(get_image(playerSheet, [25, 100, 351, 451]))
playerImages.append(get_image(playerSheet, [425, 100, 351, 451]))
playerImages.append(get_image(playerSheet, [825, 100, 351, 451]))
playerImages.append(get_image(playerSheet, [1225, 100, 351, 451]))

playerImages.append(get_image(playerSheet, [25, 700, 351, 451]))
playerImages.append(get_image(playerSheet, [425, 700, 351, 451]))
playerImages.append(get_image(playerSheet, [825, 700, 351, 451]))
playerImages.append(get_image(playerSheet, [1225, 700, 351, 451]))

playerImages.append(get_image(playerSheet, [25, 1275, 351, 451]))
playerImages.append(get_image(playerSheet, [425, 1275, 351, 451]))
playerImages.append(get_image(playerSheet, [825, 1275, 351, 451]))
playerImages.append(get_image(playerSheet, [1225, 1275, 351, 451]))

playerImages.append(get_image(playerSheet, [25, 1875, 351, 451]))
playerImages.append(get_image(playerSheet, [425, 1875, 351, 451]))
playerImages.append(get_image(playerSheet, [825, 1875, 351, 451]))
playerImages.append(get_image(playerSheet, [1225, 1875, 351, 451]))

scale(playerImages, 0.12)

npcImages = [[]]
npcScale = 2

npcSheet = image.load('images/npcs/c1.png')
npc1 = []
npc1.append(get_image(npcSheet, [7, 34, 18, 31]))
npc1.append(get_image(npcSheet, [7, 2, 18, 31]))
npc1.append(get_image(npcSheet, [7, 66, 18, 31]))
npc1.append(get_image(npcSheet, [7, 98, 18, 31]))
scale(npc1, npcScale)
npcImages.append(npc1)

npcSheet = image.load('images/npcs/c2.png')
npc2 = []
npc2.append(get_image(npcSheet, [70, 5, 20, 27]))
npc2.append(get_image(npcSheet, [6, 5, 20, 27]))
npc2.append(get_image(npcSheet, [6, 37, 20, 27]))
npc2.append(transform.flip(npc2[2], True, False))
scale(npc2, npcScale)
npcImages.append(npc2)

npcSheet = image.load('images/npcs/c3.png')
npc3 = []
npc3.append(get_image(npcSheet, [71, 2, 18, 31]))
npc3.append(get_image(npcSheet, [7, 2, 18, 31]))
npc3.append(get_image(npcSheet, [7, 33, 18, 31]))
npc3.append(transform.flip(npc3[2], True, False))
scale(npc3, npcScale)
npcImages.append(npc3)

npcSheet = image.load('images/npcs/c4.png')
npc4 = []
npc4.append(get_image(npcSheet, [71, 1, 18, 31]))
npc4.append(get_image(npcSheet, [7, 1, 18, 31]))
npc4.append(get_image(npcSheet, [6, 33, 19, 31]))
npc4.append(transform.flip(npc4[2], True, False))
scale(npc4, npcScale)
npcImages.append(npc4)

npcSheet = image.load('images/npcs/c5.png')
npc5 = []
npc5.append(get_image(npcSheet, [70, 5, 20, 27]))
npc5.append(get_image(npcSheet, [6, 5, 20, 27]))
npc5.append(get_image(npcSheet, [6, 37, 20, 27]))
npc5.append(transform.flip(npc5[2], True, False))
scale(npc5, npcScale)
npcImages.append(npc5)

npcSheet = image.load('images/npcs/c6.png')
npc6 = []
npc6.append(get_image(npcSheet, [70, 5, 20, 27]))
npc6.append(get_image(npcSheet, [6, 5, 20, 27]))
npc6.append(get_image(npcSheet, [6, 37, 20, 27]))
npc6.append(transform.flip(npc6[2], True, False))
scale(npc6, npcScale)
npcImages.append(npc6)

npcSheet = image.load('images/npcs/c7.png')
npc7 = []
npc7.append(get_image(npcSheet, [70, 5, 20, 27]))
npc7.append(get_image(npcSheet, [6, 5, 20, 27]))
npc7.append(get_image(npcSheet, [6, 37, 20, 27]))
npc7.append(transform.flip(npc7[2], True, False))
scale(npc7, npcScale)
npcImages.append(npc7)

npcSheet = image.load('images/npcs/c8.png')
npc8 = []
npc8.append(get_image(npcSheet, [70, 5, 20, 27]))
npc8.append(get_image(npcSheet, [6, 5, 20, 27]))
npc8.append(get_image(npcSheet, [6, 37, 20, 27]))
npc8.append(transform.flip(npc8[2], True, False))
scale(npc8, npcScale)
npcImages.append(npc8)

npcSheet = image.load('images/npcs/c9.png')
npc9 = []
npc9.append(get_image(npcSheet, [70, 5, 20, 27]))
npc9.append(get_image(npcSheet, [6, 5, 20, 27]))
npc9.append(get_image(npcSheet, [6, 37, 20, 27]))
npc9.append(transform.flip(npc9[2], True, False))
scale(npc9, npcScale)
npcImages.append(npc9)

npcSheet = image.load('images/npcs/c10.png')
npc10 = []
npc10.append(get_image(npcSheet, [7, 35, 18, 28]))
npc10.append(get_image(npcSheet, [7, 3, 18, 28]))
npc10.append(get_image(npcSheet, [7, 67, 19, 28]))
npc10.append(transform.flip(npc10[2], True, False))
scale(npc10, npcScale)
npcImages.append(npc10)

npcSheet = image.load('images/npcs/c11.png')
npc11 = []
npc11.append(get_image(npcSheet, [103, 2, 18, 30]))
npc11.append(get_image(npcSheet, [39, 2, 18, 30]))
npc11.append(get_image(npcSheet, [7, 33, 18, 30]))
npc11.append(transform.flip(npc11[2], True, False))
scale(npc11, npcScale)
npcImages.append(npc11)

npcSheet = image.load('images/npcs/c12.png')
npc12 = []
npc12.append(get_image(npcSheet, [103, 2, 18, 30]))
npc12.append(get_image(npcSheet, [39, 2, 18, 30]))
npc12.append(get_image(npcSheet, [7, 33, 18, 30]))
npc12.append(transform.flip(npc12[2], True, False))
scale(npc12, npcScale)
npcImages.append(npc12)

npcSheet = image.load('images/npcs/c13.png')
npc13 = []
npc13.append(get_image(npcSheet, [7, 35, 18, 28]))
npc13.append(get_image(npcSheet, [7, 3, 18, 28]))
npc13.append(get_image(npcSheet, [7, 67, 18, 28]))
npc13.append(transform.flip(npc13[2], True, False))
scale(npc13, npcScale)
npcImages.append(npc13)