global bx,by,vx,vy,pw,hit

vx=20
vy=0
bx=200
by=100
pw=30
hit=0

def setup():
    createCanvas(400,200)
    
def draw():
    global bx,by,vx,vy,pw,hit
    background(200)
    
    if bx<0 or bx>canvasWidth:
        vx=-vx
    if by>canvasHeight:
        vy=-vy
        if abs(mouseX-bx) <pw:
            hit += 1
    else:
        vy +=1

    bx +=vx
    by +=vy
    
    fill(0)
    ellipse(bx,by,30,30)
    rect(mouseX-pw,canvasHeight-10,pw*2,10)
    text(f'hit:{hit}',10,30)
    