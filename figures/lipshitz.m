## -*- Mode: octave -*-

x = [-30:30]/10
for d=0:0.1:3
  plot(x, sin(x), x+d, x+sin(d), '1', x+d, sin(d)-x, '1')
  pause(0.1)
end

