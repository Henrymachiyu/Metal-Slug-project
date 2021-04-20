from cmu_112_graphics import *

def appStarted(app):
    app.started = False 
    app.continu = False 
    #https://www.greenmangaming.com/blog/the-timeless-perfection-of-metal-slug/
    app.imagecover = app.loadImage("cover.jpg")
    #http://pixelartmaker.com/art/6a45404d913e6d1
    app.startb = app.loadImage("start.png")
    #http://pixelartmaker.com/art/ecf2c202c2ff4da
    app.continb = app.loadImage("continue1.png")
    app.hp = 100
    app.kill = 0
    app.x = 50
    app.y = app.height*4/5
    # no move motion right 
    app.move = False
    #https://www.fightersgeneration.com/characters2/marco-metalslug-a2.html
    # same site for the running and shooting images 
    app.nomove0 = app.loadImage("nomove0.png")
    app.nomove1 = app.loadImage("nomove1.png")
    app.nomove2 = app.loadImage("nomove2.png")
    app.nomove3 = app.loadImage("nomove3.png")
    app.nomove4 = app.loadImage("nomove4.png")
    app.nomove5 = app.loadImage("nomove5.png")
    app.nomove6 = app.loadImage("nomove6.png")
    app.nomove7 = app.loadImage("nomove7.png")
    app.nomoveSprite = [app.nomove0,app.nomove1,app.nomove2,
                        app.nomove3,app.nomove4,app.nomove5,
                        app.nomove6,app.nomove7]
    app.nomovecounter = 0
    # no move motion left
    app.nomove0l = app.loadImage("nomove0.png").transpose(Image.FLIP_LEFT_RIGHT)
    app.nomove1l = app.loadImage("nomove1.png").transpose(Image.FLIP_LEFT_RIGHT)
    app.nomove2l = app.loadImage("nomove2.png").transpose(Image.FLIP_LEFT_RIGHT)
    app.nomove3l = app.loadImage("nomove3.png").transpose(Image.FLIP_LEFT_RIGHT)
    app.nomove4l = app.loadImage("nomove4.png").transpose(Image.FLIP_LEFT_RIGHT)
    app.nomove5l = app.loadImage("nomove5.png").transpose(Image.FLIP_LEFT_RIGHT)
    app.nomove6l = app.loadImage("nomove6.png").transpose(Image.FLIP_LEFT_RIGHT)
    app.nomove7l = app.loadImage("nomove7.png").transpose(Image.FLIP_LEFT_RIGHT)
    app.nomoveSpritel = [app.nomove0l,app.nomove1l,app.nomove2l,
                        app.nomove3l,app.nomove4l,app.nomove5l,
                        app.nomove6l,app.nomove7l]
    app.nomovecounterl = 0

    # Moving right
    app.moveright = True
    app.run0 = app.loadImage("run0.png")
    app.run1 = app.loadImage("run1.png")
    app.run2 = app.loadImage("run2.png")
    app.run3 = app.loadImage("run3.png")
    app.run4 = app.loadImage("run4.png")
    app.run5 = app.loadImage("run5.png")
    app.run6 = app.loadImage("run6.png")
    app.run7 = app.loadImage("run7.png")
    app.run8 = app.loadImage("run8.png")
    app.run9 = app.loadImage("run9.png")
    app.runsprite = [app.run0,app.run1,app.run2,app.run3,
                    app.run4,app.run5,app.run6,app.run7,app.run8,
                    app.run9]
    app.runcounter = 0
    # Moveleft
    app.runl0 = app.loadImage("run0.png").transpose(Image.FLIP_LEFT_RIGHT)
    app.runl1 = app.loadImage("run1.png").transpose(Image.FLIP_LEFT_RIGHT)
    app.runl2 = app.loadImage("run2.png").transpose(Image.FLIP_LEFT_RIGHT)
    app.runl3 = app.loadImage("run3.png").transpose(Image.FLIP_LEFT_RIGHT)
    app.runl4 = app.loadImage("run4.png").transpose(Image.FLIP_LEFT_RIGHT)
    app.runl5 = app.loadImage("run5.png").transpose(Image.FLIP_LEFT_RIGHT)
    app.runl6 = app.loadImage("run6.png").transpose(Image.FLIP_LEFT_RIGHT)
    app.runl7 = app.loadImage("run7.png").transpose(Image.FLIP_LEFT_RIGHT)
    app.runl8 = app.loadImage("run8.png").transpose(Image.FLIP_LEFT_RIGHT)
    app.runl9 = app.loadImage("run9.png").transpose(Image.FLIP_LEFT_RIGHT)
    app.runspritel = [app.runl0,app.runl1,app.runl2,app.runl3,
                    app.runl4,app.runl5,app.runl6,app.runl7,app.runl8,
                    app.runl9]
    app.runcounterl = 0
    # shooting 
    app.shoot = False
    app.shoot1 = app.loadImage("shot1.png")
    app.shoot2 = app.loadImage("shot2.png")
    app.shoot3 = app.loadImage("shot3.png")
    app.shoot4 = app.loadImage("shot4.png")
    app.shoot5 = app.loadImage("shot5.png")
    app.shoot6 = app.loadImage("shot6.png")
    app.shoot7 = app.loadImage("shot7.png")
    app.shoot8 = app.loadImage("shot8.png")
    app.shoot9 = app.loadImage("shot9.png")
    app.shotsprite = [ app.shoot1, app.shoot2, app.shoot3, app.shoot4,
                        app.shoot5, app.shoot6, app.shoot7, app.shoot8,
                         app.shoot9]
    app.shotcounter = 0 

def timerFired(app):
    if (app.move == False) and (app.moveright == True):
        app.nomovecounter = (1 + app.nomovecounter) % len(app.nomoveSprite)
    elif (app.move == False) and (app.moveright == False):
        app.nomovecounterl = (1 + app.nomovecounterl) % len(app.nomoveSpritel)
    elif (app.move == True) and (app.moveright == True):
        app.runcounter = (1 + app.runcounter) % len(app.runsprite)
    elif (app.move == True) and (app.moveright == False):
        app.runcounterl = (1 + app.runcounterl) % len(app.runspritel)
    if (app.shoot == True):
        app.shotcounter = (1 + app.shotcounter) % len(app.shotsprite)

def isinside(x1,y1,x2,y2,x,y):
    if x1 <= x <= x2 and y1 <= y <=y2:
        return True
    else:
        return False

def mousePressed(app,event):
    x = event.x
    y = event.y
    startx1,startx2,starty1,starty2 = 245, 563, 292,412
    contx1,contx2,conty1,conty2 = 243, 575, 408, 397

    if isinside(startx1,starty1,startx2,starty2,x,y):
        app.started = True

    elif isinside(contx1,conty1,contx2,conty2,x,y):
        app.continu = True

def keyPressed(app,event):
    if event.key == "r":
        appStarted(app)
    elif event.key == "Right":
        app.move = True
        app.moveright = True
        app.shoot = False
        app.x += 20
    elif event.key == "Left":
        app.move = True
        app.moveright = False
        app.shoot = False
        app.x -= 20
    elif event.key == "Up":
        app.y -= 10
    elif event.key == "Down":
        app.y += 10
    elif event.key == "s":
        app.shoot = True
    else:
        app.move = False

def redrawAll(app,canvas):
    if app.started == False:
        canvas.create_image(app.width/2, app.height/2, 
        image=ImageTk.PhotoImage(app.imagecover))
        # start
        canvas.create_image(app.width/2, app.height*3/5, 
        image=ImageTk.PhotoImage(app.startb))
        # continue
        canvas.create_image(app.width/2, app.height*4/5, 
        image=ImageTk.PhotoImage(app.continb))

    elif app.started == True:
        if app.shoot == False:
            if (app.move == False) and (app.moveright == True):
                sprite = app.nomoveSprite[app.nomovecounter]
                canvas.create_image(app.x, app.y, 
                image=ImageTk.PhotoImage(sprite))
            elif (app.move == False) and (app.moveright == False):
                spritel = app.nomoveSpritel[app.nomovecounterl]
                canvas.create_image(app.x, app.y, 
                image=ImageTk.PhotoImage(spritel))
            elif (app.move == True) and (app.moveright == True):
                runsprite = app.runsprite[app.runcounter]
                canvas.create_image(app.x, app.y, 
                image=ImageTk.PhotoImage(runsprite))     
            elif (app.move == True) and (app.moveright == False):
                runspritel = app.runspritel[app.runcounterl]
                canvas.create_image(app.x, app.y, 
                image=ImageTk.PhotoImage(runspritel)) 

        elif app.shoot == True:
            shotsprite = app.shotsprite[app.shotcounter]
            canvas.create_image(app.x, app.y, 
            image=ImageTk.PhotoImage(shotsprite))             

runApp(width=800, height=600)


