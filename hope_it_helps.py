this is my critiquue of your file and how you can get this working:

the reason we have sprite groups is so we dont have to explicitly know whats in there and
for that matter all items in group can have the same name and diff attributes the
group just makes it easier to do checks:

    #in update method
    for i in all_sprites:
        mouse_pos = pygame.mouse.get_pos()
        if i.rect.collidepoint(mouse_pos):
            do something
    #now what i assume you want which is click drag and drop
    #to do this doesent the way you were trying doesnt
    #actually actually work because you would want to detect if
    #you are 1. being clicked 2. holding click down 3. when click is
    # let go if thats a legal move so we have to move the procedure to the
    #game event loop and we will loop through all sprites there to change update

so for instance to create your 'buttons' use a loop instead using variable x,y
so for example say first button needed to be at 0,0 and and next one needed to be at 20,20
and so on:

    x= 0
    y = 0
    #number of buttons
    num = 20
    #5 to a row
    for i in range(20):
        button = Button(x,y,etc...)
        all_sprites.add(button)
        if x== 5 or x == 10 or x == 15:
            x=0
        else:
            x += 2


later on you could draw them like:


    for i in all_sprites:
        gamedisplay blit
        #or its better with sprites
    pygame.draw(all_sprites)
    #which will draw the whole group with one line of code.

ok so now lets get down to your problem everything i put down below will have
to be added to your code possibly inplace of what you have but i cant tell for sure
so i leave it up to you. You have a lot of code here and I really think the game
is doable but your code is a mess and overly explicit making it overwhelmin
to try and go in and fix anything without worrying the whole thing collapses
trust me i know. For now i will show you how to make moves basically but you will
have to tweak it but please go back and do yourself a favor and anytime you have to
make the buttons or access the buttons use for loops and sprite groups as above.
consider two sprite groups too one for black one for white that way all you have to
do is seperate the state for who is moving with a bool for instance black_moving
or white_moving as a bool in your event loop that way if its whites turn i.e.
white_moving == True only look through the white sprite group to detect collision
and trigger movement.

first i dont know if its there but this needs to be called once every loop:
    #more on this in a minute
    for i in all_buttons:
        i.update()

now for button detection in you running while loop:
        #create a bool variable in your __init__ of the buttons class
        self.is_clicked = False

now in the game loop:
    if event.type == pygame.MOUSEBUTTONDOWN:
        #if its whites turn, you would have to create another bool variable
        if is_whites_turn == true:
            for i in all_white_buttons:
                x = pygame.mouse.get_pos()
                if i.rect.collidepoint(x):
                    i.is_clicked = True
                    #attribute i created up above
                    break
                    #we can stop looking cause only one can be clicked
                ###you have to do a seperate for loop for the blacl pieces
                ###thus seperating turns

        if event.type == pygame.MOUSEBUTTONUP:
            
            for i in both black and white sprites:
                write your logis to see if 'i' new position is
                legal compared to the original position
                that means you will have to have a attribute
                that stores coords of the original spot of the button
                and in the update only updates those coords if new coords
                legal and only change when is_clicked is false

                ####you also need to do another for loop to cahnge is_clicked
                ###to false so the button stops moving
so now this is the reason for the update call every loop as back in the button.update() method
we look to see if self.is_moving is true and if so change pos to the mouse pos


    class buttons:
        init:


        def update():
            if self.is_clicked == True:
                pos = pygame.mouse.get_pos()
                self.move_ip(pos)
                
now that update is being called every loop and the events are checked every loop
you should have something to work with at least
