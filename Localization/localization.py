p = [0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1, 1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
  """自己位置推定"""
    q = []
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    q = [k/sum(q) for k in q]
    return q

def move(p, U):
  """自己位置推定から得られた場所から移動後の位置確率"""
  q = []
  for i in range(len(p)):
    s = p[(i-U) % len(p)] * pExact + p[(i-U+1) % len(p)] * pUndershoot + p[(i-U-1) % len(p)] * pOvershoot
    q.append(s)
  return q

for k in range(len(measurements)):
  p = sense(p, measurements[k])
  p = move(p, motions[k])

print p
