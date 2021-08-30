hora=0
minutos=0
segundos=0

def setup():
  
  global hora
  global minutos
  global segundos
  size(960, 250)
  
  
def draw():
  global hora
  global minutos
  global segundos
  
  background(34,22,216)
  
  fill(3,77,6)
  rect(0,200,segundos,200)
  fill(234)
  square(minutos,100,16)
  fill(246,255,3)
  ellipse(hora,50,40,40)

  if hora>width:
      hora=0      
  else:
      hora = map(hour(),50,0,width,0)

      
  if minutos>width:
      minutos=0      
  else:
      minutos = map(minute(),59,0,width,0)
      
  
  if segundos>width:
      segundos=0      
  else:
      segundos = map(second(),59,0,width,0)
    
